"""
This module prints text from a specific debug path.
It is a separate script on its own.
"""

import logging

import pymupdf

from src.ocr_engine.tesseract_engine import TesseractEngine
from src.config import DEBUG_PDF_PATH, TESS_DATA_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelno)s - %(funcName)s - %(message)s",
)

pdf = pymupdf.open(DEBUG_PDF_PATH)
tesser_eng = TesseractEngine(TESS_DATA_PATH)
for page_number, page_text in tesser_eng.process_doc(pdf):
    print(page_text)
    # log with page_number + 1 because it is not zero-indexed
    logging.info("Page %s : Char length = %s", page_number + 1, len(page_text))
