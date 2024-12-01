import FuncionesDeDía
import FuncionesDeDatos
import ClasesTareas
import OrgCalendario


horassemana = []
agenda = []


accion = 0


day1horas = []
day1cronograma = []


day2horas = []
day2cronograma = []


day3horas = []
day3cronograma = []


day4horas = []
day4cronograma = []


day5horas = []
day5cronograma = []


day6horas = []
day6cronograma = []


day7horas = []
day7cronograma = []


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
    print("Elija 'F' para ver qué tareas debe hacer cada día")
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
        #print(tiempoTareas)


    #E: IMPRIMIR TAREAS
    if accion.lower()=="e":
        if len(listaTareas)==0:
            print("¡Aún no has ingresado tareas!")
        else:
            for tarea in listaTareas:
                print(tarea)
   
    #F: ORGANIZAR CUÁNDO HACER LAS TAREAS
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
        #print(today)
        OrgCalendario.añadirTareas(listaTareas,today,horasOcupadas,weekcronograma)
   
    if accion.lower()=="g":
        materiaPedida=input("¿Qué materia deseas ver?, envía 'todas' para ver todas tus materias clasificadas por materia: ")
        OrgCalendario.clasificarPorMateria(listaTareas,materiaPedida)
        
