'''
Fetches runtime constants from .env
'''

import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = os.environ.get("PDF_PATH")
TESS_DATA_PATH = os.environ.get("TESS_DATA_PATH")
