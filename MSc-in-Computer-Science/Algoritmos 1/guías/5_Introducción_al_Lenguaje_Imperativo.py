
#============================================================================================================================================
# Práctica 6: Introducción al Lenguaje Imperativo
#============================================================================================================================================

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 # Definir las siguientes funciones y procedimientos:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. problema imprimir_hola_mundo () {
  requiere: {True}
  asegura: {Imprime "¡Hola mundo!" por consola.}
}"""

def imprimir_hola_mundo() -> None:
  print("¡Hola mundo!")

"""2. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante el caracter \n."""

def imprimir_un_verso() -> None:
  print("There was a time... \n I met a girl of a different kind...!")

"""3. raiz_de_2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round."""

from math import sqrt # utilizando "from", nos ahorramos tener que escribir math.sqrt -> solo escribimos sqrt

def raiz_de_2() -> float:
  return round(sqrt(2), 4)

"""4. factorial_de_dos()
problema factorial_2 () : Z {
  requiere: {True}
  asegura: {res = 2!}
}"""

def factorial_de_dos() -> int:
  res:int = 1*2
  return res

"""5. perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando import math y
la constante math.pi:
problema perimetro () : R {
  requiere: {True}
  asegura: {res = 2*π}
}"""

from math import pi

def perimetro() -> float:
  res:int = 2*pi
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 # Definir las siguientes funciones y procedimientos con parámetros:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. problema imprimir_saludo (in nombre: String) {
  requiere: {True}
  asegura: {imprime "Hola < nombre >"por pantalla}
}"""

def imprimir_saludo(nombre: str) -> None:
  print(f"Hola {nombre}")

"""2. raiz_cuadrada_de(numero): que devuelva la raíz cuadrada del número."""

def raiz_cuadrada_de(numero: float) -> float:
  return sqrt(numero)    

"""3. fahrenheit_a_celsius(temp_far): que convierta una temperatura en grados Fahrenheit a grados Celcius.
problema fahrenheit_a_celsius (in t: R) : R {
  requiere: {True}
  asegura: {res = ((t - 32)*5)/9}
}"""

def fahrenheit_a_celsius(t: float) -> float:
  return round(((t-32)*5)/9 , 2) # tantos decimales me molestaban

"""4. imprimir_dos_veces(estribillo): que imprima dos veces el estribillo de una canción. Nota: Analizar el comportamiento del operador (*)
con strings."""

def imprimir_dos_veces(estribillo: str) -> str:
  return 2*estribillo

"""5. problema es_multiplo_de (in n: Z, in m:Z) : Bool {
  requiere: {m = 0}
  asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m*k)}
}"""

def es_multiplo_de(n: int, m: int) -> bool:
  res: bool = n % m == 0 # % es la función módulo (mod de Haskell)
  return res

"""6. es_par(numero): que indique si numero es par (usar la función es_multiplo_de())."""

def es_par(numero: float) -> bool:
  res: bool = es_multiplo_de(numero,2)
  return res

"""7. cantidad_de_pizzas(comensales, min_cant_de_porciones) que devuelva la cantidad de pizzas que necesitamos para que cada comensal coma
como mínimo min_cant_de_porciones porciones de pizza. Considere que cada pizza tiene 8 porciones y que se prefiere que sobren porciones."""

# La operación 'div' de Haskell corresponde a // en Python

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
  cantidad_porciones: int = comensales*min_cant_de_porciones
  if cantidad_porciones % 8 == 0: # si #porciones es multiplo de 8
    return cantidad_porciones // 8 # con cant_porciones // 8 alcanza
  else:
    return (cantidad_porciones // 8) + 1 #sino, hay que sumar 1

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 # Resuelva los siguientes ejercicios utilizando los operadores lógicos and, or, not (sin utilizar if):
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0."""

def alguno_es_0(numero1: float, numero2: float) -> bool:
  res: bool = (numero1 == 0) or (numero2 == 0)
  return res

"""2. ambos_son_0(numero1, numero2): dados dos números racionales, decide si ambos son iguales a 0."""

def ambos_son_0(numero1: float, numero2: float) -> bool:
  res: bool = (numero1 == 0) and (numero2 == 0)
  return res

"""3. problema es_nombre_largo (in nombre: String) : Bool {
  requiere: { True }
  asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
}"""

def es_nombre_largo(nombre: str) -> bool:
  res: bool = (len(nombre) >= 3) and (len(nombre) <= 8)
  return res

"""4. es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400, o bien es múltiplo de 4
pero no de 100."""

def es_bisiesto(año: int) -> bool:
  res: bool = (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0) # reemplazo directamente las condiciones del enunciado.
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
En una plantación de pinos, de cada árbol se conoce la altura expresada en metros. El peso de un pino se puede estimar a partir de la altura
de la siguiente manera:
  -3 kg por cada centímetro hasta 3 metros,
  -2 kg por cada centímetro arriba de los 3 metros.
  Por ejemplo:
  -2 metros pesan 600 kg, porque 200*(3 [kg]) = 600 [kg]
  -5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.

Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino fuera de este rango
no le sirve a la fábrica.

Definir las siguientes funciones, deducir qué parámetros tendrán a partir del enunciado. Se pueden usar funciones auxiliares si fuese necesario
para aumentar la legibilidad.
  1. Definir la función peso_pino
  2. Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
  3. Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
  4. Definir sirve_pino usando composición de funciones.
"""

"""
Defino: h = altura [cm]
  si h < 300 [cm] => peso = h*(3 [kg])
  si h > 300 [cm] => peso = 300*(3 [kg]) + (h-300)*(2 [kg])
"""

def peso_pino(altura: int) -> int: # Esta función recibe la altura del pino en cm, y devuelve su peso en kg.
  if altura <= 300:
    return altura*3 # peso en kg
  if altura > 300:
    return 900 + (altura-300)*2

def es_peso_util(peso: int) -> bool: # Esta función recibe el peso del pino en kg y decide si es útil para la fábrica.
  res: bool = (peso >= 400 and peso <= 1000)
  return res

def sirve_pino(altura: int) -> bool: # Esta función recibe la altura del pino en cm, y decide si su peso es útil para la fábrica.
  res: bool = (peso_pino(altura) >= 400 and peso_pino(altura) <= 1000)
  return res

def sirve_pino_composicion(altura: int) -> bool: # Uso composición de funciones
  return es_peso_util(peso_pino(altura))

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Implementar los siguientes problemas de alternativa condicional (if/else). Los enunciados pueden no ser del todo claros, especificar los
# problemas en nuestro lenguaje de especificación y programar en base a tu propuesta de especificación.

"""1. devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en caso contrario."""

"""Especificación:
problema devolver_el_doble_si_es_par(numero : Z) : Z {
  requiere: {True}
  asegura: {si numero es impar -> res = numero}
  asegura: {si numero es par -> res = 2*numero}
}"""

def devolver_el_doble_si_es_par(numero: int) -> int:
  res: int = numero
  if res % 2 == 0:
    return 2*res
  else:
    return res

"""2. devolver_valor_si_es_par_si_no_el_que_sigue(numero): devuelve el mismo número si es par, y si no, el siguiente. Analizar distintas
formas de implementación (usando un if-then-else y dos if). ¿Todas funcionan?"""

"""Especificación:
problema devolver_valor_si_es_par_si_no_el_que_sigue(numero : Z) : Z {
  requiere: {True}
  asegura: {si numero es impar -> res = numero+1}
  asegura: {si numero es par -> res = numero}
}"""

# Implementación 1: if -> then -> else
def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int) -> int:
  res: int = numero
  if res % 2 == 0:
    return res
  else:
    return res + 1

# Implementación 2: if -> if
"""
  res: int = numero
  if res % 2 == 0:
    return res
  if res % 2 != 0:
    return res + 1
"""

# Vemos que ambas implementaciones funcionan, pero la primera es más compacta (y por lo tanto más fácil).

"""3. devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero): en otro caso, devolver el número original. Analizar distintas
formas de implementación (usando un if-then-else, dos if, o alguna opción de operación lógica). ¿Todas funcionan? ¿Cuál es el resultado
si la entrada es 18?"""

"""Especificación:
problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero : Z) : Z {
  requiere: {True}
  asegura: {si numero % 9 == 0 -> res = 3*numero}
  asegura: {si numero % 3 == 0 -> res = 2*numero}
  asegura: {si no se cumple ninguna de las anteriores -> res = numero}
}"""

# Implementación 1:
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
  res: int = numero
  if res % 9 == 0:
    return 3*numero
  elif res % 3 == 0:
    return 2*numero
  else:
    return numero
"""
  if res % 9 == 0:
    return 3*numero
  else:
    if res % 3 == 0:
      return 2*numero
    else:
      return numero
"""
# Vemos que la segunda alternativa también funciona, pero es menos compacta. El 18 devuelve 18*3 = 54 ya que implementamos primero el
# chequeo de divisibilidad por nueve (que es el más fuerte), y luego el de divisibilidad por 3.

"""4. lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga "Tu nombre tiene muchas
letras!" y si no, "Tu nombre tiene menos de 5 caracteres"."""

"""Especificación:
problema lindo_nombre(nombre : string) : string {
  requiere: {True}
  asegura: {si len(nombre) >= 5 -> res = "Tu nombre tiene muchas letras!".}
  asegura: {si len(nombre) < 5 -> res = "Tu nombre tiene menos de 5 caracteres".}
}"""

def lindo_nombre(nombre: str) -> str:
  res: str = nombre
  if len(nombre) >= 5:
    res = "Tu nombre tiene muchas letras!"
  else:
    res = "Tu nombre tiene menos de 5 caracteres"
  return res

"""5. elRango(numero) que imprime por pantalla "Menor a 5" si el número es menor a 5, "Entre 10 y 20" si el número está en ese rango y
"Mayor a 20" si el número es mayor a 20."""

"""Especificación:
problema el_rango(numero : Z) : Z {
  requiere: {True}
  asegura: {si numero < 5 -> res = "Menor a 5".}
  asegura: {si 10 <= numero <= 20 -> res = "Entre 10 y 20".} Agrego la condición mayor/menor igual
  asegura: {si numero > 20 -> res = "Mayor a 20".}
  asegura: {si numero no se encuentra en ninguno de dichos intervalos -> res = "No responde".} Agrego esta condición
}"""

def el_rango(numero: int) -> str:
  res: str = ''
  if numero < 5:
    res = 'Menor a 5'
  elif (numero >= 10) and (numero <= 20):
    res = 'Entre 10 y 20'
  else:
    if numero > 20:
      res = 'Mayor a 20'
    else:
      res = 'No responde'
  return res

"""6. En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan a los 65 años.
Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de las personas se les ordena ir a trabajar.
Implemente una función que, dados los parámetros de sexo (F o M) y edad, imprima la frase que corresponda según el caso: "Andá de vacaciones"
o "Te toca trabajar"."""

"""Especificación:
problema trabajo_o_vacaciones(edad: int, sexo: string) : string {
  requiere: {True}
  asegura: {si (18 < edad < 65, y sexo == "M") -> res = "Te toca trabajar".}
  asegura: {si (18 < edad < 60, y sexo == "F") -> res = "Te toca trabajar".}
  asegura: {en otro caso, res = "Andá de vacaciones".}
}"""

def trabajo_o_vacaciones(edad: int, sexo: str) -> str:
  res: str = ''
  if ((edad > 18 and edad < 65) and sexo == 'M') or ((edad > 18 and edad < 60) and sexo == 'F'):
    res = 'Te toca trabajar'
  else:
    res = 'Andá de vacaciones'
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 # Implementar las siguientes funciones usando repetición condicional while:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. Escribir una función que imprima los números del 1 al 10."""

def uno_al_diez() -> int:
  n: int = 1
  while n >= 1:
    print(n)
    if n == 10:
        break
    n += 1 # esta versión es más elegante
#   n = n + 1 también sirve

"""2. Escribir una función que imprima los números pares entre el 10 y el 40."""

def pares_10_al_40() -> int:
  n: int = 12
  while n >= 12:
    print(n)
    if n == 38:
      break
    n += 2

"""3. Escribir una función que imprima la palabra "eco" 10 veces."""

def palabra_repetida(palabra: str) -> str: # el argumento palabra, permite que pueda repetir 10 veces cualquier palabra
  n: int = 1
  while n >= 1:
    print(palabra)
    if n == 10:
      break
    n += 1

"""4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro
(que será positivo) hasta el 1, y por último "Despegue"."""

def cuenta_regresiva(numero: int) -> None:
  res: int = numero
  while res <= 10:
    print(res)
    if res == 1:
      print("Despegue")
      break
    res -= 1

"""5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, "el año de partida" y "algún año de llegada",
siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos de un año y la función debe mostrar el texto:
"Viajó un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de año."""

def viaje_temporal(año_de_partida: int, año_de_llegada: int) -> str:
  año: int = año_de_partida - 1
  while año >= año_de_llegada:
    print(f"Viajó un año al pasado, estamos en el año: {año}")
    if año == año_de_llegada:
      break
    año -= 1

"""6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C., donde
conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada salto!"""

def viaje_temporal_extremo(año_de_partida: int, año_de_llegada: int) -> str:
  año: int = año_de_partida - 20
  while año >= año_de_llegada:
    print(f"Viajó un año al pasado, estamos en el año: {año}")
    if año == año_de_llegada:
      break
    año -= 20

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 7 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la función range para generar una secuencia de
# números en un rango dado, admite un valor inicial i, un valor final f y un paso p. Ver documentación:
# https://docs.python.org/es/3/library/stdtypes.html#typesseq-range

"""1. Escribir una función que imprima los números del 1 al 10."""

def for_uno_al_diez() -> int:
  for i in range(1,11,1):
    print(i)

"""2. Escribir una función que imprima los números pares entre el 10 y el 40."""

def for_pares_10_al_40() -> int:
  for i in range(12,39,2):
    print(i)

"""3. Escribir una función que imprima la palabra "eco" 10 veces."""

def for_palabra_repetida(palabra: str) -> str: # el argumento palabra, permite que pueda repetir 10 veces cualquier palabra
  for i in range(1,11,1):
    print(palabra)

"""4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro
(que será positivo) hasta el 1, y por último "Despegue"."""

def for_cuenta_regresiva(numero: int) -> None:
  for i in range(numero,0,-1): # ahora tuvimos que poner hasta 0, pues no incluye al último -> el ultimo será 1
    print(i)
  print("Despegue")

"""5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, "el año de partida" y "algún año de llegada",
siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos de un año y la función debe mostrar el texto:
"Viajó un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de año."""

def for_viaje_temporal(año_de_partida: int, año_de_llegada: int) -> str:
  for i in range(año_de_partida-1,año_de_llegada-1,-1):
    print(f"Viajó un año al pasado, estamos en el año: {i}")

"""6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C., donde
conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada salto!"""

def for_viaje_temporal_extremo(año_de_partida: int, año_de_llegada: int) -> str:
  for i in range(año_de_partida-20,año_de_llegada-1,-20):
    print(f"Viajó un año al pasado, estamos en el año: {i}")

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 8 # Realizar la ejecución simbólica de los siguientes códigos:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. x=5 ; y=7; x = x + y"""

x = 5 # Se define la variable x
y = 7 # Se define la variable y
x = x+y # Se actualiza el valor de x, y el resultado es x = 5+7 = 12

"""2. x=5 ; y=7 ; z=x+y; y = z * 2"""

x = 5
y = 7
z = x+y # z = 12
y = 2*z # Ahora actualizo y, por lo tanto y = 2*12 = 24

"""3. x=5 ; y=7 ; x="hora"; y = x * 2"""

x = 5
y = 7
x = "hora" # Ahora actualizo la variable x y cambia su tipo de int a str
y = 2*x # Ahora multiplico por 2 al string. El resultado es horahora

"""4. x=False ; res=not(x)"""

x = False
res = not(x) # Not(False) = True

"""5. x=False ; x=not(x)"""

x = False
x = not(x) # Actualizo -> x = not(False) = True

"""6. x=True ; y=False ; res=x and y; x = res and x"""

x = True
y = False
res = x and y # True and False = False
x = res and x # res and x = False and True = False

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 9 # Sea el siguiente código:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def rt(x: int, g: int) -> int:
  g = g + 1
  return x + g

g: int = 0
def ro(x: int) -> int:
  global g
  g = g + 1
  return x + g

"""1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?"""

"""El resultado de evaluar 3 veces seguidas a la función ro(1) es 2, 3 y 4, pues tenemos los siguientes casos:
Primera evaluación:
  g = g + 1 -> g = 1 pues estaba definida fuera de la función con el valor de g = 0.
  luego return x+g = 1 + 1 = 2.
Segunda evaluación:
  Ahora g = 1 -> g = g + 1 = 1 + 1 = 2
  luego, return x + g = 2 + 1 = 3.
Tercera evaluación:
  Análogamente, el resultado será 4."""

"""2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?"""

"""Como en este caso g no es una variable global, no se actualizará fuera de la función. De esta forma al llamar varias veces a la función rt,
siempre se obtendrá el mismo valor. Como g = g + 1 y x = 1 y g=0 -> res = x + g = 1 + 1 = 2 siempre."""

"""3. En cada función, realizar la ejecución simbólica."""

"""Listo, se verificó lo afirmado para el ítem 1. y 2."""

"""4. Dar la especificación para cada función, rt y ro."""

"""
Especificación de la función 1:
problema rt(x: Z, g: Z) : Z {
  requiere: {True}
  asegura: {El resultado de evaluar rt(x,g) es x+g, donde g es una variable local definida como g = g + 1.}
}

Especificación de la función 2:
problema ro(x: Z) : Z {
  requiere: {True}
  asegura: {El resultado de evaluar ro(x) es x+g, donde g es una variable global definida dentro de la función como g = g + 1.}
  asegura: {Inicialmente, el valor de g es g = 0.}
}"""

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————