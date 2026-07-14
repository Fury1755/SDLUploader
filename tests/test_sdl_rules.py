"""
Tests text parsing rules.
"""

import pytest

from file_splitter.text_parser.sdl_rules import rules
from dataclasses import fields


@pytest.mark.parametrize(
    "text, expected_name",
    [
        ("badabadadba", None),
        (
            "Moonshine\nShadow Ronin Mifune Pte Ltd\nbababa",
            "Shadow Ronin Mifune Pte Ltd",
        ),
        ("mcdonald Pte\n mcdonald Ltd", None),
    ],
)
def test_get_name(text: str, expected_name: str | None):
    """
    Tests whether get_name returns the line where a line contains "Pte" and "Ltd".

    We assume that line is the company name.
    """

    name = rules.get_name(text)

    assert name == expected_name


@pytest.mark.parametrize(
    "text, is_final",
    [
        ("Page 2103902190 of 2", False),
        ("page 3 of 3", False),
        ("", False),
        ("Page 10 of 10", True),
        ("Page 9 of 9", True),
    ],
)
def test_is_final_page(text: str, is_final: bool):
    """
    Tests whether is_final_page identifies "Page x of y" as the final page for x == y.
    """

    assert is_final == rules.is_final_page(text)


def test_metadata_defaults():
    """
    Quick sanity check.
    Tests whether the default values of the Metadata class are as expected.
    """

    example = rules.Metadata()

    assert example.name is None
    assert example.is_final_page is False


def test_metadata_field_count():
    """
    Tests whether the properties of metadata are accounted for in testing.
    Will fail if someone forgets to update the metadata tests (including this one) when
    adding a new property to the dataclass.
    """

    example = rules.Metadata()
    assert len(fields(example)) == 2
