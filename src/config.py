"""
Fetches runtime constants from .env
"""

import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = os.environ["PDF_PATH"]
TESS_DATA_PATH = os.environ["TESS_DATA_PATH"]
WORKSPACE_FOLDER_PATH = os.environ["WORKSPACE_FOLDER_PATH"]
