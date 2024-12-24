from Librerias import *

def Programa():

    photo1 = PhotoImage(file="Imagen1.gif")
    photo2 = PhotoImage(file="Imagen2.gif")
    photo3 = PhotoImage(file="Imagen3.gif")


    i1 = Label(ventana, image=photo1).place(x=40, y=90)
    i2 = Label(ventana, image=photo2).place(x=430, y=90)
    i3 = Label(ventana, image=photo3).place(x=830, y=90)

    etiqueta = tkinter.Label(ventana, text = "Administrador de proyectos", bg = "light blue", font = "Helvetica 30")
    etiqueta.pack(fill = tkinter.X)

    boton1 = tkinter.Button(ventana,text = "Crear Proyecto", padx = 50, pady = 20, command = CrearProyecto, font="Helvetica 17",bg = "white") #Crea la ventana ==> Crear Proyecto
    boton1.place(x = 20,y =350)

    boton2 = tkinter.Button(ventana,text = "Recuperar Proyecto", padx = 50, pady = 20, command = AbrirArchivo, font="Helvetica 17",bg = "white") # Crea la Ventana ==> Recuperar proyecto
    boton2.place(x = 380,y =350)

    boton3 = tkinter.Button(ventana, text = "Actividades de Proyecto", padx = 10, pady = 20, command = ActividadesDeProyecto, font="Helvetica 17",bg = "white") # Crea la Ventana ==> Actividades de Proyecto
    boton3.place(x = 790,y =350)


    BarraDeMenus()
    ventana.mainloop()

Programa()
