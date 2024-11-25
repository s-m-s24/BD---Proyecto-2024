from datetime import datetime
import FuncionesDeDatos


# Get the current date
current_date = datetime.now()


# Extract month and day
month = current_date.month
day = current_date.day


dias_por_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
today=FuncionesDeDatos.obtener_dia_tareas(current_date.day,current_date.month,dias_por_mes)


nombresTareas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
duracionTareas=[1,2,3,1,1,1,2,1,1,2,3,1,1,1,2,1]
diaTareas=[26,27,27,27,28,28,28,28,29,29,30,30,30,30,31,31]
mesTareas=11
añoTareas=2024


def todayPrint():
    """
    Imprime el día de hoy. Ya sé, re inútil pero bue. Tenía ganas de que fuera una función
    """


    print("Hoy es: ",day,"/",month)


    return today


def ingresarTareas(listaTareas,fechas,tiempoTareas):


    """
    Permite a un usuario ingresar tareas sin horario fijo, pero con una duración elegida y fecha límite
    """


    valido=False


    i=0


    class Tareas:
        nombre: str
        duracion: int
        mes:int
        dia:int
        año: int
        dificultad: int
        materia:str


        def __init__(self, nombre, duracion,dia,mes,año,dificultad,materia):
            self.nombre = nombre
            self.duracion = duracion
            self.dia = dia
            self.mes = mes
            self.año = año
            self.dificultad = dificultad
            self.materia = materia
       
        def __getitem__(self, key):
        # Usamos un diccionario para hacer que los atributos sean accesibles por nombre
            atributos = {
                "nombre": self.nombre,
                "duracion": self.duracion,
                "dia": self.dia,
                "mes": self.mes,
                "año": self.año
            }
            return atributos[key]
        
        def get_day (self):
            month = self.mes
            month -= 1

            dia_del_mes = sum(dias_por_mes[0:month:1]) + self.dia

            if (self.año == 2025):
                day=dia_del_mes+365
                return day
            else:
                return dia_del_mes


        def __str__(self):
            return f"Nombre: {self.nombre}, Duración: {self.duracion}h, Fecha: {self.dia}/{self.mes}/{self.año}"#, Dificultad: {self.dificultad}, Materia: {self.materia}
    
    ingresar=input("¿Quieres ingresar una tarea?: ")
    #print(ingresar)

    while ingresar.lower() in ["si","sí"] :
        
        nombre = input("Ingrese el nombre de esta tarea: ")


        duracion = input("Ingrese la duración de esta tarea: ")
        while(duracion.isnumeric()==False):
            duracion=input("No ingresó un número, por favor ingrese un número: ")
        duracion=int(duracion)

        tiempoTareas=tiempoTareas+duracion

        valido=False

        while valido == False:

            mes = input("Ingrese el mes en que vence esta tarea: ")
            mes = FuncionesDeDatos.verificar_num(mes,12,1)

            diaMax = dias_por_mes[mes-1]
            dia = input("Ingrese el dia en que vence esta tarea: ")
            dia = FuncionesDeDatos.verificar_num(dia,diaMax,1)

            año = input("Ingrese el año en que vence esta tarea: ")
            año = FuncionesDeDatos.verificar_num(año,2025,2024)

            day = FuncionesDeDatos.obtener_dia_tareas(dia,mes,dias_por_mes)
            valido=True

            if año==2025:
                day=day+365

            if today>day:
                print("El día que has ingresado ya pasó, por favor reingresa la fecha")
                valido=False

        dificultad = input("Ingrese la dificultad de esta tarea en una escala del 1 al 10, en el que 1 es el más fácil y 10 el más difícil: ")
        dificultad = FuncionesDeDatos.verificar_num(dificultad,10,1)

        materia = input("Ingrese la materia de esta tarea: ")

        tarea = Tareas(nombre,duracion,dia,mes,año,dificultad,materia)
        
        listaTareas=FuncionesDeDatos.ordenar_lista_tareas(listaTareas,fechas,day,tarea)

        ingresar=input("¿Quieres ingresar una tarea?: ")

    return listaTareas, fechas, tiempoTareas
    """
    for num in range(16):
        nombre=nombresTareas[num]
        duracion=duracionTareas[num]
        dia=diaTareas[num]
        mes=mesTareas
        año=añoTareas
        tarea = Tareas(nombre,duracion,dia,mes,año)
        listaTareas.append(tarea)
        #print(tarea)
    """