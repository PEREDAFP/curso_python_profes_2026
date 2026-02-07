# Pediremos INTENTOS veces un número al usuario para ver si adivina el número generado 
# aleatoriamente.
# Se deben dar las indicaciones de mayor o menor, según corresponda, para facilitar la adivinación
# En esta versión introducimos las excepciones para evitar que el usuario introduzca un valor distinto
# a un número
# Las volveremos a ver en ficheros.

import random
magico = random.randint(1,1000)
INTENTOS = 6 #Debemos tener en cuenta que range(1,x) devuelve una lista de números de 1 a x-1
for i in range(1,INTENTOS):
    try:
        usuario = int(input('Introduce el número:'))
    except:
        print("Debes introducir números enteros")
        continue
    if usuario == magico: break
    if usuario < magico:
        print(f"El número introducido {usuario} es menor que el mágico")
    else:
        print(f"El número introducido {usuario} es mayor que el mágico")
if i < INTENTOS:
    print(f"Acertaste el número mágico {magico} en un total de {i} intentos")
else:
    print(f"El número mágico era {magico}. Otra vez será")