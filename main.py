#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from LeerXML import Leer
from Funciones.Graficar import graficar
from Procesar import Procesar
#----------------------------------------------------CLASES--------------------------------------------------


#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
ruta="entrada1.xml"
cabeceras=None
datos=None

#-------------------------------------------------MENU-------------------------------------------------------
def CargarArchivo():
    global ruta
    print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def ProcesarArchivo():
    if ruta!="":
        print("\n---------------------------------PROCESAR ARCHIVO---------------------------------\n")
        global cabeceras
        global datos
        print(" > Leyendo archivo...")
        archivo = Leer(ruta)
        print(" > Obteniendo información de las matrices...")
        archivo.ObtenerCabeceras()
        cabeceras = archivo.getCabeceras()
        archivo.extraerDatos()
        print(" > Datos extraídos del archivo")
        datos=archivo.getLista()
        print(" > Procesando datos...")
        procesar=Procesar(datos,cabeceras)
        print(" > Calculando matrices de patrones de acceso...")
        procesar.obtenerPatronesAcceso()
        print(" > Formando grupos...")
        procesar.buscarGrupos()
        procesar.gruposFrecuencias()
        print(" > Realizando suma de tuplas...")
        procesar.sumar()
        print(" > Matrices reducidas de frecuencias de accesos obtenidas")
        print(" > Archivo procesado con éxito")
        
        input("\n- PRESIONE ENTER PARA CONTINUAR...")
        #procesar.imprimir()
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def EscribirArchivo():
    if ruta!="":
        print("hacer algo")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def MostrarEstudiante():
    if ruta!="":
        print("\n-------------------------------DATOS DEL ESTUDIANTE-------------------------------\n")
        print("  > Daniel Reginaldo Dubon Rodriguez")
        print("  > 201901772")
        print("  > Introduccion a la Progrmacion y Computacion 2 Seccion \"A\"")
        print("  > Ingenieria en Ciencias y Sistemas")
        print("  > 5to Semestre")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def GenerarGrafica():
    if ruta!="":
        '''
        archivo = Leer(ruta)
        archivo.ObtenerCabeceras()
        cabeceras = archivo.getCabeceras()
        archivo.extraerDatos()
        datos=archivo.getLista()
        '''
        z=len(cabeceras)+1
        opcion=0
        while opcion!=z:
            cont=0
            String=""
            print("\n--------------------------------SELECCIONAR GRÁFICA-------------------------------")
            for i in cabeceras.iterar():
                cont+=1
                String+=str("\n ")+str(cont)+str(". ")+str(i.dato.nombreMatriz)
            print(String)
            print(" "+str(cont+1)+". Regresar\n")
            try:
                opcion=int(input("- Ingrese una opción:\n  > "))
                if opcion>z or opcion<1:
                    print("\n > Opción inválida...")
                    input(" - PRESIONE ENTER PARA CONTINUAR...")
                else:
                    if opcion!=z:
                        graficar(opcion,datos,cabeceras)
            except:
                print("\n > Opción inválida...")
                input(" - PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def salir():
    print("  > Saliendo...\n")

def menu():
    opcion=0
    while opcion!=6:
        print("\n----------------------------------MENÚ PRINCIPAL----------------------------------\n")
        print(" 1. Cargar archivo")
        print(" 2. Procesar archivo")
        print(" 3. Escribir archivo salida")
        print(" 4. Mostrar datos del estudiante")
        print(" 5. Generar gráfica")
        print(" 6. Salir\n")
        opcion=int(input("- Ingrese una opción:\n  > "))
        switch={1:CargarArchivo, 2: ProcesarArchivo, 3: EscribirArchivo, 4: MostrarEstudiante, 5: GenerarGrafica, 6: salir}
        func=switch.get(opcion,"Opción inválida")
        try:
            func()
        except:
            print("\n > Opción inválida...")
            input(" - PRESIONE ENTER PARA CONTINUAR...")
menu()