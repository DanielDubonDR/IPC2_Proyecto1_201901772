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
            m1 = linked_list()
            if nombreMatriz==i.dato.nombreMatriz:
                n=matriz.getAttribute("n")
                m=matriz.getAttribute("m")
                cantidad=int(n)*int(m)
                cont=0
                for x in range(int(n)):
                    for y in range(int(m)):
                        if cont==0:
                            listaPrueba.append(i)
                        dt = matriz.getElementsByTagName("dato")[cont]
                        aux = dato(dt.firstChild.data,(x+1),(y+1))
                        listaPrueba.append(aux)
                        cont += 1
                        
ObtenerCabeceras()
print(cabeceras)

print(listaPrueba)