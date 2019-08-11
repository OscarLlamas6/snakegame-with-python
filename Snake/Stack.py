
class node: # Creamos la clase node
    def __init__(self, y=None, x=None,next=None):
        self.y = y
        self.x = x
        self.next = next


class StackList: # Creamos la stack_list

    def __init__(self):
        self.head = None

    def push(self, y, x):
        self.head = node(y=y,x=x, next=self.head)

    def pop(self):
        if self.head is not None:
            if self.head.next is not None:
                aux = self.head.next
                self.head = aux
        
