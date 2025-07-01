.global _start

.section .data
msg:
    .asciz "Hola Mundo\n"

.section .text
_start:
    ldr r0, =1          @ stdout
    ldr r1, =msg        @ mensaje
    ldr r2, =11         @ longitud
    mov r7, #4          @ syscall write
    svc #0

    mov r7, #1          @ syscall exit
    mov r0, #0
    svc #0
