#!/usr/bin/env python3
# Actividad A: El crecimiento exponencial en un tablero de ajedrez
casillas = 64
total_granos = 0
for i in range(0, casillas):
   
    total_granos += 2**i
    print(f"Para la casilla {i}: total granos:{total_granos} en esta casilla:{2**i}")
    
# Reto visual: Python permite usar guiones bajos para leer mejor los números
print("\nTotal legible:")
print(f"{total_granos:,}".replace(",", ".")) # Formato europeo