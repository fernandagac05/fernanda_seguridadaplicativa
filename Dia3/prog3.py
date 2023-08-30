#Actividad 1
#Programa que muestra una cadena al revés

#string ="Fernanda"
#print(string[::-1])

#Palindromo
entrada = input("¿Será palindomo?: " )

if (entrada[::-1].lower == entrada.lower):
    print("Es palindromo")
    
else:
    print("No es palindromo")