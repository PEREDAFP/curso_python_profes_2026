//Ejercicio para comprobar el desbordamiento
#include <stdio.h>
int main() {
    // Definimos el entero máximo posible en 32 bits
    long long numero = 9223372036854775807; 
    
    printf("Número actual: %lld\n", numero);
    
    // Sumamos 1. La lógica dice que debería subir, pero...
    numero = numero + 1; 
    
    printf("Después de sumar 1: %lld\n", numero);
    
    return 0;
}