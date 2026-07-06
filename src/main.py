"""
Orchestrator module. There should be no external dependencies here!
"""

import logging

import pymupdf

from src.ocr_engine.tesseract_engine import TesseractEngine
from src.config import PDF_PATH, TESS_DATA_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelno)s - %(funcName)s - %(message)s",
)

pdf = pymupdf.open(PDF_PATH)

# text_stream is a generator that returns
#  the corresponding iterable when called.
if TESS_DATA_PATH is None:
    raise RuntimeError("TESS_DATA_PATH missing")
tesser_eng = TesseractEngine(TESS_DATA_PATH)
for page_number, page_text in tesser_eng.process_doc(pdf):
    logging.info("Processed page %s", page_number)
    print(page_text)
