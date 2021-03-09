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

class Leer:
    doc=None
    matrices=None
    cabeceras=None
    cabecerasCircular=None
    listaM=None
    listaOrdenada=None

    def __init__(self, ruta):
        print(" > Leyendo archivo...")
        global doc
        global matrices
        global cabeceras
        global cabecerasCircular
        global listaM
        global listaOrdenada
        doc=minidom.parse(ruta)
        matrices=doc.getElementsByTagName("matriz")
        cabeceras = linked_list()
        cabecerasCircular = linked_list()
        listaM = linked_list_circular()
        listaOrdenada = linked_list_circular()

    def ObtenerCabeceras(self):
        print(" > Obteniendo información de las matrices...")
        contador = 0
        for matriz in matrices:
            nombreMatriz=matriz.getAttribute("nombre")
            n=matriz.getAttribute("n")
            m=matriz.getAttribute("m")
            aux = cabecera(contador, nombreMatriz, n, m)
            cabeceras.append(aux)
            cabecerasCircular.append(aux)
            contador += 1


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
                        if int(xx)>int(n):
                            s=str(" - ERROR: fila: ")+str(xx)+str(" fuera del rango de la matriz establecida")
                            print(s)
                        if int(y)>int(m):
                            s=str(" - ERROR: columna: ")+str(y)+str(" fuera del rango de la matriz establecida")
                            print(s)
                        aux = dato(i.dato.id,dt.firstChild.data,(xx),(y))
                        listaM.append(aux)
                        cont += 1
        
        print(" > Datos extraídos del archivo")
       
   
    def verificarOrden(self):
        print(" > Verificando si los datos estan ordenados...")
        desordenado=False
        for i in cabeceras.iterar():
            n=int(i.dato.n)
            m=int(i.dato.m)
            magnitud=n*m
            cont=0
            x=1
            y=1
            for datos in listaM.iterar():
                if int(datos.dato.id)==int(i.dato.id):
                    if int(datos.dato.x)==x and int(datos.dato.y)==y:
                        cont+=1
                    y+=1
                    if y==m+1:
                        y=1
                        x+=1
            if cont!=magnitud:
                desordenado=True
                break
        return desordenado
        
    def ordenar(self):
        print(" > Ordenando datos...")
        global listaOrdenada
        for i in cabeceras.iterar():
            n=int(i.dato.n)
            m=int(i.dato.m)
            magnitud=n*m
            for x in range(1,n+1):
                for y in range(1,m+1):
                    id=self.buscarxy(int(i.dato.id),x,y).dato.id
                    numero=self.buscarxy(int(i.dato.id),x,y).dato.numero
                    xx=self.buscarxy(int(i.dato.id),x,y).dato.x
                    yy=self.buscarxy(int(i.dato.id),x,y).dato.y
                    aux=self.buscarxy(int(i.dato.id),x,y)
                    axx=dato(id,numero,xx,yy)
                    if aux==False:
                        print(" - ERROR: Hacen falta datos, anulando proceso...")
                    else:
                        listaOrdenada.append(axx)
        print(" > Datos ordenados")
        

    def getCabeceras(self):
        return cabeceras

    def getCabecerasCircular(self):
        return cabecerasCircular

    def getLista(self):
        if self.verificarOrden():
            print(" > Los datos estan desordenados")
            self.ordenar()
            print(listaOrdenada)
            return listaOrdenada
        else:
            print(" > Los datos estan ordenados")
            return listaM

    def buscarxy(self, id, x, y):
        encontrado=False
        aux=None
        for buscar in listaM.iterar():
            if int(buscar.dato.id)==id and int(buscar.dato.x)==x and int(buscar.dato.y)==y:
                encontrado=True
                aux=buscar
                break
        if encontrado==True:
            return aux
        else:
            return False



    


