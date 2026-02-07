#!/usr/bin/env python3

# Vamos a mostrar un programa que va a ir creando números cada vez más grandes y llegará el momento en el que el sistema operativo no
# pueda darnos más memoria y...
import sys
import time

import sys

# Aumentamos el límite a 1.000.000.000 dígitos (o el número que necesites) para evitar la limitación de las versiones 3.10 y superiores
sys.set_int_max_str_digits(1000000000)
def romper_la_ram():
    print("--- INICIANDO PROTOCOLO DE DESTRUCCIÓN DE RAM ---")
    print("Pulsa Ctrl+C para abortar antes de que sea tarde...\n")
    time.sleep(2)

    base = 2
    exponente = 10  # Empezamos con 2^10 (1024)
    
    try:
        while True:
            # 1. Calculamos el número
            inicio = time.perf_counter()
            numero_gigante = base ** exponente
            fin = time.perf_counter()
           
            # 2. Medimos cuánto ocupa en memoria (en Bytes)
            # sys.getsizeof() nos dice el tamaño del objeto en RAM
            tamano_bytes = sys.getsizeof(numero_gigante)
            
            # Convertimos a Megabytes para que sea legible
            tamano_mb = tamano_bytes / (1024 * 1024)
            
            print(f"Exponente: 2^{exponente}")
            print(f"Dígitos (aprox): {len(str(numero_gigante))}") 
            print(f"Tiempo de cálculo: {fin - inicio:.4f} seg")
            print(f"RAM ocupada por este número: {tamano_mb:.4f} MB")
            print("-" * 30)
            
            # 3. DUPLICAMOS la apuesta para la siguiente vuelta
            # El crecimiento será explosivo
            exponente = exponente * 2
            
            # Pequeña pausa para que te dé tiempo a arrepentirte
            time.sleep(1)

    except MemoryError:
        print("\n!!! MEMORY ERROR !!!")
        print("El sistema operativo ha denegado más memoria.")
        print("Has alcanzado el límite físico de tu máquina.")
    except KeyboardInterrupt:
        print("\n--- ABORTADO POR EL USUARIO ---")
        print("Sabia decisión. Tu RAM vive para luchar otro día.")

if __name__ == "__main__":
    romper_la_ram()