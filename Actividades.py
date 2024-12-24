import os
from Librerias import *

def ActividadesDeProyecto():

    Ocultar()

    ventana3 = tkinter.Toplevel()
    ventana3.geometry("1000x600")
    ventana3.config(bg="White")
    ventana3.title("Programa informático del grupo 7")
    ventana3.resizable(0,0)
    cabezera = tkinter.Label(ventana3, text="Actividades de proyecto", bg="light blue", font="Helvetica 30")
    cabezera.pack(fill=tkinter.X)

    photo4 = PhotoImage(file="Imagen4.gif")
    i1 = Label(ventana3, image=photo4).place(x=500, y=90)


    boton1 = tkinter.Button(ventana3, text="Crear una nueva actividad", padx=54, pady=10, command = lambda:[NuevaActividad(0,0)], font="Helvetica 20",bg="white")
    boton1.place(x=0, y=92)

    boton2 = tkinter.Button(ventana3, text="Modificar una actividad", padx=73, pady=10, command= ModificarActividad,
                            font="Helvetica 20", bg ="white")
    boton2.place(x=0, y=166)

    boton3 = tkinter.Button(ventana3, text="Eliminar una actividad"
                                           "", padx=80, pady=10,command=BorrarActivdad,
                            font="Helvetica 20", bg = "white")
    boton3.place(x=0, y=240)

    boton4 = tkinter.Button(ventana3, text="Crear una nueva Relación", padx=54, pady=10, command=CrearRelacion,
                            font="Helvetica 20", bg="white")
    boton4.place(x=0, y=314)

    boton5 = tkinter.Button(ventana3, text="Borrar Relación", padx=117, pady=10, command=Borrar_Relacion,
                            font="Helvetica 20", bg="white")
    boton5.place(x=0, y=388)

    boton_Atras = tkinter.Button(ventana3, text="Atrás", command=lambda :[Mostrar(),ventana3.withdraw()]

                                 , padx=20, pady=5,
                                 font="Helvetica 10")
    boton_Atras.place(x=40, y=520)

    boton_Informe = tkinter.Button(ventana3, text="Informes de Actividades", bg="white"

                                 , padx=20, pady=20,
                                 font="Helvetica 12", command=EmitirInforme)
    boton_Informe.place(x=260, y=500)

    ventana3.mainloop()

#Funcion que crea ventana para abrir el proyecto y ver sus actividades. VER CON ELIAS........
def Abrir_Proyecto_Actividades():
    ventana6 = tkinter.Tk()
    ventana6.geometry("300x250")
    ventana6.config(bg="white")
    ventana6.resizable(0,0)
    titulo = tkinter.Label(ventana6, text="Atención!", font="Helvetica 30")
    titulo.pack(fill=tkinter.X)

    Label_Buscador = tkinter.Label(ventana6,text = "Favor seleccionar proyecto\n para visualizar actividades.", font="Helvetica 15", bg="white")
    Label_Buscador.pack()
    Label_Buscador.place(x = 20,y = 70)

    boton_seleccionar = tkinter.Button(ventana6,text="Seleccionar", padx=30,pady=20, command=AbrirArchivo)
    boton_seleccionar.place(x = 100, y = 150)

def ModificarActividad():
    ventanaModificarActivdad = tkinter.Tk()
    ventanaModificarActivdad.geometry("500x350")
    ventanaModificarActivdad.title("Programa informático del grupo 7")
    ventanaModificarActivdad.resizable(0, 0)

    tituloBorrarActividad = tkinter.Label(ventanaModificarActivdad, text="Modificar Actividad:", font="Helvetica 30")
    tituloBorrarActividad.pack(fill=tkinter.X)

    # Lista para borrar
    my_listbox = Listbox(ventanaModificarActivdad, width=50)
    my_listbox.pack(pady=15)

    #ESTA LISTA DONDE IRAN TODAS LAS ACTIVIDADES VISIBLES PARA EL USUARIO
    my_list = []
    #Abrimos el archivo que contiene el identificador del proyecto actual.
    idePryActual = open("./identificador.txt","rt")
    ideAct = idePryActual.readline() #ahora tenemos el identificador del proyecto actual
    idePryActual.close()

    #Ahora abrimos el archivo de actividades que corresponde al identificador de proyecto actual
    actiActual = open(f"./Actividades/act{ideAct}.txt","rt")
    ListaDeTodasLasActividades = actiActual.readlines() #Esta lista ahora tiene todas las actividades con todos sus datos en cada posicion de la lista
    actiActual.close()
    #Teniendo la lista de todas las actividades de un determinado proyecto, la agregamos a "my_list" donde se mostrará al usuario una lista con las actividades
    for K in range (len(ListaDeTodasLasActividades)):
        ElementoDeLista = ListaDeTodasLasActividades[K] #Ahora elementoDeLista tendrá todos los datos de una actividad en concreto
        ElementoDeLista = ElementoDeLista.split(";") #Ahora lo transformamos a una lista donde cada elemento es un dato en especifico de la actividad
        my_list.append(f"{ElementoDeLista[1]}_{ElementoDeLista[0]}") #Agrega a my_list la lista de actividad al estilo de "nombre_identificador"


    for item in my_list:
        my_listbox.insert(END, item)

    def AbrirActividadAModificar():
        seleccionado = my_listbox.curselection()
        seleccionado = my_listbox.get(seleccionado)
        NuevaActividad(1,seleccionado)

    my_buttom = Button(ventanaModificarActivdad, text="Abrir",command=AbrirActividadAModificar)
    my_buttom.pack(pady=10)

    global my_label
    my_label = Label(ventanaModificarActivdad, text="")
    my_label.pack(pady=5)


    ventanaModificarActivdad.mainloop()


def BorrarActivdad():
    ventanaBorrarActivdad = tkinter.Tk()
    ventanaBorrarActivdad.geometry("500x350")
    ventanaBorrarActivdad.title("Programa informático del grupo 7")
    ventanaBorrarActivdad.resizable(0,0)

    tituloBorrarActividad = tkinter.Label(ventanaBorrarActivdad, text="Eliminar Actividad:", font="Helvetica 30")
    tituloBorrarActividad.pack(fill=tkinter.X)


    #Lista para borrar
    my_listbox = Listbox(ventanaBorrarActivdad, width=50)
    my_listbox.pack(pady=15)


    #ESTA LISTA ES PARA LA LISTA VISUAL DE LA INTERFAZ
    my_list = []
    # Abrimos el archivo que contiene el identificador del proyecto actual.
    idePryActual = open("./identificador.txt", "rt")
    ideAct = idePryActual.readline()  # ahora tenemos el identificador del proyecto actual
    idePryActual.close()

    # Ahora abrimos el archivo de actividades que corresponde al identificador de proyecto actual
    actiActual = open(f"./Actividades/act{ideAct}.txt", "rt")
    ListaDeTodasLasActividades = actiActual.readlines()  # Esta lista ahora tiene todas las actividades con todos sus datos en cada posicion de la lista
    actiActual.close()
    # Teniendo la lista de todas las actividades de un determinado proyecto, la agregamos a "my_list" donde se mostrará al usuario una lista con las actividades
    for K in range(len(ListaDeTodasLasActividades)):
        ElementoDeLista = ListaDeTodasLasActividades[K]  # Ahora elementoDeLista tendrá todos los datos de una actividad en concreto
        ElementoDeLista = ElementoDeLista.split(";")  # Ahora lo transformamos a una lista donde cada elemento es un dato en especifico de la actividad
        my_list.append(f"{ElementoDeLista[1]}_{ElementoDeLista[0]}")  # Agrega a my_list la lista de actividad al estilo de "nombre_identificador"

    for item in my_list:
        my_listbox.insert(END, item)

    def delete():
        #En las siguientes dos lineas asignamos a la variabale "seleccionado" el nombre de la actividad seleccionada por el usuario
        seleccionado = my_listbox.curselection()
        seleccionado = my_listbox.get(seleccionado)

        seleccionado = seleccionado.split("_")  # Ahora seleccionado es una lista que tiene el [nombre,identificador] de la actividad a borrar

        #La siguiente lista contendrá los datos actualizados de las actividades del proyecto
        ListaDeTodasLasActividadesActualizada = []
        for K in range (len(ListaDeTodasLasActividades)):
            subListaAct = ListaDeTodasLasActividades[K]
            subListaAct = subListaAct.split(";") #Ahora tenemos una lista con todos los datos de cada actividad por ciclo

            if not(seleccionado[0] == subListaAct[1]): #verifica si el nombre de la actividad seleccionado es igual al nombre de otra actividad del proyecto y si es así no lo agrega a la nueva lista
                ListaDeTodasLasActividadesActualizada.append(ListaDeTodasLasActividades[K])
            else:
                Eliminar = ListaDeTodasLasActividades[K]
        #Eliminamos la actividad que se quiere eliminar pero fuera del bucle para no generar errores de indices
        ListaDeTodasLasActividades.remove(Eliminar)

        #Ahora abrimos el txt de la actividad y sobreescribimos t0do con la ListaDeTodasLasActividadesActualizada
        ActiAEditar = open(f"./Actividades/act{ideAct}.txt","wt")
        for j in range(len(ListaDeTodasLasActividadesActualizada)):
            ActiAEditar.write(ListaDeTodasLasActividadesActualizada[j])
        ActiAEditar.close()


        my_listbox.delete(ANCHOR)
        my_label.config(text="")

    def select():
        my_label.config(text=my_list.get(ANCHOR))

    def delete_all():
        #Como se borra t0do, solo basta con sobreescribir t0do el txt de la actividad con un espacio vacio
        ActiAEditar = open(f"./Actividades/act{ideAct}.txt", "wt")
        ActiAEditar.write("")
        ActiAEditar.close()
        my_listbox.delete(0,END)

    my_buttom = Button(ventanaBorrarActivdad, text="Borrar", command=delete)
    my_buttom.pack(pady=10)


    global my_label
    my_label = Label(ventanaBorrarActivdad, text="")
    my_label.pack(pady=5)

    my_buttom3 = Button(ventanaBorrarActivdad, text="Borrar Todo", command=delete_all)
    my_buttom3.pack(pady=2)

    ventanaBorrarActivdad.mainloop()



def NuevaActividad(modificar,selecct):
    #Los parametros modificar y selecct:
    #"modificar" puede tener 2 valores.

    #modificar = 1; signifca que estamos hablando de modificar una actividad y...
    #selecct = "nombre_identificador"; de la actividad que queramos modificar

    #modificar = 0; significa que estamos creando una actividada nueva y por ende...
    #selecct = 0; selecct tambien valdrá cero

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

        BotonOk = tkinter.Button(VentError, text="Entendido", padx=20, pady=10, command=lambda:[cerrarError(),boton_done.config(state=NORMAL)])
        BotonOk.place(x=100, y=230)

        leti = Label(VentError, image=photo5).place(x=100, y=50)



    ventana4 = tkinter.Tk()
    ventana4.geometry("550x400")
    ventana4.title("Programa informático del grupo 7")
    ventana4.resizable(0,0)
    if modificar==0 and selecct==0:
        titulo = tkinter.Label(ventana4,text="Ingrese datos de nueva actividad:",font = "Helvetica 20")
        titulo.pack()
        titulo.place(x=30,y=30)
    else:
        titulo = tkinter.Label(ventana4, text="Modifique los datos de la actividad:", font="Helvetica 20")
        titulo.pack()
        titulo.place(x=30, y=30)

    frame_cuadro = Frame(ventana4,width=800, height= 600 )
    frame_cuadro.place(x=50,y=100)

    #frame para el boton
    frame_boton = Frame(ventana4,width=800, height=600)
    frame_boton.place(x=400,y=310)

    #funcion para el boton "hecho" EXPLICACION
    #Al cerrar la ventana se crea el objeto actividadUno y se le asocia con la clase NuevaActividadClase
    #Se le pasa como parametro los datos en los cuadros de texto de las interfaz con el metodo .get()
    def cerrar_ventana_actPro(modify,selecc):
        #Ahora "selecc" es una lista [nombre,identificador]


        #Creamos el objeto ActividadUno y le asignamos los valores de los cuadros de texto como parametros
        actividadUno = NuevaActividadClase(cuadro_identificador.get(), cuadro_nombre.get(),cuadro_fecha_temprano.get(), cuadro_duracion.get())
        validacion = ElTodo.ValidarProyectoOActivdad(actividadUno.identificador,actividadUno.nombre,actividadUno.duracion,actividadUno.fechaTemprano,"",0)

        # Leemos el identificador del proyecto actual
        IdentificadorParaActividades = open("./identificador.txt", "rt")
        ideAct = IdentificadorParaActividades.readline()
        IdentificadorParaActividades.close()

        #Verificamos que los datos sean validos y que se trate de una modificacion de actividad
        if validacion and modify==1:
            modifAct = open(f"./Actividades/act{ideAct}.txt","rt")
            TodosLosDatos = modifAct.readlines() #Ahora todas las actividades del proyecto
            modifAct.close()
            NuevaListaModificada = []  #Lista donde iran los datos nuevos y modificados

            for I in range (len(TodosLosDatos)):

                liNea = TodosLosDatos[I]
                AuxLIn = liNea # guardamos la actividad sin dividir en lista
                liNea = liNea.split(";") #Ahora linea tiene todos los datos de una actividad en concreto en forma de lista

                if not(liNea[0]==selecc[1] and liNea[1]==selecc[0]): #Verifica que el nombre y el identificador no sean iguales
                    NuevaListaModificada.append(AuxLIn)

            ActModificada = actividadUno.identificador +";"+ actividadUno.nombre+";"+actividadUno.duracion+";"+actividadUno.fechaTemprano+"\n" #Crea la actividad modificada
            NuevaListaModificada.append(ActModificada) #Agrega la actividad modificada al archivos de actividades del determinado proyecto
            modifAct = open(f"./Actividades/act{ideAct}.txt", "wt") #Abrimos el archivo de actividades en modo sobreescribir
            for k in range (len(NuevaListaModificada)):
                modifAct.write(f"{NuevaListaModificada[k]}") #sobrescribimos t0do con la NuevaListaModificada
            modifAct.close()
            ventana4.destroy()

        elif validacion and modify==0: #verifica si los datos son validos y si se está creando una actividad nueva

            # Creacion del archivo txt que tendrá los datos de las actividades
            nuevaActFile = open(f"./Actividades/act{ideAct}.txt", "at")
            nuevaActFile.write(f"{actividadUno.identificador};{actividadUno.nombre};{actividadUno.duracion};{actividadUno.fechaTemprano}\n")
            nuevaActFile.close()
            #Archivo contenedor de los datos cerrado

            #Y cerramos la ventana
            ventana4.destroy()

        else:
            VentanaError()
            boton_done.config(state = tkinter.DISABLED)

    #cuadro de texto del identificador de la actividad (numerico de 3 siglas XXX)
    cuadro_identificador = Entry(frame_cuadro)
    cuadro_identificador.grid(row=0,column=1)
    nombre_identificador = Label(frame_cuadro,text="Identificador (Numerico XXX):")
    nombre_identificador.grid(row=0,column=0, sticky= "w",pady=10,padx=10)

    #cuadro de nombre de la actividad (alfanumerico de tamaño hasta 20)
    cuadro_nombre = Entry(frame_cuadro)
    cuadro_nombre.grid(row=1, column=1)
    nombre_nombre = Label(frame_cuadro, text="Nombre:")
    nombre_nombre.grid(row=1, column=0, sticky="w", pady=10, padx=10)

    #cuadro de duracion de la actividada (numerico de 2 siglas XX, en dias)
    cuadro_duracion = Entry(frame_cuadro)
    cuadro_duracion.grid(row=2, column=1)
    nombre_duracion = Label(frame_cuadro, text="Duracion (dias XX):")
    nombre_duracion.grid(row=2, column=0, sticky="w", pady=10, padx=10)

    #cuadro de fecha de inicio temprano (AAAAMMDD)
    cuadro_fecha_temprano = Entry(frame_cuadro)
    cuadro_fecha_temprano.grid(row=3, column=1)
    nombre_fecha_temprano = Label(frame_cuadro, text="Inicio temprano (AAAA/MM/DD):")
    nombre_fecha_temprano.grid(row=3, column=0, sticky="w", pady=10, padx=10)
    #En la siguiente linea verificamos si de esta modificando una actividad
    if modificar==1:
        #Para saber que actividad vamos a modificar
        selecct = selecct.split("_")

        #Abrimos el identificador del proyecto
        id = open("./identificador.txt","rt")
        idePro = id.readline()
        id.close()

        #Abrimos el archivo de las actividades del proyecto actual
        ActToModificar = open(f"./Actividades/act{idePro}.txt","rt")
        TodasLasActividades = ActToModificar.readlines()
        ActToModificar.close()
        for K in range(len(TodasLasActividades)):
            linea = TodasLasActividades[K]
            linea = linea.split(";") #Ahora linea tiene todos los datos de una actividad en concreto
            fechamodi = linea[3]
            palabra =""
            for j in fechamodi:
                if not(j=="\n"):
                    palabra = palabra + j
            linea[3] = palabra
            if linea[0]==selecct[1] and linea[1]==selecct[0]:
                cuadro_identificador.insert(0,linea[0])
                cuadro_nombre.insert(0,linea[1])
                cuadro_duracion.insert(0,linea[2])
                cuadro_fecha_temprano.insert(0,linea[3])
                continue

    #boton de terminado
    boton_done = Button(frame_boton,text="Hecho",width=10,command=lambda:[cerrar_ventana_actPro(modificar,selecct)])
    boton_done.grid(row=5,column=0)

    ventana4.mainloop()

    #Parte de anahi
class Relacion:
    def __init__(self,id, prec, sg, proye):
        self.id = id
        self.prec = prec
        self.sg = sg
        self.proye= proye


def RelacionesdeProyecto():

    ventana = Toplevel()
    ventana.geometry("1000x500")
    ventana.config(bg="White")
    ventana.resizable(0,0)
    ventana.title("Programa informático del grupo 7")

    cabezera = tkinter.Label(ventana, text="Relaciones de proyecto", font="Helvetica 30")
    cabezera.pack(fill=tkinter.X)

    boton1 = tkinter.Button(ventana, text="Crear una nueva Relación", padx=54, pady=10, command=CrearRelacion,
                            font="Helvetica 20", bg="white")
    boton1.place(x=80, y=250)

    boton2 = tkinter.Button(ventana, text="Borrar Relación", padx=73, pady=10, command=Borrar_Relacion,
                            font="Helvetica 20", bg="white")
    boton2.place(x=540, y=250)


def CrearRelacion():

    ventana7 = tkinter.Toplevel()
    ventana7.geometry("500x350")
    ventana7.resizable(0,0)
    titulo = tkinter.Label(ventana7, text="Relación de actividades", font="Helvetica 30")
    titulo.pack(fill=tkinter.X)

    frame_cuadro = Frame(ventana7, width=800, height=600)
    frame_cuadro.place(x=50, y=100)

    frame_boton = Frame(ventana7, width=800, height=600)
    frame_boton.place(x=400, y=310)

#Verifica si ya se ha generado la relación entre 2 actividades
    def Cantidad_relacion(An, Sg, p):
        Ok=False
        texto = open(f'./Relaciones/rel{p}.txt', 'r') #Lectura del archivo
        filetext = texto.read() #se guarda en una lista
        texto.close()
        palabra= An+';'+Sg+'\w*'
        matches = re.findall(palabra, filetext) #se evalua si ya a aparecido las activdades en el archivo usando la libreria re y se guardan en la lista
        palabra2= Sg+';'+An+'\w*'
        matches2= re.findall(palabra2, filetext)#Se evalua la siguiente codición

        #se obtiene las longitud de las listas creadas
        M=len(matches2)
        N = len(matches)
        if (N<1 and M<1): #si las lista tiene una longitud menor a 1 aun no existe tal relació
            Ok=True
        else:
            Ok=False
            #Si es que la longitud es mayor ya existe la relacion entre las actividades
        return Ok

#verifica la existencia de un archivo que contega a las actividades del proyecto
    def Verificar_ExistenciaRel(p):
        file = f'./Relaciones/rel{p}.txt'
        exists = os.path.exists(file) #Verifica si existe el archivo mediante la libreria os generando un valor booleano
        if (exists):
            aux = 1
        else:
            aux = 0
        return aux #Retorna el valor de la variable

#Función que evalua si un proyecto ya ha llegado al limite de relaciones
    def CantidadporProyecto(p):
        #declaracion de variables locales
        Valido = False
        with open('relacion.txt') as archivo:
            total_lineas = sum(1 for lineas in archivo)#cuenta la cantidad de lineas que tiene el archivo
        if total_lineas<149: #verifica que no ha llegado al limite
            Valido = True
        else :
            Valido= False
        return Valido #Retorna el valor booleano

#Función que verifica si ya existe una relación con el mismo identificador
    def Verificar_RelRepetidas(ident, p):
        ok=False
        datos=[]
        with open(f'./Relaciones/rel{p}.txt') as fname: #Lectura del archivo que guarda las relaciones
            for lineas in fname:
                datos.extend(lineas.split(';'))#separa cada elemento que se encuentra en una linea del  txt y las carga como elemeto independiente en la lista datos
        c = 0
        s = 0
        N = len(datos)
        for i in range(N):
            if datos[i] == ident: #Verifica si ya existe una relacion con el mismo id e incrementa el contador
                c = c+1
            else:
                s = s + 1
        if c == 0: #Si es que aun no existe retorna un valor True si no retorna un False y un mensaje de error
            ok= True
        else:
            ok = False

        return ok #Retorno de la variable booleana

    #Funcion que verifica la existencia de la actividad
    def Buscar_actividades(An, As, idproyecto):
        datos2=[]
        Validar=False
        with open(f"./Actividades/act{idproyecto}.txt") as fname: #Lectura del archivo donde se encuentran las actividades
            for lineas in fname:
                datos2.extend(lineas.split(';'))#separa cada elemento que se encuentra en una linea del  txt y las carga como elemeto independiente en la lista datos
        c = 0
        c2=0
        s = 0
        N = len(datos2)
        for i in range(N):
            if datos2[i] == An: #Si encuentra coincidencia con la actividad precedente incrementa su contador
                c = c+1
            else:
                s = s + 1
            if datos2[i]==As:  #Si encuentra coincidencia con la actividad siguiente  incrementa su contador
                c2=c2+1
            else:
                s=s+1


        if c > 0 and c2>0: #Si ambos valores se encuentran en el archivo actividad devuelve un valor True, si no devuelve False
            Validar = True
        else:
            Validar = False

        return Validar  # Retorno del valor booleano

    def Verificar_actividades(p):
        Existe=False
        file = f'./Actividades/act{p}.txt'
        exists = os.path.exists(file)
        if exists:
            Existe=True
        else:
            Existe = False
        return Existe

    #Función que verifica la existencia de un proyecto
    def Buscar_proyecto(pro):
        Existe=False
        file = f'./Proyectos/pry{pro}.txt'
        exists = os.path.exists(file)
        if exists:
            Existe=True
        else:
            Existe = False
        return Existe


    def CrearNRel():
        #Se crea un objeto tipo relación
        Nrelacion=Relacion(cuadro_identificador.get(), cuadro_AP.get(), cuadro_AS.get(), cuadro_Pro.get())

        ID=Nrelacion.id
        Act_an=Nrelacion.prec
        Act_sg= Nrelacion.sg
        pro=Nrelacion.proye
        rango = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Valido = False
        #Codigos para la validación de las entradas
        if (len(ID)<=3 and len(ID)>0):
            for i in ID:
                if i in rango:
                    Valido=True
        else:
            Valido = False
        if ((len(Act_an)<=3 and len(Act_an)>0) and Valido ):
            for i in Act_an:
                if i in rango:
                    Valido=True
        else:
            Valido= False
        if ((len(Act_sg)<=3 and len(Act_sg)>0) and Valido):
            for i in Act_sg:
                if i in rango:
                    Valido= True
        else:
            Valido= False
        if ((len(pro)<=3 and len(pro)>0) and Valido ):
            for i in pro:
                if i in rango:
                    Valido=True
        else:
            Valido= False
        if (Buscar_proyecto(Nrelacion.proye)  and Valido):
            Valido = True
        else:
            Valido = False
        if (Verificar_actividades(Nrelacion.proye) and Valido):
            Valido = True
        else:
            Valido=False
        if (Valido and Nrelacion.sg != Nrelacion.prec):
            Valido = True
        else:
            Valido = False
        if(Valido and Buscar_actividades(Nrelacion.prec, Nrelacion.sg, Nrelacion.proye)):
            Valido = True
        else:
            Valido = False
        if (Verificar_ExistenciaRel(Nrelacion.proye)==1 and Valido):
            if (Verificar_RelRepetidas(Nrelacion.id, Nrelacion.proye) and CantidadporProyecto(Nrelacion.proye)
                    and Cantidad_relacion(Nrelacion.prec, Nrelacion.sg, Nrelacion.proye)):
                    Valido=True
            else:
                    Valido = False
        elif (Verificar_ExistenciaRel(Nrelacion.proye)==0 and Valido):
            Valido=True
        else:
            Valido=False


        #Si los datos son validos se escriben en un archivo txt y se cierra la ventana si no se muestra un mensaje de error
        if Valido:
            ideRelac=Nrelacion.proye

            # Creacion del archivo txt que tendrá los datos de las actividades en la carpeta Relaciones
            nuevaRelFile = open(f"./Relaciones/rel{ideRelac}.txt", "at")
            nuevaRelFile.write(f"{Nrelacion.id};{Nrelacion.prec};{Nrelacion.sg}\n")
            nuevaRelFile.close()
            #Archivo contenedor cerrado
            #creacion de un archivo que guarda los proyectos que se han trabajado
            proyectos=open("proyectostrabajados.txt", "at")
            proyectos.write(f"{Nrelacion.proye}\n")
            proyectos.close()
            # Archivo contenedor de los datos cerrado
            ventana7.destroy()

        else:
            messagebox.showerror(message="Datos ingresados incorrectos", title="Error",command=boton_done.config(state=DISABLED))


    #Elementos de la interfaz
    cuadro_identificador = Entry(frame_cuadro)
    cuadro_identificador.grid(row=0,column=1)
    Text_identificador = Label(frame_cuadro,text="Identificador (Numerico XXX):")
    Text_identificador.grid(row=0,column=0, sticky= "w",pady=10,padx=10)

    cuadro_AP = Entry(frame_cuadro)
    cuadro_AP.grid(row=1, column=1)
    Text_AP = Label(frame_cuadro, text="Identificador Actividad Precedente (Numerico XXX):")
    Text_AP.grid(row=1, column=0, sticky="w", pady=10, padx=10)

    cuadro_AS = Entry(frame_cuadro)
    cuadro_AS.grid(row=2, column=1)
    Text_AS= Label(frame_cuadro, text="Identificador Actividad siguiente (Numerico XXX) :")
    Text_AS.grid(row=2, column=0, sticky="w", pady=10, padx=10)

    cuadro_Pro = Entry(frame_cuadro)
    cuadro_Pro.grid(row=3, column=1)
    Text_Pro = Label(frame_cuadro, text="Identificador Proyecto (Numerico XXX) :")
    Text_Pro.grid(row=3, column=0, sticky="w", pady=10, padx=10)


    boton_done = Button(frame_boton,text="Hecho",width=10, command=CrearNRel)
    boton_done.grid(row=5,column=0)



def Borrar_Relacion():
    ventana8 =Toplevel()
    ventana8.geometry("700x500")
    titulo = tkinter.Label(ventana8, text="Borrar relación" ,font="Helvetica 30")
    titulo.pack(fill=tkinter.X)

    lstRelaciones=Listbox(ventana8, width=30, height=10)
    lstRelaciones.place(x=200, y=200)

    frame_cuadro = Frame(ventana8, width=800, height=600)
    frame_cuadro.place(x=50, y=100)

    frame_boton = Frame(ventana8, width=200, height=600)
    frame_boton.place(x=400, y=310)

    barra=Scrollbar(ventana8, command=lstRelaciones.yview())
    barra.place(x=380, y =200)

    lstRelaciones.config(yscrollcommand=barra)

#Verifica si ya se ha trabajado con el proyecto seleccionado
    def Verificar(id):
        Ok = False
        texto = open(f'proyectostrabajados.txt.', 'r')#lectura del archivo que contiene la lista de los proyectos trabajados
        filetext = texto.read() #Se guarda en una lista el contenido
        texto.close()
        palabra = id + '\w*'
        matches = re.findall(palabra, filetext)#Se busca el proyecto y se guarda en la lista
        N = len(matches)

        #si ya se ha trabajado con este proyecto aparecera al menos una vez y el tamaño de la lista va a se mayor que 0 si no el tamaño sera cero lo que indica
        #Que no se a trabajado con ese proyecto
        if (N > 0):
            Ok = True
        else:
            Ok = False
        return Ok

#Valida los datos ingresados en el programa
    def Validar_Datos(ID, Indice):
        rango = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Valido = False
        if (len(ID)<=3 and len(ID)>0 and len(Indice)>0):
            for i in Indice:
                if i in rango:
                    Valido = True
        else:
            Valido = False
        return Valido

#Si es que ya se ha trabajado con la actividad muestra la lista de relaciones en una list box
    def Datos():
        ID = cuadro_identificador.get()

        if (Verificar(ID) ):#verificación de la entrada
            f= open(f"./Relaciones/rel{ID}.txt", "r") #apertura del archivo si es que existe
            lineas =f.readlines()
            f.close() # Cierre del archivo
            for i in lineas:
                lstRelaciones.insert(END, i) #carga el archivo en la list box
            if len (lineas)<1:#Si es que ya se han eliminado todas las actividades muestra un mensaje
                messagebox.showerror(message="Se han eliminado todas las relaciones del proyecto", title="Error")

        else:
            messagebox.showerror(message="Este proyecto no posee relaciones o no existe", title="Error")

#Borra la relacion elegida por el usuario
    def Borrar():
        proyecto=cuadro_identificador.get()
        posicion=cuadro_indice.get()
        Valido= True
        c=0
        M=0
        if (Validar_Datos(proyecto, posicion) and Verificar(proyecto)) : #obtiene las validaciones correspodientes
            f = open(f"./Relaciones/rel{proyecto}.txt", "r") #lectura del archivo
            lineas = f.readlines()
            f.close() #Cierre del archivo
            M = len(lineas)
            rango = []
            for i in range(M):
                rango.append(i +1)
            pos = int(posicion) #convierte la entrada a entero
            c = 0
            for i in range(M): #Verifica si la variable está en el rango
                if (rango[i] == pos):
                    c = 1
            Valido=True
        else:
            Valido=False
        #Validaciones
        if (c==1 and Valido):
            Valido = True
        else:
            Valido=False

        if Valido:
            #apertura y lectura del archivo
            f = open(f"./Relaciones/rel{proyecto}.txt", "w")
            linea = lineas[pos-1]
            lineas.remove(linea) #eliminacion de la relacion en la posicion dada
            for linea in lineas:
                f.write(linea) #escritura del achivo
            f.close()
            ventana8.destroy() #Cierre del programa
        else:
            messagebox.showerror(message="El valor ingresado no es válido", title="Error")


    #Parte de la interfaz grafica
    cuadro_identificador = Entry(frame_cuadro)
    cuadro_identificador.grid(row=0, column=1)
    Text_identificador = Label(frame_cuadro, text="Identificador del Proyecto (XXX) : ")
    Text_identificador.grid(row=0, column=0, sticky="w", pady=10, padx=8)

    cuadro_indice = Entry(frame_cuadro)
    cuadro_indice.grid(row=5, column=1)
    Text_indice = Label(frame_cuadro, text="Ingrese la posición donde se encuentra la relación: ")
    Text_indice.grid(row=5, column=0, sticky="w", pady=10, padx=10)
    botonHecho= Button(ventana8, text="Mostrar Relaciones del proyecto", command=Datos)
    botonHecho.place(x=500, y=100)
    borrar_Indice= Button(ventana8, text="Borrar", command=Borrar)
    borrar_Indice.place(x=400, y=400)