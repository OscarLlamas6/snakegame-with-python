class Nodo: #Clase nodo
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.siguiente = None
        self.anterior = None


class ListaDoble: #Clase Lista Doblemente Enlazada 
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def listavacia(self): #Metodo booleano para verificar si la lista esta o no vacia
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self, y, x): #Metodo para agregar al inicio de la lista
        if self.listavacia():
            self.primero = self.ultimo = Nodo(y, x)
        else:
            aux = Nodo(y, x)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.size = self.size + 1

    def agregar_final(self, y, x): #Metodo para agregar al final de la lista
        if self.listavacia():
            self.primero = self.ultimo = Nodo(y, x)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(y, x)
            self.ultimo.anterior = aux
        self.size = self.size + 1

    def eliminar_ultimo(self):
        if self.listavacia():
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
        self.size = self.size - 1








