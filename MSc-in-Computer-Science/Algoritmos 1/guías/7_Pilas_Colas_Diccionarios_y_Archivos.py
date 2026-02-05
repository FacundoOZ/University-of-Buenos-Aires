
#============================================================================================================================================
# Práctica 8: Pilas, Colas, Diccionarios y Archivos
#============================================================================================================================================

import os
import random as rd
from typing import Union              # Union sirve para representar valores de más de un tipo (versión <= 3.9)
from queue  import Queue     as cola  # (FIFO: First In, First Out)
from queue  import LifoQueue as pila  # (LIFO: Last In, First Out)

# Parte 1: Pilas
#———————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema generar_numeros_al_azar (in cantidad: Z, in desde: Z, in hasta: Z) : pila[Z] {
  requiere: {cantidad ≥ 0}
  requiere: {desde ≤ hasta}
  asegura: {El tamaño de res es igual a cantidad}
  asegura: {Todos los elementos de res son valores entre desde y hasta (inclusive), seleccionados aleatoriamente con probabilidad uniforme.}
}

Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >,< hasta >) que devuelve un número
en el rango indicado. Recuerden importar el módulo random con import random. Además, pueden usar la clase LifoQueue() que es un ejemplo de
una implementación básica de una pila:

from queue import LifoQueue as pila #importa LifoQueue y le asigna el alias pila:

  p = pila() #crea una pila
  p.put(1) # apila un 1
  elemento = p.get() # desapila
  p.empty() # devuelve true si y solo si la pila está vacía"""

def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int) -> pila[int]:
  res: pila[int] = pila()
  for i in range(cantidad):
    res.put(rd.randint(desde,hasta))
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema cantidad_elementos (in p: pila) : Z {
  requiere: {True}
  asegura: {res es igual a la cantidad de elementos que contiene p}
}
No se puede utilizar la función LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el parámetro de
entrada, ya que los elementos se eliminan al accederse. Dado que la especificación lo define como de tipo in, debe restaurarse
posteriormente."""

def cantidad_elementos(p: pila) -> int:
  res: int = 0
  q: pila = pila()
  while not p.empty():
    q.put(p.get())     # Obtengo el valor de la pila y lo guardo temporalmente en q
    res += 1           # Sumo 1 a cantidad (que era cero)
  while not q.empty(): # Vuelvo a apilar p
    p.put(q.get())
  return res

# Al obtener los valores 1 vez, los apilo al revés, entonces hago el proceso 2 veces para obtener la forma original de pila (con q).

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema buscar_el_maximo (in p: pila[Z]) : Z {
  requiere: {p no está vacía}
  asegura: {res es un elemento de p}
  asegura: {res es mayor o igual a todos los elementos de p}
}"""

def buscar_el_maximo(p: pila[int]) -> int:
  q: pila = pila()
  lista: list = []
  while not p.empty():
    x = p.get()               # Obtengo el valor de la pila
    lista.append(x)           # Voy guardándolos en una lista
    q.put(x)                  # Lo guardo temporalmente en q
  for j in range(len(lista)): # Vuelvo a apilar p
    y = q.get()
    p.put(y)
  res: int = lista[0]
  for i in range(len(lista)):
    if lista[i] > res:
      res = lista[i]
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema buscar_nota_maxima (in p: pila[seq⟨Char⟩ x Z]) : seq⟨Char⟩ x Z {
  requiere: {p no está vacía}
  requiere: {los elementos de p no tienen valores repetidos en la segunda posición de las tuplas}
  asegura: {res es una tupla de p}
  asegura: {No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}"""

def buscar_nota_maxima(p: pila[tuple[str,int]]) -> tuple[str,int]:
  q: pila[tuple[str,int]] = pila()
  lista: list[tuple[str,int]] = []
  while not p.empty():
    t1 = p.get()                    # Obtengo la tupla t1
    lista.append(t1)                # Genero una lista
    q.put(t1)                       # Apilo inversamente
  for i in range(len(lista)):
    t2 = q.get()                    # Obtengo t1
    p.put(t2)                       # Apilo correctamente

  res: tuple[str,int] = lista[0]
  for tupla in lista:
    if tupla[1] > res[1]:           # res es la tupla_maxima
      res = tupla
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 # Implementar una solución que utilize pilas, para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema esta_bien_balanceada (in s: seq⟨Char⟩) : Bool {
  requiere: {s solo puede tener números enteros, espacios y los símbolos ’(’, ’)’, ’+’, ’-’, ’*’, ’/’}
  asegura: {res = true ↔ (La cantidad de paréntesis de apertura ’(’ es igual a la de cierre ’)’ y para todo prefijo de ‘s‘, la cantidad de
            paréntesis de cierre no supera a la de apertura.}
}

Por cada paréntesis de cierre debe haber uno de apertura correspondiente antes de él. Las fórmulas pueden tener:
  números enteros
  operaciones básicas +, -, * y /
  paréntesis
  espacios
Entonces las siguientes son fórmulas aritméticas con sus paréntesis bien balanceados:
  1 + (2 x 3 - (20 / 5) )
  10 * (1 + (2 * (- 1) ) )
Y la siguiente es una fórmula que no tiene los paréntesis bien balanceados:
  1 + ) 2 x 3 ( ()"""

def esta_bien_balanceada(s: str) -> bool:
  q: pila[str] = pila() # Creo una pila vacía.
  for letra in s:       # Para cada letra en el string s,
    if letra == '(':    # si ésta es "(",
      q.put('(')        # lo agrego a q,
    elif letra == ')':  # sino, si es ")",
      if q.empty():     # Si no había un ( antes de éste, entonces
        return False    # no está bien balanceada -> false.
      q.get()           # Sino, emparejo con un "("
  return q.empty()      # Deben haberse cerrado todos

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# La notación polaca inversa, también conocida como notación postfix, es una forma de escribir expresiones matemáticas en la que los
# operadores siguen a sus operandos. Por ejemplo, la expresión “3 + 4” se escribe como “3 4 +” en notación postfix. Para evaluar una expresión
# en notación postfix, se puede usar una pila. Implementar una solución para el siguiente problema.

"""problema evaluar_expresion (in s: seq⟨Char⟩) : R {
  requiere: {s solo contiene números enteros (de 1 dígito) y los operadores binarios +, -, * y /}
  requiere: {Todos los elementos (operandos y operadores) están separados por un único espacio}
  requiere: {La expresión es sintácticamente válida: cada operador binario tiene exactamente dos operandos previos disponibles en el momento
             de su evaluación.}
  asegura: {res es el valor obtenido al evaluar la expresión postfija representada por s}
}

Para resolver este problema, se recomienda seguir el siguiente algoritmo:
  1. Dividir la expresión en tokens (operandos y operadores) utilizando espacios como delimitadores.
  2. Recorre los tokens uno por uno.
      a) Si es un operando, agrégalo a una pila.
      b) Si es un operador, saca los dos operandos superiores de la pila, aplícale el operador y luego coloca el resultado en la pila.
  3. Al final de la evaluación, la pila contendrá el resultado de la expresión.

Ejemplo de uso:
  expresion = "3 4 + 5 * 2-"
  resultado = evaluar_expresion(expresion)
  print(resultado) # Debería imprimir 33"""

""" El funcionamiento es el siguiente:
3 4 + 5 * 2 -
3 + 4 5 * 2 -
7 5 * 2 -
7 * 5 2-
35 2 -
35 - 2
33"""
def evaluar_expresion(s: str) -> float:
  res: float = 0.0
  lista: list[str] = list(s) # Genero una lista de strings a partir de s
  i: int = 0
  while i < len(lista):
    if lista[i] == ' ':     # Remuevo todos los espacios
      lista.pop(i)
    i += 1

  p: pila[int] = pila()
  op: dict = {'+': lambda x,y: x+y,'-': lambda x,y: x-y,'*': lambda x,y: x*y,'/': lambda x,y: x/y}
  for j in range(len(lista)):
    if type(lista[j]) == str and lista[j] not in ['+','-','*','/']:
      p.put(int(lista[j]))
    elif lista[j] in op: # lista[j] = '+' ó '-' ó '*' ó '/' (si es clave en el diccionario op), entonces:
      x_f = p.get()
      x_0 = p.get()
      p.put(op[lista[j]](x_0, x_f)) # Aplica la función lambda asociada a la clave 'lista[j]'
  res = p.get()
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 7 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema intercalar (in p1: pila, in p2: pila) : pila {
  requiere: {p1 y p2 tienen la misma cantidad de elementos}
  asegura: {res solo contiene los elementos de p1 y p2}
  asegura: {res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original}
  asegura: {El tope de la pila res es el tope de p2}
  asegura: {El tamaño de res es igual al doble del tamaño de p1}
}
Nota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final."""

def intercalar(p1: pila, p2: pila) -> pila:
  res: pila = pila()
  q: pila = pila()
  while not p1.empty() and not p2.empty():
    x1 = p1.get()       # Obtengo un elemento de pila_1,
    q.put(x1)           # y lo coloco en q (una pila total auxiliar)
    x2 = p2.get()       # Obtengo un elemento de pila_2,
    q.put(x2)           # y lo coloco encima. Esto se repite para cada hilera
  while not q.empty():
    y = q.get()         # Ahora obtengo los elementos de q
    res.put(y)          # y los apilo correctamente en res.
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 2: Colas
#———————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 8 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema generar_nros_al_azar2 (in cantidad: Z, in desde: Z, in hasta: Z) : cola[Z] {
  requiere: {cantidad ≥ 0}
  requiere: {desde ≤ hasta}
  asegura: {El tamaño de res es igual a cantidad}
  asegura: {Todos los elementos de res son valores entre desde y hasta (inclusive), seleccionados aleatoriamente con probabilidad uniforme.}
}

Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >,< hasta >) que devuelve un número
en el rango indicado. Recuerden importar el módulo random con import random. Pueden usar la clase Queue() que es un ejemplo de una
implementación básica de una cola:

from queue import Queue as cola #importa Queue y le asigna el alias cola
  c = cola() #creo una cola
  c.put(1) # encolo el 1
  elemento = c.get() # desencolo
  c.empty() # devuelve true si y solo si la cola está vacía"""

def generar_numeros_al_azar2(cantidad: int, desde: int, hasta: int) -> cola[int]:
  res: cola[int] = cola()
  for i in range(cantidad):
    res.put(rd.randint(desde,hasta))
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 9 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema cantidad_elementos2 (in c: cola) : Z {
  requiere: {True}
  asegura: {res es igual a la cantidad de elementos que contiene c}
}

No se puede utilizar la función Queue.qsize(). Comparar el resultado con la implementación utilizando una pila en lugar de una cola."""

def cantidad_elementos2(c: cola) -> int:
  res: int = 0
  d: cola = cola()
  while not c.empty():
    d.put(c.get())
    res += 1
  while not d.empty():
    c.put(d.get())
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 10 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema buscar_el_maximo2 (in c: cola[Z]) : Z {
  requiere: {c no está vacía}
  asegura: {res es un elemento de c}
  asegura: {res es mayor o igual a todos los elementos de c}
}
Comparar con la versión usando pila."""

def buscar_el_maximo2(c: cola[int]) -> int:
  d: cola = cola()
  lista: list[int] = []
  while not c.empty():
    x = c.get()
    d.put(x)
    lista.append(x)
  while not d.empty():
    c.put(d.get())
  res: int = lista[0]
  for i in range(len(lista)):
    if lista[i] > res:
      res = lista[i]
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 11 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema buscar_nota_minima (in c: cola[seq⟨Char x Z⟩]) : (seq⟨Char x Z⟩) {
  requiere: {c no está vacía}
  requiere: {los elementos de c no tienen valores repetidos en la segunda componente de las tuplas}
  asegura: {res es una tupla de c}
  asegura: {No hay ningún elemento en c cuya segunda componente sea menor que la de res }
}"""

def buscar_nota_minima(c: cola[tuple[str,int]]) -> tuple[str,int]:
  lista: list[tuple[str,int]] = []
  d: cola[tuple[str,int]] = cola()
  while not c.empty():
    x = c.get()
    lista.append(x)
    d.put(x)
  while not d.empty():
    c.put(d.get())

  res: tuple[str,int] = lista[0]
  for tupla in lista:
    if tupla[1] < res[1]:
      res = tupla
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 12 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema intercalar2 (in c1: cola, in c2: cola) : cola {
  requiere: {c1 y c2 tienen la misma cantidad de elementos}
  asegura: {res solo contiene los elementos de c1 y c2}
  asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
  asegura: {El primer elemento de res es el primer elemento de c1}
  asegura: {El tamaño de res es igual al doble del tamaño de c1}
}"""

def intercalar2(c1: cola, c2: cola) -> cola:
  res: cola = cola()
  while not c1.empty() and not c2.empty():
    res.put(c1.get())
    res.put(c2.get())
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 13 # Bingo
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Un cartón de bingo contiene 12 números al azar en el rango [0,99]. Implementar una solución para cada uno de los siguientes problemas.
"""1. problema armar_secuencia_bingo () : cola[Z] {
  requiere: {True}
  asegura: {res solo contiene 100 números del 0 al 99 inclusive, sin repetidos}
  asegura: {Los números de res están ordenados al azar}
}
Para generar números pseudoaleatorios pueden usar la función random.randint(< desde >,< hasta >) que devuelve un número en el rango indicado.
Recuerden importar el módulo random con import random."""

def armar_secuencia_bingo() -> cola[int]:
  res: cola[int] = cola()
  lista: list[int] = []
  while len(lista) < 100:
    n = rd.randint(0,99)
    if n not in lista:
      lista.append(n)
      res.put(n)
  return res

"""2. problema jugar_carton_de_bingo (in carton: seq⟨Z⟩, in bolillero: cola[Z]) : Z {
  requiere: {carton solo contiene 12 números, sin repetidos, con valores entre 0 y 99, ambos inclusive}
  requiere: {bolillero solo contiene 100 números, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
  asegura: {res es la cantidad mínima de jugadas necesarias para que todos los números del carton hayan salido del bolillero}
}"""

def jugar_carton_de_bingo(carton: list[int], bolillero: cola[int]) -> int:
  res: int = 0
  cont: int = 0
  while not bolillero.empty():
    x = bolillero.get()
    res += 1
    if x in carton:
      cont += 1
    if cont == 12:
      break
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 14 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atención para los pacientes que van
llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la más urgente y requiere atención inmediata)
junto con su nombre y la especialidad médica que le corresponde. Implementar una solución para el siguiente problema."""

"""problema pacientes_urgentes (in c:cola[Z x seq⟨Char⟩ x seq⟨Char⟩]) : Z {
  requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
  asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un número menor a 4}
}"""

def pacientes_urgentes(c: cola[tuple[int,str,str]]) -> int:
  lista: list[tuple[int,str,str]] = []
  d: cola = cola()
  while not c.empty():
    x = c.get()
    lista.append(x)
    d.put(x)
  while not d.empty():
    c.put(d.get())

  res: int = 0
  tripla: tuple[int,str,str] = ()
  for tripla in lista:
    if tripla[0] < 4:
      res += 1
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 15 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""La gerencia de un banco nos pide modelar la atención de los clientes usando una cola donde se van registrando los pedidos de atención. Cada
vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que está a la entrada: Nombre y Apellido, DNI, tipo de
cuenta (true si es preferencial o false en el caso contrario) y si tiene prioridad (true o false) por ser adulto +65, embarazada o con
movilidad reducida.
La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta bancaria
preferencial y por último el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada."""

"""1. Dar una especificación para el problema planteado."""

"""problema atencion_a_clientes (in c:cola[seq⟨Char⟩ x Z x bool x bool]) : cola[seq⟨Char⟩ x Z x bool x bool] {
  requiere: {El primer elemento de c es un string, el segundo un número natural de 7 u 8 dígitos y el tercero y el cuarto son verdadero o
             falso.}
  requiere: {Si el cliente es preferencial el tercer elemento de c vale True, sino False.}
  requiere: {Si el cliente es adulto de +65 años de edad, si está embarazada o presenta movilidad reducida, el cuarto elemento de c vale
             True, sino False.}
  asegura: {Si c[3] == True el cliente tiene prioridad N°1. Los clientes de este subgrupo respetarán el orden de llegada del subgrupo.}
  asegura: {Si c[2] == True el cliente tiene prioridad N°2. Los clientes de este subgrupo respetarán el orden de llegada del subgrupo.}
  asegura: {Si c[3] y c[2] == False el cliente tiene prioridad N°3. Los clientes de este subgrupo respetarán el orden de llegada del subgrupo.}
  asegura: {res es una cola cuyos primeros elementos son el subgrupo N°1, sus elementos siguientes el subgrupo N°2 y sus últimos elementos el
  subgrupo N°3, todos en su orden de llegada.}
}"""

"""2. Implementar atencion_a_clientes(in c : cola[tuple[str,int,bool,bool]]) → cola[tuple[str,int,bool,bool]] que dada la cola de ingreso de
clientes al banco devuelve la cola en la que van a ser atendidos."""

def atencion_a_clientes(c: cola[tuple[str,int,bool,bool]]) -> cola[tuple[str,int,bool,bool]]:
  res: cola[tuple[str,int,bool,bool]] = cola()
  c1: cola[tuple[str,int,bool,bool]] = cola() # Subgrupo N°1 (máxima prioridad)
  c2: cola[tuple[str,int,bool,bool]] = cola() # Subgrupo N°2 (segundo lugar)
  c3: cola[tuple[str,int,bool,bool]] = cola() # Subgrupo N°3 (última prioridad)
  while not c.empty():
    x = c.get()
    if x[3] == True:
      c1.put(x)
    elif x[2] == True:
      c2.put(x)
    else:
      c3.put(x)
  while not c1.empty():
    res.put(c1.get()) # Coloco todo el subgrupo N°1
  while not c2.empty():
    res.put(c2.get()) # Luego, el resto
  while not c3.empty():
    res.put(c3.get())
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 3: Diccionarios
#——————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 16 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema calcular_promedio_por_estudiante (in notas: seq⟨seq⟨Char⟩ x R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
  requiere: {El primer componente de las tuplas de notas no es una cadena vacía}
  requiere: {El segundo componente de las tuplas de notas está en el rango [0, 10]}
  asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
  asegura: {Todos los nombres de notas (primer componente) son clave en res}
  asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (primer componente de notas)}
}"""

def promedio(lista: list[float]) -> float:
  suma_total: float = 0.0
  for nota in lista:
    suma_total += nota
  return suma_total/len(lista)

def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
  dic_aux: dict[str,list[float]] = {}
  for tupla in notas:             # Creo las claves (sin valores) en el diccionario auxiliar (si ya se creó se sobreescribe)
    dic_aux[tupla[0]] = []      # Creo una lista vacía de notas
  for tupla in notas:             # Appendeo todas las notas que haya asociadas a la clave tupla[0], en la clave tupla[0]
    dic_aux[tupla[0]].append(tupla[1])

  res: dict[str,float] = {}
  for clave, valores in dic_aux.items():
    res[clave] = promedio(valores)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 17 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los usuarios del sistema. El
# navegador debe permitir al usuario navegar hacia atrás en la historia de navegación.

"""1. Crea un diccionario llamado historiales que almacenará el historial de navegación para cada usuario. Las claves del diccionario serán
los nombres de usuario y los valores serán pilas de String."""

def historiales(lista: list[tuple[str,str]]) -> dict[str,pila[str]]:
  res: dict[str,pila[str]] = {}
  for tupla in lista:     # Creo las claves de res como pilas vacías (si la clave ya existe, se sobreescribe)
    res[tupla[0]] = pila()
  for tupla in lista:     # En cada clave, se agrega el sitio web al valor de dicha clave (a la pila)
    res[tupla[0]].put(tupla[1])
  return res

"""2. Implementar una solución para el siguiente problema.
problema visitar_sitio (inout historiales: Diccionario⟨seq⟨Char⟩,pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩) {
  requiere: {Ninguno de los Strings de los parámetros es vacío}
  asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historiales@pre[usuario]}
  asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila que tiene solo el
            elemento sitio}
  asegura: {No se modifica ningún otro historial salvo, si existe, el de usuario}
  asegura: {Todos los pares clave-valor de historiales@pre están en historiales}
  asegura: {Todos los pares clave-valor de historiales están en historiales@pre, salvo historiales[usuario] que podría no existir en
            historiales@pre}
}"""

def visitar_sitio(historiales: dict[str,pila[str]], usuario: str, sitio: str) -> None:
  if usuario not in historiales.keys():
    historiales[usuario] = pila()       # Creamos la clave usuario cuyo valor es una pila vacía
    historiales[usuario].put(sitio)     # Colocamos sitio en la pila
  else:
    historiales[usuario].put(sitio)     # Si usuario (clave) ya existe, agregamos sitio a su (valor) pila

"""3. Implementar una solución para el siguiente problema.
problema navegar_atras (inout historiales: Diccionario⟨seq⟨Char⟩,pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {Ninguno de los Strings de los parámetros es vacío}
  requiere: {usuario es una clave de historiales}
  requiere: {La pila asociada a usuario no está vacía}
  asegura: {res es igual al tope de historiales@pre[usuario]}
  asegura: {historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de historiales@pre[usuario]}
  asegura: {En historiales, salvo la pila asociada a usuario, no se modifica ningún otro por clave-valor}
}
Ejemplo de uso:
  historiales = {}
  visitar_sitio(historiales, "Usuario1", "google.com")
  visitar_sitio(historiales, "Usuario1", "facebook.com")
  navegar_atras(historiales, "Usuario1")
  visitar_sitio(historiales, "Usuario2", "youtube.com")"""

def navegar_atras(historiales: dict[str,pila[str]], usuario: str) -> str:
  res: str = historiales[usuario].get()
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 18 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Se debe desarrollar un sistema de gestión de inventario para una tienda de ropa. Este sistema debe permitir llevar un registro de los
productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y calcular el valor total del
inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacenará la información de los productos. En este
diccionario, cada clave será el nombre de un producto, y su valor asociado será otro diccionario con los atributos del producto. Este
segundo diccionario tendrá dos claves posibles: ’precio’y ’cantidad’, cuyos valores serán de tipo float e int, respectivamente.
Un ejemplo de inventario, con un solo producto, es: {“remera”: {“precio”: 999.99, “cantidad”: 3}}). Implementar una solución para cada uno
de los siguientes problemas. Agregar en las funciones los tipos de datos correspondientes (ver nota al final de la primera especificación)."""

"""1.problema agregar_producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in precio: R,
                                in cantidad: Z) {
  requiere: {T ∈ [Z,R]}
  requiere: {cantidad ≥ 0}
  requiere: {precio ≥ 0}
  requiere: {Ninguno de los Strings de los parámetros es vacío}
  requiere: {nombre no es una clave de inventario }
  asegura: {Todas los pares clave-valor de inventario@pre están tal cual en inventario}
  asegura: {Todas los pares clave-valor de inventario están en inventario@pre y, además, hay una nueva con clave igual a nombre y como valor
            tendrá un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”, cantidad)}
}
Se necesitará un diccionario cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores serán de tipo float y enteros
respectivamente. Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la siguiente manera:

En Python 3.9:
  Es necesario importar Union desde el módulo typing para indicar que los valores pueden ser de más de un tipo.
  from typing import Union
  mi diccionario: dict[str, Union[int, float]]
En Python 3.10 o superior:
  No es necesario importar Union, ya que se puede usar el operador | para representar una unión de tipos.
  mi diccionario: dict[str, int | float]"""

def agregar_producto(inventario: dict[str,dict[str,float|int]], nombre: str, precio: float, cantidad: int) -> None:
  if nombre not in inventario.keys():
    inventario[nombre] = {'precio': precio, 'cantidad': cantidad}

"""2. problema actualizar_stock (inout inventario: Diccionario ⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in cantidad: Z) {
  requiere: {T ∈ [Z,R]}
  requiere: {cantidad ≥ 0}
  requiere: {nombre es una clave existente en el inventario}
  requiere: {Ninguno de los Strings de los parámetros es vacío}
  asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del valor que tiene como clave nombre}
  asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
  asegura: {En inventario, el valor asociado a la clave nombre, tendrá el mismo precio que antes y la cantidad será cantidad}
}"""

def actualizar_stock(inventario: dict[str,dict[str,float|int]], nombre: str, cantidad: int) -> None:
  inventario[nombre]['cantidad'] = cantidad

"""3. problema actualizar_precio (inout inventario: Diccionario⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in precio: R) {
  requiere: {T ∈ [Z,R]}
  requiere: {precio ≥ 0}
  requiere: {nombre es una clave existente en el inventario}
  requiere: {Ninguno de los Strings de los parámetros es vacío}
  asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del valor que tiene como clave nombre}
  asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
  asegura: {En inventario el diccionario asociado a nombre, tendrá la misma cantidad que antes y el precio será precio}
}"""

def actualizar_precio(inventario: dict[str,dict[str,float|int]], nombre: str, precio: float) -> None:
  inventario[nombre]['precio'] = precio

"""4. problema calcular_valor_inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
  requiere: {T ∈ [Z,R]}
  requiere: {Ninguno de los Strings del inventario es vacío}
  asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
}
Ejemplo de uso:
  inventario = {}
  agregar_producto(inventario, "Camisa", 20.0, 50)
  agregar_producto(inventario, "Pantalón", 30.0, 30)
  actualizar_stock(inventario, "Camisa", 10)
  valor_total = calcular_valor_inventario(inventario)
  print("Valor total del inventario:", valor_total) # Debería imprimir 1100.0"""

def calcular_valor_inventario(inventario: dict[str,dict[str,float|int]]) -> float:
  res: float = 0.0
  for precio in inventario:
    res += inventario[precio]['precio'] * inventario[precio]['cantidad']
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 4: Archivos
#——————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 19 # Implementar una solución para cada uno de los siguientes problemas:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

"""Para usar archivos contamos con las funciones: open, close, read, readline, readlines, write, os.path.join(), os.path.exists(). Para más
información referirse a la documentación: https://docs.python.org/es/3/tutorial/inputoutput.html#reading-and-writing-files"""

"""1. problema contar_lineas (in nombre_archivo: seq⟨Char⟩) : Z {
  requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
  asegura: {res es igual a la cantidad de líneas que contiene el archivo indicado por nombre_archivo}
}"""

def contar_lineas(nombre_archivo: str) -> int:
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  res: list[str] = archivo.readlines()
  archivo.close()
  return len(res)

"""2. problema existe_palabra (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
  requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
  requiere: {palabra no es vacía}
  asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre_archivo}
}"""

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
  res: bool = False
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  texto: str = archivo.read()
  archivo.close()
  if palabra in texto:
    res = True
  return res

"""3. problema cantidad_de_apariciones (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
  requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
  requiere: {palabra no es vacía}
  asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre_archivo}
}"""

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
  res: int = 0
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  texto: str = archivo.read()
  archivo.close()
  i: int = 0
  while i <= len(texto) - len(palabra):
    if palabra == texto[i:i + len(palabra)]:
      res += 1
    i += 1
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 20 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema agrupar_por_longitud (in nombre_archivo: seq⟨Char⟩) : Diccionario⟨Z,Z⟩ {
  requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
  asegura: {Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre_archivo, res[n] es igual
            a la cantidad de palabras de esa longitud}
  asegura: {No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo}
}

Por ejemplo, el diccionario {1: 2, 2: 10, 5: 4}, indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras
de longitud 5. Para este ejercicio se consideran como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco."""

def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  texto: list[str] = archivo.readlines()
  archivo.close()

  longitudes: list[int] = []
  cont: int = 0
  for linea in texto:
    for letra in linea:
      if letra != ' ' and letra != '\n':
        cont += 1
      else:
        longitudes.append(cont)
        cont = 0
    if cont > 0:                        # Última palabra del texto
      longitudes.append(cont)

  res: dict[int,int] = {}
  for num in longitudes:
    if num in res:                      # Si una longitud dada (num) en longitudes, ya es clave de res
      res[num] += 1                     # Suma uno
    else:
      res[num] = 1                      # Si no, la crea
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 21 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema la_palabra_mas_frecuente (in nombre_archivo: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {nombre_archivo es un archivo existente y accesible que tiene, por lo menos, una palabra}
  asegura: {res es una palabra que aparece en el archivo nombre_archivo}
  asegura: {No hay ninguna palabra contenida en el archivo nombre_archivo que aparezca más veces que la palabra res}
}
Para resolver el problema se aconseja utilizar un diccionario de palabras."""

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  texto: list[str] = archivo.readlines()
  archivo.close()

  diccionario: dict[str,int] = {}
  palabra: str = ''
  for linea in texto:
    for letra in linea:
      if letra != ' ' and letra != '\n':
        palabra += letra
      else:
        if palabra in diccionario:
          diccionario[palabra] += 1
        else:
          diccionario[palabra] = 1
        palabra = ''
    if len(palabra) > 0:    # Agrego la última palabra
      if palabra in diccionario:
        diccionario[palabra] += 1
      else:
        diccionario[palabra] = 1
  valor_max: int = 0
  for valor in diccionario.values():
    if valor > valor_max:
      valor_max = valor
  for clave in diccionario.keys():
    if diccionario[clave] == valor_max:
      res: str = clave
      break
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 22 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema clonar_sin_comentarios (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩) {
  requiere: {nombre_archivo_entrada es el path con el nombre de un archivo existente y accesible}
  requiere: {nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear}
  asegura: {El archivo indicado por nombre_archivo_salida contiene las mismas líneas y en el mismo orden que el archivo nombre_archivo_entrada,
            excepto aquellas que comienzan con el carácter #}
}
Para este ejercicio vamos a considerar que una línea es un comentario si tiene un ‘#’como primer carácter de la línea, o si no es el primer
carácter, se cumple que todos los anteriores son espacios. Por ejemplo, si se llama a clonar sin comentarios con un archivo con este contenido:
  # esto es un comentario
  # esto tambien
  esto no es un comentario # esto tampoco
  nombre_archivo_salida solo contendrá la última línea:
  esto no es un comentario # esto tampoco"""

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
  ruta_entrada = os.path.join('Archivos',nombre_archivo_entrada)
  archivo = open(ruta_entrada,'r')
  texto: list[str] = archivo.readlines()
  archivo.close()

  nuevo_texto: str = ''
  for linea in texto:
    if linea[0] != '#':
      nuevo_texto += linea
  ruta_salida = os.path.join('Archivos',nombre_archivo_salida)
  archivo_salida = open(ruta_salida,'w')
  archivo_salida.write(nuevo_texto)
  archivo_salida.close()

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 23 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema invertir_lineas (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩ ) {
  requiere: {nombre_archivo_entrada es el path de un archivo de texto existente y accesible}
  requiere: {nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear}
  asegura: {El archivo dado por nombre_archivo_salida contiene las mismas líneas que el archivo nombre_archivo_entrada, pero en orden inverso}
}
Por ejemplo, si el archivo contiene lo siguiente:
  Esta es la primera linea.
  Y esta es la segunda.
debe generar:
  Y esta es la segunda.
  Esta es la primera linea."""

def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
  ruta_entrada = os.path.join('Archivos',nombre_archivo_entrada)
  archivo = open(ruta_entrada,'r')
  texto: list[str] = archivo.readlines()
  archivo.close()

  p: pila[str] = pila()           # Apilamos las lineas en una pila
  for linea in texto:
    p.put(linea)
  ruta_salida = os.path.join('Archivos',nombre_archivo_salida)
  archivo_salida = open(ruta_salida,'w') # Si el archivo no existe, 'w' lo crea. Si existe, lo sobreescribe
  archivo_salida.write(p.get())   # Desapilamos. La primera línea, requiere
  archivo_salida.write('\n')      # un salto de línea (pues era la última)
  while not p.empty():            # Las demás no.
    archivo_salida.write(p.get())
  archivo_salida.close()

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 24 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema agregar_frase_al_final (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
  requiere: {nombre_archivo es el path de un archivo existente y accesible}
  requiere: {frase no es vacía}
  asegura: {frase se agrega como una nueva línea al final del archivo nombre_archivo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica."""

def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'a')        # 'a' permite agregar contenido (solo al final), sin borrar el anterior
  archivo.write('\n' + frase)
  archivo.close()

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 25 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Dado un archivo de texto y una frase, implementar una función agregar_frase_al_principio (in nombre_archivo : str, in frase : str), que
# agregue la frase al comienzo del archivo original (similar al ejercicio anterior, sin hacer una copia del archivo).

"""problema agregar_frase_al_principio (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
  requiere: {nombre_archivo es el path de un archivo existente y accesible}
  requiere: {frase no es vacía}
  asegura: {frase se agrega como primera línea del archivo nombre_archivo, desplazando las anteriores hacia abajo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica."""

def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
  ruta = os.path.join('Archivos',nombre_archivo)
  archivo = open(ruta,'r')
  texto: str = archivo.read()                     # Copio el contenido del archivo
  archivo.close()

  archivo = open(ruta,'w')
  archivo.write(frase + '\n' + texto)             # Agrego mi frase y luego el contenido original
  archivo.close()

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 26 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema listar_palabras_de_archivo (in nombre_archivo: seq⟨Char⟩ ) : seq⟨seq⟨Char⟩⟩ {
  requiere: {nombre_archivo es el path de un archivo existente y accesible}
  asegura: {res contiene exactamente las palabras legibles distintas que aparecen en el archivo nombre_archivo}
}
Definimos una palabra legible como:
"secuencias de texto formadas por números, letras mayúsculas/minúsculas y los caracteres ‘ ’ (espacio) y ‘_’(guion bajo) que tienen longitud>=5"

Referencia: https://docs.python.org/es/3/library/functions.html#open

Para resolver este ejercicio se puede abrir un archivo en modo binario ‘b’. Al hacer read() vamos a obtener una secuencia de bytes, que al
hacer chr(byte) nos va a devolver un carácter correspondiente al byte leído. Una vez implementada la función, probarla con diferentes archivos
binarios (.exe, .zip, .wav, .mp3, etc)."""

def listar_palabras_de_archivo(nombre_archivo: str) -> list[str]:
  res: list[str]      = []
  palabra_actual: str = ""

  with open(nombre_archivo, "rb") as f:
    contenido = f.read()
    for byte in contenido:
      c = chr(byte)
      if (c.isalnum() or c == ' ' or c == '_'):
        palabra_actual += c
      else:
        if len(palabra_actual) >= 5 and palabra_actual not in res:
          res.append(palabra_actual)
        palabra_actual = ""
    if len(palabra_actual) >= 5 and palabra_actual not in res:    # Por si el archivo termina con una palabra válida
      res.append(palabra_actual)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 27 # Implementar una solución para el siguiente problema:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema calcular_promedio_por_estudiante (in nombre_archivo notas: seq⟨Char⟩, in nombre_archivo promedios: seq⟨Char⟩) {
  requiere: {nombre_archivo notas es el path de un archivo existente y accesible, con formato CSV: cada línea tendrá número de LU, materia,
             fecha y nota, todo separado por comas}
  requiere: {nombre_archivo promedios es el path de un archivo distinto, accesible para escritura}
  asegura: {El archivo nombre_archivo promedios contiene una línea por estudiante del archivo nombre_archivo notas, con su LU y su promedio
            separados por una coma}
}
El contenido del archivo nombre_archivo notas tiene el siguiente formato:
  nro de LU (str), materia (str), fecha (str), nota (float)
Analizar el problema y modularizar el código apropiadamente. Una opción es implementar una función auxiliar que cumpla la siguiente
especificación.

problema promedio_estudiante (in notas_de_estudiantes: seq⟨seq⟨Char⟩⟩, in lu: seq⟨Char⟩ ) : R {
  requiere: {notas_de_estudiantes tiene el contenido del archivo de notas. Cada elemento de la lista es una línea de ese
  archivo, con formato CSV: tendrá número de LU, materia, fecha y nota, todo separado por comas}
  requiere: {lu corresponde a una LU presente en notas_de_estudiantes}
  asegura: {res es el promedio de las notas asociadas a lu en notas_de_estudiantes}
}"""

def promedio_estudiante(notas_de_estudiantes: list[str], lu: str) -> float:
  suma: float = 0.0
  cantidad: int = 0
  for linea in notas_de_estudiantes:
    datos = linea.strip().split(",")
    lu_linea = datos[0]
    nota = float(datos[3])
    if lu_linea == lu:
      suma += nota
      cantidad += 1
  return suma / cantidad

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    with open(nombre_archivo_notas, "r", encoding="utf-8") as f:      # Leo todas las líneas del archivo de notas
      lineas = f.readlines()
    lus = []                                                          # Obtengo LU's distintas
    for linea in lineas:
      lu = linea.strip().split(",")[0]
      if lu not in lus:
        lus.append(lu)
    with open(nombre_archivo_promedios, "w", encoding="utf-8") as f:  # Escribo el archivo de promedios
      for lu in lus:
        prom = promedio_estudiante(lineas, lu)
        f.write(f"{lu},{prom}\n")

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————