# Definimos los posibles valores booleanos
valores = [True, False]

print("Tabla de verdad - Operador AND")
print("A\tB\tA and B")
for a in valores:
    for b in valores:
        print(f"{a}\t{b}\t{a and b}")

print("\nTabla de verdad - Operador OR")
print("A\tB\tA or B")
for a in valores:
    for b in valores:
        print(f"{a}\t{b}\t{a or b}")
