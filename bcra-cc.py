import requests
import pandas as pd
from datetime import datetime

# API Elegida: Estadística BCRA
# TOKEN: eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA
# HEADER: Authorization: BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA

# Authentication
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA'
}

# Construcción de URL
    
url_base_cc = "https://api.estadisticasbcra.com"

    # cc: ENDPOINT
url_endpoint_cc = "/cuentas_corrientes"

    # usd: ENDPOINT 2
url_endpoint_usd = "/usd"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # cc: CONCAT
full_url_cc = url_base_cc + url_endpoint_cc

    # cc: Debug print
print("Making request to:", full_url_cc)  

# cc: GET method from REQUESTS library
response_cc = requests.get(full_url_cc, headers=headers)

    # cc: Debug print (STATUS CODE)
print("Response status code (cc):", response_cc.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_cc.status_code == 200:
    
    # cc: JSON format to python dict
    data = response_cc.json()
    
    # cc: Python dict convertion to dataframe (Pandas)
    df_cc = pd.DataFrame(data)
    
    # cc: Convert 'd' (date) column in cc response, to datetime format
    df_cc['d'] = pd.to_datetime(df_cc['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 11, 1)
    end_date = datetime(2023, 11, 30)
    
    # cc: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_cc = df_cc[(df_cc['d'] >= start_date) & (df_cc['d'] <= end_date)]
    
    # cc: Print text explaining the following dataframe
    print("Monto en cuentas corrientes (expresado en miles de pesos):\n", filtered_df_cc)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_cc.status_code)
    