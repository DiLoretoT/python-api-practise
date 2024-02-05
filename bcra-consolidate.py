import requests
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta

# Leer el archivo creado "config.jason" para obtener el api token y autenticar correctamente.
with open('config.json') as config_file:
    config = json.load(config_file)
api_token = config['api_token']

# Definición de header con referencia al .json que contiene el token de autenticación.
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Creación de función que: 
#   - Define la URL
#   - Asigna la respuesta a la variable "response"
#   - Define las variables que se usarán de filtro de fechas: "start_date" y "end_date"
#   - Si el código indica que la respuesta fue satisfactoria:
#       -
#       -
#       -
#       -
#       -

def consolidate(endpoint, description):
    url = f'https://api.estadisticasbcra.com{endpoint}'
    response = requests.get(url, headers=headers)
    start = datetime.utcnow() - timedelta(days=7)
    end = datetime.utcnow() - timedelta(days=1)
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 1, 23)
    
    if response.status_code == 200: 
        
        data = response.json()
        
        df = pd.DataFrame(data)
        
        df.rename(columns={'d': 'Date', 'v': 'Value'}, inplace= True)
        
        df['Date'] = pd.to_datetime(df['Date'])
        
        filtered_df = df[(df['Date'] >= start) & (df['Date'] <= end)]
        
        print(f"""
----------------------------------------
Debug info:

Making request to: {url}
Response status code: {response.status_code}
----------------------------------------

{description}
{filtered_df.to_string(index=False)}
""")

        
    else: 
        print(f'Failed to fetch data from {endpoint}. Status code:', response.status_code)
        
# Function excecution by providing endpoints

if __name__ == "__main__":
    
    # Endpoints and descriptions
    endpoints = [
        ("/plazo_fijo", "Monto de plazos fijos (miles de pesos):"),
        ("/depositos", "Monto de depositos (miles de pesos):"),
        ("/cajas_ahorro", "Monto de cajas de ahorro (miles de pesos):"),
        ("/cuentas_corrientes", "Monto de cuentas corrientes (miles de pesos):"),
        ("/usd", "Cotización del dolar blue:"),
        ("/usd_of", "Cotización del dolar oficial:")
    ]
    
    for endpoint, description in endpoints:
        consolidate(endpoint, description)
