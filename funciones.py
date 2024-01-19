#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 23/5/2019  8:00am 
#Fecha de última Modificación: 27/5/2019  6:00pm
#Versión: 3.7.2

#Funciones

#importación de librerias
from archivos import*
from clases import*


#Definicion de funciones

def analizarCodigo(listaRopa,codigo):
    """
    Funcionamiento: validar el código ingresado por el usuario.
    Entradas: codigo y lista de objetos.
    Salidas: variable true.
    """
    if codigo[1:].isdigit() and len(codigo)==4:
        for objeto in listaRopa:
            if codigo==objeto.getCodigo():
                print("Código ya registrado.")
                return
        return True
    else:
        print("Formato inválido.")
        return    

def analizarPrecio(precio):
    """
    Funcionamiento: valida el precio ingresado por el usuario.
    Entradas: precio
    Salidas: N/A
    """
    while precio>90000 or precio<=0:
        print("Precio inválido. El monto debe ser un número positivo menor a 90 000.")
        precio=int(input("Precio: "))

    
def agregarCamisa(listaRopa,codigo):#1
    """
    Funcionamiento: permite el ingreso de datos (camisas) al inventario.
    Entradas: codigo y lista de objetos.
    Salidas: nuevo objeto en la lista de ropa.
    """
    try:
        x=analizarCodigo(listaRopa,codigo)
        if x==True:
            print("--Indique las características de la camisa--")
            marca=input("Marca: ")
            tela=input("Tela (algodón, lino, punto): ")
            precio=int(input("Precio: "))
            analizarPrecio(precio)
            tipo=input("Tipo (polo, vestir): ")
            manga=input("Manga (larga, corta): ")
            ropaNueva=Camisa(codigo,marca,tela,precio,tipo,manga)#Instanciar variable
            listaRopa.append(ropaNueva)
            grabar("TECfashion",listaRopa)
            print("\n---Datos guardados correctamente!---")
        return
    except ValueError:
        print("El precio debe ser un número. Intente de nuevo.")
        return
    
def agregarPantalon(listaRopa,codigo):#2
    """
    Funcionamiento: permite el ingreso de datos (pantalones) al inventario.
    Entradas: codigo y lista de objetos.
    Salidas: nuevo objeto en la lista de ropa.
    """
    try:
        x=analizarCodigo(listaRopa,codigo)
        if x==True:
            print("--Indique las características del pantalón--")
            marca=input("Marca: ")
            tela=input("Tela (algodón, lino, punto): ")
            precio=int(input("Precio: "))
            analizarPrecio(precio)
            talla=int(input("Talla (28,30,32,34,36,38,40): "))
            tipo=input("Tipo (largo, corto): ")
            ropaNueva=Pantalon(codigo,marca,tela,precio,talla,tipo)#Instanciar variable
            listaRopa.append(ropaNueva)
            grabar("TECfashion",listaRopa)
            print("\n---Datos guardados correctamente!---")
        return
    except ValueError:
        print("El precio debe ser un número. Intente de nuevo.")
        return

def agregarSueter(listaRopa,codigo):#3
    """
    Funcionamiento: permite el ingreso de datos (sueters) al inventario.
    Entradas: codigo y lista de objetos.
    Salidas: nuevo objeto en la lista de ropa.
    """
    try:
        x=analizarCodigo(listaRopa,codigo)
        if x==True:
            print("--Indique las características del suerter--")
            marca=input("Marca: ")
            tela=input("Tela (algodón, lino, punto): ")
            precio=int(input("Precio: "))
            analizarPrecio(precio)
            tipo=input("Tipo (con gorro, sin gorro): ")
            ropaNueva=Sueter(codigo,marca,tela,precio,tipo)#Instanciar variable
            listaRopa.append(ropaNueva)
            grabar("TECfashion",listaRopa)
            print("\n---Datos guardados correctamente!---")
        return
    except ValueError:
        print("El precio debe ser un número. Intente de nuevo.")
        return
    
def eliminarProducto(listaRopa,codEliminar):#4
    """
    Funcionamiento: elimina un objeto de la lista.
    Entradas: codigo y lista de objetos.
    Salidas: lista de ropa sin el objeto eliminado.
    """
    for objeto in listaRopa:
        if codEliminar==objeto.getCodigo():
            print("\nSe eliminarán los siguientes datos:")
            objeto.mostrar()
            listaRopa.remove(objeto)
            grabar("TECfashion",listaRopa)
            print("\n---El producto se ha eliminado correctamente!---")
            return
    print("El código no se encuentra registrado.")
    return
    
def cambiarPrecioProducto(listaRopa,codigo):#5
    """
    Funcionamiento: cambiar dato (precio) de un objeto.
    Entradas: codigo y lista de objetos.
    Salidas: lista de ropa con el objeto modificado.
    """
    for objeto in listaRopa:
        if codigo==objeto.getCodigo():
            objeto.mostrar()
            precioNuevo=int(input("\nIndique el nuevo precio del producto: "))
            analizarPrecio(precioNuevo)
            objeto.setPrecio(precioNuevo)
            grabar("TECfashion",listaRopa)
            print("\n---El precio se ha modificado correctamente!---")
            return
    print("El código no se encuentra registrado.")
    return

def mostrarTodo(listaRopa):#6
    """
    Funcionamiento: mostrar todos los datos de los objetos guardados.
    Entradas: lista de objetos.
    Salidas: datos guardados.
    """
    mostrarCamisas(listaRopa)
    mostrarPantalon(listaRopa)
    mostrarSueter(listaRopa)
    return

def mostrarCamisas(listaRopa):#7.1
    """
    Funcionamiento: mostrar los datos de objetos(camisas)  
    Entradas: lista de objetos.
    Salidas: datos de los objetos.
    """
    print("\n"+"Camisas Registradas".center(26,"-"))
    nuevaLista=[]
    for objeto in listaRopa:
        if objeto.prenda=="Camisa":
            nuevaLista.append(objeto)
            objeto.mostrar()
    if nuevaLista==[]:
        print("-"*29)
        print("No hay camisas registrados.")
    return

def mostrarPantalon(listaRopa):#7.2
    """
    Funcionamiento: mostrar los datos de objetos(pantalones)
    Entradas: lista de objetos.
    Salidas: datos de los objetos.
    """
    print("\n"+"Pantalones Registrados".center(26,"-"))
    nuevaLista=[]
    for objeto in listaRopa:
        if objeto.prenda=="Pantalon":
            nuevaLista.append(objeto)
            objeto.mostrar()
    if nuevaLista==[]:
        print("-"*29)
        print("No hay pantalones registrados.")
    return
     
def mostrarSueter(listaRopa):#7.3
    """
    Funcionamiento: mostrar los datos de objetos(sueters)
    Entradas: lista de objetos.
    Salidas: datos de los objetos.
    """
    print("\n"+"Sueters Registrados".center(26,"-"))
    nuevaLista=[]
    for objeto in listaRopa:
        if objeto.prenda=="Sueter":
            nuevaLista.append(objeto)
            objeto.mostrar()
    if nuevaLista==[]:
        print("-"*29)
        print("No hay sueters registrados.")
    return
    
