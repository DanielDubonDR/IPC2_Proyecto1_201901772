'''
class cliente:
    def __init__(self,id , nombre, no_habitacion):
        self.id = id
        self.nombre = nombre
        self.no_habitacion = no_habitacion

    def __str__(self):
        String = str("id: ") + str(self.id) + str("\nNombre: ") + str(self.nombre) + str("\nHabitación No. ") + str(self.no_habitacion)+str("\n")
        return String
'''

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
        return self.contador

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

'''
c1 = cliente(0,"Estuardo Zapeta", 101)
c2 = cliente(1,"Marco López", 103)
c3 = cliente(2,"Josué Armas", 204)
c4 = cliente(3,"Gladis Olmos", 302)

lista = linked_list()
lista.append(c1)
lista.append(c2)
lista.append(c3)
lista.append(c4)

l2=linked_list()
l2.append(c2)
l2.append(c3)

print(lista.search(2).dato.nombre)

print(l2)
'''