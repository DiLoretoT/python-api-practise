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
    
url_base_ca = "https://api.estadisticasbcra.com"

    # ca: ENDPOINT
url_endpoint_ca = "/cajas_ahorro"

    # usd: ENDPOINT 2
url_endpoint_usd = "/usd"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # ca: CONCAT
full_url_ca = url_base_ca + url_endpoint_ca

    # ca: Debug print
print("Making request to:", full_url_ca)  

# ca: GET method from REQUESTS library
response_ca = requests.get(full_url_ca, headers=headers)

    # ca: Debug print (STATUS CODE)
print("Response status code (Cajas de ahorro):", response_ca.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_ca.status_code == 200:
    
    # ca: JSON format to python dict
    data = response_ca.json()
    
    # ca: Python dict convertion to dataframe (Pandas)
    df_ca = pd.DataFrame(data)
    
    # ca: Convert 'd' (date) column in ca response, to datetime format
    df_ca['d'] = pd.to_datetime(df_ca['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 11, 1)
    end_date = datetime(2023, 11, 30)
    
    # ca: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_ca = df_ca[(df_ca['d'] >= start_date) & (df_ca['d'] <= end_date)]
    
    # ca: Print text explaining the following dataframe
    print("Monto en cajas de ahorro (expresado en miles de pesos):\n", filtered_df_ca)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_ca.status_code)
    