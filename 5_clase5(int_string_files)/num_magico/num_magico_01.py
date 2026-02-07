# Pediremos INTENTOS veces un número al usuario para ver si adivina el número generado 
# aleatoriamente.
# Se deben dar las indicaciones de mayor o menor, según corresponda, para facilitar la adivinación

import random
magico = random.randint(1,1000)
INTENTOS = 5
for i in range(1,INTENTOS):
    usuario = int(input('Introduce el número:'))
    if usuario == magico: break
    if usuario < magico:
        print(f"El número introducido {usuario} es menor que el mágico")
    else:
        print(f"El número introducido {usuario} es mayor que el mágico")
if i < INTENTOS:
    print(f"Acertaste el número mágico {magico} en un total de {i} intentos")
else:
    print(f"El número mágico era {magico}. Otra vez será")