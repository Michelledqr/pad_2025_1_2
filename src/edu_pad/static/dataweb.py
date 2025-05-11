import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

class Dataweb:
    def __init__(self):
        self.url="https://tradingeconomics.com/currencies/"
    
    def obtener_datos(self):
        try:
            # url + headers - navigation simulator
            headers={
                'User-Agent': 'Mozilla/5.0'
            }
            response = requests.get(self.url, headers=headers)
            if response.status_code != 200:
                print("URL reporting error, not responding or don't exists")
            content = response.text  # Extrae el contenido de la respuesta HTTP
            soup = BeautifulSoup(response.text, 'html.parser')
            tabla = soup.select_one('[class="card"] table')
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columnas = [td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)
            df = pd.DataFrame(filas,columns=nombre_columnas)
            #print(df.head())
            return df
        except Exception as err:
            print("Error in gather data function - check the code")

#dw = Dataweb()
#datos=dw.obtener_datos()
#print(datos.head())
#print (dw.url +" afuera")