class node:  # Creamos la clase node
    def __init__(self, username="", score=0, next=None):
        self.username = username
        self.score = score
        self.next = next


class QueueList:  # Creamos la clase linked_list

    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, username, score):
        self.size+=1
        if not self.head:
            self.head = node(username=username, score=score)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(username=username, score=score)
      

    def dequeue(self):
        self.size = self.size -1
        if self.head is not None:
            aux = self.head.next
            self.head = aux



