from LinkedList import linked_list
from Funciones.Graficar import graficar

class dato:
    def __init__(self, id, numero, x, y):
        self.id = id
        self.numero = numero
        self.x = x
        self.y = y

    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\nNumero: ") + str(self.numero) + str("\nx: ") + str(self.x) + str("\ny: ") + str(self.y)+ str("\n")
        return String

class Procesar:

    lista=None

    def __init__(self, datos, cabeceras):
        self.datos=datos
        self.cabeceras=cabeceras
        global lista
        lista=linked_list()

    def imprimir(self):
        print(lista)
        graficar(1,lista, self.cabeceras)

    def obtenerPatronesAcceso(self):
        for i in self.datos.iterar():
            cambio=int(i.dato.numero)
            if cambio>0:
                cambio = 1
            else:
                cambio = 0
            aux = dato(i.dato.id,cambio,i.dato.x,i.dato.y)
            lista.append(aux)

    def buscar(self):
        print(lista.searchxyz(2, 3 ,6))
        '''
        for i in lista.iterar():
            if i.dato.id==0:
                print(i)
                '''
            