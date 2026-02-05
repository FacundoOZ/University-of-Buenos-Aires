
#============================================================================================================================================
# Práctica Especial: Ejercicios Integradores de Python
#============================================================================================================================================

from queue import LifoQueue as pila
from queue import Queue as cola

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 # Veterinaria - Stock
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# En la veterinaria 'Exactas’s pets', al finalizar cada día, el personal registra en papeles los nombres y la cantidad actual de los
# productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección de la veterinaria han pedido desarrollar una solución en
# Python que les permita analizar las fluctuaciones del stock. Se pide implementar una función, que reciba una lista de tuplas donde cada
# tupla contiene el nombre de un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario que tenga
# como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico registrado.

"""problema stock_productos(in stock_cambios : seq⟨str x Z⟩) : diccionario⟨str, Z x Z⟩ {
  requiere: {Todos los elementos de stock cambios están formados por un str no vacío y un entero ≥ 0.}
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
  asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
  asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese producto en stock
            cambios y como segundo valor el mayor.}
}"""

def stock_productos(stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
  res: dict[str,tuple[int,int]] = {}

  for tupla in stock_cambios:                         # Por cada tupla de la lista de tuplas
    if tupla[0] not in res.keys():                    # Si tupla[0] no es clave de res,
      res[tupla[0]] = (tupla[1], tupla[1])            # Genero la clave y su valor será la tupla elemental (min=max)
    else:
      if tupla[1] < res[tupla[0]][0]:                 # Si la clave existe y el nuevo valor es menor al menor histórico,
        lista_menor: list[int]  = list(res[tupla[0]]) # Convierto tupla a lista
        lista_menor[0]          = tupla[1]            # Cambio solo el valor del mínimo
        res[tupla[0]]           = tuple(lista_menor)  # Reconvierto a tupla y actualizo valor de res
      elif tupla[1] > res[tupla[0]][1]:               # Si la clave existe y el nuevo valor es mayor,
        lista_mayor: list[int]  = list(res[tupla[0]]) # Idem,
        lista_mayor[1]          = tupla[1]            # Pero con el mayor
        res[tupla[0]]           = tuple(lista_mayor)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 # Veterinaria - Filtrar códigos de barra
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos códigos de barras terminan en
números primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre de esta idea, solicita una
función en Python que facilite esta gestión. Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un
código de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de la lista original cuyos
últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).
Nota: Un número primo es aquel que solo es divisible por sí mismo y por 1. Algunos ejemplos de números primos de hasta tres dígitos son:
2, 3, 5, 101, 103, 107, etc."""

"""problema filtrar_codigos_primos(in codigos_barra : seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos.}
  requiere: {No hay elementos repetidos en codigos_barra.}
  asegura: {Los últimos 3 dígitos de cada uno de los elementos de res forman un número primo.}
  asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo están en res.}
  asegura: {Todos los elementos de res están en codigos_barra.}
}"""

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
  lista_primos: list[int] = []
  for numero in codigos_barra: # n % 1000 = n <-> n tiene 3 dígitos o menos
    if ((numero % 1000) == numero) and (es_primo(numero) == True) and (numero not in lista_primos):
      lista_primos.append(numero)
  return lista_primos

def es_primo(n: int) -> bool: # Función auxiliar. Si n es primo, devuelve True
  res: bool = True
  if n <= 1:
    res = False
  else:
    for j in range(2,n): # [2,3,4,...,n-1] pues si ninguno divide, 1 y n siempre dividen, y será primo
      if (n % j) == 0:
        res = False
        break
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 # Veterinaria - Flujo de pacientes
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando al local. Se
# necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una función en Python que encuentre
# la secuencia más larga de consultas consecutivas que solo contenga los tipos de mascota 'perro' o 'gato'. Se pide implementar una función
# que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el índice donde comienza la subsecuencia más
# larga que cumpla con estas condiciones.

"""problema subsecuencia_mas_larga(in tipos_pacientes_atendidos : seq⟨str⟩) : Z {
  requiere: {tipos_pacientes_atendidos tiene, por lo menos, un elemento 'perro' o 'gato'.}
  asegura: {res es el índice donde empieza la subsecuencia más larga de tipos_pacientes_atendidos que contiene solo elementos 'perro' o 'gato'.}
  asegura: {Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera.}
}"""

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
  i_actual: int    = 0                                      # Genero un índice para ir contando la posición donde arranca un conteo
  suma_actual: int = 0                                      # Genero un índice para saber la cantidad de posiciones repetidas actuales
  res: int         = 0                                      # res = i_max
  suma_max: int    = 0
  for i in range(len(tipos_pacientes_atendidos)):
    if tipos_pacientes_atendidos[i] == 'perro' or tipos_pacientes_atendidos[i] == 'gato':
      if i == 0:                                            # Caso base
        suma_actual = 1
        i_actual    = i
      elif (tipos_pacientes_atendidos[i] != tipos_pacientes_atendidos[i-1]): # Si el paso actual y el anterior tienen distintas mascotas,
        suma_actual = 1                                     # reseteo la suma
        i_actual    = i                                     # y el índice actual
      else:
        suma_actual += 1                                    # Si son iguales, sumo más valores
        if suma_actual > suma_max:                          # Si la secuencia actual tiene long = max, se contempla la primera solamente
          res      = i_actual
          suma_max = suma_actual
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 # Veterinaria - Tabla turnos
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los días, en orden de lunes a domingo,
y cada fila un rango de una hora. Hay cuatro filas para los turnos de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde (14,15,16
y 17). Para hacer más eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables, están
asignadas de manera continuada en los turnos de cada día. Para ello se pide desarrollar una función en Python que, dada la matriz de turnos,
devuelva una lista de tuplas de bool, una por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo
si todos los valores de los turnos de la mañana para ese día son iguales entre sí. El segundo elemento debe ser True si y solo si todos los
valores de los turnos de la tarde para ese día son iguales entre sí. Siempre hay una persona responsable en cualquier horario de la
veterinaria."""

"""problema un_responsable_por_turno(in grilla_horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool x Bool⟩ {
  requiere: {|grilla_horaria| = 8.}
  requiere: {Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor 8).}
  requiere: {No hay cadenas vacías en las listas de grilla_horaria.}
  asegura: {|res| = |grilla_horaria[0]|.}
  asegura: {El primer valor de la tupla en res [i], con i en Z, es igual a True si y solos si los primeros 4 valores de la columna i de
            grilla_horaria son iguales entre sí.}
  asegura: {El segundo valor de la tupla en res [i], con i en Z, es igual a True si y solos si los últimos 4 valores de la columna i de
            grilla_horaria son iguales entre sí.}
}"""

"""La matriz grilla horaria es de la forma:

      Lunes  Martes  Miércoles  Jueves  Viernes  Sábado  Domingo
9  h    'A'
10 h    'A'
11 h    'A'
12 h    'A'
-------------------------------------------------------------------
14 h    'J'
15 h    'J'
16 h    'J'
17 h    'J'
=> [(True,True)] (por ej. para el lunes)"""

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
  res: list[tuple[bool,bool]] = []
  for j in range(len(grilla_horaria[0])):           # j representa las columnas de grilla_horaria (elijo la fila 0)
    col_actual: list[bool] = [False,False]          # Creo una lista (las tuplas no son modificables)
    x = grilla_horaria[0][j]                        # Primer elemento (primera fila) de la columna j
    y = grilla_horaria[4][j]                        # Quinto elemento (quinta fila) de la columna j
    if (x == grilla_horaria[1][j] and x == grilla_horaria[2][j] and x == grilla_horaria[3][j]):
      col_actual[0] = True
    if (y == grilla_horaria[5][j] and y == grilla_horaria[6][j] and y == grilla_horaria[7][j]):
      col_actual[1] = True
    tup_actual: tuple[bool] = tuple(col_actual)     # Convierto a tupla
    res.append(tup_actual)                          # Agrego a res
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 # Sala de Escape - Promedio de salidas
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de una habitación
resolviendo enigmas, llevan un registro meticuloso de todas las salas de escape que hay en Capital. Este registro indica si han visitado una
sala y si pudieron o no salir de ella. Un 0 significa que no fueron, un 61 que no lograron salir a tiempo, y un número entre 1 y 60
representa los minutos que les tomó escapar exitosamente. Con estos datos, pueden comparar sus logros y desafíos en cada nueva aventura que
emprenden juntos. Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos)
registrados para cada sala de escape en Capital, escribir una función en Python que devuelva un diccionario. En este nuevo diccionario, las
claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada persona logró
salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir)."""

"""problema promedio_de_salidas(in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z x R>> {
  requiere: {registro tiene por lo menos un integrante.}
  requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
  requiere: {Todos los valores de registro tiene la misma longitud.}
  requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive.}
  asegura: {res tiene las mismas claves que registro.}
  asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto
            a 61 que figuran en sus valores de registro.}
  asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0, es el promedio
            de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro, sino es 0.0.}
}
Ejemplo: dada la entrada {'a': [61,60,59,58], 'b': [1,2,3,0]}, la salida es {'a': (3,59.0), 'b': (3,2.0)}."""

def promedio_de_salidas(registro: dict[tuple[str,list[int]]]) -> dict[str,tuple[int,float]]:
  res: dict[str,tuple[int,float]]         = {}
  for jugador in registro.keys():                           # Por cada jugador ('a','b',etc.) de registro,
    huidas_y_promedio: list[int,float]  = []
    cant_huidas: int    = 0
    suma: int           = 0
    for elem in registro[jugador]:                          # Por cada elemento de la lista del jugador ('a','b',etc.)
      if elem > 0 and elem < 61:                            # Si se cumple la condición
        cant_huidas += 1                                    # Se agrega 1 huida al contador
        suma        += elem                                 # Sumo los minutos a la suma total
    huidas_y_promedio   = [cant_huidas, suma/(cant_huidas)] # Completo las huidas y promedio (solo de huidas)
    res[jugador]        = tuple(huidas_y_promedio)          # Convierto a tupla y agrego valor a la clave 'jugador' de res
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 # Sala de Escape - Tiempo más rápido
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una función en Python que devuelva la
# posición (índice) en la cual se encuentra el tiempo más rápido, excluyendo las salas en las que no haya salido (0 o mayor a 60).

"""problema tiempo_mas_rapido(in tiempos salas: seq⟨Z⟩) : Z {
  requiere: {Hay por lo menos un elemento en tiempos salas entre 1 y 60 inclusive.}
  requiere: {Todos los tiempos en tiempos salas están entre 0 y 61 inclusive.}
  asegura: {res es la posición de la sala en tiempos salas de la que más rápido se salió (en caso que haya más de una, devolver la primera,
            osea la de menor índice).}
}"""

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
  res: int    = 0
  t_min: int  = 60                                      # Inicializo el t_min en el t limite de escape
  for i in range(len(tiempos_salas)):                   # Me importa el índice => uso range(len(...))
    if tiempos_salas[i] < t_min:                        # Si un tiempo en un dado índice es menor al t_min actual,
      t_min = tiempos_salas[i]                          # Ahora es mi t_min!
      res = i                                           # Actualizo la posición de res, hasta que encuentre (si hay) uno menor
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 7 # Sala de Escape - Racha más larga
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una función en Python
# que devuelva una tupla con el índice de inicio y el índice de fin de la subsecuencia más larga de salidas exitosas de salas de escape
# consecutivas.

"""problema racha_mas_larga(in tiempos: seq⟨Z⟩) : <Z x Z> {
  requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive.}
  requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive.}
  asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga.}
  asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga.}
  asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61.}
  asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61.}
  asegura: {La primera posición de res es menor o igual a la segunda posición de res.}
  asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res.}
  asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y
            la segunda posición de res.}
  asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
}"""

def racha_mas_larga(tiempos: list[int]) -> tuple[int,int]:
  huida: list[int]    = list(range(1,61))                  # Rango de huida
  i_actual: int       = 0                                  # Índice actual
  i_max: int          = 0                                  # Índice máximo histórico
  cant_actual: int    = 0                                  # Cantidad actual
  cant_max: int       = 0                                  # Cantidad máxima histórica
  for i in range(len(tiempos)):                            # Necesito el índice => uso range(len(...))
    if tiempos[i] in huida:
      if i == 0:                                           # Caso elemental
        i_actual = 0
        cant_actual += 1
      else:
        if (tiempos[i-1] not in huida) and (tiempos[i] in huida):
          i_actual = i                                     # Empiezo un nuevo índice
          cant_actual = 1                                  # y empiezo a contar nuevamente
        else:
          cant_actual += 1                                 # Agrego a mi cantidad
      if cant_actual > cant_max:                           # Máximos
        i_max = i_actual
        cant_max = cant_actual
  lista_deseada: list[int] = [i_max, i_max + cant_max - 1] # Creo la lista deseada
  res: tuple[int,int] = tuple(lista_deseada)               # Convierto a tupla
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 8 # Sala de Escape - Escape en solitario
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos
(en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en
Python que devuelva los índices de todas las filas (que representan las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0),
pero el tercero sí fue independientemente de si salió o no)."""

"""problema escape_en_solitario(in amigos: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {Hay por lo menos una sala en amigos.}
  requiere: {Hay 4 amigos en amigos.}
  requiere: {Todos los tiempos en cada sala de amigos están entre 0 y 61 inclusive.}
  asegura: {La longitud de res es menor igual que la longitud de amigos.}
  asegura: {Por cada sala en amigos cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala
            en amigos debe aparecer res.}
  asegura: {Para todo i en a res se cumple que el primer, segundo y cuarto valor de amigos[i] es 0, y el tercer valor es distinto de 0.}
}
Ejemplo de matriz:

      'Facu'    'Lauti'    'Eitan'    'Rodri'
Sala 1    0          0     1,...,60,61     0        =>  FILA 0
Sala 2
Sala 3
Sala 4
"""

def escape_en_solitario(amigos: list[list[int]]) -> list[int]:
  res: list[int]   = []
  rango: list[int] = list(range(1,62))
  for fila in range(len(amigos[0])):                           # Elijo la fila 0 como referencia (podría haber sido cualquiera)
    if (amigos[fila][0] == 0) and (amigos[fila][1] == 0) and (amigos[fila][3] == 0) and (amigos[fila][2] in rango):
      res.append(fila)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 9 # Juego de la Gallina
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""El juego de la gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario; si alguno se
desvía de la trayectoria de choque pierde y es humillado por comportarse como un 'gallina'. Se hizo un torneo para ver quién es el menos
gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores juegan y se chocan entre sí, entonces pierde
cada uno 5 puntos por haberse dañado. Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas. Si uno no se desvía y el otro
sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos. En este torneo, cada persona que participa tiene una
estrategia predefinida para competir: o siempre se devía, o nunca lo hace. Se debe programar la función 'torneo de gallinas' que recibe un
diccionario (donde las claves representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas
estrategias) y devuelve un diccionario con los puntajes obtendidos por cada jugador."""

"""problema torneo_de_gallinas(in estrategias: dict<str, str>) : dict<str, Z> {
  requiere: {estrategias tiene por lo menos 2 elementos (jugadores).}
  requiere: {Las claves de estrategias tienen longitud mayor a 0.}
  requiere: {Los valores de estrategias sólo pueden ser los strs 'desviador' ó 'chocador'.}
  asegura: {Las claves de res y las claves de estrategias son iguales.}
  asegura: {Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar el
            torneo, dado que jugó una vez contra cada otro jugador.}
}
Ejemplo:
estrategias = {'A': 'desviador', 'B': 'chocador', 'C': 'chocador'}
torneo_de_gallinas(estrategias) = {'A': -15-15 = -30,
                                  'B': 10 - 5 = 5,
                                  'C': 10 - 5 = 5}"""

def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
  res: dict[str,int]  = {}
  suma_puntos: int    = 0                                            # Suma de puntos actuales para el jugador i-ésimo
  for i in estrategias.keys():
    for j in estrategias.keys():                                     # Dado un jugador i-ésimo, calculo el resultado de i contra los demás
      if i == j:                                                     # Un jugador no juega contra si mismo
        suma_puntos += 0
      else:                                                          # Todas las combinaciones posibles
        if   estrategias[i] == 'chocador'  and estrategias[j] == 'chocador':
          suma_puntos -= 5
        elif estrategias[i] == 'desviador' and estrategias[j] == 'desviador':
          suma_puntos -= 10
        elif estrategias[i] == 'chocador'  and estrategias[j] == 'desviador':
          suma_puntos += 10
        elif estrategias[i] == 'desviador' and estrategias[j] == 'chocador':
          suma_puntos -= 15
    res[i] = suma_puntos                                             # Agrego el resultado i-ésimo contra todos los j-ésimos como clave de res
    suma_puntos = 0                                                  # Reseteo la suma actual
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 10 # Cola en el Banco
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por las tuplas
(nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser 'común' o 'vip'. Se nos pide implementar una
función en python que dada una cola de clientes del banco, devuelva una nueva cola con los mismos clientes pero en donde los clientes vip
están primero que los clientes comunes manteniendo el orden original de los clientes vips y los comunes entre sí."""

"""problema reordenar_cola_priorizando_vips(in fila_clientes: cola<str x str>) : cola<str> {
  requiere: {La longitud de los valores de la primera componente de las tuplas de la cola fila_clientes es mayor a 0.}
  requiere: {Los valores de la segunda componente de las tuplas de la cola fila_clientes son 'común' o 'vip'.}
  requiere: {No hay dos tuplas en fila_clientes que tengan la primera componente iguales entre sí.}
  asegura: {todo valor de res aparece como primera componente de alguna tupla de fila_clientes.}
  asegura: {|res| = |filaCliente|.}
  asegura: {res no tiene elementos repetidos.}
  asegura: {No hay ningún cliente 'común' antes que un 'vip' en res.}
  asegura: {Para todo cliente c1 y cliente c2 de tipo 'común' pertenecientes a fila_clientes si c1 aparece antes que c2 en fila_clientes
            entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
  asegura: {Para todo cliente c1 y cliente c2 de tipo 'vip' pertenecientes a fila_clientes si c1 aparece antes que c2 en fila_clientes
            entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
}
Ejemplo: dada la entrada filaClientes conteniendo los elementos en el orden ('Ana', 'comun'), ('Juli', 'vip') y ('Fede', 'vip'), la salida
esperada no modifica filaClientes, y devuelve una cola con los siguientes elementos en este orden: 'Juli', 'Fede','Ana'."""

def reordenar_cola_priorizando_vips(fila_clientes: cola[tuple[str,str]]) -> cola[str]:
  res: cola[str]                  = cola()
  comunes: cola[str]              = cola()
  vips: cola[str]                 = cola()
  list_aux: list[tuple[str,str]]  = []
  while not fila_clientes.empty():         # De fila_clientes, obtengo
    cliente: str = fila_clientes.get()     # cada tupla,
    list_aux.append(cliente)               # la guardo en una lista auxiliar,
    if cliente[1] == 'vip':                # y si se cumplen las condiciones (el 2° elemento de la tupla es vip o común),
      vips.put(cliente[0])                 # agrego solo los nombres a una cola vip
    elif cliente[1] == 'comun':
      comunes.put(cliente[0])              # o una cola común
  while not vips.empty():
    res.put(vips.get())                    # Agrego los vips a res,
  while not comunes.empty():
    res.put(comunes.get())                 # y luego los comunes
  for elem in list_aux:
    fila_clientes.put(elem)                # Restauro la fila_clientes (el orden no cambió)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 11 # Sufijos que son palíndromos
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide programar en python
# la siguiente función:

"""problema cuantos_sufijos_son_palindromos(in texto: str) : Z {
  requiere: {True}
  asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto.}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el al final de la texto. Ej: 'Diego', el conjunto de
sufijos es: 'Diego', 'iego','ego','go', 'o'. Para este ejercicio no consideraremos a '' como sufijo de ningún texto."""

def cuantos_sufijos_son_palindromos(texto: str) -> int:
  palabra: list[str] = []      # Creo una lista de strings vacía.
  for letra in texto:          # Convierto el texto (str) a una lista de cada letra (list[str])
    palabra.append(letra)

  cant: int = 0                # Creo un contador de palíndromos
  while palabra:               # Mientras palabra != [] (tenga más de 0 elementos)
    if es_palindromo(palabra): # Si es palíndromo
      cant += 1                # Sumo 1
    palabra.pop(0)             # Quito el primer elemento
  return cant

def es_palindromo(palabra: list[str]) -> bool:
  res: bool = False
  for i in range(len(palabra)):
    if palabra[i] == palabra[len(palabra)-1-i]: # Si la primera letra = última letra (y voy incrementando)
      res = True                                # Es palíndromo
    else:
      res = False
      break
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 12 # Ta-Te-Ti
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Ana y Beto juegan al Ta-Te-Ti. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su ficha en cada turno.
Juegan intercaladamente y comienza Ana. Ana pone siempre una 'X' en su turno y Beto pone una 'O' en el suyo. Gana la persona que logra poner
3 fichas suyas consecutivas en forma vertical. Si el tablero está completo y no ganó nadie, entonces se declara un empate. El tablero comienza
vacío, representado por ' ' en cada posición. Notar que dado que juegan por turnos y comienza Ana poniendo una 'X' se cumple que la cantidad
de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' son uno más que la cantidad de 'O'. Se nos pide implementar una función en
python quien gano el tateti que determine si ganó alguno, o si Beto hizo trampa (puso una 'O' cuando Ana ya había ganado)."""

"""problema quien_gano_el_tateti(in tablero:seq⟨seq⟨Char⟩⟩) : Z {
  requiere: {tablero es una matriz cuadrada.}
  requiere: {5 ≤ |tablero[0]| ≤ 10.}
  requiere: {tablero sólo tiene 'X', 'O' y '' (espacio vacío) como elementos.}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'.}
  asegura: {res=1 ⇔ hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' en forma vertical(misma columna).}
  asegura: {res=2 ⇔ hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X'  en forma vertical(misma columna).}
  asegura: {res=0 ⇔ no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical.}
  asegura: {res=3 ⇔ hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa).}
}"""

def quien_gano_tateti(tablero: list[list[str]]) -> int:
  res: int    = 0
  A: bool     = False                     # Defino los booleanos
  B: bool     = False
  for i in range(len(tablero)-2):         # i son las filas
    for j in range(len(tablero)):         # j son las columnas
      if tablero[i][j] == 'X' and tablero[i+1][j] == 'X' and tablero[i+2][j] == 'X':
        A = True                          # Chequeo la condición para A, pero debo cubrir todos los casos, entonces sigo
      elif tablero[i][j] == 'O' and tablero[i+1][j] == 'O' and tablero[i+2][j] == 'O':
        B = True                          # Chequeo la condición para B
  if A == True and B == False:            # Casos
    res = 1
  elif A == False and B == True:
    res = 2
  elif A and B:
    res = 3
  else:
    res = 0
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 13 # Hospital - Atención por Guardia
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes
y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. En enfermería,
hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). A partir
de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación."""

"""problema orden_de_atencion(in urgentes: cola<Z>, in postergables: cola<Z>) : cola<Z> {
  requiere: {No hay elementos repetidos en urgentes.}
  requiere: {No hay elementos repetidos en postergables.}
  requiere: {La intersección entre postergables y urgentes es vacía.}
  requiere: {|postergables| = |urgentes|.}
  asegura: {No hay repetidos en res.}
  asegura: {res es permutación de la concatenación de urgentes y postergables.}
  asegura: {Si urgentes no es vacía, en la cabeza de res hay un elemento de urgentes.}
  asegura: {En res no hay dos seguidos de urgentes.}
  asegura: {En res no hay dos seguidos de postergables.}
  asegura: {Para todo c1 y c2 de tipo 'urgente' pertenecientes a urgentes, si c1 aparece antes que c2 en urgentes entonces c1 aparece antes
            que c2 en res.}
  asegura: {Para todo c1 y c2 de tipo 'postergable' pertenecientes a postergables, si c1 aparece antes que c2 en postergables entonces c1
            aparece antes que c2 en res.}
}"""

def orden_de_atencion(urgentes: cola[int], postergables: cola[int]) -> cola[int]:
  res: cola[int]   = cola()
  u_aux: cola[int] = cola()
  p_aux: cola[int] = cola()
  while not postergables.empty():       # Como |post| = |urg| elijo postergables (pues es el segundo que coloco)
    u = urgentes.get()                  # Guardo el valor de urgentes
    res.put(u)                          # Agrego a res
    u_aux.put(u)                        # Coloco en u_aux
    p = postergables.get()              # Guardo el valor de postergables
    res.put(p)                          # Agrego a res
    p_aux.put(p)                        # Coloco en p_aux
  while not u_aux.empty():              # Vuelvo a generar urgentes,
    urgentes.put(u_aux.get())
  while not p_aux.empty():              # y postergables
    postergables.put(p_aux.get())
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 14 # Hospital - Alarma epidemiológica
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de
# atención por guardia dados por una lista de expedientes. Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención.
# Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por
# esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

"""problema alarma_epidemiologica(in infecciosas : seq⟨str⟩, in registros : seq⟨Z x str⟩, in umbral : R) : dict<str, R> {
  requiere: {0 < umbral < 1.}
  asegura: {Las claves de res pertenecen a infecciosas.}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el
            total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el
            total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
}
Ejemplo:
  infecciosas = ['covid','peste','gripe']
  registros = [(901,'gripe'),(902,'tos'),(904,'covid'),(985,'cancer'),(928,'gripe')]
  umbral = 0.2

  dix = {'covid': 1/5 = 0.2, 'peste': 0/5 = 0, 'gripe': 2/5 = 0.4}, entonces:
  res = {'covid': 0.2, 'gripe': 0.4}
"""

def alarma_epidemiologica(infecciosas: list[str], registros: list[tuple[int,str]], umbral: float) -> dict[str,float]:
  res: dict[str,float] = {}
  total_pacientes: int = len(registros)
  for enfermedad in infecciosas:
    cant_actual: int = 0
    for j in range(len(registros)):
      if registros[j][1] == enfermedad:
        cant_actual += 1
    if cant_actual/total_pacientes >= umbral:
      res[enfermedad] = cant_actual/total_pacientes
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 15 # Hospital - Empleado del mes
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las
horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene
el máximo valor de cantidad total de horas, y devolverlas en una lista."""

"""problema empleados_del_mes(horas: dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías.}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs.}
  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs,
            entonces ID pertenece a res.}
}
Ejemplo:
  horas: {1: [5,6,6,8,6], 2: [8,8,8,8,8], 3: [6,10,6,8,5]}
  empleados_del_mes = [2]"""

def cant_horas(lista: list[int]) -> int:
  res: int = 0                           # Creo una función que sume la cantidad de elementos de una lista
  for i in lista:
    res += i
  return res

def empleados_del_mes(horas: dict[int,list[int]]) -> list[int]:
  lista_horas: list[int] = []                                   # Genero una lista de horas totales
  for clave in horas.keys():                                    # Agrego la cant_horas de cada empleado a la lista
    lista_horas.append(cant_horas(horas[clave]))
  maximo: int = 0
  for j in lista_horas:                                         # Busco el máximo de la lista
    if j > maximo:
      maximo = j
  res: list[int] = []
  for clave in horas.keys():                                    # Para cada clave de horas, si cant_horas de esa clave = máximo, agrego a res
    if cant_horas(horas[clave]) == maximo:
      res.append(clave)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 16 # Hospital - Nivel de ocupación
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son
los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama está ocupada o no. Si el valor es
verdadero (True) indica que la cama está ocupada. Se nos pide programar en Python una función que devuelve una secuencia de reales, indicando
la proporción de camas ocupadas en cada piso."""

"""problema nivel_de_ocupacion(in camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas_por_piso|.}
  asegura: {Para todo 0≤i<|res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido su total de camas).}
}
Ejemplo: dada la entrada camas_por_piso = [[True,  False, True],
                                          [False, False, True],
                                          [True,  True,  True]],
devuelve res = [2/3,1/3,1.0]."""

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
  res: list[float] = []
  for fila in camas_por_piso:     # Por cada fila de la matriz,
    cant: int = 0                 # genero (o reseteo) una cantidad de camas.
    for cama in fila:             # Por cada elemento de la fila,
      if cama:                    # si hay una cama,
        cant += 1                 # sumo 1 a cantidad, sino paso a la siguiente.
    res.append(cant/(len(fila)))  # Al terminar la fila, agrego el float a res.
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 17 # Cambiar matriz
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: {Todas las filas de A tienen la misma longitud}
  requiere: {El mínimo número que aparece en A es igual a 1}
  requiere: {El máximo número que aparece en A es igual a #filas de A por #columnas de A}
  requiere: {No hay enteros repetidos en A}
  requiere: {Existen al menos dos enteros distintos en A}
  modifica: {A}
  asegura: {A tiene exactamente las mismas dimensiones que A@pre}
  asegura: {El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre}
  asegura: {A[i][j] != A@pre[i][j] para todo i, j en rango}
}
Ejemplo: dada la entrada A = [[1,2,3],[4,5,6]], una posible solución es A = [[4,5,6],[1,2,3]]."""

def cambiar_matriz(A: list[list[int]]) -> None:
  primera_fila: list[int] = []  # Creo una lista vacía
  for elem in A[0]:
    primera_fila.append(elem)   # Guardo la primera fila de A en mi lista vacía
  for fila in range(len(A)-1):
    A[fila] = A[fila+1]         # Cambio todas las filas por la fila de abajo (la última será igual a la anteúltima)
  A[len(A)-1] = primera_fila    # Cambio la última fila por la primera (que guardé anteriormente)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 18 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema maximas_cantidades_consecutivos(in v: seq⟨Z⟩) : Diccionario⟨Z,Z⟩ {
  requiere: {True}
  asegura: {Las claves de res son exactamente los números que aparecen al menos una vez en v.}
  asegura: {Para cada clave k de res, su valor es igual a la máxima cantidad de apariciones consecutivas de k en v, donde dicha cantidad de
            apariciones es mayor o igual 1.}
}
Ejemplo:
  v = [3,4,5,5,4,4,6]
  maximas_cantidades_consecutivos = {3: 1, 4: 3, 5: 2, 6: 1}"""

def maximas_cantidades_consecutivos(v: list[int]) -> dict[int,int]:
  res: dict[int,int]      = {}
  chequeados: list[int]   = []
  for elem in v:                          # Por cada elemento que hay en v
    if elem not in chequeados:            # Si no lo hemos calculado aún
      chequeados.append(elem)             # Lo agrego a la lista de calculados
      cant_actual: int = 0                # Contador
      maximo_actual: int = 0
      for i in range(len(v)):             # Por cada índice en v:
        if v[i] == elem:                  # Si v[i] es el elemento actual
          if i == 0:                      # Caso especial
            cant_actual = 1               # Empiezo a contar
          elif v[i-1] != elem:            # Si antes había otro elemento, empiezo a contar de nuevo
            cant_actual = 1
          else:
            cant_actual += 1              # Si no, sumo 1 al contador
          if cant_actual > maximo_actual: # Si la cantidad actual es la mayor hasta ahora,
            maximo_actual = cant_actual   # Tenemos un nuevo máximo
        else:                             # Si v[i] no es elem, empezamos desde 0.
          cant_actual = 0
      res[elem] = maximo_actual           # Tras recorrer toda la lista v, agrego el máximo a la clave elem.
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 19 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema maxima_cantidad_primos(in A: seq⟨seq⟨Z⟩⟩) : Z {
  requiere: {Todas las filas de A tienen la misma longitud.}
  asegura: {Existe alguna columna c en A para la cual res de sus elementos son números primos.}
  asegura: {Todas las columnas de A tienen a lo sumo res elementos que son números primos.}
}"""

def maxima_cantidad_primos(A: list[list[int]]) -> int:
  res: int = 0
  for columna in range(len(A[0])):   # Por cada columna de A,
    primos_columna: int = 0          # cuento los primos en dicha columna.
    for fila in range(len(A)):       # Para cada elemento,
      if es_primo(A[fila][columna]): # Si el elemento es primo,
        primos_columna += 1          # sumo uno, sino paso al siguiente
    if primos_columna > res:         # Si la cantidad de primos de la columna es > res,
      res = primos_columna           # res será (por ahora) dicho número
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 20 # Dadas las siguientes definiciones, resolver:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# -Tupla positiva: par de números enteros en el cual el producto de ambos números es positivo. Ejemplo: (2,3)
# -Tupla negativa: par de números enteros en el cual el producto de ambos números es negativo. Ejemplo: (3,-2)
# -Tupla nula: par de números enteros en el cual el producto de ambos números es igual a cero. Ejemplo: (0,0)

"""problema tuplas_positivas_y_negativas(inout c: cola⟨ZxZ⟩ ) {
  requiere: {c no tiene tuplas repetidas.}
  modifica: {c}
  asegura: {c contiene todas las tuplas positivas y todas las tuplas negativas de c@pre y además no contiene ninguna otra tupla.}
  asegura: {No hay niguna tupla negativa en c que aparezca antes que alguna tupla positiva.}
  asegura: {Para todas las tuplas positivas t1 y t2 en c, con t1 != t2, si t1 aparece antes que t2 en c@pre, entonces t1 aparece antes que
            t2 en c.}
  asegura: {Para todas las tuplas negativas t1 y t2 en c, con t1 != t2, si t1 aparece antes que t2 en c@pre, entonces t1 aparece antes que
            t2 en c.}
}"""

def tuplas_positivas_y_negativas(c: cola[tuple[int,int]]) -> None:
  c_pos: cola[tuple[int,int]] = cola()
  c_neg: cola[tuple[int,int]] = cola()
  c_nul: cola[tuple[int,int]] = cola()
  while not c.empty():
    x = c.get()
    if x[0]*x[1] > 0:
      c_pos.put(x)
    elif x[0]*x[1] < 0:
      c_neg.put(x)
    elif x[0]*x[1] == 0:
      c_nul.put(x)
  while not c_pos.empty():
    c.put(c_pos.get())
  while not c_neg.empty():
    c.put(c_neg.get())

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 21 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema resolver_cuenta(in s: string): R {
  requiere: {Cada caracter de s es '+', '-', '.' (separador decimal) o es un dígito.}
  requiere: {No hay dos operadores consecutivos en s (los operadores son '+' y '-').}
  requiere: {El último caracter de s es un dígito.}
  requiere: {El primer caracter de s es un dígito o un operador.}
  requiere: {En las posiciones adyacentes a cada aparición de '.' en s, hay un dígito.}
  requiere: {Entre un operador y el operador inmediato siguiente hay a lo sumo un separador decimal.}
  requiere: {Antes del primer operador hay a lo sumo un separador decimal.}
  requiere: {Después del último operador hay a lo sumo un separador decimal.}
  asegura: {res es igual al resultado de la operación aritmética representada por s.}
}
Hint: las funciones int o float permiten convertir strings en números enteros o flotantes respectivamente.
Ejemplo: Para el input '+10' se debe devolver 10."""

def resolver_cuenta(s: str) -> float:
  terminos: list[int] = []            # Genero una lista con los términos
  res: int|float      = 0
  for i in range(len(s)):
    if len(s) == 1 and s[0] != '+' and s[0] != '-':
      res = int(s[0])                 # Caso especial, único dígito
      break
    if i == 0:                        # Agrego el primero
      terminos.append(0)
    elif s[i] == '+' or s[i] == '-':
      terminos.append(i)
    elif i == len(s)-1:               # Agrego el último (necesito agregar el elemento del final)
      terminos.append(len(s))         # Me adelanto un índice
  for j in range(len(terminos) - 1):
    término_actual: str = ''
    for digito in range(terminos[j], terminos[j+1]):
      término_actual += s[digito]
    if '.' in término_actual:         # Si el término actual tiene '.' es un float, 
      res += float(término_actual)
    else:                             # Si no, es un entero
      res += int(término_actual)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 22 # Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema palabras_por_vocales(in texto: string): Diccionario⟨Z,Z⟩ {
  requiere: {Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo.}
  asegura: {Los valores de res son positivos.}
  asegura: {Si existe una palabra en texto con x vocales en total, x es clave de res.}
  asegura: {Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en
            texto con ese número de vocales.}
}
Ejemplo:
texto = 'un arbol y un coche tienen iguales vocales'
res = {1: 2, 2: 2, 3: 2, 4: 1}"""

def cantidad_de_vocales(palabra: str) -> int:
  vocales: int = 0                            # Creo una función para contar las vocales de una palabra.
  for letra in palabra:
    if letra in ['a','e','i','o','u']:
      vocales += 1
  return vocales

def palabras_por_vocales(texto: str) -> dict[int,int]:
  lista: list[str] = []                                # Primero separo el texto en una lista de palabras
  for j in range(len(texto)):
    if j == 0:
      if texto[0] != ' ':
        palabra_actual: str = texto[0]
    else:
      if texto[j-1] == ' ' and texto[j] != ' ':
        palabra_actual: str = texto[j]                 # Arranca una nueva palabra
      elif texto[j-1] != ' ' and texto[j] != ' ':
        palabra_actual += texto[j]                     # Sigo agregando letras a una palabra ya iniciada.
        if j == len(texto)-1:                          # Caso especial, justo es la última palabra.
          lista.append(palabra_actual)
      elif texto[j-1] != ' ' and texto[j] == ' ':
        lista.append(palabra_actual)                   # Terminó la palabra, entonces, la agrego a lista.
        palabra_actual = ''
  res: dict[int,int] = {}
  for palabra in lista:                                # Por cada palabra de la lista,
    if cantidad_de_vocales(palabra) not in res.keys():
      res[cantidad_de_vocales(palabra)] = 1            # si su cantidad de vocales no es clave de res, la agrego.
    elif cantidad_de_vocales(palabra) in res.keys():
      res[cantidad_de_vocales(palabra)] += 1           # si ya es clave, sumo uno
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 23 # Acomodar
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""El próximo 19 de Noviembre se realizará en Argentina la segunda vuelta de las elecciones presidenciales. En esta competirán solo 2 listas
(Lista UP; Lista DOWN). En la mayor parte del país los salones de las escuelas ofician de cuartos oscuros. En ellos, las autoridades de mesa
colocan las boletas sobre los pupitres. Dado que esta elección se realizará en una eṕoca donde muy probablemente haga mucho calor, no será
raro el caso en el cual las boletas se vuelen y mezclen a causa de ventiladores prendidos a máxima potencia. Cuando esto ocurra, las
autoridades deberán entrar al cuarto oscuro, juntar todas las boletas, acomodarlas por partido y volver a distribuirlas en sus lugares.
Implementar una función acomodar que tome una lista con strings que representan el nombre de lista (UP o DOWN) y devuelva una lista con la
misma cantidad de elementos de cada uno de los posibles strings pero agrupadas, las de Lista UP al principio y las de lista DOWN al final.
No está permitido utilizar las funciones sort() y reverse()."""

"""problema acomodar(in s: seq<String>) : seq<String> {
  requiere: { Todos los elementos de s son o bien "DOWN" o bien "UP".}
  asegura: {|res| = |s|.}
  asegura: { Todos los elementos de res son o bien "DOWN" o bien "UP".}
  asegura: {res contiene la misma cantidad de elementos "UP" que s.}
  asegura: {res contiene todas las apariciones de "UP" antes de las apariciones de "DOWN".}
}
Ejemplo:
Dada s = ["DOWN", "UP", "DOWN", "DOWN", "UP"], se debería devolver res = ["UP", "UP", "DOWN", "DOWN", "DOWN"]."""

def acomodar(s: list[str]) -> list[str]:
  res: list[str]      = []
  lista_A: list[str]  = []
  lista_B: list[str]  = []
  for elem in s:
    if elem == 'UP':                     # Agrego los elementos UP a lista_A,
      lista_A.append(elem)
    elif elem == 'DOWN':                 # y los DOWN a lista_B
      lista_B.append(elem)
  for elem in lista_A:                   # Agrego a res la lista_A completa,
    res.append(elem)
  for elem in lista_B:                   # y luego la lista_B completa.
    res.append(elem)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 24 # Posición umbral
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Durante una noche en un restaurante pasan varios grupos de diversa cantidad de personas. Para llevar control de esto, el dueño va anotando
en su libreta cuánta gente entra y sale. Para hacerlo rápido decide que la mejor forma de llevarlo adelante es escribir un número al lado
del otro, usando números positivos para los grupos que entran y negativos para los que salen. Gracias a estas anotaciones el dueño es capaz
de hacer análisis del flujo de clientes. Por ejemplo, le interesa saber en qué momento de la noche superó una determinada cantidad de
clientes totales que ingresaron (sin importar cuántos hay en el momento en el local).
Implementar la función pos_umbral, que dada una secuencia de enteros (puede haber negativos) devuelve la posición en la cual se supera el
valor de umbral, teniendo en cuenta sólo los elementos positivos. Se debe devolver -1 si el umbral no se supera en ningún momento."""

"""problema pos_umbral (in s: seq<Z>, in u: Z) : Z {
  requiere: {u ≥ 0}
  asegura: {res=-1 si el umbral no se supera en ningún momento.}
  asegura: {Si el umbral se supera en algún momento, res es la primera posición tal que la sumatoria de los primeros res+1 elementos
            (considerando solo aquellos que son positivos) es estrictamente mayor que el umbral u.}
}
Ejemplo:
Dadas s = [1,-2,0,5,-7,3], y u = 5, se debería devolver res = 3."""

def pos_umbral(s: list[int], u: int) -> int:
  res: int    = 0
  suma: int   = 0
  for j in range(len(s)):                    # Por cada elemento de s,
    if s[j] > 0:                             # si es > 0,
      suma += s[j]                           # lo sumo.
      if suma > u:                           # Si la suma superó el umbral, listo!
        res = j                              # res = índice donde se superó el umbral.
        break
  if suma <= u:                              # Si no, res=-1
    res = -1
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 25 # Columnas repetidas
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Implementar la función columnas_repetidas, que dada una matriz no vacía de m columnas (con m par y m ≥ 2) devuelve True si las primeras m/2
columnas son iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias como matriz si todos los elementos de la primera
secuencia tienen la misma longitud."""

"""problema columnas_repetidas(in mat:seq<seq<Z>>) : Bool {
  requiere: {|mat| > 0}
  requiere: {todos los elementos de mat tienen igual longitud m, con m > 0 (los elementos de mat son secuencias).}
  requiere: {todos los elementos de mat tienen longitud par (la cantidad de columnas de la matriz es par).}
  asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a las últimas m/2 columnas.}
}
Ejemplo: Dada la matriz m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]], se debería devolver res = true.
TIP: para dividir un número entero x por 2 y obtener como resultado un número entero puede utilizarse la siguiente instrucción: int(x/2)."""

def columnas_repetidas(mat: list[list[int]]) -> bool:
  res: bool = True                                            # Asumimos que la matriz cumple lo pedido
  for col in range(int(len(mat[0])/2)):
    for fil in range(len(mat)):                               # Si algún elemento no es igual al elemento fila+(ancho/2) en una fila dada,
      if mat[fil][col] != mat[fil][col + int(len(mat[0])/2)]:
        res = False                                           # res = False y se termina el problema
        break
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 26 # Rugby de 4 naciones
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Desde hace más de 10 años existe en el mundo del rugby un torneo que disputan anualmente 4 selecciones del sur global (Argentina,
Australia, Nueva Zelanda y Sudáfrica). Este torneo se llama 'The rugby championship' o comunmente '4 naciones', ya que suplantó al viejo
'3 naciones'. Implementar la función cuenta_posiciones_por_nacion que dada la lista de naciones que compiten en el torneo, y el diccionario
que tiene los resultados de los torneos anuales en el formato año: posiciones_naciones, donde año es un número entero y posiciones_naciones
es una lista de strings con los nombres de las naciones, genere un diccionario de naciones: #posiciones, que para cada Nación devuelva la
lista de cuántas veces salió en esa posición."""

"""problema cuenta_posiciones_por_nacion(in naciones: seq<String>, in torneos: dict<Z,seq<String>>): dict<String,seq<Z>> {
  requiere: {naciones no tiene elementos repetidos.}
  requiere: {Los valores del diccionario torneos son permutaciones de la lista naciones (es decir, tienen exactamente los mismos elementos
             que naciones, en cualquier orden posible).}
  asegura: {res tiene como claves los elementos de naciones.}
  asegura: {El valor en res de una nación es una lista de |naciones| elementos que indica en la posición i cuántas veces salió esa nación
            en la i-ésima posición.}
}
Ejemplo: Dados:
  naciones= ["arg", "aus", "nz", "sud"]
  torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
debe devolver:
  res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}.
Tip: para crear una lista con tantos ceros como naciones se puede utilizar la siguiente sintaxis lista_ceros = [0]*len(naciones)."""

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int,list[str]]) -> dict[str,list[int]]:
  res: dict[str,list[int]] = {}
  for nacion in naciones:                               # Por cada nación de la lista naciones,
    clave_actual: str = nacion                          # genero una clave con su nombre,
    lista_nacion_actual: list[int] = [0]*len(naciones)  # y una lista vacía con la longitud de naciones.
    for clave in torneos.keys():                        # Por cada clave del diccionario torneos,
      for i in range(len(torneos[clave])):              # por cada índice de la lista de cada clave,
        if torneos[clave][i] == clave_actual:           # si el índice de la clave es la clave_actual
          lista_nacion_actual[i] += 1                   # suma 1 al valor que tenía (si era 0 -> 1, sino sigue sumando)
          break                                         # y listo! (no hace falta seguir contando)
    res[nacion] = lista_nacion_actual                   # Agrego lista a clave de res, y reseteo lista_nacion_actual=[0,...,0] y clave_actual
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 27 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema cantidad_parejas_que_suman(in s: seq⟨Z⟩, in n: Z) : Z {
  requiere: { }
  asegura: {res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j).}
}
Ejemplo: cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2."""

def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
  res: int = 0                                               # Inicializo res (res debe estar por la especificación)
  for j in range(len(s)):                                    # Hago un for sobre j,
    for i in range(len(s)):                                  # y sobre i, recorro absolutamente todos los casos, pero...
      if (i<j) and (s[i] + s[j] == n):                       # pido que se cumpla la condición i<j y s[i]+s[j]==n simultáneamente.
        res += 1                                             # Si esto pasa, una pareja se agregará a res
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 28 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, un método de
pago (los métodos de pago son strings conformados por letras minúsculas) y una cantidad de productos. La fila de clientes se representa
como una cola de String x String x Z, donde el primer elemento es el nombre del cliente, el segundo es el método de pago y el tercero es
la cantidad de productos. Implementar la función pasar_por_autoservicio:"""

"""problema pasar_por_autoservicio (inout clientes: cola⟨ String x String x Z ⟩) : String {
  requiere:{Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí.}
  requiere:{Las terceras componentes de clientes son números positivos.}
  requiere:{Existe al menos un elemento c dentro de la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15.}
  modifica: {clientes}
  asegura: {Sea c el primer elemento insertado en la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15, entonces res = c0.}
  asegura: {clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, en el mismo
            orden que en clientes@pre.}
}
Ejemplo: pasar_por_autoservicio(clientes) debe devolver "Bruno" (y quitar su tupla de la cola) si clientes es una cola en la cual se insertaron
(en orden) los siguientes elementos:
  ("Ana", "efectivo", 13)
  ("Juan", "qr", 22)
  ("Bruno", "tarjeta", 14)"""

def pasar_por_autoservicio(clientes: cola[tuple[str, str, int]]) -> str:
  res: str                                    = ''                            # Genero un string vacío
  lista_elementos: list[tuple[str, str, int]] = []                            # Genero una lista vacía
  cola_aux: cola[tuple[str, str, int]]        = cola()                        # Genero una cola auxiliar
  while not clientes.empty():                                                 # Mientras clientes no esté vacía,
    x: tuple[str, str, int] = clientes.get()                                  # obtengo (todos) sus elementos en x,
    lista_elementos.append(x)                                                 # los appendeo a una lista,
    cola_aux.put(x)                                                           # y los coloco en la cola aux.
  for i in range(len(lista_elementos)):                                       # Por cada i de lista, (busco ordenadamente, en orden FIFO)
    if res == '':                                                             # si no encontré al cliente para pasar por autoservicio
      if lista_elementos[i][1] != 'efectivo' and lista_elementos[i][2] <= 15: # nos fijamos si el i-ésimo cliente cumple las condiciones
        res = lista_elementos[i][0]                                           # si es así => res=1° componente de dicho elemento de lista
        if res != '':                                                         # si encontramos a alguien, entonces saqué un elemento de cola,
          cola_aux.get(lista_elementos[i])                                    # lo saco de cola aux, para saber que ahora hay 1 menos
      else:
        clientes.put(lista_elementos[i])                                      # Si no se cumplen las condiciones, lo pongo nuevamente
        cola_aux.get(lista_elementos[i])                                      # Le saco uno a cola aux para que su longitud sea la de clientes
    else:                                                                     # Si ya encontramos a alguien, listo! no buscamos mas
      if res != '' and not cola_aux.empty():                                  # Mientras haya gente en cola (y en cola_aux),
        clientes.put(lista_elementos[i])                                      # El resto de clientes se retornaran a cola 'clientes' en orden.
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 29 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""problema intercambiar_e_invertir_columnas(inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
  requiere: {Todas las filas de A tienen la misma longitud (estrictamente positiva).}
  requiere: {|A| > 0}
  requiere: {0 ≤ col1 < |A[0]|}
  requiere: {0 ≤ col2 < |A[0]|}
  requiere: {col1 ≠ col2}
  modifica: {A}
  asegura: {A tiene exactamente las mismas dimensiones que A@pre.}
  asegura: {A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ col1 y j ≠ col2.}
  asegura: {A[i][col1] = A@pre[|A|-1-i][col2] para todo i tal que 0 ≤ i < |A|.}
  asegura: {A[i][col2] = A@pre[|A|-1-i][col1] para todo i tal que 0 ≤ i < |A|.}
}
Ejemplo: Si m = [[1,2,3],[40,50,60],[-7,-8,-9]], luego de ejecutarse intercambiar_e_invertir_columnas(mat,1,2) debería ocurrir que print(m)
muestre [[1,-9,-8],[40,60,50],[-7,3,2]]."""

def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
  transponer(A)                                               # PASO 1: transpongo la matriz
  matriz_nueva = []                                           # PASO 2: Creo una matriz nueva, para poder invertir las filas deseadas
  for fila in range(len(A)):                                  # Ahora,
    if fila != col1 and fila != col2:                         # Si no es una fila deseada,
      matriz_nueva.append(A[fila])                            # se agrega la fila tal como está
    elif fila == col1:                                        # si es la fila deseada 1 (el parámetro col1),
      matriz_nueva = matriz_nueva + [invertir_lista(A[fila])] # invertimos.
    elif fila == col2:                                        # Con fila deseada 2 (el parámetro col2), IDEM
      matriz_nueva = matriz_nueva + [invertir_lista(A[fila])]
  A.clear()
  for fila in matriz_nueva:
    A.append(fila)
  permutar(A, col1, col2)                                     # PASO 3: permuto la matriz transpuesta e invertida
  transponer(A)                                               # PASO 4: vuelvo a transponer para obtener lo pedido.

#———————————————————————————————————————————————————————————————————————————————————————
# Funciones Auxiliares
#———————————————————————————————————————————————————————————————————————————————————————
# Genero una función auxiliar que permuta dos filas de una matriz (recibe la matriz, y las dos filas que desea permutar):
def permutar(A: list[list[int]], fila1: int, fila2: int) -> None:
  res: list[list[int]] = []
  for i in range(len(A)):                                         # Por cada fila de la matriz,
    if i != fila1 and i != fila2:                                 # si i no es fila1 o fila2,
      res.append(A[i])                                            # agrego la fila tal cual es.
    else:                                                         # Si no, 
      if i == fila1:                                              # si la fila es fila1, colocamos fila2 en res,
        res.append(A[fila2])
      elif i == fila2:                                            # o viceversa.
        res.append(A[fila1])
  A.clear()
  for fila in res:
    A.append(fila)

# Genero una función auxiliar para obtener las columnas de una matriz (transponer):
def transponer(A: list[list[int]]) -> None:
  res: list[list[int]] = []
  for j in range(len(A[0])):                # Para cada elemento de las filas,
    columna: list[int] = []
    for i in range(len(A)):                 # Para cada lista columna, agrego los valores por columna (recorro i)
      columna.append(A[i][j])
    res.append(columna)
  A.clear()
  for fila in res:
    A.append(fila)                          # Agrego a res las columnas como filas

# Genero una función auxiliar para invertir los elementos de una lista (en nuestro caso, filas o columnas de matriz)
def invertir_lista(lista: list[int]) -> list[int]:
  res: list[int]  = []                             # Genero una lista vacía
  p: pila[int] = pila()                            # Creo una pila vacía (uso una pila porque es un elemento LIFO, Last In First Out)
  for elem in lista:                               # Coloco en la pila los elementos de la lista
    p.put(elem)
  while not p.empty():                             # Coloco en res los elementos de la pila (ahora tendrán el orden invertido)
    res.append(p.get())
  return res
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 30 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Se realizaron dos censos en los cuales se le preguntó a cada persona en que localidad vive. Estos datos fueron almacenados en dos
diccionarios cuyas claves son los nombres de las personas, y sus valores las localidades en las cuales viven. Implementar la función
mantuvieron_residencia:"""

"""problema mantuvieron_residencia(in censo1: Diccionario⟨String,String⟩, in censo2: Diccionario⟨String,String⟩): Diccionario⟨String,Z⟩ {
  requiere: {Las claves de censo1 son las mismas que las claves de censo2.}
  asegura: {k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en censo1 como en censo2, este
            es igual a k.}
  asegura: {El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, es decir, que
            mantuvieron su residencia en la misma localidad entre ambos censos.}
}
Ejemplo: mantuvieron_residencia({'Juan':'Merlo','Ana':'Merlo'}, {'Juan':'Castelar','Ana':'Merlo'}) debe devolver {'Merlo':1}."""

def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
  res: dict[str,int] = {}
  for clave in censo1.keys():          # Como las claves de c1 y c2 son las mismas, uso c1 como referencia
    if censo1[clave] == censo2[clave]: # Si el valor de 'clave' es igual en c1 y c2,
      if censo1[clave] not in res:     # y ésta no es clave de res,
        res[censo1[clave]] = 1         # la creo en res por primera vez.
      else:
        res[censo1[clave]] += 1        # Si ya es clave, sumo uno a su valor.
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Preguntas Teóricas: Indique la opción correcta:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""La principal diferencia entre testing de caja blanca y de caja negra es que en testing de caja blanca tenemos acceso a:
  1. Al código fuente del programa que queremos testear.
  2. A la documentación del programa que queremos testear.
  3. Al Control Flow Graph (CFG) del programa que queremos testear."""

# La opción correcta es la 1.

"""¿Por qué en Paradigma Imperativo no existe la transparencia referencial?
  1. Utilizamos otro mecanismo de repetición de código, en lugar de recursión usamos la iteración (for, while, do while).
  2. Tenemos una nueva instrucción, la asignación, que nos permite cambiar el valor de una variable.
  3. El orden en que se ejecutan las instrucciones del programa es diferente."""

# La opción correcta es la 2.

"""Supongamos que un programa tiene un ciclo que itera sobre todos los elementos de una lista de tamaño n. Si el programa realiza una
operación constante dentro de ese ciclo (por ejemplo, incrementa en 1 cada valor de la lista), ¿cómo afecta el tamaño de la lista al número
de operaciones?
  1. Si la lista tiene más elementos, el número de operaciones aumentará.
  2. El número de operaciones no cambia con el tamaño de la lista.
  3. El número de operaciones depende del contenido de la lista, no del tamaño."""

# La opción correcta es la 1.

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————