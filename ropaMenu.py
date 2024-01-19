#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 23/5/2019  8:00am 
#Fecha de última Modificación: 27/5/2019  6:00pm
#Versión: 3.7.2

#Principal

#importación de librerias
from archivos import*
from funciones import*
from clases import Camisa
from clases import Pantalon
from clases import Sueter

#Definicion de funciones:
print("TEC fashion".center(26,"-"))
def menu():
      """
      Funcionamiento: desplegar el menú principal para el usuario.
      Entradas: N/A
      Salidas: información solicitada por el usuario.
      """
      try:
            while True:
                  print("\n"+"Menú Principal".center(26,"-"))
                  print("1-Registro de camisas")
                  print("2-Registro de pantalones")
                  print("3-Registro de sueters")
                  print("4-Eliminar producto")
                  print("5-Cambiar precio")
                  print("6-Mostrar inventario completo")
                  print("7-Mostrar inventario de un producto")
                  print("8-Terminar")
                  opcion=int(input("\nEscoja una opción: "))
                  print("-"*29)
                  if opcion==1:
                        codigo=input("Código (ej: C123): ")
                        codigo=codigo.upper()
                        if codigo.startswith("C"):
                              agregarCamisa(listaRopa,codigo)
                        else:
                              print("El código de la camisa debe iniciar con la letra 'C' (ej: C123).")
                  elif opcion==2:
                        codigo=input("Código (ej: P123): ")
                        codigo=codigo.upper()
                        if codigo.startswith("P"):
                              agregarPantalon(listaRopa,codigo)
                        else:
                              print("El código del pantalón debe iniciar con la letra 'P' (ej: P123).")
                  elif opcion==3:
                        codigo=input("Código (ej: S123): ")
                        codigo=codigo.upper()
                        if codigo.startswith("S"):
                              agregarSueter(listaRopa,codigo)
                        else:
                               print("El código del sueter debe iniciar con la letra 'S' (ej: S123).")
                  elif opcion==4:
                        codEliminar=input("Indique el código del producto a eliminar: ")
                        codEliminar=codEliminar.upper()
                        eliminarProducto(listaRopa,codEliminar)
                  elif opcion==5:
                        codigo=input("Indique el código del producto: ")
                        codigo=codigo.upper()
                        cambiarPrecioProducto(listaRopa,codigo)
                  elif opcion==6:
                        mostrarTodo(listaRopa)
                  elif opcion==7:
                        menuSecundario()
                  elif opcion==8:
                        grabar("TECfashion",listaRopa)
                        break
                  else:
                        print("Opción incorrecta.")
      except ValueError:
            print("-"*29)
            print("Opción incorrecta.")
            menu()


def menuSecundario():
      """
      Funcionamiento: desplegar el menú secundarioal usuario.
      Entradas: N/A
      Salidas: la informacion que solicita el usuario.
      """
      print("\n"+"Menú Secundario".center(26,"-"))
      print("1-Información completa de todas las camisas")
      print("2-Información completa de todos los pantalones")
      print("3-Información completa de todas las suerters.")
      try:
            opcionMenuSec=int(input("\nEscoja una opción: "))
            print("-"*29)
            if opcionMenuSec==1:
                  mostrarCamisas(listaRopa)
            elif opcionMenuSec==2:
                  mostrarPantalon(listaRopa)
            elif opcionMenuSec==3:
                  mostrarSueter(listaRopa)
            else:
                  menuSecundario()
      except ValueError:
            menuSecundario()
#------------------------------------------------------------------------------------------------------------

#Definición de variables globales
listaRopa=[]
#Programa Principal
listaRopa=lee("TECfashion",listaRopa)
menu()
