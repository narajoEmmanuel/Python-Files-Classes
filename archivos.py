#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 23/5/2019  8:00am 
#Fecha de última Modificación: 27/5/2019  6:00pm
#Versión: 3.7.2

#Archivos

#importación de librerías
import pickle

#Definicion de funciones:

def grabar(TECfashion,listaRopa):
    """
    Entradas: nombre del archivo a grabar y la lista biblioteca
    Funcion: Graba un archivo
    Salidas: No tiene
    """
    try:
        f=open(TECfashion,"wb")
        pickle.dump(listaRopa,f)
        f.close()
    except:
        print("Error al grabar el archivo: ",TECfashion)
    return

def lee(TECfashion,listaRopa):
    """
    Entradas: nombre del archivo a leer y la lista biblioteca.
    Funcion: Lee un archivo previamente nombrado
    Salidas: No tiene
    """
    try:
        f=open("TECfashion","rb")
        listaRopa=pickle.load(f)
        f.close()
    except FileNotFoundError:
        grabar(TECfashion,listaRopa)
    except:
        print("Error al leer el archivo: ", TECfashion)
    return listaRopa

