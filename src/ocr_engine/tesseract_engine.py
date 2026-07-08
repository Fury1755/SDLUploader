"""
Contains all the relevant functions for tesseract's OCR pipeline: preprocessing, text extraction and document orchestration.
"""

import numpy as np
import cv2
from pymupdf import Document, Page
from tesserocr import PyTessBaseAPI
from PIL import Image

from src.ocr_engine.preprocessing_utils import deskew_image, page_to_numpy
from src.ocr_engine.base import OCREngine


# we pass OCREngine as a parameter, meaning that
#  TesseractEngine inherits its ABC methods
class TesseractEngine(OCREngine):
    def __init__(self, tess_data_path: str):
        self._tess_data_path = tess_data_path
        self._api = None  # lazy initialization for extra control

    def _get_api(self):
        if self._api is None:
            try:
                self._api = PyTessBaseAPI(path=self._tess_data_path)
            except Exception:
                raise RuntimeError("API initialization failed")
        return self._api  # so that methods can actually access it

    def _close_api(self):
        if self._api is not None:
            self._api.End()

    def _preprocess(self, img: np.ndarray) -> np.ndarray:
        """
        Args:
            img(np.ndarray): OpenCV image as numpy array
        Returns:
            Preprocessed image (BGR) as numpy array
        """

        # pylint: disable=E1101

        # we skip greyscale because pymupdf already loads the pixmap as
        #  grayscale

        img = deskew_image(img)

        denoised = cv2.bilateralFilter(img, 9, 75, 75)

        # THRESH_BINARY turns every pixel below the threshold white, and every
        #  pixel above the threshold black.
        # THRESH_OTSU figures out what the threshold value should be by seeing
        #  where the variance between two groups is minimized/maximized.
        _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        return binary

    def process_page(self, page: Page):
        """
        Extracts text from a single page using a pre-existing tesseract API instance. Also includes pre-processing.

        Args:
            img(np.ndarray): The image's numpy array

        Returns:
            A string containing the contents of the page.
        """

        # convert img to numpy array
        img_np = page_to_numpy(page)

        # preprocessing
        preprocessed = self._preprocess(img_np)

        # convert to PIL Image
        pil_img = Image.fromarray(preprocessed)

        # get the API (should already be initialized)
        api = self._get_api()

        # pass the PIL Image into the engine
        api.SetImage(pil_img)

        # run the engine and extract the text
        text = api.GetUTF8Text()

        return text

    def process_doc(self, doc: Document):
        """
        Lazily streams tuples containing the page number and the text contents of a pdf.

        Args:
            pdf(pymupdf.Document): The pdf's structure (not the entire pdf!) loaded into memory
        Returns:
            A generator object that returns Tuples sequentially when called.
            The tuple contains the page number, and the page contents respectively.
            Example: [0, "The first page"]
        """

        # initialize the api
        if self._tess_data_path is None:
            raise RuntimeError(
                "tesseract.tesseract_orchestrator.py received None in TESS_DATA_PATH"
            )

        self._get_api()
        for i in range(len(doc)):  # pylint: disable=C0200
            page = doc[i]
            yield (i, self.process_page(page))
        self._close_api()
