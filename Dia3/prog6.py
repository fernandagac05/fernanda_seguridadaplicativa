#Actividad 2
#Modificar el código para hacer una calculadora que reciba parámetros implementando funciones

def suma(num1, num2): return num1 + num2
def resta(num1, num2): return num1 - num2
def multi(num1, num2): return num1 * num2
def divi(num1, num2): return num1 / num2

print("1. SUMA 2. RESTA 3. MULTI 4. DIVI.")
opcion = input("Elige una operacion: ")
num1 = input("Escribe el primer numero: ")
num2 = input("Escribe el segundo numero: ")


def operacion(opcion):
    
    if (opcion == 1):
        print(suma(num1,num2))
        
    elif (opcion == 2):
        print(resta(num1, num2))
        
    elif (opcion == 3):
        print(multi(num1, num2))
        
    elif (opcion == 4):
        print(divi(num1, num2)) 
        
    else: print("Mal")
        
    





