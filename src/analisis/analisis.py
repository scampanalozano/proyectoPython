import pandas as pd
import os
from ..decoradores.decoradores import timeit, logit


@logit
@timeit
def load_data(data_path):
    if data_path.endswith(".csv"):
        df= pd.read_csv(data_path)
        
    else: 
        raise ValueError("Unsupport file format")
    print("Datos cargados correctamente")
    
    return df


@logit
@timeit
def clean_data(df):
    df["price"]= df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    
    print ("Datos limpiados correctamente")
    
    return df


@logit
@timeit
def analisis_datos(df):
    print("Analisis de datos")
    print(df.describe())
    print("\n Productos con los precios mas altos")
    preciosAltos = df.nlargest(5, "price")
    print(preciosAltos)
    return(preciosAltos)
    

@logit
@timeit
def save_clean_data(df, outputh_path):
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path, index=False)
    else:
        raise ValueError("Unsupport file format")
    print (f"Clean data saved to {outputh_path}")

    


if __name__ =="__main__":
    data_path="data/raw/productos.csv"
    outputh_path= "data/procesados/datos_procesados.csv"
     
    df = load_data(data_path)
    df = clean_data(df)
    df = analisis_datos(df)
    os.makedirs("data/procesados", exist_ok=True)
    
    save_clean_data(df, outputh_path)
