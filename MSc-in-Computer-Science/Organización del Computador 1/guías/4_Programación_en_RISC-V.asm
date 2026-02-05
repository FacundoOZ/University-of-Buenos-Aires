
#============================================================================================================================================
# Práctica 4: Programación en RISC-V
#============================================================================================================================================

# Parte 1: Convención de llamada
#———————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Los siguientes programas fueron escritos por 2 programadores sin comunicarse. Programador A escribió las funciones etiquetadas como
FUNCION, mientras que Programador B escribió sus casos de test. Tanto los testeos como las funciones debían utilizar la convención de llamada
estándar, ya que luego se agregarían al resto del código de la empresa donde ambos trabajan. Aunque ambos dicen haber cumplido con esto, al
evaluar, todos los tests fallan. Para cada programa:"""

# -Comentar los casos de test y explicar qué se está evaluando.
# -Comentar el código de la función, explicar su funcionamiento y darle un nombre descriptivo.
# -Marcar el prólogo y el epílogo de la función.
# -Encontrar los errores causados por no seguir la convención y decidir si es culpa del Programador A y/o B. Justificar.
# -Arreglar la función, los casos de test y comprobar el funcionamiento en el emulador Ripes.

# A)
main:
  li   s1, 2024
  mv   a0, s1
  jal  ra, FUNCION
  add  a0, s1, a0
  bnez a0, noFunciona
funciona:
  li   a1, 1
  j    fin
noFunciona:
  li   a1, 0
fin:
  j    fin

FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  not  s1, a0
  addi a0, s1, 1
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

# B)
main:
  li  a0, 4
  li  a1, 6
  jal ra, FUNCION
  li  a2, 10
  bne a0, a2, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j fin

FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  add  a3, a0, a1
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

# C)

main:
  li  a0, 1
  li  a1, 2
  jal ra, FUNCION
  li  a3, 3
  bne a0, a3, noFunciona #(4*1-2/2)!=3
  li  a0, 3
  jal ra, FUNCION
  li  a3, 11
  bne a0, a3, noFunciona #(4*3-2/2)!=11
  li  a1, 12
  jal ra, FUNCION
  li  a3, 6
  bne a0, a3, noFunciona #(4*3-12/2)!=6
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  slli a2, a0, 2
  srai a1, a1, 1
  sub  a0, a2, a1
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

# D)

main:
  li  a0, 4
  li  a1, 87
  jal ra, FUNCION
  li  a2, 87
  bne a0, a2, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin


FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  mv   a0, a2
  bgt  a0, a5, terminar
  mv   a0, a5
terminar:
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

# E)
main:
  li  a3, 4
  jal ra, FUNCION
  li  a2, 10
  bne a0, a2, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  mv   a1, a0
  mv   a0, zero
inicioCiclo:
  beq  a1, zero, finCiclo
  add  a0, a0, a1
  addi a1, a1, -1
  j    inicioCiclo
finCiclo:
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

# F)

main:
  li  a0, 7
  li  a1, 13
  jal ra, FUNCION
  mv  s1, a0
  li  a1, -1
  jal ra, FUNCION
  beq a0, a2, equivalentes
diferentes:
  li  a1, 0
  j   fin
equivalentes:
  li  a1, 1
fin:
  j   fin


FUNCION:
  addi sp, sp, -4
  sw   ra, 0(sp)
  mv   a2, a1
  bgt  a1, zero, inicioCiclo
  sub  a2, zero, a1
inicioCiclo:
  blt  a2, a0, finCiclo
  sub  a2, a2, a0
  j    inicioCiclo
finCiclo:
  mv   s1, a0
  mv   a0, a2
  bgt  a1, zero, terminar
  beq  a0, zero, terminar
  sub  a0, s1, a0 #(-n)%m=m-(n%m)
terminar:
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Programar en RISC-V las siguientes funciones y al menos 2 casos de test que comprueben el funcionamiento de cada una de ellas. Se debe
usar la convención de llamada de RISC-V."""

# A) Multiplicación:    mult(x,y) = x*y \ptd x, y \in \bb{Z}

# B) Fibonacci Iterativo:

# C) Mayor en R^2:

"""
                          {1}  {x_1 > x_2 y y_1 > y_2}
mayor(x_1,y_1,x_2,y_2) := {-1} {x_2 > x_1 y y_2 > y_1}
                          {0}  {si no}
"""

# D) División:          div(x,y) = \floor x/y \floor \ptd x, y \in \bb{Z}

# Parte 2: Uso del stack
#———————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Los siguientes programas fueron escritos por 3 programadores sin comunicarse. Programador A escribió las funciones etiquetadas como
FUNCION utilizando funciones auxiliares etiquetadas como FUNCION_AUX, provenientes del Programador B, mientras que Programador C escribió sus
asos de test. Tanto los testeos como las funciones debían utilizar la convención de llamada estándar, y también deben hacerlo las funciones
auxiliares. Aunque Programador A y C dicen haber cumplido con esto, al evaluar, todos los tests fallan. Para cada programa:"""

# -Comentar los casos de test y explicar qué se está evaluando.
# -Comentar el código de la función y función auxiliar, explicar su funcionamiento y darle un nombre descriptivo.
# -Marcar el prólogo y el epílogo de la función.
# -Encontrar los errores causados por no seguir la convención y decidir cuáles Programadores son los culpables. Justificar.
# -Arreglar las funciones, los casos de test y comprobar el funcionamiento en el emulador Ripes.
# -Realizar un seguimiento del stack.

# A)
main:
  li  a0, 4
  li  a1, 87
  li  a2, -124
  li  a3, -14
  jal ra, FUNCION
  li  a2, -124
  bne a0, a2, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  addi sp, sp, -12
  sw   a2, 0(sp)
  sw   a3, 4(sp)
  sw   ra, 8(sp)
  jal  ra, FUNCION_AUX
  mv   s1, a0
  lw   a0, 0(sp)
  lw   a1, 4(sp)
  jal  ra, FUNCION_AUX
  mv   a1, s1
  jal  ra, FUNCION_AUX
  lw   ra, 8(sp)
  addi sp, sp, 12
  ret

FUNCION_AUX:
  addi sp, sp, -4
  sw   ra, 0(sp)
  bgt  a1, a0, terminar
  mv   a0, a1
terminar:
  ret


# B)

main:
  li  a0, 3
  li  a1, 10
  li  a2, -5
  li  a3, 2
  li  a4, 5
  li  a5, -1
  jal ra, FUNCION
  li  a2, 1
  bne a0, a2, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  jfin

FUNCION:
  addi sp, sp, -12
  sw   a2, 0(sp)
  sw   s0, 4(sp)
  sw   ra, 8(sp)
  li   s0, 1
  mv   a2, a4
  jal  ra, FUNCION_AUX
  bne  a0, s0, return
  lw   a0, 0(sp)
  mv   a1, a3
  mv   a2, a5
  jal  ra, FUNCION_AUX
  bne  a0, s0, return
  lw   s0, 4(sp)
  lw   ra, 8(sp)
  addi sp, sp, 12
return:
  ret

FUNCION_AUX:
  addi sp, sp,-4
  sw   ra, 0(sp)
  sub  a3, a2, a0
  blt  a3, zero, afuera
  sub  a5, a2, a1
  bgt  a5, zero, afuera
adentro:
  li   a0, 1
  j    terminar
afuera:
  li   a0, 0
terminar:
  lw   ra, 0(sp)
  addi sp, sp, 4
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Programar en RISC-V las siguientes funciones y al menos 2 casos de test que comprueben el funcionamiento de cada una de ellas. Se debe
usar la convención de llamada de RISC-V."""

# A)
# i)  Inv(x) = -x
# ii) InvertirArreglo: Dado un puntero a un arreglo de enteros de 32 bits y la cantidad de elementos, cambia cada valor del arreglo por su
# inverso aditivo.

# B)
# i)  Es Potencia de Dos:
"""                   {1}  {\ex k \in \bb{N} : 2^k = x}
esPotenciaDeDos(x) :=
                    {0}  {si no}"""
# ii) Potencias en Arreglo: Dado un puntero a un arreglo de enteros sin signo de 8 bits y la cantidad de elementos, devuelve cuantos de ellos
# son potencias de 2. Ayuda: pensar como una potencia de dos se ve en base binaria.

# C)
# i)  Evaluar Monomio: evaluarMonomio(x,c,p) = c * (x**p)
# ii) Evaluar Polinomio: Dado un puntero a un arreglo de enteros de 32 bits, la cantidad de elementos del arreglo y un entero x, evalua en x
# el polinomio construido usando como coeficientes los valores dentro del arreglo. Ejemplo: el arreglo [3, -1, 5, 0, 2] equivaldría al
# polinomio P(x) = 3 - x + 5 * (x**2) + 2 * (x**4).

# Parte 3: Recursión
#———————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Los siguientes programas fueron escritos por 2 programadores sin comunicarse. Programador A escribió las funciones recursivas etiquetadas
como FUNCION, mientras que Programador B escribió sus casos de test. Las funciones debían utilizar la convención de llamada estándar, ya que
luego se agregarían al resto del código de la empresa donde ambos trabajan. Aunque A dice haber cumplido con esto, al evaluar, todos los
tests fallan. Para cada programa:"""

# -Comentar los casos de test y explicar qué se está evaluando.
# -Comentar el código de la función, explicar su funcionamiento y darle un nombre descriptivo.
# -Marcar el prólogo y el epílogo de la función.
# -Indicar el caso base, y la definición recursiva de la función.
# -Encontrar los errores causados por no seguir la convención o hacer mal uso del stack. Justificar.
# -Arreglar la función, y comprobar el funcionamiento en el emulador Ripes.
# -Para un caso de test, realizar un gráfico del flujo que realiza el programa.

# A)
main:
  li  a0, 13
  li  a1, 5
  jal FUNCION
  li  a1, 3                    # 13 mod(5) = 3
  bne a0, a1, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  blt a0, a1, terminar
  sub a2, a0, a1
  jal FUNCION
terminar:
  ret


# B)
main:
  li  a0, 4
  jal FUNCION
  li  a1, 5
  bne a0, a1, noFunciona
  li  a0, 5
  jal FUNCION
  li  a1, 8
  bne a0, a1, noFunciona
  li  a0, 6
  jal FUNCION
  li  a1, 13
  bne a0, a1, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  addi sp, sp, -8
  sw   a0, 0(sp)
  sw   ra, 4(sp)
  li   a1, 1
  beq  a0, zero, casoBase0
  beq  a0, a1, casoBase1
  addi a0, a0, -1
  jal  FUNCION
  mv   a1, a0
  lw   a0, 0(sp)
  addi a0, a0, -2
  jal  FUNCION
  add  a0, a1, a0
  j    prologo
casoBase0:
  li   a0, 1
  j    prologo
casoBase1:
  li   a0, 1
prologo:
  lw   ra, 4(sp)
  addi sp, sp, 8
  ret

# C)
main:
  li  a0, 4
  jal FUNCION
  li  a1, 10
  bne a0, a1, noFunciona
funciona:
  li  a1, 1
  j   fin
noFunciona:
  li  a1, 0
fin:
  j   fin

FUNCION:
  beq  a0, zero, casoBase
  addi sp, sp, -8
  sw   a0, 0(sp)
  sw   ra, 4(sp)
  addi a0, a0, -1
  jal  FUNCION
  lw   a1, 0(sp)
  add  a0, a1, a0
  j    prologo
casoBase:
  li   a0, 0
prologo:
  lw   ra, 4(sp)
  addi sp, sp, 8
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 8 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Programar en RISC-V las siguientes funciones recursivas y al menos 2 casos de test que comprueben el funcionamiento de cada una de ellas.
Se debe usar la convención de llamada de RISC-V."""

# A) Factorial:
"""         {1}              {si x = 0}
fact(x) :=
          {x * fact(x-1)}  {si no}"""

# B) Profundidad de Collatz: Según la conjetura de Collatz, si se aplica la función:
"""     {n/2}   {si n es par}
f(n) :=
      {3n+1}  {si n es impar},"""
# a un número natural cualquiera, con suficientes repeticiones se llegará al número 1. Por ejemplo 6->3->10->5->16->8->4->2->1.
# -Implementar la función esPar, que dado un número devuelve 0 si es impar y 1 si es par.
# -Utilizar esPar para construir una función que dado un número devuelve la cantidad de repeticiones necesarias de f para llegar a 1.
# Por ejemplo: Pc(1) = 0 y Pc(6) = 8.

# C) Fibonacci_3:
"""       {0}                               {si x = 0}
        {1}                               {si x = 1}
F_3(x) :=
        {2}                               {si x = 2}
        {F_3(x-1) + F_3(x-2) + F_3(x-3)}  {si no}"""

# D) Fibonacci_n: n será un argumento con la función asociada:
"""       {x}                     {si x < n}
F_n(x) :=
        {\S{i=1}{n}{F_n(x-i)}}  {si no},"""

# E) Raíz de una Función Lineal: Dados 3 argumentos: min, max, y un puntero a una función lineal f, escribir una función que devuelva 0 si f
# no contiene una raíz en el intervalo [min,max] o la raíz en caso contrario. Ayuda: utilizar la instrucción jalr para llamar a una función
# por puntero y el método de bisección para encontrar la raíz.


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————