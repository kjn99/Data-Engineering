import requests
import pandas as pd

base_url = 'https://f9demo.kronoscope.fountain9.com'

# URL of the API endpoint
url = f"{base_url}/atlas/auth/api/token"

# Data to be sent in the POST request
data = {
    "user_name": "user1@f9demo.com",
    "password": "demo_1970",
    "is_superuser": "false"
}
print('getting the token...')
response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
    res = response.json()
    token = res['access']
else:
    print(f"Request failed with status code {response.status_code}")


    


# URL of the API endpoint
url = f"{base_url}/atlas/timeseries/api/get_plans_data?dataset_id=1&plan_id=All_Fixed_Duration_Purchase_Plan_2023_01_02_17_24_19&plan_type=Purchase Plan&sep=,"

# Data to be sent in the POST request
params = {
    'dataset_id': '1',
    'plan_id': 'All_Fixed_Duration_Purchase_Plan_2023_01_02_17_24_19',
    'plan_type' : 'Purchase Plan',
    'sep' : ','
}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print('get_plans_data api started...')

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occured: {err}")
except Exception as err:
    print(f"other error occured: {err}")



if response.status_code == 200:
    print(response)

    df = pd.read_csv('data.csv')
    print(df.head())
    total_qty = df.groupby('sku_id')['purchase_quantity_for_selected_duration'].sum().reset_index()
    print(total_qty)
    total_qty.to_csv('total_purchase_quantity.csv', index=False)
    print("Total purchase quantities have been saved to total_purchase_quantity.csv")

else:
    print(f"Request failed with status code {response.status_code}")
    

    


    
