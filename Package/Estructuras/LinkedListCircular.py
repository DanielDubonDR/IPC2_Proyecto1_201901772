class cliente:
    def __init__(self, id, nombre, no_habitacion):
        self.id = id
        self.nombre = nombre
        self.no_habitacion = no_habitacion

    def __str__(self):
        String = str("id: ") + str(self.id) + str("\nNombre: ") + str(self.nombre) + \
            str("\nHabitación No. ") + str(self.no_habitacion)+str("\n")
        return String

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

       

    def imprimir(self):
        if self.head is None:
            return
        node = self.head
        print(node.dato.nombre, end=" => ")
        while node.next != self.head:
            node = node.next
            print(node.dato.nombre, end=" => ")

    def eliminar(self, no_habitacion):
        node = self.head
        previous = None

        while True:
            if node.dato.no_habitacion == no_habitacion:
                if previous is not None:
                    previous.next = node.next
                else:
                    while node.next != self.head:
                        node = node.next
                    node.next = self.head.next
                    self.head = self.head.next
                self.size -= 1
                return True
            elif node.next == self.head:
                return False

            previous = node
            node = node.next

            def iterar(self):
                node = self.head
                while node != None:
                    yield node
                    node = node.next

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


c1 = cliente(0,"Estuardo Zapeta", 101)
c2 = cliente(1,"Marco López", 103)
c3 = cliente(2,"Josué Armas", 204)
c4 = cliente(3,"Gladis Olmos", 302)

lista = linked_list_circular()
lista.append(c1)
lista.append(c2)
lista.append(c3)
lista.append(c4)

print(lista)