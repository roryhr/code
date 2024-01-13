import pytest

from bin_pack.box import Part, Box


@pytest.fixture()
def box():
    return Box(volume_capacity=11, weight_capacity=3)


def test_add_success(box):
    assert box.add(Part(volume=10, weight=2))


def test_add_failure(box):
    assert not box.add(Part(volume=12, weight=2))
