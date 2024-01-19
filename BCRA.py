import requests
import pandas as pd
from datetime import datetime

# API Elegida: Estadística BCRA

# Authentication
# TOKEN: eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA
# HEADER: Authorization: BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxNTE1MTQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc21hcnRpbmRsQGdtYWlsLmNvbSJ9.AEKuP7C4xJFh6BnYU3dMkZWRhAfbvAgh_VwidJqcGIMql3_kd8XKom6tPSpx7G33kuW7myqj1rNWx5_eqtyqoA'
}

# Construcción de URL
    #URL BASE
URL_Base = "https://api.estadisticasbcra.com"
    #ENDPOINT
URL_Endpoint = "/plazo_fijo"
    #PARAMETERS    
params = {'start_date': '2023-01-01','end_date': '2023-01-17'}
#CONCAT
Full_URL = URL_Base + URL_Endpoint

print("Making request to:", Full_URL)  # Debug print

# GET method de la librería REQUESTS
response = requests.get(Full_URL, headers=headers)

print("Response status code:", response.status_code)  # Debug print

# Validación de código de estado
if response.status_code == 200:
    data = response.json()
        
    df = pd.DataFrame(data)
    df['d'] = pd.to_datetime(df['d'])
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 17)
    filtered_df = df[(df['d'] >= start_date) & (df['d'] <= end_date)]
    
    print(filtered_df)
    
else:
    print('Failed to fetch data. Status code: ', response.status_code)
    