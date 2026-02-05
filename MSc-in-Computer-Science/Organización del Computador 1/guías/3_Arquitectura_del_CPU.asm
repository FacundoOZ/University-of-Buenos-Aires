
#============================================================================================================================================
# Práctica 3: Arquitectura del CPU (Central Processing Unit)
#============================================================================================================================================

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Dado el siguiente arreglo de enteros de 16 bits en lenguaje Java: int[] arreglo16b = {-1, 170, 255, -255, 0, 32, 10000, 0},
si t0 = 0xCC, escribir un programa que dado un index i, devuelve el arreglo16b[i]."""

"""La dirección es:
  DIRECCIÓN = BASE + OFFSET(BASE).
Por lo tanto:
  DIR = 0xCC + 2*i (pues cada índice i tiene 2 bytes)"""

# Input : a0 = i al índice del arreglo:

slli t1, a0, 1      # t1 = i*2,             (cada elemento tiene 2 bytes)
add  t1, t0, t1     # t1 = 0xCC + (2*i)     (calculo la dirección)
lh   a0, 0(t1)      # a0 = memoria[t1]      (en a0, cargo con offset=0, la base (0xCC + 2*i))

# Cargamos media palabra (16 bits) y se extiende el signo a 32 bits). Output : a0 = arreglo16b[i]

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Dado los siguientes dos programas y suponiendoque ambos empiezanen la dirección 0x00.
# A) Escribir en qué dirección se encuentra cada etiqueta.
# B) Para cada instrucción de salto, escribir el offset que se aplicará al PC.

# Programa 1:
# A)
Inicio:
  addi a0, zero, 10       # 0x00
  addi a1, zero, 50       # 0x04
Ciclo:
  ble  a1, zero, Fin      # 0x08
  sub  a1, a1, a0         # 0x0C
  j    Ciclo              # 0x10
Fin:
  beq  a1, zero, Inicio   # 0x14

"""B) Los saltos son los siguientes:
    ble a1, zero, Fin
    j Ciclo
    beq a1, zero, Inicio

1. ble es un salto condicional, entonces:
  Offset = target - current = 0x14 - 0x08 = 0x0C
2. j es un salto incondicional, entonces:
  Offset = target - current = 0x08 - 0x10 = -0x08
3. beq es un salto condicional, entonces:
  Offset = target - current = 0x00 - 0x14 = -0x14"""

# Programa 2:
# A)
Inicio:
  li  a1, 0xFFFFFFFF  # 0x00
  li  a2, 0x1         # 0x04
Vuelta:
  beq a1, a2, Inicio  # 0x08
  sub a2, a2, a1      # 0x0C
  nop                 # 0x10
  j   Vuelta          # 0x14

"""B) Los saltos son los siguientes:
    beq a1, a2, Inicio
    j Vuelta

1. beq es un salto condicional, entonces:
  Offset = target - current = 0x00 - 0x08 = -0x08
2. j es un salto incondicional, entonces:
  Offset = target - current = 0x08 - 0x14 = -0x0C"""

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Dado el siguiente programa en lenguaje C:
""" int x = 2;
  int y = 32;
  x = x + y """
# A) Traducir a lenguaje ensamblador de RISC-V. Usar los registros t0 y t1 inicializados con números de 8 bits para representar a las
# variables x e y, respectivamente.

addi t0, zero, 2    # Agrego la constante 2 al registro t0=x (sumo 0 + 2)
addi t1, zero, 32   # Agrego la constante 32 al registro t1=y (sumo 0 + 32)
add  t0, t0,   t1      # Sumo x = x+y

# B) Escribir un programa que guarde en t2 un número de 32 bits dividiendo sus 12 bits más significativos en t0 y sus otros 20 bits en t1.

# Dado t2 un número de 32-bits, procedemos de la siguiente forma:
srli t0, t2, 20     # Desplazamos a derecha 20 unidades para obtener los 12 bits más significativos (MSB) en t0
li   t3, 0x000FFFFF # Creamos un número de la forma 0000 0000 0000 1111 1111 1111 1111 1111
and  t1, t2, t3     # Con AND, convierto en 0 los primeros 12 bits más significativos, obteniendo los 20 menos significativos (LSB) en t1
slli t2, t0, 20     # Volvemos los 12 bits más significativos a su posición original
or   t2, t2, t1     # Escribimos t2 como los 12 bits (MSB) de t0 + los 20 bits (LSB) de t1 utilizando or.

"""Recordar que:
  and = True    <=>     x = True , y = True
  or  = False   <=>     x = False, y = False"""

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# A) Ensamblar el siguiente código escrito en lenguaje RISC-V:

addi a6, x0, 10 # I-type, opcode = 0010011, funct3 = 0x0, rd = rs1 + imm
add  a0, a1, a6 # R-type, opcode = 0110011, funct3 = 0x0, funct7 = 0x00, rd = rs1 + rs2
bltz x1, 0x0ABC # pseudoinstrucción => bltz rs, offset = blt rs, x0, offset # B-type

""" Sabemos que RISC-V utiliza encoding de 5 bits (para x0, x1, ..., x31) y utilizando la referencia de su set de instrucciones, tenemos que:
-addi a6, x0,  10:
    (rd, rs1, imm)
  Tenemos que:
  10      = 1010                  => necesitamos [20:31] = im[11:0] por lo tanto, 10 = 000000001010 (el número debe tener 12 bits)
  x0      = zero = 0 (default)    => necesitamos [15:19] por lo tanto, x0 = 00000 (5 bits)
  funct3  = 0x0 (hexadecimal) = 0 => necesitamos [12:14] por lo tanto, funct3 = 000 (3 bits)
  a6      = x16 = 10000           => necesitamos [7:11] (ya los tenemos, por default), por lo tanto, a6 = 10000
  opcode  = 0010011               => necesitamos [0:6] => listo!, opcode = 0010011
-add  a0, a1,  a6:
    (rd, rs1, rs2)
  Tenemos que:
  [25:31] = funct7 = 0x00 = 0000000
  [20:24] = rs2 = a6 = x16 = 10000
  [15:19] = rs1 = a1 = x11 = 01011
  [12:14] = funct3 = 0x0 = 000
  [7:11]  = rd = a0 = x10 = 01010
  [0:6]   = opcode = 0110011
-blt  x1,  x0,  0x0ABC:
    (rs1, rs2, offset)
  Tenemos que:
  [25:31] = imm[12|10:5] = 0x0ABC[12|10:5] = 1 101011
  [20:24] = rs2 = x0 = zero = 0 = 00000
  [15:19] = rs1 = x1 = 00001
  [12:14] = funct3 = 0x4 = 100
  [7:11]  = imm[4:1|11] = 0x0ABC[4:1|11] = 1100 0
  [0:6]   = opcode = 1100011
Vemos que 0x0ABC = 0 x 16^3 + 10 x 16^2 + 11 x 16^1 + 12 x 16^0 = 0 + 2560 + 176 + 12 = 2748 = 101010111100 (número negativo)"""

# Finalmente:

""" addi a6, x0, 10 = 000000001010 00000 000 10000 0010011
  add  a0, a1, a6 = 0000000 10000 01011 000 01010 0110011
  bltz x1, 0x0ABC = 1 101011 00000 00001 100 1100 0 1100011"""

# B) Desensamblar el siguiente programa escrito en lenguaje de máquina RISC-V:

"""i) I-type:
  imm[11:0]    rs1   funct3 rd    opcode
  011111111111 00000 000    01010 0010011"""

addi a0, zero, 2047 # (addi rd, rs1, imm)

"""ii) I-type:
  imm[11:0]    rs1   funct3 rd    opcode
  010101010101 00000 000    01011 0010011"""

addi a1, zero, 1365

"""iii) I-type:
  imm[11:0]    rs1   funct3 rd    opcode
  000000000000 00000 000    00000 0010011"""

addi zero, zero, zero

"""iv) R-type:
  funct7  rs2   rs1   funct3 rd    opcode
  0000000 01010 01011 100    01100 0110011"""

xor a2, a1, a0

"""v) B-type:
  imm[12|10:5] rs2   rs1   funct3 imm[4:1|11] opcode
  1111111      00000 01100 000    10101       1100011"""

beq a2, zero, -6

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 9 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Se cuenta con cuatro datos sin signo de un byte cada uno almacenados en el registro t0 y queremos sumar el valor de los cuatro datos.
Escribir un programa en lenguaje ensamblador RISC-V que realice esta operación y almacene el resultado en el registro t0.
Ejemplo: t0 0x90 0x1A 0x00 0x02. Con este dato el registro debería valer 0x000000AC."""

# t0 = 0x90 0x1A 0x00 0x02

andi t1, t0, 0xFF       # b0
srli t0, t0, 8
andi t2, t0, 0xFF       # b1
srli t0, t0, 8
andi t3, t0, 0xFF       # b2
srli t0, t0, 8
andi t4, t0, 0xFF       # b3

add  t0, t1, t2
add  t0, t0, t3
add  t0, t0, t4

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 10 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""En la arquitectura RISC-V tenemos una instrucción denominada sll que, dado un registro destino y dos registros fuente, mueve el primer
registro fuente tantos bits a izquierda como indique el segundo registro fuente y guarda el resultado en el registro de destino.
Por ejemplo, tenemos un dato en t0 y un valor en t1:
  t0 0x08 0x2B 0x00 0x23
  t1 0x00 0x00 0x00 0x04,
Luego de hacer slli t0, t0, t1, el registro t0 quedaría de la siguiente forma:
  t0 0x82 0xB0 0x02 0x30.
Suponiendo que el valor a shiftear se encuentra en el registro t0, que el resultado se guarda en t0 y que la cantidad de posiciones se
encuentra en el registro t1 (entendido como  un número entero sin signo), se pide:"""
# A) Escribir el pseudocódigo del programa sll asumiendo que no tenemos dicha instrucción disponible.
# B) Escribir el programa de sll en lenguaje assembler de RISC-V.
# C) El programa creado, ¿usa otros registros además de t0 y t1? Si lo hace, modificar el programa de modo que solo se alteren los valores
# de t0 y t1.

# A)
"""
while (t1 > 0):
  t0 = t0 << 1
  t1 = t1 - 1
"""

# B)
ciclo_sll:
  beq  t1, zero, fin
  slli t0, t0,    1
  addi t1, t1,   -1
  j    ciclo_sll

fin:

# C) No, el programa creado no usa otros registros, solo modifica los registros t0 y t1.

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 11 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Dado vector de enteros Arreglo y su Longitud, escribir un programa que en cuentre el valor máximo del Arreglo. Se puede asumir que el
inicio de del arreglo está en t0 y la longitud en t1.
Ejemplo:
  Entrada: Arreglo = [3, 1, 4, 1, 5, 9, 2, 6], Longitud = 8.
  Salida: 9."""

lw   t2, 0(t0)             # max = primer elemento
addi t0,   t0,  4
addi t1,   t1, -1

ciclo:
  beq  t1, zero, fin
  lw   t3, 0(t0)
  blt  t3,   t2, continuar
  mv   t2,   t3

continuar:
  addi t0, t0,  4
  addi t1, t1, -1
  j    ciclo

fin:
  mv   t0, t2              # resultado en t0

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 12 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Sean dos vectores s y q tales que las direcciones de inicio se encuentran en t0 y t1 respectivamente. Sabiendo que la longitud de ambos se
encuentra en t2, escribir un programa que copie la información de q a s."""

ciclo:
  beq  t2, zero, fin
  lw   t3, 0(t1)
  sw   t3, 0(t0)

  addi t0, t0,  4
  addi t1, t1,  4
  addi t2, t2, -1
  j    ciclo

fin:

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 13 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Sean dos vectores s y q tales que las direcciones de inicio se encuentran en t0 y t1 respectivamente. Sabiendo que la longitud de ambos se
encuentra en t2, escribir un programa que copie los elementos pares de q a s. Si la posición i de q no tiene un elemento par, se debe poner
un 0 en s."""

ciclo:
  beq  t2, zero, fin
  lw   t3, 0(t1)

  andi t4,   t3, 1
  bne  t4, zero, impar
  sw   t3, 0(t0)
  j    continuar

impar:
  sw   zero, 0(t0)

continuar:
  addi t0, t0,  4
  addi t1, t1,  4
  addi t2, t2, -1
  j    ciclo

fin:

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 14 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""La arquitectura RISC-V posee operaciones aritméticas sobre números enteros codificados en notación complemento a 2 de 32 bits. El programa
sumar64 realiza la suma en notación complemento a 2 de dos números enteros de 64 bits en esta arquitectura. En los registros t0 y t1 se
indican las direcciones de cada número y en t2 se indica la posición de memoria en donde debe guardarse el resultado. Se pide:"""
# A) Escribir el pseudocódigo del programa sumar64.
# B) Escribir sumar64 en código assembler de RISC-V.

# A)
"""
a_low  = mem[t0]
a_high = mem[t0+4]
b_low  = mem[t1]
b_high = mem[t1+4]

sum_low = a_low + b_low
carry = overflow(sum_low)

sum_high = a_high + b_high + carry

guardar sum_low y sum_high
"""

# B)
sumar64:
  lw   t3, 0(t0)  # a_low
  lw   t4, 4(t0)  # a_high
  lw   t5, 0(t1)  # b_low
  lw   t6, 4(t1)  # b_high

  add  t7, t3, t5 # sum_low
  sltu t8, t7, t3 # carry
  add  t9, t4, t6
  add  t9, t9, t8 # sum_high

  sw   t7, 0(t2)
  sw   t9, 4(t2)
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 15 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""sumaVector64 es un programa que suma los valores de un vector de n posiciones enteras de 64 bits codificados en notación complemento a 2.
En t0 se recibe la cantidad de elementos que tiene el vector y en t1 la posición de memoria en donde está almacenado dicho vector. En t2 se
recibe la posición de memoria en donde debe guardarse el resultado. Suponiendo que se cuenta con el programa sumar64 descripto en el
ejercicio anterior, se pide:"""
# A) Escribir el pseudocódigo del programa sumaVector64.
# B) Escribir sumaVector64 en código assembler de RISC-V.

# A)
"""
resultado = 0
for i in 0..n-1:
  resultado += vector[i]
guardar resultado
"""

# B)
sumaVector64:
  sw   zero, 0(t2)   # Resultado = 0 (low)
  sw   zero, 4(t2)   # Resultado = 0 (high)

ciclo:
  beq  t0, zero, fin

  mv   a0, t1        # Número actual
  mv   a1, t2        # Acumulador
  mv   a2, t2
  jal  sumar64

  addi t1, t1,  8    # Siguiente número
  addi t0, t0, -1
  j    ciclo

fin:
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————