"""
This module holds the class statement_splitter.
It is a sequential, incremental state machine.
"""

import os
import re

from pymupdf import Document, Page
from tqdm import tqdm

from src.ocr_engine.base import OCREngine
from file_splitter.text_parser import rules_engine
from src.file_splitter.os_utils import create_folder


class PDFInstance:
    """
    This class is a pdf instance that grows in size, then flushes itself and saves its contents
    as a new file when the criteria is reached.
    It is a state machine that creates a new pdf file when the conditions are reached.
    """

    def __init__(self, ocr_engine: OCREngine, runtime_parent_dir: str):
        # this is an existing instance of an initialized OCR engine
        self._ocr_engine = ocr_engine
        self._output_folder = create_folder(runtime_parent_dir)
        self._page_buffer: list[Page] = []
        self._current_name: str | None = None

    def _flush(self):
        # guard against empty buffers, accessing indexes of empty list will crash
        if not self._page_buffer:
            return

        new_doc = Document()
        first_page = self._page_buffer[0]
        last_page = self._page_buffer[-1]

        # satisfy type checker
        assert first_page.number is not None
        assert last_page.number is not None

        new_doc.insert_pdf(
            first_page.parent, from_page=first_page.number, to_page=last_page.number
        )

        # assert a name exists
        assert self._current_name is not None

        safe_name = re.sub(r'[<>:"/\\|?*]', "_", self._current_name)
        file_path = os.path.join(self._output_folder, f"SDL_2025_{safe_name}.pdf")
        new_doc.save(file_path)
        new_doc.close()

        # reset attributes
        self._page_buffer = []
        self._current_name = None

    def split_statements(self, doc: Document):
        for page_number, page_text in tqdm(
            enumerate(self._ocr_engine.process_doc(doc)),
            total=len(doc),
            desc="Processing pages",
        ):
            metadata = rules_engine.get_metadata(page_text[1])
            page = doc[page_number]

            if metadata.name:
                if metadata.name != self._current_name:
                    self._flush()
                    self._current_name = metadata.name

            self._page_buffer.append(page)

        self._flush()  # flush the last statement
