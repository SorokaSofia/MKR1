import pandas as pd
from datetime import datetime, timedelta

# Function for reading data from a file
def read_data(filename):
    return pd.read_csv(filename, names=['product_name', 'date', 'price'], parse_dates=['date'])

# A function to determine the price change for the last month for a specific product
def price_change_last_month(data, product_name):
    today = datetime.today()
    one_month_ago = today - timedelta(days=30)
    filtered_data = data[(data['date'] >= one_month_ago) & (data['product_name'] == product_name)]
    return filtered_data
