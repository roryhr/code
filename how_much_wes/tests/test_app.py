import pytest

<<<<<<< HEAD
from app import allowed_file

=======
>>>>>>> 711bb947faec91ce78da4edc02a709438ac1b551

def test_allowed_file():
    assert allowed_file("cool_pic.jpeg")


def test_disallowed_file():
<<<<<<< HEAD
    assert not allowed_file("boring_spreadsheet.xls")
=======
    assert not allowed_file("boring_spreadsheet.xlsx")
>>>>>>> 711bb947faec91ce78da4edc02a709438ac1b551
