

class node:
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next

    def __str__(self):
        return str(self.dato)+str("\n")

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, dato):
        if not self.head:
            self.head = node(dato=dato)
            self.size+=1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node(dato=dato)
        self.size+=1

    def iterar(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        String = ""
        node = self.head
        while node != None:
            String += str(node)
            node = node.next
        return String

    def search(self, id):
        current = self.head

        while current and current.dato.id != id:
            current = current.next
        return current

    def searchxy(self, id, x, y):
        current = self.head

        while current and int(current.dato.id)!=id and int(current.dato.x)!=x and int(current.dato.y)!=y:
            current = current.next
        return current

    def searchxyz(self, id, x, y):
        aux=True
        aux2=None
        node = self.head
        while aux:
            if int(node.dato.id)==id and int(node.dato.x)==x and int(node.dato.y)==y:
                aux=False
                aux2=node
            elif node==None:
                aux=False
                aux2=0
            else:
                node = node.next
        return aux2

