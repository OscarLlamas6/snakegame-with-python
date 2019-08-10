class node:  # Creamos la clase node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:  # Creamos la clase linked_list

    def __init__(self):
        self.head = None
        size = 0

    def enqueue(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    def dequeue(self):
        aux = self.head.next
        self.head = aux
