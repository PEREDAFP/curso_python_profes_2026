#!/bin/bash

echo "== Comparando tiempos de ejecución =="

echo -e "\n[ASM] ./holamundo_ensamblador_i686/hola"
/usr/bin/time -f "Tiempo real: %e s" ./holamundo_ensamblador_i686/hola


echo -e "\n[Python] python3 ./holamundo_python/holamundo.py"
/usr/bin/time -f "Tiempo real: %e s" python3 ./holamundo_python/holamundo.py
