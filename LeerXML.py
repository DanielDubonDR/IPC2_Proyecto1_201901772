#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from LinkedList import linked_list
from LinkedListCircular import linked_list_circular
import xml.dom.minidom as minidom

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
    def __init__(self, id, numero, x, y):
        self.id = id
        self.numero = numero
        self.x = x
        self.y = y

    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\nNumero: ") + str(self.numero) + str("\nx: ") + str(self.x) + str("\ny: ") + str(self.y)+ str("\n")
        return String

class Procesar:
    doc=None
    matrices=None
    cabeceras=None
    listaM=None

    def __init__(self, ruta):
        global doc
        global matrices
        global cabeceras
        global listaM
        doc=minidom.parse(ruta)
        matrices=doc.getElementsByTagName("matriz")
        cabeceras = linked_list()
        listaM = linked_list_circular()

    def ObtenerCabeceras(self):
        contador = 0
        for matriz in matrices:
            nombreMatriz=matriz.getAttribute("nombre")
            n=matriz.getAttribute("n")
            m=matriz.getAttribute("m")
            aux = cabecera(contador, nombreMatriz, n, m)
            cabeceras.append(aux)
            contador += 1
        #print(cabeceras)

    def extraerDatos(self):
        for matriz in matrices:
            nombreMatriz=matriz.getAttribute("nombre")
            for i in cabeceras.iterar():
                m1 = linked_list()
                if nombreMatriz==i.dato.nombreMatriz:
                    n=matriz.getAttribute("n")
                    m=matriz.getAttribute("m")
                    cantidad=int(n)*int(m)
                    cont=0
                    for x in range(cantidad):
                        dt = matriz.getElementsByTagName("dato")[cont]
                        xx=dt.getAttribute("x")
                        y=dt.getAttribute("y")
                        aux = dato(i.dato.id,dt.firstChild.data,(xx),(y))
                        listaM.append(aux)
                        cont += 1
        #print(listaM)
       
    '''
    iniciar()                        
    ObtenerCabeceras()
    '''

    def getCabeceras(self):
        return cabeceras

    def getLista(self):
        return listaM

    


