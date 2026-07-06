"""
Fetches runtime constants from .env
"""

import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = os.environ["PDF_PATH"]
TESS_DATA_PATH = os.environ["TESS_DATA_PATH"]
RUNTIME_PARENT_DIR = os.environ["RUNTIME_PARENT_DIR"]
DEBUG_PDF_PATH = os.environ.get("DEBUG_PDF_PATH")
