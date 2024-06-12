import time 
import logging

#Configurar logger

logging.basicConfig(level= logging.INFO, format ="%(asctime)s == %(levelname)s == %(message)s")



#Definir el formato de los mensajes de registro.


def timeit(func):
    #Medir el tiempo de una funcion
    def wrapper(*arg,**kwargs):
        start_time= time.time()
        result = func(*arg,**kwargs)
        end_time = time.time()
        elapsed_time= end_time - start_time
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:4f} seconds")
        
        return result
    return wrapper



def logit(func):
    #decorador para registrar la ejecucion de una funcion
    def wrapper(*args,**kwargs):
        logging.info(f"Corriendo {func.__name__}")
        result = func(*args,**kwargs)
        logging.info(f"Completado {func.__name__}")
        return result
    return wrapper