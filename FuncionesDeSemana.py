import FuncionesDeDía

def imprimirSemana (horassemana,agenda):
    """
    Imprime una semana entera, día por día
    """
    for dia in range (1,8,1):
        print()
        print("Día ", dia, ":")
        horas=horassemana[dia-1]
        #print(horas)
        cronograma=agenda[dia-1]
        #print(cronograma)
        FuncionesDeDía.imprimirDía(horas,cronograma)