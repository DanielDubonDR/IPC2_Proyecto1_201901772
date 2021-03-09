from graphviz import Digraph

def graficar(id, datos, cabeceras):
    n=cabeceras.search(id-1).dato.n
    m=cabeceras.search(id-1).dato.m
    name=str("Gráficas/")+str(cabeceras.search(id-1).dato.nombreMatriz)+str(".gv")
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

    #print(dot.source)
    dot.render(name, view=True, format="png")