      

class node:
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next

    def __str__(self):
        return str(self.dato)+str("\n")


class linked_list_circular:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, dato):
        if self.size == 0:
            self.head = node(dato=dato)
            self.head.next = self.head
        else:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            new_node = node(dato=dato, next=cur.next)
            cur.next = new_node
        self.size += 1


    def iterar(self):
        node = self.head
        yield node
        while node.next != self.head:
            node = node.next
            yield node

    def searchxy(self, id, x, y):
        aux=True
        aux2=None
        node = self.head
        while aux:
            if int(node.dato.id)==id and int(node.dato.x)==x and int(node.dato.y)==y:
                aux=False
                aux2=node
            else:
                node = node.next
        return aux2

    def __len__(self):
        return self.size

    def __str__(self):
        String = ""
        if self.head is None:
            return
        node = self.head
        String += str(node)
        while node.next != self.head:
            node = node.next
            String += str(node)
        return String

