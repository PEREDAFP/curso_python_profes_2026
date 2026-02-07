//Ejercicio para comprobar el desbordamiento
#include <stdio.h>
int main() {
    // Definimos el entero máximo posible en 32 bits
    int numero = 2147483647; 
    
    printf("Número actual: %d\n", numero);
    
    // Sumamos 1. La lógica dice que debería subir, pero...
    numero = numero + 1; 
    
    printf("Después de sumar 1: %d\n", numero);
    
    return 0;
}