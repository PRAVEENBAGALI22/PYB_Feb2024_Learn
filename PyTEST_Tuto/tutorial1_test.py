import math

import pytest


def test_sq():
    num = 25
    assert 5 == math.sqrt(num)


def test_square():
    n2 = 5
    assert 25 == n2 * n2

@pytest.mark.sanity
def test_name():
    name = "Praveen"
    assert len(name) == 5