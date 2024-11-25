import FuncionesDeDía
import FuncionesDeDatos
import ClasesTareas
import OrgCalendario


horassemana = []
agenda = []


accion = 0


day1horas = [9,10,11,12,13,14,15]
day1cronograma = ["nada","nada","tango","nada","nada","lengua","nada"]


day2horas = [6,7,8,9,10,11,12,13,14]
day2cronograma = ["nada","nada","tango","BD","nada","lengua","nada","paintball","p"]


day3horas = [8,9,10,11,12]
day3cronograma = ["nada","nada","nada","nada","nada"]


day4horas = [9,10,11,12,13,14,15,16,17,18,19,20]
day4cronograma = ["nada","nada","nada","nada","tango","BD","tango","BD","nada","nada","nada","nada"]


day5horas = [11,12,13,14]
day5cronograma = ["tango","BD","tango","BD"]


day6horas = [14,15,16,17,18,19,20]
day6cronograma = ["nada","nada","lengua","nada","nada","nada","l"]


day7horas = [18,19,20]
day7cronograma = ["nada","nada","nada"]


weekhoras = [day1horas,day2horas,day3horas,day4horas,day5horas,day6horas,day7horas]
weekcronograma = [day1cronograma,day2cronograma,day3cronograma,day4cronograma,day5cronograma,day6cronograma,day7cronograma]


listaTareas = []
fechas=[]


tiempoTareas = 0
tiempoLibre = 0


today=ClasesTareas.todayPrint()


while True:


    print("Ingrese qué desea hacer: ")
    print("Elija 'A' para crear un día")
    print("Elija 'B' para imprimir el cronograma de un día en su semana")
    print("Elija 'C' para ingresar actividades fijas")
    print("Elija 'D' para ingresar tareas no fijas")
    print("Elija 'E' para imprimir su lista de tareas no fijas")
    accion=input("")


    if accion.lower() in ["a","b","c"]:
        dia = input("Ingrese el dia sobre el que desea trabajar (del 1 al 7): ")
        dia = FuncionesDeDatos.verificar_num(dia,7,1)
        dia=dia-1


    #A:CREAR DÍA
    if accion.lower()=="a":
        if len(weekhoras[dia])==0:
            weekhoras[dia], weekcronograma[dia] = FuncionesDeDía.crearDia ()
        elif len(weekhoras[dia])>=0:
            print("Este día ya ha sido creado.")
            confirmacion=input("¿Deseas volver a crearlo? Esta acción reiniciará el cronograma de este día: ")
            if confirmacion.lower() in ["sí", "si"] :
                weekcronograma[dia]=[]
                weekhoras[dia]=[]
                weekhoras[dia], weekcronograma[dia] = FuncionesDeDía.crearDia ()


    #B: IMPRIMIR DÍA
    if accion.lower()=="b":
        if len(weekhoras[dia])==0:
            print("¡Aún no has ingresado información sobre ese día!")
        else:
            FuncionesDeDía.imprimirDía ( weekhoras[dia],weekcronograma[dia])


    #C: ACT FIJA EN UN DÍA
    if accion.lower()=="c":
        if len(weekhoras[dia])==0:
            print("¡Aún no has creado ese día! Primero creálo y luego podrás ingresar tareas")
        else:
            weekhoras[dia], weekcronograma[dia] = FuncionesDeDía.ingresarActividades (weekhoras[dia], weekcronograma[dia])


    #D: TAREAS
    if accion.lower()=="d":
        listaTareas,fechas, tiempoTareas= ClasesTareas.ingresarTareas(listaTareas,fechas,tiempoTareas)
        #listaTareas = ["lengua","mates","historia","ingles","<"]
        #fechas = [12,13,13,14,15,16,17,18,18,18]
        #tiempoTareas = 20
        #print(tiempoTareas)


    #E: IMPRIMIR TAREAS
    if accion.lower()=="e":
        if len(listaTareas)==0:
            print("¡Aún no has ingresado tareas!")
        else:
            for tarea in listaTareas:
                print(tarea)
   
    tiempoOcupado=0
    horasOcupadas=[]
    for dias in weekcronograma:
        #print(dias)
        tiempoOcupado=0
        for act in dias:
            if act != "nada":
                tiempoOcupado = tiempoOcupado + 1
        #print(tiempoOcupado)
        horasOcupadas.append(tiempoOcupado)
           
    if accion.lower()=="f":
        print(horasOcupadas)


    if accion.lower()=="g":
        print(today)
        OrgCalendario.añadirTareas(listaTareas,today,horasOcupadas,weekcronograma)
   