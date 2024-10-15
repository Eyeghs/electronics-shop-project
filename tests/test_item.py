import sys, pytest
sys.path.insert(0, '../homework-1')
from src.item import Item

@pytest.fixture
def item1():
    return Item("Test Item", 100, 2)

def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    print(Item.all)
    assert len(Item.all) == 5

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
    
def test_str_repr(item1):
    assert str(item1) == "Test Item"
    assert repr(item1) == "Item('Test Item', 100, 2)"
    
def test_name_setter(item1):
    item1.name = "New Test Item"
    assert item1.name == "New Test I"
    
def test_name_getter(item1):
    assert item1.name == "Test Item"
    
def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    
if __name__ == '__main__':
    pytest.main(['--cov=src', '--cov-report=term-missing', 'test_item.py'])