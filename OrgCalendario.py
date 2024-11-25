import FuncionesDeDatos

def añadirTareas (tareas, today, horasOcupadas,cronograma):


    dia =[]


    for num in range (1,8,1):
        toAppend = num + today
        dia.append(toAppend)


    for tarea in tareas:
        print(tarea)


    recorrido = [_dia for _dia in dia][-2::-1]

    tareasOrdenadas = [[] for _ in range(7)]


    for n,dia in enumerate(recorrido):
        print(f'{'='*100}')
        print(f'Dia actual: {dia} - Horas ya ocupadas: {horasOcupadas[5 - n]} Cronograma de este día {cronograma[5 - n]}')


        horasOcupadasDiaActual = horasOcupadas[5 - n]
        horasOcupadasPorTareas = 0
        
        while(horasOcupadasDiaActual + horasOcupadasPorTareas < 10) and len(tareas) >= 1:
            print(f"tarea {tareas[-1].nombre} vence el {tareas[-1].get_day()} y hoy es {dia}")
            if tareas[-1].get_day() >= dia:
                tareasOrdenadas[5 - n].append(tareas.pop(-1))
                horasOcupadasPorTareas += tareasOrdenadas[5 - n][-1]['duracion']
            else:
                break


        print('Tareas agregadas al dia actual:')
        for tarea in tareasOrdenadas[5 - n]:
            print(tarea)


    return

