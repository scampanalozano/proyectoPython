import requests
from bs4 import BeautifulSoup
import pandas as pd

def obtenerDatos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.content
    else:
        raise Exception(f"Error: {url}")


    

def analizar_producto(producto):
    title= producto.find("a", class_="title").text.strip()
    description= producto.find("p", class_="description").text.strip()
    price = producto.find("h4", class_="price").text.strip()
 
    return{
        "title": title,
        "description": description,
        "price": price       
    }
    
def scrape(url):
    contador_paginas = obtenerDatos(url)
    soup = BeautifulSoup(contador_paginas, "html.parser")
    
    productos = soup.find_all("div", class_="thumbnail")
    
    data=[]
    
    for producto in productos:
        producto_info= analizar_producto(producto)
        data.append(producto_info)
    
    return pd.DataFrame(data)

base_url= ("https://webscraper.io/test-sites/e-commerce/allinone")

df = scrape(base_url)

df.to_csv('data/raw/productos.csv', index= False)





    






    
    
