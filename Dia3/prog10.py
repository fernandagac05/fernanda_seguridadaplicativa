#De las sig lista realizar las funciones:
#Obtener promedio
#Aspirantes que reprobaron

calif = [8, 9, 10, 6, 6, 7, 8, 9, 5, 6, 7, 6, 8, 8, 9, 9, 5, 6, 7, 9, 10, 7, 8, 9, 9]

def promedio(calif):
    prom = sum(calif)/len(calif)
    print("El promedio es: ", prom)
    pass

def reprobaron(calif):
    x = 0
    for alumno in calif:
        if (alumno == 5):
            x = x+1
    print("Los reprobados son: ", x)
            
    pass

promedio(calif)
reprobaron(calif)