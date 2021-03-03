from graphviz import Digraph

def graficar(id, datos, cabeceras):
    n=cabeceras.search(id-1).dato.n
    m=cabeceras.search(id-1).dato.m
    s1=str(cabeceras.search(id-1).dato.nombreMatriz)+str(" n = ")+str(n)+str(" m = ")+str(m)
    dot = Digraph(comment='Grafica')
    dot.node('A', 'Matrices')
    dot.node('B', s1)
    dot.edges(['AB'])

    cont=1
    for i in datos.iterar():
        if i.dato.id==(id-1):
            dot.node(str(cont),str(i.dato.numero))
            cont+=1

    magnitud=(int(n)*int(m))-int(m)

    for i in range(1,int(m)+1):
       dot.edge('B',str(i))

    for i in range(1,magnitud+1):
        dot.edge(str(i),str(i+int(m)))

    '''
    cont2=0
    for i in datos.iterar():
        if cont2<int(m):
            if i.dato.id==(id-1):
                dot.edge('B',str(i.dato.numero))
        cont2+=1
        
    
    
    cont3=1
    for i in datos.iterar():
        if cont3<=magnitud:
            if i.dato.id==(id-1):
                dot.edge(str(cont3),str(i.dato.numero+int(m)))
        cont3+=1
    
    '''
    '''
    for x in range(1,m):
        dot.edge('B',str(i.dato.numero+m))

    for x in range(1,magnitud):
        dot.edge(str(cont),str(i.dato.numero+m))

    '''
    #print(dot.source)
    dot.render('D://test-output/round-tble.gv', view=True, format="png")