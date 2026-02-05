
#============================================================================================================================================
# Práctica 7: Funciones sobre Listas (Tipado Complejo)
#============================================================================================================================================

# Parte 1: Recorrido y búsqueda de secuencias
#————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 # Codificar en python las siguientes funciones sobre secuencias:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
Nota: Cada problema puede tener más de una implementación. Probar utilizando distintas formas de recorrido sobre secuencias, y distintas
funciones de Python. No te conformes con una solución, recordar que siempre conviene consultar con tus docentes.
"""

"""1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
  requiere: {True}
  asegura: { (res = true) ↔ (existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
}"""

def pertenece(s: list[int], e: int) -> bool:
  res: bool = False
  for i in range(len(s)):
    if e == s[i]:
      res = True
  return res

"""2. problema divide_a_todos (in s:seq⟨Z⟩, in e: Z) : Bool {
  requiere: { e = 0 }
  asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
}
Nota: Implementar al menos de 3 formas distintas."""

def divide_a_todos(s: list[int], e: int) -> bool:
  res: bool = True
  for i in range(len(s)):
    if s[i] % e != 0:
      res = False
      break
  return res

"""3. problema suma_total (in s:seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: { res es la suma de todos los elementos de s }
}
Nota: no utilizar la función sum() nativa."""

def suma_total(s: list[int]) -> int:
  res: int = 0
  for i in range(len(s)):
    res += s[i]
  return res

"""4. problema maximo (in s:seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { res = al mayor de todos los números que aparece en s }
}
Nota: no utilizar la función max() nativa."""

def maximo(s: list[int]) -> int:
  res: int = s[0] # Caso Crítico!
  for i in range(1,len(s)):
    if s[i] > res:
      res = s[i]
  return res

"""5. problema minimo (in s:seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { res = al menor de todos los números que aparece en s }
}
Nota: no utilizar la función min() nativa."""

def minimo(s: list[int]) -> int:
  res: int = s[0] # Caso Crítico!
  for i in range(1,len(s)):
    if s[i] < res:
      res = s[i]
  return res

"""6. problema ordenados (in s:seq⟨Z⟩) : Bool {
  requiere: {True}
  asegura: { res = true ↔ (para todo i ∈ Z si 0 ≤ i < (|s|-1) → s[i] < s[i+1] }
}"""

def ordenados(s: list[int]) -> bool:
  res: bool = False
  if len(s) == 1: # Agrego un caso especial
    res = True
  for i in range(len(s)-1):
    if s[i] < s[i+1]:
      res = True
    else:
      res = False
      break
  return res

"""7. problema pos_maximo (in s:seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: {(Si |s| = 0, entonces res = -1; si no, res = al índice de la posición donde aparece el mayor elemento de s (si hay varios es la
            primera aparición) }
}"""

def pos_maximo(s: list[int]) -> int:
  res: int = 0
  if len(s) == 0:
    res = -1
  for i in range(len(s)):
    if s[i] > s[res]:
      res = i
  return res

"""8. problema pos_minimo (in s:seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: {(Si |s| = 0, entonces res = -1; si no, res = al índice de la posición donde aparece el menor elemento de s (si hay varios es la
            última aparición) }
}"""

def pos_minimo(s: list[int]) -> int:
  res: int = 0
  if len(s) == 0:
    res = -1
  for i in range(len(s)):
    if s[i] < s[res]:
      res = i
  return res

"""9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7.
Ejemplo:[“termo”, “gato”, “tener”, “jirafas”], devuelve falso.

problema long_mayor_a_siete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
  requiere: {True}
  asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s|-1)) y (|s[i]| > 7) }
}"""

def long_mayor_a_siete(s: list[list[str]]) -> bool:
  res: bool = False
  for palabra in s:
    if len(palabra) > 7:
      res = True
  return res

"""10. Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso contrario. Las
cadenas de texto vacías o con 1 sólo elemento son palíndromo.

problema es_palindroma (in s:seq⟨Char⟩) : Bool {
  requiere: {True}
  asegura: { (res = true) ↔ (s es igual a su reverso) }
}"""

def es_palindroma(s: list[str]) -> bool:
  res: bool = False
  if s == s[::-1]: # Los casos especiales ya están cubiertos en el if.
    res = True
  return res

"""11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 números iguales consecutivos, en cualquier posición y False en caso contrario.

problema iguales_consecutivos (in s:seq⟨Z⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) ↔ (existe i,j,k ∈ Z tal que (0 ≤ i,j,k < (|s| - 1)) y (i + 2 = j + 1 = k) y (s[i] = s[j] = s[k]))}
}"""

def iguales_consecutivos(s: list[int]) -> bool:
  res: bool = False
  for i in range(0,len(s)-2):
    if s[i] == s[i+1] == s[i+2]:
      res = True
  return res

"""12. Recorrer una palabra en formato string y devolver True si ésta tiene al menos 3 vocales distintas y False en caso contrario.

problema vocales_distintas (in s:seq⟨Char⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) ↔ (existe i,j,k ∈ Z tal que (0≤i,j,k<(|s|-1)) y (s[i]=s[j]=s[k]) y (s[i],s[j],s[k] ∈ {‘a‘,‘e‘,‘i‘,‘o‘,‘u‘}))}
}"""

def vocales_distintas(s: list[str]) -> bool:
  res: bool = False
  vocales: list[str] = ['a','e','i','o','u']
  lista: list[str] = []
  for letra in s:
    if letra in vocales and letra not in lista:
      lista.append(letra)
    if len(lista) == 3:
      res = True
      break
  return res

"""13. Recorrer una seq⟨Z⟩ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos subsecuencias de igual
longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía.

problema pos_secuencia_ordenada_mas_larga (in s:seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { (res = i) ↔ (existe i,j ∈ Z tal que (0 ≤ i,j < (|s|-1)) y i ≤ j y (para todo k tal que i ≤ k < j → s[k] ≤ s[k +1]) y j-i+1 es
  máximo e i es el mínimo valor que lo cumple) }
}"""

def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
  res: int = 0
  secuencia_mas_larga: list[int] = []
  secuencia_actual: list[int] = []
  indice_actual: int = 0
  for i in range(0,len(s)):
    if (i == len(s)-1): # Caso especial para el último elemento de la lista.
      if(s[i-1] <= s[i]):
        secuencia_actual.append(s[i])
        if(len(secuencia_actual) > len(secuencia_mas_larga)):
          res = indice_actual
          secuencia_mas_larga = secuencia_actual
    else:
      if s[i] <= s[i+1]: # Si están ordenados,
        if (len(secuencia_actual) == 0):
          indice_actual = i
        secuencia_actual.append(s[i]) # Guardamos el valor iésimo.
      else:
        secuencia_actual.append(s[i])
        if(len(secuencia_actual) > len(secuencia_mas_larga)):
          res = indice_actual
          secuencia_mas_larga = secuencia_actual
        secuencia_actual = [] # Reseteamos el valor de la secuencia actua a 0.
  return res

"""14. Cantidad de dígitos impares.
problema cantidad_digitos_impares (in numeros:seq⟨Z⟩) : Z {
  requiere: { Todos los elementos de números son mayores o iguales a 0 }
  asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
}
Por ejemplo, si la lista de números es [57,2383,812,246], entonces el resultado esperado sería 5 (los dígitos impares son 5,7,3,3,1)."""

def cantidad_digitos_impares(numeros: list[int]) -> int:
  res: int = 0
  for elemento in numeros:
    for digito in str(elemento):
      if int(digito) % 2 == 1:
        res += 1
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 2: Recorrido: fitrando, modificando y procesando secuencias
#——————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 # Implementar las siguientes funciones sobre secuencias pasadas por parámetro:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. problema ceros_en_posiciones_pares (inout s:seq⟨Z⟩) {
  requiere: {True}
  modifica: { s }
  asegura: {(|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i es par, entonces s[i] = 0)}
}"""

def ceros_en_posiciones_pares(s: list[int]) -> None:
  for i in range(len(s)):
    if i % 2 == 0:
      s[i] = 0

"""2. problema ceros_en_posiciones_pares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {True}
  asegura: {(|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es par, entonces res[i] = 0)}
}"""

def ceros_en_posiciones_pares2(s: list[int]) -> list[int]:
  res: list[int] = []
  for i in range(len(s)):
    if i % 2 == 0:
      res.append(0)
    else:
      res.append(s[i])
  return res

"""3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios, sino que borra la
vocal y concatena a continuación.
problema sin_vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {True}
  asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}
Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena original, conservando el
orden de los elementos restantes."""

def sin_vocales(s: list[str]) -> list[str]:
  res: list[str] = []                        # res es una seq⟨Char⟩ (lista de strings). Comenzamos a la lista vacía.
  vocales: list[str] = ['a','e','i','o','u'] # Hacemos una lista de vocales
  for i in range(len(s)):
    if s[i] in vocales:                      # Si s[i] es una vocal, no hacemos nada
      pass
    else:
      res.append(s[i])                       # Sino, generamos la nueva lista res
  return res                                 # s no se ve modificada ! -> se cumple la especificación.

"""4. problema reemplaza_vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {True}
  asegura: { |res| = |s| }
  asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
                                                (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i]))}
}"""

def reemplaza_vocales(s: list[str]) -> list[str]:
  res: list[str] = []
  vocales: list[str] = ['a','e','i','o','u']
  for i in range(len(s)):
    if s[i] in vocales:
      res.append('-')
    else:
      res.append(s[i])
  return res

"""5. problema da_vuelta_str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {True}
  asegura: { |res| = |s| }
  asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s|-i-1] }
}"""

def da_vuelta_str(s: list[str]) -> list[str]:
  res: list[str] = []
  for i in range(len(s)-1,-1,-1):
    res.append(s[i])
  return res

"""6. problema eliminar_repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: {True}
  asegura: {(|res|≤|s|) ∧ (para todo i ∈ Z si 0≤i<|s| → pertenece(s[i],res)) ∧ (para todo i,j ∈ Z si (0≤i,j<|res| ∧ i=j) → res[i]=res[j])}
}"""

def eliminar_repetidos(s: list[str]) -> list[str]:
  res: list[str] = []
  lista: list[str] = []
  for i in range(len(s)):
    if s[i] in s and s[i] not in lista:
      res.append(s[i])
      lista.append(s[i])
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Implementar una función para conocer el estado de aprobación de una materia a partir de las notas obtenidas por un/a alumno/a cumpliendo
# con la siguiente especificación:

"""problema resultado_materia (in notas: seq⟨Z⟩) : Z {
  requiere: { |notas| > 0 }
  requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
  asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
  asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio está entre 4 (inclusive) y 7 }
  asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}"""

def promedio(notas: list[int]) -> float:
  return round((suma_total(notas)/len(notas)), 2)

def resultado_materia(notas: list[int]) -> int:
  res: int = 0
  for i in range(len(notas)):
    if notas[i] < 4 or promedio(notas) < 4:
      res = 3
      break
    elif promedio(notas) < 7:
      res = 2
    else: # este caso ocurrirá solo cuando promedio(notas) >= 7
      res = 1
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el saldo
inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de dinero y “R” para retiro de dinero, y
además el monto de cada operación. Por ejemplo, si la lista de tuplas es [(‘‘I’’, 2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces
el saldo actual es 1280."""

"""problema saldo_actual (in movimientos: seq⟨Char x Z⟩) : Z {
    requiere: { Para todo i ∈ Z si 0 ≤ i < |movimientos| → movimientos[i]0 ∈ {“I”,“R”} y movimientos[i]1 > 0 }
    asegura: { res = Sum{i}{ingresos}{ movimientos[i]_1 } - Sum{i}{retiros}{ movimientos[i]_1 } }
}"""

def saldo_actual(movimientos: list[tuple[str,int]]) -> int:
  res: int = 0
  for i in range(len(movimientos)):
    if movimientos[i][0] == 'I': # Ingresa dinero => sumo
      res += movimientos[i][1]
    if movimientos[i][0] == 'R': # Retiro dinero => resto
      res -= movimientos[i][1]
  return res
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 3: Matrices
#——————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 # Analizando parámetros in y out vs. resultado:
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. problema pertenece_a_cada_uno_version_1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
  requiere: {True}
  asegura: { |res| ≥ |s| }
  asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
}
Nota: Reutilizar la función pertenece() implementada previamente para listas."""

"""El problema propone lo siguiente:
  - Recibo s = [ [1,2], [9,4] ]    # s es una lista de listas de enteros (matriz)
  - Recibo e = 2                   # e es un número entero
  - Recibo res = [ True, True ]    # res es una lista de boolianos        ->      se modifica res al implementar la función

  Si el valor e, está incluido en la lista i-ésima de s (pertenece a s[i]), para cada i en s, entonces res[i] = True
  (la posición i-ésima de res es True).
"""

def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]) -> None:
  for i in range(len(s)):
    if pertenece(s[i], e) == True:
      res[i] = True # Se cumple la especificación, y funciona para |res| >= |s|

"""2. problema pertenece_a_cada_uno_version_2 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
  requiere: {True}
  asegura: { |res| = |s| }
  asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
}"""

# Ahora, res debe ser recortada si inicialmente |res| > |s|
def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]) -> None:
  lista: list[bool] = []
  for i in range(len(s)):
    if pertenece(s[i], e) == True:
      res[i] = True
      lista.append(True)
    else:
      lista.append(False)
  res[:] = lista # [:] sirve para modificar res fuera de la función

"""3. problema pertenece_a_cada_uno_version_3 (in s:seq⟨seq⟨Z⟩⟩, in e:Z) : seq⟨Bool⟩ {
  requiere: {True}
  asegura: { |res| = |s| }
  asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
}"""

def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int) -> list[bool]:
  res: list[bool] = [] # Ahora debo crear a res
  for i in range(len(s)):
    if pertenece(s[i], e) == True:
      res.append(True)
    else:
      res.append(False)
  return res

"""4. Pensar: ¿Cómo cambia este problema respecto de la versión 1? Pensar en relación de fuerza entre: implementación en
Python y las especificaciones. ¿Se puede usar la implementación del ejercicio 2 para la especificación del 1? ¿Se puede
usar la implementación del ejercicio 1 para la especificación del 2? Justificar su respuesta."""

# La implementación del ejercicio 2 no puede usarse para el ejercicio 1 porque pertenece_a_cada_uno_version_2 corta la lista res, siempre que
# res, sea originalmente mayor a la cantidad de listas que contiene s que se pasó como parámetro de la función.
# La implementación del ejercicio 1 para la especificación del 2 tampoco puede utilizarse para la especificación del ejercicio 2, porque la
# especificación 2 asegura que |res|=|s|, pero si res > s inicialmente, la implementación de 1 no recorta a la lista, por lo que no se cumple
# el asegura.

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 # Implementar las siguientes funciones sobre matrices (secuencias de secuencias):
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""1. problema es_matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
  requiere: {True}
  asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
}"""

def es_matriz(s: list[list[int]]) -> bool: # Vale para matrices cuadradas o no cuadradas!
  res: bool = False
  for i in range(len(s)):
    if len(s[i]) == len(s[0]):
      res = True
    else:
      res = False
      break
  return res

"""2. problema filas_ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
  requiere: { esMatriz(m) }
  asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(m[i])) }
}
Nota: Reutilizar la función ordenados() implementada previamente para listas."""

def filas_ordenadas(m: list[list[int]], res: list[bool]) -> None:
  for i in range(len(res)):
    if ordenados(m[i]) == True:
      res[i] = True

"""3. problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
  requiere: { esMatriz(m) }
  requiere: { c < |m[0]| }
  requiere: { c ≥ 0 }
  asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en el mismo orden que aparecen }
}"""

def columna(m: list[list[int]], c: int) -> list[int]:
  res: list[int] = []
  for i in range(len(m)):
    res.append(m[i][c])
  return res

"""4. problema columnas_ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
  requiere: { esMatriz(m) }
  asegura: { Para toda columna c ∈ m → (res[c] = true ↔ ordenados(columna(m,c))) }
}
Nota: Reutilizar la función ordenados() implementada previamente para listas."""

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
  res: list[bool] = []
  for i in range(len(m[0])): # elijo a la primer fila ([0]) como referencia, solo por elegir (las filas tienen la misma longitud)
    if ordenados(columna(m,i)) == True:
      res.append(True)
    else:
      res.append(False)
  return res

"""5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
  requiere: { esMatriz(m) }
  asegura: { Devuelve mt (o sea la matriz transpuesta) }
}
Nota: Usar columna() para ir obteniendo todas las columnas de la matriz."""

def transponer(m: list[list[int]]) -> list[list[int]]:
  mt: list[list[int]] = [] # esto representa una matriz vacía
  for i in range(len(m[0])): # elijo la primera fila ([0])
    mt.append(columna(m,i))
  return mt

"""6. Ta-Te-Ti Tradicional:
problema quien_gana_tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
  requiere: { esMatriz(m) }
  requiere: { |m| = 3 }
  requiere: { |m[0]| = 3 }
  requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
  requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
  requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
  requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
  requiere: { Para todo i,j ∈ {0,1,2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = ” ”}
  asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
  asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
  asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
}"""

def quien_gana_tateti(m: list[list[str]]) -> int:
  res: int = 2
  dim: list[int] = [0,1,2] # dimensión = 3x3
  circ: list[str] = ['O','O','O']
  cruz: list[str] = ['X','X','X']
  for i in dim:
    if m[i] == circ or columna(m,i) == circ or [m[0][0],m[1][1],m[2][2]] == circ or [m[0][2],m[1][1],m[2][0]] == circ:
      res = 0
      break
    if m[i] == cruz or columna(m,i) == cruz or [m[0][0],m[1][1],m[2][2]] == cruz or [m[0][2],m[1][1],m[2][0]] == cruz:
      res = 1
      break
  return res

"""7.Opcional: Implementar una función que tome un entero d y otro p y eleve una matriz cuadrada de tamaño d con valores generados al azar a
la potencia p. Es decir, multiplique a la matriz generada al azar por sí misma p veces. Realizar experimentos con diferentes valores de d.
¿Qué pasa con valores muy grandes?

problema exponenciacion_matriz (in d:Z, in p:Z) : seq⟨seq⟨Z⟩⟩ {
  requiere: { d,p ∈ Z y d,p > 0 }
  asegura: { esMatriz(m) y |columna(m,0)| = d y |columna(transponer(m),0)| = d y res = Prod_{i=1}^p (m) }
}

Nota 1. Recordá que en la multiplicación de una matriz cuadrada de dimensión d por si misma cada posición se calcula como:
  res[i][j] = Sum_{k=0}^{d-1} (m[i][k] x m[k][j])

Nota 2. Para generar una matriz cuadrada de dimensión d con valores aleatorios hay muchas opciones de implementación, analizar las siguientes
usando la biblioteca numpy (ver recuadro):

Opción 1:
  import numpy as np
  m = np.random.random((d, d))
  \footnote{https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random}

Opción 2:
  import numpy as np
  m = np.random.randint(i,f, (d, d)) \footnote{https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html}

Para poder importar la biblioteca numpy es necesario instalarla primero. Y para ello es necesario tener instalado un gestor de paquetes, por
ejemplo pip3 (Ubuntu: sudo apt install pip3. Windows: se instala junto con Python). Una vez instalado pip3 se ejecuta pip3 install numpy."""
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Parte 4: Programas Interactivos Usando Secuencias
#——————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 7 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""Vamos a elaborar programas interactivos (usando la función input()) que nos permita solicitar al usuario información cuando usamos las
funciones.
\footnote{https://docs.python.org/es/3/library/functions.html?highlight=input#input}"""
"""1. Implementar una función para construir una lista con los nombres de mis estudiantes. La función solicitará al usuario los nombres hasta
que ingrese la palabra “listo”, o vacío (el usuario aprieta ENTER sin escribir nada). Devuelve la lista con todos los nombres ingresados."""

def nombres_estudiantes() -> list[str]:
  res: list[str] = []
  while True:
    nombre = input("Nombre del estudiante (presione ENTER o escriba 'listo' al terminar): ")
    if nombre == '' or nombre == 'listo':
      break
    res.append(nombre)
  return res

"""2. Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE). El usuario debe
seleccionar en cada paso si quiere:
  “C” = Cargar créditos,
  “D” = Descontar créditos,
  “X” = Finalizar la simulación (terminar el programa).
En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a asumir que el monedero
comienza en cero. Para guardar la información grabaremos en el historial tuplas que representen los casos de cargar (“C”, monto a cargar) y
descontar crédito (“D”, monto a descontar)."""

def historial_monedero() -> list[tuple[str,int]]:
  res: list[tuple[str,int]] = []
  while True:
    operation: str = input("Ingrese la operación: \n 'C': Cargar créditos. \n 'D': Descontar créditos. \n 'X': Finalizar simulación.")
    if operation == 'C':
      carga: int = input('Ingrese el monto que desea agregar: ')
      res.append(('C',carga))
    elif operation == 'D':
      descarga: int = input('Ingrese el monto que desea descontar: ')
      res.append(('D',descarga))
    elif operation == 'X':
      break
  return res

"""3. Analizar la fortaleza de una contraseña. Solicitar al usuario que ingrese un texto que será su contraseña. Armar una función que tenga
de parámetro de entrada un string con la contraseña a analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA.
Nota: en python la “ñ/ñ” es considerado un carácter especial y no se comporta como cualquier otra letra. String es seq⟨Char⟩. Consejo: para ver
si una letra es mayúscula se puede ver si está ordenada entre A y Z.

La contraseña será VERDE si:
  a) la longitud es mayor a 8 caracteres
  b) tiene al menos 1 letra minúscula.
  c) tiene al menos 1 letra mayúscula.
  d) tiene al menos 1 dígito numérico (0..9)
  La contraseña será ROJA si:
  a) la longitud es menor a 5 caracteres.
  En caso contrario será AMARILLA."""

def fortaleza_contraseña() -> str:
  minus = 'abcdefghijklmnñopqrstuvwxyz'
  mayus = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
  num = '0123456789'
  spec = "°´'¨|¡!¿?#$%&()[]{=+-*/.,:;_}"
  
  while True:
    contraseña: str = input("Ingrese una contraseña: ")

    cant_minus, cant_mayus, cant_num, cant_spec = False
    for i in minus:
      if i in contraseña:
        cant_minus = True
        break
    for j in mayus:
      if j in contraseña:
        cant_mayus = True
        break
    for k in num:
      if k in contraseña:
        cant_num = True
        break
    for l in spec:
      if l in contraseña:
        cant_spec = True
        break
    if len(contraseña) > 8 and cant_minus and cant_mayus and (cant_num or cant_spec):
      fortaleza: str = 'VERDE'
      break
    elif len(contraseña) < 5:
      fortaleza: str = 'ROJA'
      break
    else:
      fortaleza: str = 'AMARILLA'
      break
  return fortaleza

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————