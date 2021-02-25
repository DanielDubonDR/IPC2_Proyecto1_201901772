class cliente:
  def __init__(self, nombre, no_habitacion):
    self.nombre = nombre
    self.no_habitacion = no_habitacion

class node:
  def __init__(self, cliente=None, next=None):
    self.cliente = cliente
    self.next = next

class linked_list:
  def __init__(self):
    self.head = None

  def insertar(self, cliente):
    if not self.head:
      self.head = node(cliente=cliente)
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = node(cliente=cliente)
  
  def imprimir(self):
    node = self.head
    while node != None:
      print(node.cliente.nombre, end = "=>")
      node = node.next
    
  def eliminar(self, no_habitacion):
    current = self.head
    previous = None

    while current and current.cliente.no_habitacion != no_habitacion:
      previous = current
      current = current.next
    if previous is None:
      self.head =current.next
    elif current:
      previous.next = current.next
      current.next = None

c1 = cliente("Estuardo Zapeta", 101)
c2 = cliente("Marco López", 103)
c3 = cliente("Josué Armas", 204)
c4 = cliente("Gladis Olmos", 302)

lista = linked_list()
lista.insertar(c1)
lista.insertar(c2)
lista.insertar(c3)
lista.insertar(c4)

lista.imprimir()