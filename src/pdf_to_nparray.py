"""
Converts pdfs to numpy arrays for tesseract/paddleOCR to read
"""

import pymupdf
import numpy as np


def page_to_numpy(page: pymupdf.Page, dpi: int = 300) -> np.ndarray:
    """
    Args:
        page(pymupdf.Page): The individual page of pymupdf's Document object
        dpi(int): The dpi of the numpy array. Set to 300 because that's the office
                    printer's dpi.

    Returns:
        The page's numpy array.
    """

    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)  # pylint: disable=E0602
    return img
