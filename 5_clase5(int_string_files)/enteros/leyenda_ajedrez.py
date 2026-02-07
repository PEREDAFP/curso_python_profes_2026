#!/usr/bin/env python3
# Actividad A: El crecimiento exponencial en un tablero de ajedrez
casillas = 64
granos = 1  # Empezamos con 1 grano
total_granos = 0

print(f"Casilla 1: {granos} grano")

for i in range(2, casillas + 1):
    granos = granos * 2
    total_granos += granos
    # Imprimimos solo algunas para no saturar la pantalla
    if i == 64:
        print(f"Casilla {i}: {granos} granos")

# Reto visual: Python permite usar guiones bajos para leer mejor los números
print("\nTotal legible:")
print(f"{total_granos:,}".replace(",", ".")) # Formato europeo