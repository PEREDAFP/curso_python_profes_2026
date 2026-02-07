#!/usr/bin/env python3

with open("datos.txt",'a', encoding='utf-8') as f:
    f.write("Línea añadida") #Observa que no se añade un retorno de carro en esa línea añade \n y compara
print("Hemos añadido una línea")

#Después de ejecutar este programa vuelve a ejecutar 01_fichero.py y observa qué ha ocurrido