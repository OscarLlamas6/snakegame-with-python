
class node: # Creamos la clase node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list: # Creamos la clase linked_list

    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = node(data=data, next=self.head)

    def pop(self):
        aux = self.head.next
        self.head = aux
