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

class lsreducir:
    def __init__(self, id, f1, f2):
        self.id = id
        self.f1 = f1
        self.f2 = f2
    
    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\nf1: ") + str(self.f1) + str("\nf2: ") + str(self.f2)+  str("\n")
        return String

class frecuencias:
    def __init__(self, id, grupo, frecuencia):
        self.id = id
        self.grupo = grupo
        self.frecuencia = frecuencia
    
    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\nfila: ") + str(self.grupo) + str("\nfrecuencia: ") + str(self.frecuencia)+  str("\n")
        return String

class Procesar:

    lista=None
    listaf=None
    listagrupos=None

    def __init__(self, datos, cabeceras):
        self.datos=datos
        self.cabeceras=cabeceras
        global lista
        global listaf
        global listagrupos
        lista=linked_list()
        listaf=linked_list()
        listagrupos=linked_list()
        

    def imprimir(self):
        print(lista)
        graficar(2,lista, self.cabeceras)

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
        #print(lista.searchxyz(2, 3 ,2))
        ids=len(self.cabeceras)
        for id in range(int(ids)):
            
            n=self.cabeceras.search(id).dato.n
            m=self.cabeceras.search(id).dato.m
            aux=int(n)+1
            for i in range(1, int(n)):
                agregarMismo=True
                repetido=False
                for v in listaf.iterar():
                    if int(v.dato.f2)==i and int(v.dato.id==id):
                        repetido=True
                        break
                if repetido==True:
                    continue
                ccn=0
                for j in range(1,aux-i):
                    cont=0
                    for mm in range(1,int(m)+1):
                        if int(lista.searchxyz(id, i ,mm).dato.numero)==int(lista.searchxyz(id, (j+i) ,mm).dato.numero):
                            cont+=1
                            
                            '''
                            string = str("id ")+str(id)+str(" pares ") +str(i)+str(",")+str(mm)+str(" con ")+str(j+i)+str(",")+str(mm)
                            print(string)
                            '''         
                    if cont==int(m):
                        ccn+=1
                        '''
                        string = str("se encontro coincidencias en la matriz ")+str(id)+str(" filas ")+str(i)+str(" con ")+str(j+i)
                        print(string)
                        '''

                        if agregarMismo==True:
                            ags=lsreducir(id, i,i)
                            listaf.append(ags)
                            agregarMismo=False
                    
                        aux1=lsreducir(id, i,(j+i))
                        listaf.append(aux1)
                if ccn==0:
                    '''
                    string = str("NO se encontro coincidencias en la matriz ")+str(id)+str(" fila ")+str(i)
                    print(string)
                    '''
                    ags=lsreducir(id, i,i)
                    listaf.append(ags)
                elif ccn>0:
                    ccn=0
        #self.sumar()
        self.gruposFrecuencias()
        #print(listaf)
        

    def sumar(self):
        idm=len(self.cabeceras)
        for idmatriz in range(idm):
            for ad in listaf.iterar():
                if ad.dato.id==idmatriz:
                    
                    
                    n=self.cabeceras.search(idmatriz).dato.n
                    self.frecuencia(idmatriz, n, 3)
                    #print(self.datos.searchxy(idmatriz,ad.dato.f2,1))

        #print(self.datos.searchxy(0,1,1))
        #print(listaf)
    def frecuencia(self, id, n, f):
        c=0
        for i in listaf.iterar():
            if i.dato.id==id and int(i.dato.f1)==f:
                c+=1
                print(i)
        st=str(" en ")+str(f)+str(" se repite ")+str(c)    
        print(st)

    def gruposFrecuencias(self):
        idm=len(self.cabeceras)
        for idmatriz in range(idm):
            n=self.cabeceras.search(idmatriz).dato.n
            for i in range(1,int(n)+1):
                c=0
                for ad in listaf.iterar():
                    if int(ad.dato.id)==idmatriz and int(ad.dato.f1)==i: 
                            c+=1
                #st=str("id ")+str(idmatriz)+str(" en ")+str(i)+str(" se repite ")+str(c)    
                #print(st)
                if c>0:
                    aux=frecuencias(idmatriz,i,c)
                    listagrupos.append(aux)
        print(listagrupos)        
                    
