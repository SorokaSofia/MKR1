import pandas as pd
from datetime import datetime, timedelta

# Function for reading data from a file
def read_data(filename):
    return pd.read_csv(filename, names=['product_name', 'date', 'price'], parse_dates=['date'])
