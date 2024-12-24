from Librerias import *

def CrearProyecto():


    Ocultar()

    ventana2 = tkinter.Toplevel()
    ventana2.geometry("1000x600")
    ventana2.config(bg="white")
    ventana2.resizable(0,0)
    cabezera = tkinter.Label(ventana2, text="Crear Proyecto", bg="light blue", font="Helvetica 30")
    cabezera.pack(fill=tkinter.X)

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

        BotonOk = tkinter.Button(VentError, text="Entendido", padx=20, pady=10, command=lambda:[cerrarError(),boton_siguiente.config(state=NORMAL)])
        BotonOk.place(x=100, y=230)

        leti = Label(VentError, image=photo5).place(x=100, y=50)

    def siguiente():
        NuevoProyecto = ProyectoNuevo(textoIdentificador.get(),textoNombre.get(),textoFecha.get(),textoDescripcion.get())
        Validacion = ElTodo.ValidarProyectoOActivdad(NuevoProyecto.identificador,NuevoProyecto.nombre,"",NuevoProyecto.fechaTemprano,NuevoProyecto.descripcion,1)
        if Validacion:
            # Aca creamos el archivo donde se guardará cada proyecto que se cree
            archivoProyecto = open(f"./Proyectos/pry{NuevoProyecto.identificador}.txt", "at")
            archivoProyecto.write(
                f"{NuevoProyecto.identificador};{NuevoProyecto.nombre};{NuevoProyecto.descripcion};{NuevoProyecto.fechaTemprano}\n")
            archivoProyecto.close()

            # En las siguientes 3 (29,30,31) lineas creamos un txt en la carpeta raiz del programa que tendrá el identificador de proyecto actual (El que se esté usando)
            # el parametro "wt" hace que se sobreescriba todp lq hay y borrando lq habia antes, de este modo siempre tendrá el identificador que se usa y no otro
            identificadorProyectoTxt = open("./identificador.txt", "wt")
            identificadorProyectoTxt.write(f"{NuevoProyecto.identificador}")
            identificadorProyectoTxt.close()

            ventana2.withdraw()
            Mostrar()
        else:
            VentanaError()
            boton_siguiente.config(state=DISABLED)

    #Identificadores de formulario

    identificadorProyecto = tkinter.Label(ventana2, text="   Identificador de proyecto:", padx=38, pady=10,font="Helvetica 20")
    identificadorProyecto.place( x=0 , y=142)

    nombreProyecto = tkinter.Label(ventana2, text="Nombre del proyecto:", padx=73, pady=10,font="Helvetica 20")
    nombreProyecto.place(x = 0 , y=216)

    descripcionProyecto = tkinter.Label(ventana2, text="Descripcion Proyecto:", padx=70, pady=10,font="Helvetica 20")
    descripcionProyecto.place(x = 0 , y=290)

    fechaPrevistaProyecto = tkinter.Label(ventana2, text="Fecha inicio previsto:", padx=74, pady=10,font="Helvetica 20")
    fechaPrevistaProyecto.place(x=0, y=364)

    boton_siguiente = tkinter.Button(ventana2, text="Siguiente",padx=20, pady=5,font="Helvetica 10",command=siguiente)
    boton_siguiente.place(x=800, y=500)

    boton_Atras = tkinter.Button(ventana2, text="Atrás" , command = lambda :[Mostrar(),ventana2.withdraw()],padx=20, pady=5,font="Helvetica 10")
    boton_Atras.place(x=100, y=500)


    aux = tkinter.Label(ventana2, text ="AAAA/MM/DD", padx = 20 , pady = 5 , font = "Helvetica 15")
    aux.place(x = 820 , y = 392)

    # Cuadros de entrada de texto

    textoIdentificador = tkinter.Entry(ventana2,font = "Helvetica 30")
    textoIdentificador.place(x =500, y = 150 )

    textoNombre = tkinter.Entry(ventana2, font="Helvetica 30")
    textoNombre.place(x=500, y=225)

    textoDescripcion = tkinter.Entry(ventana2, font="Helvetica 15")
    textoDescripcion.place(x=500, y=300)

    textoFecha = tkinter.Entry(ventana2, font="Helvetica 20")
    textoFecha.place(x=500, y=390)


    ventana2.mainloop()


