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

# Handle case where no data is available for the last month
if filtered_data.empty:
    return "Немає доступних даних за останній місяць для даного товару."


# Calculating price changes
initial_price = filtered_data['price'].iloc[0]
final_price = filtered_data['price'].iloc[-1]
price_change = final_price - initial_price
return f"Зміна ціни за останній місяць для '{product_name}': {price_change} грн"


# Main script execution
data = read_data('file.txt')
print(price_change_last_month(data, 'Кава'))
