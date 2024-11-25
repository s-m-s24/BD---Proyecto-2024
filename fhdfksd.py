class tarea:
    mes : int
    dia : int

    def __init__(self, mes : int, dia : int):
        self.mes = mes
        self.dia = dia

    def get_fecha(self):
        return self.mes, self.dia
    
def get_dia_año(dia: int, mes: int):
    mes -= 1

    dias_por_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

    dia_del_mes = sum(dias_por_mes[:mes]) + dia

    return dia_del_mes

a = [tarea(3, 6)]
a.append(tarea(4, 26))
a.append(tarea(12, 15))
a.append(tarea(7, 3))

#print([objeto.get_fecha() for objeto in a])
print(get_dia_año(31,11))