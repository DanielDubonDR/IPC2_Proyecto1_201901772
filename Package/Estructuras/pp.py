class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
 
class create_circular_linked_list(object):
    
    
    def __init__(self):
        self.head = None
 
    def is_empty(self):
        
        return self.head is None
 
    def length(self):
       
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
                         # Si el siguiente nodo del nodo actual es el nodo principal, significa que este nodo es el nodo de cola
                         # Si no, mueva el puntero hacia atrás
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count
 
    def add_first(self, data):
        
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
                         # Mueva el puntero al nodo de cola
            while cur.next is not self.head:
                cur = cur.next
                         # El nodo de cola apunta al nuevo nodo
            cur.next = node
                         # El nuevo nodo apunta al nodo principal original
            node.next = self.head
                         # Luego dele el título del nodo principal al nuevo nodo
            self.head = node
 
    def add_last(self, data):
        
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
                         # Mueve el puntero al final
            while cur.next is not self.head:
                cur = cur.next
                         # El nodo de cola apunta al nuevo nodo
            cur.next = node
                         # El nuevo nodo apunta al nodo principal
            node.next = self.head
 
    def insert_node(self, index, data):
                
        node = Node(data)
        if index < 0 or index > self.length():
            print ("Posición de inserción incorrecta")
            return False
        elif index == 0:
            self.add_first(data)
        else:
            cur = self.head
            pre = Ninguno # pre es el nodo anterior del nodo señalado por el puntero actual
            count = 0
                         # Mueva el puntero a la posición para insertar
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            pre.next = node
            node.next = cur
 
    def remove_node(self, data):
                
        if self.is_empty():
            return
                 # Si el nodo a eliminar es el nodo principal
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
                         # Mover a la posición del nodo que se va a eliminar
            while cur.data != data:
                pre = cur
                cur = cur.next
                         # Apunte el nodo precursor del nodo que se va a eliminar al nodo posterior, de modo que se omita el nodo central
            pre.next = cur.next
 
    def travel(self):
                
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)
 
    def is_exist(self, data):
                 
        cur = self.head
        while cur is not None:
                         # Encuentra el nodo encontrado
            if cur.data == data:
                return True
                         # La cola ha sido encontrada
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False
 
 
if __name__ == '__main__':
    lists = create_circular_linked_list()
    lists.add_last(2)
    lists.add_first(1)
    lists.add_first(0)
    lists.add_last(3)
    lists.insert_node(2, 8)
    lists.travel()
    print ("Longitud de la lista:", lists.length ())
    lists.remove_node(8)
    lists.travel()
    print(lists.is_exist(2))
