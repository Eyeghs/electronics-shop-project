import sys, pytest
sys.path.insert(0, '..')
from src.keyboard import Keyboard

@pytest.fixture
def keyboard1():
    return Keyboard("Test Keyboard", 10000, 5)

def test_init(keyboard1):
    assert str(keyboard1) == "Test Keyboard"
    assert repr(keyboard1) == "Keyboard('Test Keyboard', 10000, 5)"