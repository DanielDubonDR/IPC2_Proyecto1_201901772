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
    def __init__(self, id,g, f1, f2):
        self.id = id
        self.g = g
        self.f1 = f1
        self.f2 = f2
    
    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\nf1: ")+ str("\ngrupo: ") + str(self.g) + str(self.f1) + str("\nf2: ") + str(self.f2)+  str("\n")
        return String

class frecuencias:
    def __init__(self, id, g, grupo, frecuencia):
        self.id = id
        self.g = g
        self.grupo = grupo
        self.frecuencia = frecuencia
    
    def __str__(self):
        String = str("id: ") + str(self.id)+ str("\ngrupo: ") + str(self.g)+ str("\nfila: ") + str(self.grupo) + str("\nfrecuencia: ") + str(self.frecuencia)+  str("\n")
        return String

class Procesar:

    lista=None
    listaf=None
    listagrupos=None
    listaPrevSuma=None

    def __init__(self, datos, cabeceras):
        self.datos=datos
        self.cabeceras=cabeceras
        global lista
        global listaf
        global listagrupos
        global listaPrevSuma
        lista=linked_list()
        listaf=linked_list()
        listagrupos=linked_list()
        listaPrevSuma=linked_list()
        

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
            gg=1
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
                        string = str("se encontro coincidencias en la matriz ")+str(id)+str(" grupo ")+str(gg)+str(" filas ")+str(i)+str(" con ")+str(j+i)
                        print(string)
                        '''

                        if agregarMismo==True:
                            ags=lsreducir(id,gg, i,i)
                            listaf.append(ags)
                            agregarMismo=False
                    
                        aux1=lsreducir(id,gg, i,(j+i))
                        listaf.append(aux1)
                if ccn==0:
                    '''
                    string = str("NO se encontro coincidencias en la matriz ")+str(id)+str(" grupo ")+str(gg)+str(" fila ")+str(i)
                    print(string)
                    '''
                    ags=lsreducir(id,gg, i,i)
                    listaf.append(ags)
                elif ccn>0:
                    ccn=0
                gg+=1
        #self.sumar()
        self.gruposFrecuencias()
        #print(listaf)
    '''    
    def frecuencia(self, id, n, f):
        c=0
        for i in listaf.iterar():
            if i.dato.id==id and int(i.dato.f1)==f:
                c+=1
                print(i)
        st=str(" en ")+str(f)+str(" se repite ")+str(c)    
        print(st)
    '''
    def gruposFrecuencias(self):
        idm=len(self.cabeceras)
        for idmatriz in range(idm):
            n=self.cabeceras.search(idmatriz).dato.n
            cont=1
            for i in range(1,int(n)+1):
                c=0
                for ad in listaf.iterar():
                    if int(ad.dato.id)==idmatriz and int(ad.dato.f1)==i: 
                            c+=1
                #st=str("id ")+str(idmatriz)+str(" en ")+str(i)+str(" se repite ")+str(c)    
                #print(st)
                if c>0:
                    aux=frecuencias(idmatriz,cont,i,c)
                    listagrupos.append(aux)
                    cont+=1
        print(listagrupos) 
        print(self.obtenerNgrupos(0))  
        print(self.obtenerFrecuenciaGrupo(0,3))     
                    
    def sumar(self):
        idm=len(self.cabeceras)
        for idmatriz in range(idm):
            n=self.cabeceras.search(idmatriz).dato.n
            m=self.cabeceras.search(idmatriz).dato.m
            for i in listaf.iterar():
                if i.dato.id==idmatriz:

                    
                    #print(self.datos.searchxy(idmatriz,ad.dato.f2,1))

        #print(self.datos.searchxy(0,1,1))
        #print(listaf)
    
    def obtenerNgrupos(self, id):
        cont=0
        for i in listagrupos.iterar():
            if i.dato.id==id:
                cont+=1
        return cont

    def obtenerFrecuenciaGrupo(self, id, grupo):
        for i in listagrupos.iterar():
            if i.dato.id==id and i.dato.g==grupo:
                return int(i.dato.frecuencia)-1