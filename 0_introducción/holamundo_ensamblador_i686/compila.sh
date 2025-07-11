#Es fácil que tengas que instalar nasm con sudo apt install nasm o similar
nasm -f elf64 holamundoi686.s -o hola.o
ld hola.o -o hola
