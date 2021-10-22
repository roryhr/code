import pytest


def test_allowed_file():
    assert allowed_file("cool_pic.jpeg")


def test_disallowed_file():
    assert not allowed_file("boring_spreadsheet.xlsx")
