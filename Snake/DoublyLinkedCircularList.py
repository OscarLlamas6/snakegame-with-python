class Nodo: #Clase nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaCircularDoble: #Clase Lista Doblemente Enlazada Circular
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def listavacia(self): #Metodo booleano para verificar si la lista esta o no vacia
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self, dato): #Metodo para agregar al inicio de la lista
        if self.listavacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__circular__()
        self.size = self.size + 1

    def agregar_final(self, dato): #Metodo para agregar al final de la lista
        if self.listavacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__circular__()
        self.size = self.size + 1

    def __circular__(self): #Metodo para crear el enlace circular
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def imprimir_adelante(self):
        if self.listavacia():
            print("Lista vacia!")
        else:
            aux = self.primero
            for i in range(self.size*5):
                print(aux.dato,end=" ")
                aux = aux.siguiente

    def imprimir_atras(self):
        if self.listavacia():
            print("Lista vacia!")
        else:
            aux = self.ultimo
            for i in range(self.size*5):
                print(aux.dato, end=" ")
                aux = aux.anterior








