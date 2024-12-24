from Librerias import *

def BarraDeMenus():
    barraMenu = Menu(ventana)
    ventana.config(menu=barraMenu, width=300, height=300)  # Borrar width y height

    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Abrir", command=AbrirArchivo)
    archivoMenu.add_command(label="Guardar", command=EmitirInforme)
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Crear Proyecto", command=CrearProyecto)
    archivoMenu.add_command(label="Recuperar Proyecto", command=AbrirArchivo)
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Cerrar", command=Ocultar)

    herramientasMenu = Menu(barraMenu, tearoff=0)
    herramientasMenu.add_command(label="Crear Actividad", command = lambda:[NuevaActividad(0,0)])
    herramientasMenu.add_command(label="Modificar Actividad", command=ModificarActividad)
    herramientasMenu.add_command(label="Eliminar Actividad",command=BorrarActivdad)
    herramientasMenu.add_separator()
    herramientasMenu.add_command(label="Crear Relacion", command=CrearRelacion)
    herramientasMenu.add_command(label="Eliminar Relacion", command=Borrar_Relacion)
    herramientasMenu.add_separator()
    herramientasMenu.add_command(label="Visualizar Actividades", command=ActividadesDeProyecto)
    herramientasMenu.add_command(label="Emitir Informe", command=EmitirInforme)

    ayudaMenu = Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Acerca de...", command=AcercaDe)

    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
