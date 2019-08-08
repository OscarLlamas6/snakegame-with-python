class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

# AGREGAR

    def Add(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# IMPRIMIR
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (" - "+printval.dataval,end="")
            printval = printval.nextval



