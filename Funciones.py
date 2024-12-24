from Librerias import *

ventana = tkinter.Tk()
ventana.geometry("1100x500")
ventana.title("Programa informático del grupo 7")
ventana.config(bg="White")
ventana.resizable(0,0)

photo5 = PhotoImage(file="Imagen_danger.gif")

def Ocultar():
    ventana.withdraw()

def Mostrar():
    ventana.deiconify()

def AcercaDe():
    messagebox.showinfo("Acerca de...", "Programa hecho por: \n*Elías Jara\n*Paul Estigarribia"
                        "\n*Anahi Talavera\n*Francisco Aguero\n*Jaime Nuñez")

def AbrirArchivo():
    # La variable archivo tiene guardad toda la direccion del archivo= D/carpeta/carpeta
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="./Proyectos")
    # Aca Guardamos todos esos datos en una lista divididos por sus "/"
    archivo = archivo.split("/")
    # Elegimos el ultimo elemento de la lista que contiene el nombre del proyecto incluido el .txt
    archivoAbierto = archivo[len(archivo) - 1]

    # Abrimos el proyecto y guardamos los datos del proyecto en una lista para usarla despues
    ProyectoAbierto = open(f"./Proyectos/{archivoAbierto}", "rt")
    DatosDelProyectoAbierto = ProyectoAbierto.readline()
    ProyectoAbierto.close()
    # Los datos del poryecto lo agregamos a una lista para un mejor manejo
    DatosDelProyectoAbierto = DatosDelProyectoAbierto.split(";")

    # Abrimos el txt donde almacenamos el identificador actual de proyecto y lo modificamos por el proyecto a elegir
    NuevoIdentificadorProyecto = open("./identificador.txt", "wt")
    NuevoIdentificadorProyecto.write(f"{DatosDelProyectoAbierto[0]}")
    NuevoIdentificadorProyecto.close()

    def VentanaError():
        def cerrarError():
            VentError.destroy()

        VentError = tkinter.Toplevel()
        VentError.geometry("300x330")
        VentError.config(bg="white")
        VentError.resizable(0, 0)
        VentError.grab_set_global()

        cabezera = tkinter.Label(VentError, text="ERROR!", font="Helvetica 25", bg="white")
        cabezera.pack(fill=tkinter.X)

        tituloError = Label(VentError,
                            text="Datos ingresados incorrectos.\nFavor ingresar los datos como se especifican.",
                            bg="white", font="Helvetica 10")
        tituloError.place(x=20, y=170)

        BotonOk = tkinter.Button(VentError, text="Entendido", padx=20, pady=10, command=cerrarError)
        BotonOk.place(x=100, y=230)

        leti = Label(VentError, image=photo5).place(x=100, y=50)

def sol_fecha(fecha):
    fecha=fecha.split("/")
    for K in range (3):
        fecha[K]=int(fecha[K])
    return fecha

def textofecha(F):
    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    fecha = str(F[2])+" de "+meses[F[1]-1]+" del "+ str(F[0])
    return fecha

def futuro(F,D):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    while D>=365:
        if bisiesto(F[0]+1):
            F[0]=F[0]+1
            D=D-366
        else:
            F[0]=F[0]+1
            D=D-365
    K=0
    while D>dias[K]:
        F[1]=F[1]+1
        D=D-dias[K]
        K=K+1
    F[2]=F[2]+D
    final=textofecha(F)
    return final

def CalculoFechas(A, identificador, duracion, relacion, contador, fechaInicio, nombre):
    A.append(0)
    A[contador] = Actividad(identificador, duracion, A[relacion], fechaInicio, nombre)

    if duracion == "f" or duracion == "F":
        RELACIONADOS=[]
        RELACIONES=[]
        for I in range(1, len(A)-1):
            for J in range(1, len(A)-1):
                if A[I].IDENTIFICADOR == A[J].IDENTIFICADOR and I != J:
                    #print("A[",I,"]=",A[I].IDENTIFICADOR,"A[",J,"]=",A[J].IDENTIFICADOR)
                    RELACIONADOS.append(I)
                    RELACIONES.append(A[I].ANT.IDENTIFICADOR)
        #print(REL)
        MAT_MAYOR = [[0,0],[0,0]]
        for I in range(len(RELACIONADOS)):
            i = RELACIONADOS[I]
            if MAT_MAYOR[0][0] < A[i].MAT[0][0]:
                MAT_MAYOR = A[i].MAT
        for I in range(len(RELACIONADOS)):
            i = RELACIONADOS[I]
            A[i].MAT = MAT_MAYOR
        for I in range(len(RELACIONADOS)):
            i = RELACIONADOS[I]
            j = RELACIONES[I]
            A[i].fechasTardias(A[j])
        for I in range(1, len(A) - 1):
            fecha = sol_fecha(A[I].FECHA_INICIO)
            fecha2 = sol_fecha(A[I].FECHA_INICIO)
            A[I].FECHA_INICIO = textofecha(fecha)
            A[I].FECHA_FIN = futuro(fecha, A[I].DURACION)
            A[I].FECHA_FIN_TARDIO = futuro(fecha2, A[I].MAT[1][1] - A[I].MAT[0][1])
            A[I].FECHA_INICIO_TARDIO = futuro(fecha2, -A[I].DURACION)

def CalculoCaminoCritico(A):
    #Calculo Camino Crítico
    CAMINO_CRITICO = []
    for I in range(1, len(A)-1):
        if (A[I].MAT[0][0] - A[I].MAT[1][0]) == 0 and (A[I].MAT[0][1] - A[I].MAT[1][1]) == 0:
            CAMINO_CRITICO.append(A[I].IDENTIFICADOR)
    return CAMINO_CRITICO

def creamat (M,N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append( [0] * N )
    return (MATRIZ)

#Procedimiento que lee una matriz
def leemat (MATRIZ):
    M = len(MATRIZ)
    N = len(MATRIZ[0])
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J] = float(input("Ingrese el elemento (%d,%d): " % (I,J)))

#Procedimiento que imprime una matriz
def imprimat (MATRIZ):
    FILAS= len(MATRIZ)
    for I in range(FILAS):
        print (MATRIZ[I])

#Procedimiento que inicializa una matriz
def iniciamat (MATRIZ,VALOR):
    M = len(MATRIZ)
    N = len(MATRIZ[0])
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J] = VALOR

class Actividad():
    #Atributos de la clase
    FIL = 2
    COL = 2

    #Atributos del objeto
    def __init__(self, IDENTIFICADOR, DURACION, ANT, FECHA_INICIO, NOMBRE):
        self.IDENTIFICADOR = IDENTIFICADOR
        self.DURACION = DURACION                            #Define duración
        self.ANT = ANT                                      #Define anterior
        self.SIG = None                                     #Crea variable SIG
        self.FECHA_INICIO = FECHA_INICIO
        self.FECHA_FIN = None
        self.FECHA_INICIO_TARDIO = None
        self.FECHA_FIN_TARDIO = None
        self.NOMBRE = NOMBRE
        self.MAT = creamat(self.FIL, self.COL)              #Crea matriz vacía
        if self.DURACION == 'i' or self.DURACION == 'I':    #Nodo Inicio
            iniciamat(self.MAT,0)                           #Inicializa MAT en 0
        elif self.DURACION == 'f' or self.DURACION == 'F':  #Nodo Fin
            iniciamat(self.MAT,"f")                         #Inicializa MAT en 'f'
            self.ANT.SIG = self                             #Actividad SIG de ANT = Actividad ACTUAL
        else:                                               #Actividad
            self.MAT[0][0] = self.ANT.MAT[0][1]
            self.MAT[0][1] = self.ANT.MAT[0][1] + self.DURACION
            self.ANT.SIG = self                             #Actividad SIG de ANT = Actividad ACTUAL

    #Método para conocer el estado del objeto
    def descripcion(self):
        print("Actividad:", self,"\nDuracion:", self.DURACION,
              "\nAnterior:", self.ANT, "\nSiguiente:", self.SIG, "\n")

    #Función interna para hallar fecha tardía
    def fechaTardia(self,SIGUIENTE):
        if self.DURACION == 'i' or self.DURACION == 'I':
            return
        self.MAT[1][1] = SIGUIENTE.MAT[1][0]
        self.MAT[1][0] = SIGUIENTE.MAT[1][0] - self.DURACION
        self.ANT.fechaTardia(self)

    #Método para hallar las fechas tardías
    def fechasTardias(self, REL):
        self.MAT[1][1] = self.MAT[0][1]
        self.MAT[1][0] = self.MAT[0][1] - self.DURACION
        REL.fechaTardia(self)

def GenerarInformacion(proyectoNro):
    #****Actividades****#
    A = creamat(1,0)
    A[0] = Actividad(0, "i", None, None, "Nodo Inicio")
    contador = 1
    fichero = open(f'./Actividades/act{proyectoNro}.txt', 'rt', encoding='utf-8')

    LINEA_ACT = fichero.readline()
    while LINEA_ACT != '':
        fichero2 = open('./Relaciones/rel001.txt', 'rt', encoding='utf-8')
        LINEA_REL = fichero2.readline()
        while LINEA_REL != '':
            if int(LINEA_REL.split(";")[0]) == int(LINEA_ACT.split(";")[0]):
                #print(LINEA_REL.split(";")[0], LINEA_ACT.split(";")[0])
                identificador = int(LINEA_REL.split(";")[0])
                duracion = int(LINEA_ACT.split(";")[2])
                relacion = int(LINEA_REL.split(";")[1])
                fechaInicio = str(LINEA_ACT.split(";")[3])
                nombre = str(LINEA_ACT.split(";")[1])
                #print(identificador, duracion, relacion)
                CalculoFechas(A, identificador, duracion, relacion, contador, fechaInicio, nombre)
                contador += 1
            LINEA_REL = fichero2.readline()
        fichero2.close()
        LINEA_ACT = fichero.readline()
    fichero.close()
    CalculoFechas(A,identificador,"f",relacion,contador,fechaInicio,nombre)


    fichero3 = open(f'./Informes/info{proyectoNro}.txt', 'at', encoding='utf-8')
    fichero3.write(f"\t*Informe sobre el proyecto {proyectoNro}*\n")
    for I in range(len(A)-1):
        fichero3.write(f"A[{A[I].IDENTIFICADOR}] --> {A[I].MAT}\n")
    fichero3.write(f"\n\t*Camino Critico*\n")
    for I in range(len(A)):
        if I in CalculoCaminoCritico(A):
            fichero3.write(f"A[{A[I].IDENTIFICADOR}] --> {A[I].MAT}\n")
    for I in range(len(A)-1):
        fichero3.write(f"\nA[{A[I].IDENTIFICADOR}] -> Nombre: {A[I].NOMBRE}\n\tFecha de Inicio: {A[I].FECHA_INICIO}\n\tFecha de Fin: {A[I].FECHA_FIN}\n")
        fichero3.write(f"\tFecha de Inicio Tardio: {A[I].FECHA_INICIO_TARDIO}\n\tFecha de Fin Tardio: {A[I].FECHA_FIN_TARDIO}\n")
    fichero3.close()

def EmitirInforme():
    ventanaEmitirInforme = tkinter.Tk()
    ventanaEmitirInforme.geometry("225x50")
    ventanaEmitirInforme.resizable(0, 0)

    miFrame = Frame(ventanaEmitirInforme, width=800, height=400)
    miFrame.place(x=0, y=0)

    textoNombre = Label(miFrame, text="Identificador del proyecto")
    textoNombre.grid(row=0, column=0, padx=0, pady=0)

    cuadroNombre = Entry(miFrame)
    cuadroNombre.grid(row=0, column=1, padx=0, pady=0)

    def Enviar():
        ENTRADA = cuadroNombre.get()
        GenerarInformacion(ENTRADA)
        ventanaEmitirInforme.destroy()

    botonEnvio = Button(miFrame, text="Enviar", command=Enviar)
    botonEnvio.grid(row=1, column=0)
