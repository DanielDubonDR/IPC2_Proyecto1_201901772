#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------

#----------------------------------------------------CLASES--------------------------------------------------


#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
ruta=""

#-------------------------------------------------MENU-------------------------------------------------------
def CargarArchivo():
    global ruta
    print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def ProcesarArchivo():
    if ruta!="":
        print("hacer algo")
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
        print("hacer algo")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def GenerarGrafica():
    if ruta!="":
        print("hacer algo")
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