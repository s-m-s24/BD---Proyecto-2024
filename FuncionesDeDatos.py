def verificar_num(variable,maximo,minimo):
    while(variable.isnumeric()==False):
        variable=input("No ingresó un número, por favor ingrese un número: ")
    variable=int(variable)
    while(variable>maximo or variable<minimo):
        variable=input("No ingresó un número válido: ")
        while(variable.isnumeric()==False):
            variable=input("No ingresó un número, por favor ingrese un número: ")
        variable=int(variable)
    variable=int(variable)
    return variable


def obtener_dia_tareas (dia,mes,dias_por_mes):
    mes -= 1


    dia_del_mes = sum(dias_por_mes[:mes]) + dia


    return dia_del_mes


def ordenar_lista_tareas (listaTareas : list,fechas,day,tarea):
    ingresado=False
    if len(listaTareas) >=1:
        indice=0
        while ingresado==False:
            for num in fechas:
                if ingresado==False and day<num:
                    listaTareas.insert(indice,tarea)
                    ingresado=True
                    fechas.insert(indice,day)
                indice=indice+1
            if ingresado==False:
                listaTareas.append(tarea)
                fechas.append(day)
                ingresado=True

    if len(listaTareas) == 0:
        listaTareas.append(tarea)
        fechas.append(day)
    
    return listaTareas
