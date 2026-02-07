#!/usr/bin/env python3
try:
    with open("datos.txt", 'w', encoding='utf-8') as f:
        f.write("Este es el dato que hemos grabado")
    print(f"Hemos terminado con {f.name}")
except:
    print("Problemillas con el fichero")