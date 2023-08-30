#Actividad 4
#Del siguiente diccionario realizar las funciones que obtengan:
#Promedio
#Los alumnos con mayor calif y menor calif

alumnos = {
    "Juan" : 8,
    "Giselle" : 9,
    "Damian" : 5,
    "Ricardo" : 6,
    "Yaotzin" : 6,
    "Erick" : 7,
    "Mario" : 8,
    "Edgar" : 9,
    "Fernanda" : 5,
    "Daniel" : 6,
    "Jesus" : 7,
    "Damian" : 8,
    "Yema" : 6,
    "Eduardo" : 9,
    "Bryan" : 9,
    "Mariano" : 10,
    "Alberto" : 8
}

def promedio(alumnos):
    prom = 0
    
    for alumno in alumnos:
        prom = prom + (int(alumnos[alumno]))
    prom = prom / len(alumnos)
    print("EL promedio es: " + str(prom))
        
    pass

def mayor(alumnos):
    for alumno in alumnos:
        if (int(alumnos[alumno]) == 10):
            print("El mayor promedio es: " + str(alumno))
    pass

def menor(alumnos):
    for alumno in alumnos:
        if (int(alumnos[alumno]) == 5):
            print("El menor promedio es: " + str(alumno))

    pass

promedio(alumnos)
mayor(alumnos)
menor(alumnos)