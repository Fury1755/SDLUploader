"""
This module tests the pdf_instance file to ensure its state management is behaving correctly.
"""

from unittest.mock import MagicMock, Mock
from file_splitter.pdf_instance import PDFInstance
from file_splitter.text_parser.sdl_rules.rules import Metadata


def test_pdf_instance_init():
    """
    Sanity check: correct default values
    """

    mock_engine = MagicMock()
    mock_str = "pathxxx"
    mock_create_folder = MagicMock()
    mock_output = MagicMock()

    mock_create_folder.return_value = mock_output

    test_instance = PDFInstance(mock_engine, mock_str, mock_create_folder)

    assert test_instance._ocr_engine == mock_engine
    assert test_instance._output_folder == mock_output
    assert test_instance._page_buffer == []
    assert test_instance._current_name is None


def test_pdf_instance_flush():
    """
    Tests if the ._flush logic works as intended (i.e. flushing when all the
    state requirements are met)
    """

    mock_ocr = Mock()
    mock_ocr.process_page.return_value = "ACME Pte Ltd"
    mock_rules_engine = Mock()
    mock_rules_engine.get_metadata.return_value = Metadata("ACME Pte Ltd", True)
