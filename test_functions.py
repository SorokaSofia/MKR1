import pytest
from datetime import datetime
from mkr import read_data, price_change_last_month  # Assuming your code is in main_module.py

# Fixture for creating test data
@pytest.fixture
def sample_data():
    # Creating a DataFrame in the code, since we can't read from files in pytest without using mocks or a file system
    import pandas as pd
    from io import StringIO
    data = """product_name,date,price
              Молоко,2024-03-15,31.00
              Молоко,2024-04-01,29.00
              Молоко,2024-04-10,32.00"""
    return pd.read_csv(StringIO(data), parse_dates=['date'])

# Tests for the read_data function
def test_read_data():
     # Here you can add a mock for pd.read_csv if you want to test the behavior of reading a file
    pass

# Parameterized test for the price_change_last_month function
@pytest.mark.parametrize("product_name,expected_result", [
    ('Молоко', "Зміна ціни за останній місяць для 'Молоко': 1 грн"),
    ('Хліб', "Немає доступних даних за останній місяць для даного товару.")
])
def test_price_change_last_month(sample_data, product_name, expected_result):
    assert price_change_last_month(sample_data, product_name) == expected_result
