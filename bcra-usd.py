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
    
url_base = "https://api.estadisticasbcra.com"

    # PF: ENDPOINT
url_endpoint_pf = "/plazo_fijo"

    # usd: ENDPOINT 2
url_endpoint_usd = "/usd"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # usd: URL CONCAT
full_url_usd = url_base + url_endpoint_usd

    # usd: Debug print
print("Making request to:", full_url_usd)

# usd: GET method from REQUESTS library
response_usd = requests.get(full_url_usd, headers=headers)

    # usd: Debug print (STATUS CODE)
print("Response status code (billetes y monedas):", response_usd.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_usd.status_code == 200:
    
    # usd: JSON format to python dict
    data = response_usd.json()
    
    # usd: Python dict convertion to dataframe (Pandas)
    df_usd = pd.DataFrame(data)
    
    # usd: Convert 'd' (date) column in PF response, to datetime format
    df_usd['d'] = pd.to_datetime(df_usd['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 31)
    
    # usd: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_usd = df_usd[(df_usd['d'] >= start_date) & (df_usd['d'] <= end_date)]
    
    # usd: Print text explaining the following dataframe
    #print("Monto en plazos fijos (expresado en miles de pesos):\n", filtered_df_usd)
    print("Cotización USD:\n", filtered_df_usd)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_usd.status_code)
    

    