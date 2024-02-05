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
    
url_base_pf = "https://api.estadisticasbcra.com"

    # PF: ENDPOINT
url_endpoint_pf = "/plazo_fijo"

    # usd: ENDPOINT 2
url_endpoint_usd = "/usd"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # PF: CONCAT
full_url_pf = url_base_pf + url_endpoint_pf

    # PF: Debug print
print("Making request to:", full_url_pf)  

# PF: GET method from REQUESTS library
response_pf = requests.get(full_url_pf, headers=headers)

    # PF: Debug print (STATUS CODE)
print("Response status code (plazos_fijos):", response_pf.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_pf.status_code == 200:
    
    # PF: JSON format to python dict
    data = response_pf.json()
    
    # PF: Python dict convertion to dataframe (Pandas)
    df_pf = pd.DataFrame(data)
    
    # PF: Convert 'd' (date) column in PF response, to datetime format
    df_pf['d'] = pd.to_datetime(df_pf['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 11, 1)
    end_date = datetime(2023, 11, 30)
    
    # PF: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_pf = df_pf[(df_pf['d'] >= start_date) & (df_pf['d'] <= end_date)]
    
    # PF: Print text explaining the following dataframe
    print("Monto en plazos fijos (expresado en miles de pesos):\n", filtered_df_pf)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_pf.status_code)
    