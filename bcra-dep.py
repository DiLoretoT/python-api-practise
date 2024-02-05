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
    
url_base_dep = "https://api.estadisticasbcra.com"

    # dep: ENDPOINT
url_endpoint_dep = "/depositos"

    # usd: ENDPOINT 2
url_endpoint_usd = "/usd"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # dep: CONCAT
full_url_dep = url_base_dep + url_endpoint_dep

    # dep: Debug print
print("Making request to:", full_url_dep)  

# dep: GET method from REQUESTS library
response_dep = requests.get(full_url_dep, headers=headers)

    # dep: Debug print (STATUS CODE)
print("Response status code (depositos):", response_dep.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_dep.status_code == 200:
    
    # dep: JSON format to python dict
    data = response_dep.json()
    
    # dep: Python dict convertion to dataframe (Pandas)
    df_dep = pd.DataFrame(data)
    
    # dep: Convert 'd' (date) column in dep response, to datetime format
    df_dep['d'] = pd.to_datetime(df_dep['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 11, 1)
    end_date = datetime(2023, 11, 30)
    
    # dep: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_dep = df_dep[(df_dep['d'] >= start_date) & (df_dep['d'] <= end_date)]
    
    # dep: Print text explaining the following dataframe
    print("Monto en depositos (expresado en miles de pesos):\n", filtered_df_dep)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_dep.status_code)
    