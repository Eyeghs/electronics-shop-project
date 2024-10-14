import sys, pytest
sys.path.insert(0, '../homework-1')
from src.item import Item

@pytest.fixture
def item1():
    return Item("Test Item", 100, 2)

def test_item_init(item1):
    assert item1.name == "Test Item"
    assert item1.price == 100
    assert item1.quantity == 2
    assert item1 in Item.all

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200
    
def test_apply_discount(item1):
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 80
    
if __name__ == '__main__':
    pytest.main(['--cov=src', '--cov-report=term-missing', 'test_item.py'])