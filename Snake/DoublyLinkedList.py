class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nextval = None

class ListaDoble:
    def __init__(self):
        self.headval = None
        size = 0

# AGREGAR

    def add(self, x, y):
        NewNode = Node(x, y)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
        size = size + 1

# IMPRIMIR
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (" - "+printval.dataval,end="")
            printval = printval.nextval



