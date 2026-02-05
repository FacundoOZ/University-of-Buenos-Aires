
#============================================================================================================================================
# Práctica 5: Ejercicios Integradores de RISC-V
#============================================================================================================================================

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 # Información Alumno
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
""" Se tiene la estructura InformacionAlumno que contiene el ID del alumno y su nota en el ultimo examen, numeros sin signo de 16 bits y
8 bits respectivamente. En memoria se encuentra un arreglo del tipo InformacionAlumno con la forma:
  Dirección    0x0000    0x0002    0x0003    0x0005    ...    0x0030    0x0032    0x0033
  Valor        5492      1         8886      6         ...    6540      10        0    

Donde el final del arreglo es demarcado por un ID nulo. Se pide:
A) Calcular cuantos bytes ocupa en memoria la estructura InformacionAlumno.
B) Escribir una funcion que dado un puntero a un arreglo de InformacionAlumno, devuelva la suma de las notas de los alumnos con ID impar.
Escribir un caso de test donde verificar el funcionamiento de la funcion."""

# A) Debido a que estamos trabajando con 8 bits, y las direcciones don de tipo 0x0000 (4 bytes en sistema Hexadecimal) -> tenemos palabras
# de 32 bits (4 bytes * 8 bits = 32 bits). La estructura InformacionAlumno ocupa:
# 16 bits (ID) + 8 bits (Nota) = 24 bits de 32 bits    ->    #bytes(InformacionALumno) = 3 bytes.

# B) Función:
#   0000   0000   0000   0000   0000   0000
#  |-------------------------| |-----------| ...
#          ID alumno               nota      ID alumno, nota, ID alumno, nota, ...

# Caso de Test:
.data                        # Sección de datos globales
tablaCalificaciones:
  .half 5523                 # Alumno 1 (ID),
  .byte 3                    # Nota 1.
  .half 8754                 # Alumno 2 (ID),
  .byte 6                    # Nota 2.
  .half 5320                 # Alumno 3
  .byte 4
  .half 1                    # Alumno 4
  .byte 5
  .half 3219                 # Alumno 5
  .byte 2
  .half 0                    # Final del arreglo

.text                        # Donde se encuentra el contenido binario del programa.
.global sumar_notas_ID_impar # Almacena las constantes globales.

# Voy a asumir que el array se encuentra en la dirección de memoria del registro a0.

sumar_notas_ID_impar:
  addi t0, zero, 0       # En res = t0, sumo 0.

loop:
  lh   t1, 0(a0)         # Load Half: cargo en t1, 16 bits de contenido de memoria que hay en dirección a0 (elijo) sin offset (cargo ID).
  beq  t1, zero, fin     # Si el ID = 0 -> ya terminé -> salgo del array -> voy a la etiqueta "fin".
  lbu  t2, 2(a0)         # Si no, cargo en otro registro (t2) 8 bits del contenido de memoria que hay en a0, 2 bytes a derecha (cargo nota).
  andi t3, t1, 1         # Si ID es impar => hago AND INMEDIATO con 1. Si t1 (ID) termina en 1 => impar => andi t3, t1, 1 => devuelve t3=1.
  beq  t3, zero, omitir  # Si t3=0 => el ID no era impar => salgo.
  add  t0, t0, t2        # Si no, t3=1 => era impar! => sumo al registro t0 (res) su valor anterior + la nueva nota (t2).

omitir:                  # Si el número no era impar,
  addi a0, a0, 3         # en la dirección de memoria a0, hago suma a0 (la dirección que había) + 3 bytes (me muevo al próximo ID), es decir,
  j    loop              # actualizo y vuelvo al loop.

fin:                     # Si llegué acá es porque terminó el array, entonces
  mv   a0, t0            # Copio el resultado final de res=t0, en la dirección de memoria a0 (a0 es un registro de valor de retorno)
  ret                    # y devuelve el resultado en a0.

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 # Crear un programa que sume los primeros n-números naturales. El valor n se encuentra en s1 y res debe devolverse en a0.
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

suma_primeros_n:
  addi t0, zero, 0   # res = t0, que inicialmente vale 0.
  addi t1, zero, 1   # Creo un iterador j=t1, cuyo valor es 1.

loop:
  bgt  t1, s1, salir # Si el valor del iterador (t1) es mayor al de n pasado por parámetro (que está en s1) => ya sumé todos => salgo.
  add  t0, t0, t1    # Si no, en mi registro t0, guardo la suma de lo que había anteriormente en t0 + el iterador actual.
  addi t1, t1, 1     # Sumo uno al iterador.
  j    loop          # y vuelvo a repetir el ciclo.

salir:
  mv a0, t0
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 # Crear un programa que calcule n!. El valor n se encuentra en s1 y res debe devolverse en a0.
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

factorial_n:
  addi t0, zero, 1   # res = t0, que inicialmente vale 1.
  addi t1, zero, 1   # Creo un iterador j=t1, cuyo valor es 1.

  beq s1, zero, caso_base # Si n=0,
  beq s1, t1, caso_base   # o bien, n=1, -> voy al caso_base.
  j   loop

caso_base:
  mv a0, t0            # Si n=0 ó n=1 => a0 = t0 = 1 => listo!
  ret                  # Salgo

loop:                  # Si no, entro al loop.
  bgt  t1, s1, salir   # Si el valor del iterador (t1) es mayor al de n pasado por parámetro (está en s1) => ya multipliqué todos => salgo.
  mul  t0, t0, t1      # Si no, en mi registro t0, guardo el producto de hacer lo que había anteriormente en t0 * el iterador actual.
  addi t1, t1, 1       # Sumo uno al iterador.
  j    loop            # y vuelvo a repetir el ciclo.

salir:
  mv a0, t0
  ret

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Crear un programa que calcule la suma de los primeros n-números naturales pares. El valor n se encuentra en s1 y res debe devolverse en a0.

"""Utilizo lo siguiente:
    suma_pares_n
    s1 = n
    a0 = resultado
"""

suma_pares_n:
  addi t0, zero, 0 # t0 = res = 0
  addi t1, zero, 1 # t1 = i = 1

loop:
  bgt  t1, s1, fin # if i > n → termina
  slli t2, t1,  1  # t2 = 2*i
  add  t0, t0, t2  # res += 2*i
  addi t1, t1, 1   # i++
  j    loop

fin:
  mv   a0, t0
  ret


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————