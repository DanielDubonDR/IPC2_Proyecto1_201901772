from graphviz import Digraph

def graficar(id, datos, cabeceras):
    s1=str(cabeceras.search(id-1).dato.nombreMatriz)+str(" n = ")+str(cabeceras.search(id-1).dato.n)+str(" m = ")+str(cabeceras.search(id-1).dato.m)
    dot = Digraph(comment='Grafica')
    dot.node('A', 'Matrices')
    dot.node('B', s1)
    dot.edges(['AB'])
    #print(dot.source)
    dot.render('D://test-output/round-tble.gv', view=True, format="png")