import pandas as pd


sales_data = {
    'date': ['2022-08-04', '2022-08-04'],
    'product': [720146, 717175],
    'store': ['4411600298', '4411600298'],
    'sales_quantity': [3.0, 2.0]
}

price_data = {
    'month_date': ['2022-08-01', '2022-08-01'],
    'product': [720146, 717175],
    'price': [1, 24]
}

availability_data = {
    'date': ['2022-08-04', '2022-08-04'],
    'product': [720146.0, 717175.0],
    'store': ['4411600298', '4411600298'],
    'availability': [96.0, 97.0]
}

target_data = {
    'month_date': ['2022-08-01', '2022-08-01'],
    'product': [720146, 717175],
    'target': [1327937.0, 45883.0]
}

df_sales = pd.DataFrame(sales_data)
df_price = pd.DataFrame(price_data)
df_availability = pd.DataFrame(availability_data)
df_target = pd.DataFrame(target_data)

df_sales['date'] = pd.to_datetime(df_sales['date'])
df_price['month_date'] = pd.to_datetime(df_price['month_date'])
df_availability['date'] = pd.to_datetime(df_availability['date'])
df_target['month_date'] = pd.to_datetime(df_target['month_date'])



print(df_sales, 'df_sales')
print(df_price, 'df_price')
print(df_availability, 'df_availability')
print(df_target, 'df_target')


merged = df_sales.merge(df_price, left_on='product', right_on='product')\
    .merge(df_availability, on=['date', 'product', 'store'])\
    .merge(df_target, left_on='product', right_on='product')


output = merged[['date', 'product', 'sales_quantity', 'price', 'availability', 'target']]
output.columns = ['Date', 'Product', 'Sales Quantity', 'Price', 'Availability', 'Monthly Target']

# output - 1
print(output)

# Calculate revenue 
merged['revenue'] = merged['price'] * merged['sales_quantity']

revenue_by_date = merged.groupby('date')['revenue'].sum().reset_index()
revenue_by_date.columns = ['Date', 'Revenue']

# output - 2
print(revenue_by_date)

# Get month-end dates
month_end_dates = pd.date_range(start='2022-08-01', end='2022-10-01', freq='M')


merged['revenue'] = merged['price'] * merged['sales_quantity']


merged['month_end'] = merged['date'] + pd.offsets.MonthEnd(0)


monthly_revenue = merged.groupby('month_end')['revenue'].sum().reset_index()
monthly_revenue.columns = ['Month End Date', 'Revenue']

# output - 3
print(monthly_revenue)
