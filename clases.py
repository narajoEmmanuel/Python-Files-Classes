#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 23/5/2019  8:00am 
#Fecha de última Modificación: 27/5/2019  6:00pm
#Versión: 3.7.2

#Clases

class Ropa: #clase base
    
    def __init__(self,pcodigo,pmarca,ptela,pprecio,pprenda):
        """
        Funcionamiento: método constructor de la clase Ropa.
        Entradas: codigo,marca,tela,precio,prenda.
        Salidas: objeto con las variables asignadas.
        """
        self.codigo=pcodigo
        self.marca=pmarca
        self.tela=ptela
        self.precio=pprecio
        self.prenda=pprenda

    def getCodigo(self):
        """
        Funcionamiento: permite obtener el valor almacenado en el atributo.
        Entradas: N/A
        Salidas: codigo del objeto.
        """
        return self.codigo

    def setPrecio(self,pprecio):
        """
        Funcionamiento: permite asignar un valor al atributo.
        Entradas: precio
        Salidas: N/A
        """
        self.precio=pprecio

    def mostrar(self):
        """
        Funcionamiento: mostrar el contenido del objeto Ropa.
        Entradas: N/A
        Salidas: datos almacenados.
        """
        print("-"*29)
        print("Prenda: "+self.prenda)
        print("Código: "+self.codigo)
        print("Marca: "+self.marca)
        print("Tela: "+self.tela)
        print("Precio: "+str(self.precio))

class Camisa(Ropa): #clase derivada de Ropa()

    def __init__(self,pcodigo,pmarca,ptela,pprecio,ptipo,pmanga):
        """
        Funcionamiento: método constructor de la clase Camisa con herencia de Ropa.
        Entradas: codigo,marca,tela,precio,tipo,manga.
        Salidas: objeto con las variables asignadas.
        """
        Ropa.__init__(self,pcodigo,pmarca,ptela,pprecio,"Camisa")
        self.tipo=ptipo
        self.manga=pmanga

    def mostrar(self):
        """
        Funcionamiento: mostrar el contenido del objeto Camisa.
        Entradas: N/A
        Salidas: datos almacenados.
        """
        Ropa.mostrar(self)
        print("Tipo: "+self.tipo)
        print("Manga: "+self.manga)

class Pantalon(Ropa): #clase derivada de Ropa()

    def __init__(self,pcodigo,pmarca,ptela,pprecio,ptalla,ptipo):
        """
        Funcionamiento: método constructor de la clase Pantalon con herencia de Ropa.
        Entradas: codigo,marca,tela,precio,talla,tipo.
        Salidas: objeto con las variables asignadas.
        """
        Ropa.__init__(self,pcodigo,pmarca,ptela,pprecio,"Pantalon")
        self.talla=ptalla
        self.tipo=ptipo
        
    def mostrar(self):
        """
        Funcionamiento: mostrar el contenido del objeto Pantalon.
        Entradas: N/A
        Salidas: datos almacenados.
        """
        Ropa.mostrar(self)
        print("Talla: "+str(self.talla))
        print("Tipo: "+self.tipo)

class Sueter(Ropa): #clase derivada de Ropa()

    def __init__(self,pcodigo,pmarca,ptela,pprecio,ptipo):
        """
        Funcionamiento: método constructor de la clase Sueter con herencia de Ropa.
        Entradas: codigo,marca,tela,precio,tipo.
        Salidas: objeto con las variables asignadas.
        """
        Ropa.__init__(self,pcodigo,pmarca,ptela,pprecio,"Sueter")
        self.tipo=ptipo

    def mostrar(self):
        """
        Funcionamiento: mostrar el contenido del objeto Sueter.
        Entradas: N/A
        Salidas: datos almacenados.
        """
        Ropa.mostrar(self)
        print("Tipo: "+self.tipo)
