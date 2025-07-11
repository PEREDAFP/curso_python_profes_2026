section .data
    msg db "Hola Mundo", 0xA
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, msg        ; dirección del mensaje
    mov rdx, len        ; longitud del mensaje
    syscall             ; llamada al sistema

    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; código de salida: 0
    syscall
