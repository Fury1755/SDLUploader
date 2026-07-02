"""
This module handles preprocessing of pdf pages for OCR.
"""

import cv2
import numpy as np


def preprocess(img_bgr: np.ndarray) -> np.ndarray:
    """
    Args:
        img_bgr(np.ndarray): OpenCV image as numpy array
    Returns:
        Preprocessed image (BGR) as numpy array
    """

    # pylint: disable=E1101
    grayscale = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2GRAY)
    denoised = cv2.bilateralFilter(grayscale, 9, 75, 75)

    # THRESH_BINARY turns every pixel below the threshold white, and every
    #  pixel above the threshold black.
    # THRESH_OTSU figures out what the threshold value should be by seeing
    #  where the variance between two groups is minimized/maximized.
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return binary
