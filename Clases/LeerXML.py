import xml.dom.minidom as minidom

doc=minidom.parse("entrada2.xml")

matrices=doc.getElementsByTagName("matriz")

for matriz in matrices:
    nombreMatriz=matriz.getAttribute("nombre")
    if nombreMatriz=="Ejemplo":
        n=matriz.getAttribute("n")
        m=matriz.getAttribute("m")
        cantidad=int(n)*int(m)
        cont=0
        for i in range(cantidad):
            dato=matriz.getElementsByTagName("dato")[i]
            print(dato.firstChild.data, end="  ")
            if i==int(n)+(cont-1):
                cont+=int(n)
                print()

