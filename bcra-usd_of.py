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

    # usd_of: ENDPOINT 2
url_endpoint_usd_of = "/usd_of"

    # PARAMETERS    
params = {'start_date': '2023-12-01','end_date': '2023-12-31'}

    # usd_of: URL CONCAT
full_url_usd_of = url_base + url_endpoint_usd_of

    # usd_of: Debug print
print("Making request to:", full_url_usd_of)

# usd_of: GET method from REQUESTS library
response_usd_of = requests.get(full_url_usd_of, headers=headers)

    # usd_of: Debug print (STATUS CODE)
print("Response status code (billetes y monedas):", response_usd_of.status_code)

# Filtering info + Data formatting

    # Check HTTP response status code
if response_usd_of.status_code == 200:
    
    # usd_of: JSON format to python dict
    data = response_usd_of.json()
    
    # usd_of: Python dict convertion to dataframe (Pandas)
    df_usd_of = pd.DataFrame(data)
    
    # usd_of: Convert 'd' (date) column in PF response, to datetime format
    df_usd_of['d'] = pd.to_datetime(df_usd_of['d'])
    
    # Declare dates variables
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 31)
    
    # usd_of: Filtering dataframe rows by dates (previous variables) in column 'd'
    filtered_df_usd_of = df_usd_of[(df_usd_of['d'] >= start_date) & (df_usd_of['d'] <= end_date)]
    
    # usd_of: Print text explaining the following dataframe
    #print("Cotización del dolar oficial:\n", filtered_df_usd_of)
    print("Cotización usd_of:\n", filtered_df_usd_of)

# Check status code if error
else:
    print('Failed to fetch data. Status code: ', response_usd_of.status_code)
    

    