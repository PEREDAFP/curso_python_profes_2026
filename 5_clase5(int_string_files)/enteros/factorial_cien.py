#!/usr/bin/env python3
# Mostramos otra librería que puede ser interesante
import math

# 1. Calculamos el factorial de 100
numero_gigante = math.factorial(100)

print(f"El factorial de 100 es:\n{numero_gigante}")

# 2. Vamos a contar cuántos dígitos tiene
num_str = str(numero_gigante)
cantidad_digitos = len(num_str)

print(f"\nEste número tiene {cantidad_digitos} dígitos.")
