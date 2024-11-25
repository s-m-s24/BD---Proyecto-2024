import FuncionesDeDatos

def crearDia ():
    """
    Crea los horarios de un día, en base a la hora en que el usuario se va a dormir y se despierta
    """
    creado=False
    while (creado==False):
        despertar = input("¿A qué hora te vas a despertar? ")
        despertar= FuncionesDeDatos.verificar_num(despertar,24,0)

        dormir=input("¿A qué hora te vas a dormir? ")
        while(FuncionesDeDatos.verificar_num(dormir,24,0)==False):
            dormir=input("No ingresó un número, por favor ingrese un número: ")
        dormir=int(dormir)

        if (despertar>=dormir):
            creado=False
            print("Ha habido un error! No puedes despertarte después de irte a dormir. Por favor vuelve a ingresar estos valores.")
            

        
        else:
           creado=True 

    horas=[]
    cronograma=[]

    for hora in range (despertar,dormir,1):
        horas.append(hora)
        cronograma.append("nada")
    return horas, cronograma





def imprimirDía (horas,cronograma):
    """
    Imprime plan del día
    """
    print("Tu día va a ser así:")
    indice = 0
    for act in horas:
        print(act, end= " | ")
        print(cronograma[indice])
        indice=indice+1





def ingresarActividades (horas,cronograma):

    """
    Permite a un usuario ingresar actividades con un horario fijo
    """

    ingreso = input("Mandá 'sí' para ingresar una actividad y 'no' para ver tu cronograma de este día. Las actividades que ingreses son fijas.: ")
    actividad="no"

    if ingreso.lower() in ["sí", "si"]:
        print("Para dejar de enviar actividades envía 'no'")
        actividad = input("Ingresá una actividad: ")

    while (actividad!="no"):

        horario = input("Ingresá a qué hora es: ")

        while(horario.isnumeric()==False):
            horario=input("No ingresó un número, por favor ingrese un número: ")
        
        horario=int(horario)

        if horas.count(horario)==1:

            indice=horas.index(horario)

            if cronograma[indice]!="nada":
                print("Ya tiene una actividad en ese horario.")
                respuesta=input("Si desea reemplazarla mande 'sí', sino mande 'no' y reingrese la actividad después. ")
                
                while (respuesta.lower() not in ["sí", "si"] and respuesta.lower() != "no"):
                    print("No ha enviado una respuesta.")
                    respuesta=input("Si desea reemplazarla mande 'sí', sino mande 'no' y reingrese la actividad después. ")
                
                if (respuesta.lower() in ["sí", "si"]):
                    cronograma[indice]=actividad

            else:
                indice=horas.index(horario)
                cronograma[indice]=actividad
        else:
            print("No estarás despiert@ en ese horario, por favor elije otro")

        actividad = input("Ingresá una actividad: ")

    
    return horas, cronograma
