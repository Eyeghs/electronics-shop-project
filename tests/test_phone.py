import sys
import pytest
from src.phone import Phone
sys.path.insert(0, '..')


@pytest.fixture
def phone1():
    return Phone("Test Phone", 120_000, 5, 2)


def test_str_repr(phone1):
    assert str(phone1) == "Test Phone"
    assert repr(phone1) == "Phone('Test Phone', 120000, 5, 2)"
