from Librerias import *


class NuevoProAc():
    pass
    def __init__(self,identificador,nombre,fechaTemprano):
        self.identificador = identificador
        self.nombre = nombre
        self.fechaTemprano = fechaTemprano

class ProyectoNuevo(NuevoProAc):
    pass
    def __init__(self,identificador,nombre,fechaTemprano,descripcion):
        super().__init__(identificador,nombre,fechaTemprano)
        self.descripcion = descripcion


class NuevaActividadClase(NuevoProAc):
    pass
    def __init__(self,identificador,nombre,fechaTemprano,duracion):
        super().__init__(identificador,nombre,fechaTemprano)
        self.duracion = duracion

class ElTodo:
    pass

    @classmethod
    def Bisiesto(self, anio):
        valor = False
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            valor = True
        return valor

    @classmethod
    def ValidaFecha(self, ListaFecha):  # ListaFecha [AAAA,MM,DD]
        valido = True
        dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ElTodo.Bisiesto(ListaFecha[0]):
            dias[1] = 29
        if ListaFecha[0] < 0:
            valido = False
        elif ListaFecha[1] < 1 or ListaFecha[1] > 12:
            valido = False
        elif ListaFecha[2] < 1 or ListaFecha[2] > dias[ListaFecha[1] - 1]:
            valido = False
        return valido

    @classmethod
    def ValidarProyectoOActivdad(self, identificador, nombre, duracion, fechaTemprano, descripcion, tipo):
        # EL parametro tipo puede tener 2 valores:
        # tipo = 0 ; significa que estamos hablando de la creacion de una actividad
        # tipo = 1 ; significa que estamos hablando de la creacion de un proyecto

        # Algoritmo para verificar los datos introducidos por el usuario
        banderaAprobado = True
        if (len(identificador) <= 3 and len(identificador) > 0):  # Verifica el tamaño del identificador
            numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for digito in identificador:
                if not ((digito in numeros)):  # verifica si cada digito del identificador es un numero
                    banderaAprobado = False
            if (len(nombre) < 21 and banderaAprobado and tipo==0) or (len(nombre) < 31 and banderaAprobado and tipo==1):  # verifica el tamaño del nombre o descripcion
                alfanumericos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G",
                                 "H", "I",
                                 "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
                                 "Z", "a",
                                 "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                                 "r", "s", "t", "u", "v", "w",
                                 "x", "y", "z"]
                for letra in nombre:
                    if not (letra in alfanumericos):  # Verifica que cada letra del nombre sea un alfanumerico
                        banderaAprobado = False
                if tipo == 0:  # verificamos si estamos creando una actividad
                    if ((len(duracion) < 3) and (len(duracion) > 0) and (banderaAprobado == True) and (duracion[0] in numeros)):
                        # la linea anterior verifica el tamaño de la duracion y si no es un numero negativo
                        for digito in duracion:
                            if not (digito in numeros):  # verifica que cada digito de la duracion sea un numero
                                banderaAprobado = False
                    else:
                        banderaAprobado = False
                elif tipo == 1: # varifica si estamos creando un proyecto
                    alfanumericos.append(" ")
                    if len(descripcion) < 61:
                        for letra in descripcion:
                            if not (letra in alfanumericos):
                                banderaAprobado = False
                    else:
                        banderaAprobado = False


                actiTemp = fechaTemprano
                actiTemp = actiTemp.split("/")  # actiTemp ahora es la lista con la fecha introducida por el usuario [AAAA/MM/DD] pero de tipo char
                if ((len(fechaTemprano) > 0) and (len(fechaTemprano) < 11) and (len(actiTemp) == 3) and banderaAprobado == True):
                    # la linea anterior verifica el tamaño maximo que puede llegar a tener la fecha AAAA/MM/DD que es 10, incluyendo las "/", tambien se verifica que
                    # la lista actiTemp tenga como tamaño = 3, por los años, meses y dias
                    tamanos = [4, 2, 2]
                    for k in range(0, 3):  # ciclo para recorrer la lista de fecha actiTemp
                        if k == 0:
                            if not (len(actiTemp[k]) == tamanos[k]):  # verifica si el tamaño del año es 4, asumimos que no se harán actividades antes del año 1000
                                banderaAprobado = False
                        elif k > 0:
                            if not (len(actiTemp[k]) <= tamanos[k] and len(actiTemp[k]) >= 1):  # verifica el tamaño de los meses [1,2]
                                banderaAprobado = False
                        if banderaAprobado == True:
                            actiTemp[k] = int(actiTemp[k]) #si todova bien convertimos a entero cada elemento de la lista de fecha
                else:
                    banderaAprobado = False
                if banderaAprobado:
                    if not (ElTodo.ValidaFecha(actiTemp)):  # Verificamos si la fecha es valida
                        banderaAprobado = False
        else:
            banderaAprobado = False
        return banderaAprobado

