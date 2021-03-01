#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from Estructuras.LinkedList import linked_list
import xml.dom.minidom as minidom

#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
doc=minidom.parse("entrada1.xml")
matrices=doc.getElementsByTagName("matriz")
cabeceras = linked_list()
listaPrueba = linked_list()

#----------------------------------------------------CLASES--------------------------------------------------
class cabecera:
    def __init__(self, id, nombreMatriz, n, m):
        self.id = id
        self.nombreMatriz = nombreMatriz
        self.n = n
        self.m = m

    def __str__(self):
        String = str("id: ") + str(self.id) + str("\nNombre: ") + str(self.nombreMatriz) + str("\nn: ") + str(self.n)+ str("\nm: ") + str(self.m)+str("\n")
        return String

class dato:
    def __init__(self, numero, x, y):
        self.numero = numero
        self.x = x
        self.y = y

    def __str__(self):
        String = str("Numero: ") + str(self.numero) + str("\nx: ") + str(self.x) + str("\ny: ") + str(self.y)+ str("\n")
        return String

class l2:
    def __init__(self, fila, dato):
        self.fila=fila
        self.dato = dato

    def __str__(self):
        String = str("Fila: ") + str(self.fila) + str("\nDato: ") + str(self.dato) + str("\n")
        return String

class l3:
    def __init__(self, id, dato):
        self.id = id
        self.dato = dato

    def __str__(self):
        String = str("id: ") + str(self.id) + str("\nDato: ") + str(self.dato) + str("\n")
        return String

'''
class lista:
    def __init__(self, id, lista):
        self.id = id
        self.lista = lista

    def __str__(self):
        String = str("id: ") + str(self.id) + str("\nlista: ") + str(self.nx) + str("\ny: ") + str(self.y)+ str("\n")
        return String
'''
#---------------------------------------------------FUNCIONES------------------------------------------------

def ObtenerCabeceras():
    contador = 0
    for matriz in matrices:
        nombreMatriz=matriz.getAttribute("nombre")
        n=matriz.getAttribute("n")
        m=matriz.getAttribute("m")
        aux = cabecera(contador, nombreMatriz, n, m)
        cabeceras.append(aux)
        contador += 1
    prueba()

def prueba():
    for matriz in matrices:
        nombreMatriz=matriz.getAttribute("nombre")
        for i in cabeceras.iterar():
            m2 = linked_list()
            if nombreMatriz==i.dato.nombreMatriz:
                n=matriz.getAttribute("n")
                m=matriz.getAttribute("m")
                cantidad=int(n)*int(m)
                cont=0
                for x in range(int(n)):
                    m1 = linked_list()
                    for y in range(int(m)):
                        dt = matriz.getElementsByTagName("dato")[cont]
                        aux = dato(dt.firstChild.data,(x+1),(y+1))
                        m1.append(aux)
                        cont += 1
                    aux1 = l2(x, m1)
                    m2.append(aux1)
            aux2 = l3(i, m2)
            listaPrueba.append(aux2)

                        
ObtenerCabeceras()
print(cabeceras)

s=listaPrueba.search(0)
print(s)