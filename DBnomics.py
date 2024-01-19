import requests
import pandas as pd

# API Elegida: DBnomics

# Construcción de URL
    #URL BASE
URL_Base = "https://api.db.nomics.world/v22"
    #ENDPOINT
URL_Endpoint = "/search"
    #PARAMETERS    
URL_Params = "?q=financial&limit=5"
#CONCAT
Full_URL = URL_Base + URL_Endpoint + URL_Params

print("Making request to:", Full_URL)  # Debug print

# GET method de la librería REQUESTS
response = requests.get(Full_URL)

print("Response status code:", response.status_code)  # Debug print

# Validación de código de estado
if response.status_code == 200:
    
    response_json = response.json()
    
    search_results = response_json['results']['docs']
    
    df = pd.DataFrame(search_results)
    
    filter = ['provider_code', 'code', 'name']
    

    print(df[filter])
    #for dataset in df:
        #print(f"\n"
         #     f"Provider: {dataset['provider_code']}\n"
          #    f"Dataset Code: {dataset['code']}\n"
           #   f"Name: {dataset['name']}")
        
else:
    print('Failed to fetch data. Status code: ', response.status_code)
    