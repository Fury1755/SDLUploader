"""
Runs the rules defined in rules.py
Handles text analysis
"""

import src.file_splitter.text_parser.rules as rules


def get_metadata(text: str) -> rules.Metadata:
    name = rules.get_name(text)
    is_final_page = rules.is_final_page(text)

    return rules.Metadata(name, is_final_page)
