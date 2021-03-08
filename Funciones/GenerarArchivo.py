import os

def obtenerNgrupos(id, listagrupos):
        cont=0
        for i in listagrupos.iterar():
            if i.dato.id==id:
                cont+=1
        return cont

def crearArchivo(string, ruta):
    try:
        arhcivo=open(ruta,'w')
        arhcivo.write(string)
        arhcivo.close()
        print(" > Se escribió el archivo correctamente")
    except:
        print(" - ERROR: Ocurrió un error al escribir el archivo")
    try:
        os.startfile(ruta)
    except:
        print(" - ERROR: No se pudo abrir el archivo automaticamente, intentelo manualmente en la ruta antes indicada")

def archivo(grupos, matricesReducidas,cabeceras, ruta):
    string=str("<?xml version=\"1.0\" ?>")+str("\n<matrices>")
    for headers in cabeceras.iterar():
        string+=str("\n\t<matriz nombre=\"")+str(headers.dato.nombreMatriz)+str("_Salida\"")+str(" n=\"")+str(obtenerNgrupos(headers.dato.id,grupos))+str("\" m=\"")+str(headers.dato.m)+str("\" g=\"")+str(obtenerNgrupos(headers.dato.id,grupos))+str("\">")
        for matrices in matricesReducidas.iterar():
            if headers.dato.id==matrices.dato.id:
                string+=str("\n\t\t<dato x=\"")+str(matrices.dato.x)+str("\" y=\"")+str(matrices.dato.y)+str("\">")+str(matrices.dato.numero)+str("</dato>")    
        
        for frecuencias in grupos.iterar():
            if frecuencias.dato.id==headers.dato.id:
                string+=str("\n\t\t<frecuencia g=\"")+str(frecuencias.dato.g)+str("\">")+str(frecuencias.dato.frecuencia)+str("</frecuencia>")
        string+=str("\n\t</matriz>\n")
    string+=str("\n</matrices>")
    #print(string)
    crearArchivo(string, ruta)