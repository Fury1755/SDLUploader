"""
Contains the rules that the engine will run.
Rules are independent and stateless.
"""

from dataclasses import dataclass
import re


@dataclass(frozen=True)  # we finally have an excuse to enforce immutability
class Metadata:
    """
    A class that contains the metadata of every individual page.

    Attributes:
        name(str | None): The name of the company
        is_end(bool): Checks if the current page is the final page of the letter.
    """

    name: str | None = None
    is_final_page: bool = False


def get_name(text: str) -> str | None:
    """
    Args:
        text(str): the text body of a single page
    Returns:
        The name of the company ('### Pte. Ltd.')
    """

    for line in text.splitlines():
        PTE = False
        LTD = False

        if ("Private" or "Pte") in line:
            PTE = True
        if ("Limited" or "Ltd") in line:
            LTD = True

        if PTE and LTD:
            return line
    return None


def is_final_page(text: str) -> bool:
    """
    Checks if the page contains a marker 'Page X of Y' where X == Y.
    Args:
        text(str): the text body of a single page
    Returns:
        A boolean if the end of the document is reached
    """

    match = re.search(r"Page (\d+) of (\d+)", text)
    # all our SDL letters don't have double digit pages but we use \d+ here for genericity

    if match:
        if int(match.group(1)) == int(match.group(2)):
            return True
    return False
