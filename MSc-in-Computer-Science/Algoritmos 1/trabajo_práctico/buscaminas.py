
#============================================================================================================================================
# Algoritmos y Estructuras de Datos I | Trabajo Práctico
#============================================================================================================================================

import os
import random
from typing import Any

# Constantes para dibujar
BOMBA: str   = chr(128163)    # Símbolo de una mina
BANDERA: str = chr(127987)    # Símbolo de bandera blanca
VACIO: str   = ' '            # Símbolo vacio inicial
EstadoJuego  = dict[str, Any] # Tipo de alias para el estado del juego

def existe_archivo(ruta_directorio: str, nombre_archivo: str) -> bool:
  """
  Recibe dos strings, el primero de ellos representa la ruta del directorio dado, y el segundo el nombre del archivo, y devuelve un booleano
  que indica si es True ó False que dicho archivo existe en el directorio especificado.
  """
  return os.path.exists(os.path.join(ruta_directorio, nombre_archivo))

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 1 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def colocar_minas(filas: int, columnas: int, minas: int) -> list[list[int]]:
  """
  Devuelve una matriz que contiene ceros (0) o menos unos (-1), donde -1 representa una mina, y éstas se encuentran distribuidas
  aleatoriamente en la matriz.
  Args:
    filas: int.  cantidad de filas de la matriz.
    columnas: int. cantidad de columnas de la matriz.
    minas: int. cantidad de minas a colocar en la matriz.
  Returns:
    list[list[int]]: Matriz de fila*columnas con minas colocadas.
  """
  res: list[list[int]] = crear_matriz(filas, columnas)
  total_casillas = filas * columnas
  posiciones_posibles = list(range(total_casillas)) # Se crea una lista de todas las posiciones posibles para una mina (en orden de aparición).
  posiciones_elegidas = []
  while len(posiciones_elegidas) < minas:           # Elige una posicion al azar. Si no habia sido elegida, la guarda en una lista.
    posicion_elegida = random.choices(posiciones_posibles, k=1)[0]  
    if posicion_elegida not in posiciones_elegidas:
      posiciones_elegidas.append(posicion_elegida)
  for pos in posiciones_elegidas:                   # Se encuentra a que fila y columna pertenece la posicion y lo cambia por una mina.
    fila = pos // columnas
    columna = pos % columnas
    res[fila][columna] = -1
  return res

def es_matriz(t: list[list[int]]) -> bool:
  """
  Verifica si la variable t es una matriz, cuadrada o no.
  Args:
    t: list[list[int]].  variable a verificar si es una matriz.
  Returns:
    bool: respuesta booleana a si es una matriz.
  """
  if (not t) or (not t[0]):      # Casos especiales: t=[] ó t=[[]]
    return False
  for fila in t:
    if len(fila) != len(t[0]): # Elejimos como referencia la fila t[0] (podría ser cualquiera)
      return False
  return True

#———————————————————————————————————————————————————————————————————————————————————————
# Función Auxiliar #
#———————————————————————————————————————————————————————————————————————————————————————
def crear_matriz(filas: int, columnas: int) -> list[list[int]]:
  """
  Crea matriz con dimensiones filas*columnas.
  Args:
    filas: int. cantidad de filas que va a tener la matriz.
    columnas: int. cantidad de columnas que va a tener la matriz.
  Returns:
    list[list[int]]: Matriz con todas las casillas en 0.
  """
  matriz: list[list[int]] = []
  for i in range(0,filas):
    fila: list = []
    for j in range(0,columnas):
      fila.append(0)
    matriz.append(fila)
  return matriz
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 2 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def calcular_numeros(tablero: list[list[int]]) -> None:
  """
  Actualiza los valores de los elementos que son 0 (los -1 quedan como estaban) por un número natural menor o igual a 8 que representa la
  cantidad de minas (-1) que rodean a dicho elemento de la posición (i,j).
  Args:
    tablero: list[list[int]].  Matriz que contiene solo ceros (0) o menos unos (-1) (donde los -1 representan representan minas).
  """
  filas: int    = len(tablero)
  columnas: int = len(tablero[0])
  for i in range(0, filas):
    for j in range(0, columnas):
      if tablero[i][j] != -1:
        tablero[i][j] = minas_adyacentes(tablero, (i,j))

#———————————————————————————————————————————————————————————————————————————————————————
# Función Auxiliar #
#———————————————————————————————————————————————————————————————————————————————————————
def minas_adyacentes(tablero: list[list[int]], posicion: tuple[int,int]) -> int:
  """
  Cuenta la cantidad de minas adyacentes a una posición dada en el tablero.
  Args:
    tablero: int. Matriz de enteros, donde -1 representa una mina, y un 0 una posicion sin mina.
    posicion: int. casilla dada como coordenadas en la que se calcula la cantidad de minas adyacentes.
  Returns:
    int: cantidad de minas adyacentes al casillero dado.
  """
  cant_minas_adyacentes: int = 0
  pos_fila: int              = posicion[0]
  pos_columna: int           = posicion[1]
  filas: int                 = len(tablero)
  columnas: int              = len(tablero[0])
  for i in range(pos_fila - 1, pos_fila + 2):
    for j in range(pos_columna - 1, pos_columna + 2):
      if 0 <= i < filas and 0 <= j < columnas: # Condicion para que no ocurra IndexError, por ej., la posición de una esquina.
        if tablero[i][j] == -1:
          cant_minas_adyacentes += 1
  return cant_minas_adyacentes
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 3 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def crear_juego(filas: int, columnas: int, minas: int) -> EstadoJuego:
  """
  Crea un juego, generando el tablero, colocando las minas, crea el tablero visible al jugador, y si el juego ya terminó.
  Args:
    filas: int. cantidad de filas que se quiera que tenga el tablero.
    columnas: int.  cantidad de columnas que se quiere que tenga el tablero.
    minas: int.  cantidad de minas que habrá en el tablero.
  Returns:
    EstadoJuego: diccionario con las siguientes claves:
      filas: int. Cantidad de filas del tablero.
      columnas: int. Cantidad de columnas del tablero.
      minas: int. Cantidad total de minas colocadas.
      tablero: list[list[int]]. Matriz con minas (-1) y números que indican minas adyacentes.
      tablero_visible: list[list[str]]. Matriz con los valores visibles para el jugador.
      juego_terminado: bool. Indica si el juego ha finalizado (True) o no (False).
  """
  res: dict[str,Any]               = {}
  tablero: list[list[int]]         = colocar_minas(filas, columnas, minas)
  calcular_numeros(tablero)        # Actualizamos los valores de tablero
  tablero_visible: list[list[str]] = vaciar_matriz(tablero)
  res['filas']                     = filas
  res['columnas']                  = columnas
  res['minas']                     = minas
  res['tablero']                   = tablero
  res['tablero_visible']           = tablero_visible
  res['juego_terminado']           = False
  return res

def estructura_y_tipos_validos(estado: EstadoJuego) -> bool:
  """
  Verifica que la estructura del estado del juego y los tipos de datos sean válidos.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
  Returns:
    bool. True si el estado tiene la estructura correcta y las matrices son validas. False en caso contrario. 
  """
  res: bool = True
  if ( # Imponemos las condiciones de los asegura:
    len(estado)               != 6 or
    len(estado['tablero'])    != estado['filas'] or
    len(estado['tablero'][0]) != estado['columnas'] or
    son_matriz_y_misma_dimension(estado['tablero'], estado['tablero_visible']) == False
  ):
    res = False
  for fila in estado['tablero']:
    for elem in fila:
      if elem not in range(-1,9):
        res = False
  for fila in estado['tablero_visible']:
    for elem in fila:
      if elem not in [VACIO, BOMBA, BANDERA, '0', '1', '2', '3', '4', '5', '6', '7', '8']:
        res = False
  return res

def son_matriz_y_misma_dimension(t1: list[list[int]], t2: list[list[int]]) -> bool:
  """
  Prueba que tanto t1 como t2 son matrices (ya sea cuadradas o no cuadradas), y si además éstas tienen la misma dimensión n x m (fila*columna).
  Args:
    t1: list[list[int]]. Primera matriz a comparar.
    t2: list[list[int]]. Segunda matriz a comparar.
  Returns:
    bool: True si son matrices y tienen misma cantidad de filas. False si una de las dos no se cumple.
  """
  res: bool = False
  if es_matriz(t1) == False or es_matriz(t2) == False:
    res = False
  else:                                                     # Es_matriz ya chequea que len de todas las filas sean iguales => solo veo fila 0.
    if (len(t1) == len(t2)) and (len(t1[0]) == len(t2[0])):
      res = True
  return res

def todas_celdas_seguras_descubiertas(tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:
  """
  Prueba si todas las posiciones (celdas) donde no hay una bomba (-1) fueron o no descubiertas.
  Args:
    tablero: list[list[int]]. tablero con minas (-1) y casillas con numeros del 0 al 8.
    tablero_visible: list[list[int]]. tablero con espacios vacios, banderas o minas.
  Returns:
    bool: True si todas las celdas sin una mina fueron descubiertas. False en caso contrario.
  """
  res: bool = True
  for i in range(0, len(tablero)):        # len(tablero) = filas!
    for j in range(0, len(tablero[0])): # Columnas
      if ((tablero[i][j] != -1) and (tablero_visible[i][j] in [VACIO,BANDERA])):
        res = False                 # Tan pronto como una condición no se cumpla -> res=False y break!
        break
      if ((tablero[i][j] == -1) and (tablero_visible[i][j] == str(tablero[i][j]))):
        res = False                 # Ídem
        break
  return res

#———————————————————————————————————————————————————————————————————————————————————————
# Función Auxiliar #
#———————————————————————————————————————————————————————————————————————————————————————
def vaciar_matriz(tablero: list[list[int]]) -> list[list[str]]:
  """
  Devuelva una matriz del mismo tamaño que el de la matriz de entrada, pero todos sus elementos son VACIO.
  Args:
    tablero: list[list[int]]. tablero con minas (-1) y casillas con numeros del 0 al 8.
  Returns:
    list[list[str]]: matriz con elementos ' '.
  """
  tablero_visible: list[list[str]] = []
  filas_tablero: int               = len(tablero)
  columnas_tablero: int            = len(tablero[0])
  for i in range(filas_tablero):
    fila: list[str] = []
    for j in range(columnas_tablero):
      fila.append(VACIO)
    tablero_visible.append(fila)
  return tablero_visible
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 4 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def obtener_estado_tablero_visible(estado: EstadoJuego) -> list[list[str]]:
  """
  Crea una copia del tablero visible.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
  Returns:
    list[list[str]]: Copia de la clave ["tablero_visible"] de la variable de entrada.
  """
  res: list[list[str]]              = [] # Copia del tablero
  tablero_original: list[list[str]] = estado['tablero_visible']
  for fila in tablero_original:
    fila_copia: list[str] = []
    for elem in fila:
      fila_copia.append(elem)
    res.append(fila_copia)
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 5 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def marcar_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
  """
  Actualiza (Si el valor es VACIO o BANDERA) el valor de la posición (fila,columna) de la clave 'tablero_visible'. Si dicha posición era
  VACIO, la cambia a BANDERA, y si era BANDERA,
  la cambia a VACIO.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    fila: int. Fila donde esta la celda a marcar.
    columna: int. Columna donde esta la celda a marcar.
  """
  if estado['tablero_visible'][fila][columna] == VACIO:
    estado['tablero_visible'][fila][columna] = BANDERA
  elif estado['tablero_visible'][fila][columna] == BANDERA:
    estado['tablero_visible'][fila][columna] = VACIO

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 6 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def descubrir_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
  """
  Si la posición (fila,columna) es una mina se termina el juego y se muestra el tablero; sino, se revela la casilla seleccionada. Si la
  casilla seleccionada es 0, se descubren todas las casillas adyacentes que tambien contengan cero, y de estas casillas descubiertas, lo mismo.
  Si se encontró una mina o se ganó el juego, el juego termina y estado['juego_terminado'] = True.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    fila: int. Fila donde esta la celda a descubrir.
    columna: int. Columna donde esta la celda a descubrir.
  """
  if estado['juego_terminado']:                                            # Si se encontró una mina o ganó el juego, se terminó.
    return
  tablero_visible: list[list[str]] = estado['tablero_visible']
  tablero: list[list[int]]         = estado['tablero']
  if tablero[fila][columna] == -1:                                         # Si es una mina se terminó el juego => muestro posiciones de todas.
    estado['juego_terminado'] = True
    tablero_visible = obtener_minas_tablero(tablero, tablero_visible)
  else:
    caminos: list[list[tuple[int,int]]] = caminos_descubiertos(tablero, tablero_visible, fila, columna)
    for camino in caminos:
      for filas, columnas in camino:
        if tablero_visible[filas][columnas] != BANDERA:
          tablero_visible[filas][columnas] = str(tablero[filas][columnas]) # Revela las casillas validas que no sean banderas.
    if todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']):
      estado['juego_terminado'] = True                                     # Si todas las casillas fueron reveladas, el juego termina.

def caminos_descubiertos(tablero: list[list[int]], tablero_visible: list[list[str]], f: int, c: int) -> list[list[tuple[int,int]]]:
  """
  Devuelve todos los caminos posibles que se descubren desde la celda seleccionada segùn las reglas del juego.
  Args:
    tablero: list[list[int]]. tablero con minas (-1) y casillas con numeros del 0 al 8.
    tablero_visible: list[list[str]]. tablero con espacios vacios, banderas o minas.
    f: int. Fila de la posicion donde se descubrio la primera celda.
    c: int. Columna de la posicion donde se descubrio la primera celda.
  Returns:
    list[list[tuple[int, int]]]: Lista de listas de tuplas, donde cada lista de tuplas representa un camino a descubrir.
  """
  res: list[list[tuple[int,int]]]     = []
  visitados: list[tuple[int,int]]     = [] # Esta lista irá agregando elementos con buscar_camino. En cada paso se vacía.
  camino_actual: list[tuple[int,int]] = []
  buscar_camino(tablero, tablero_visible, f, c, camino_actual, res, visitados)
  return res

#———————————————————————————————————————————————————————————————————————————————————————
# Funciones Auxiliares #
#———————————————————————————————————————————————————————————————————————————————————————
def obtener_minas_tablero(tablero_real: list[list[int]], tablero_visible: list[list[str]]) -> list[list[str]]:
  """
  Cambia todos los VACIO o BANDER del tablero_visible por BOMBA.
  Args:
    tablero_real: list[list[int]]. tablero con minas (-1) y casillas con numeros del 0 al 8.
    tablero_visible: list[list[int]]. tablero con espacios vacios, banderas o minas.
  Returns:
    list[list[str]]: Se devuelve tablero_visible, pero en todas las celdas donde en tablero_real habia un -1, en tablero_visible hay BOMBA.
  """
  for i in range(len(tablero_real)):
    for j in range(len(tablero_real[0])): # Recorremos ahora las posiciones de la cada fila.
      if tablero_real[i][j] == -1:      # Avanzamos en las columnas de cada fila.
        tablero_visible[i][j] = BOMBA # Si es = -1 es BOMBA, finaliza el juego.
  return tablero_visible                    # Retornamos el tablero visible. Si se descubren bombas se retornará con las bombas descubiertas.

def buscar_camino(tablero: list[list[int]], tablero_visible: list[list[str]], f: int, c: int, camino_actual: list[tuple[int,int]],
                  caminos: list[list[tuple[int,int]]], visitados: list[tuple[int,int]]) -> None:
  """
  Busca las posiciones adyacentes a la posición (f,c) y busca los caminos posibles en todas las direcciones, teniendo en cuenta tanto los
  posibles límites del tablero en cualquier dirección o las posiciones de bombas adyacentes. Si no se revela ninguna celda, no hace nada.
  Args:
    tablero: list[list[int]]. tablero con minas (-1) y casillas con numeros del 0 al 8.
    tablero_visible: list[list[str]]. tablero con espacios vacios, banderas o minas.
    f: int. Fila de la posicion donde se descubrio la primera celda.
    c: int. Columna de la posicion donde se descubrio la primera celda.
    camino_actual: list[tuple[int, int]]. Lista donde se guarda el camino que se esta tomando en esta iteración.
    caminos: list[list[tuple[int, int]]]. Lista donde se guardan todos los caminos posibles que se tomaron.
    visitados: list[tuple[int, int]]. Lista de celdas que ya fueron visitadas.
  """
  if f < 0 or f >= len(tablero) or c < 0 or c >= len(tablero[0]):
    return # Si la celda está en fuera de los límites del tablero no hay nada para revelar.
  if tablero_visible[f][c] == BANDERA:
    return # Si la celda es una bandera no se puede revelar.
  if pertenece_lista(visitados, (f, c)):
    return # Si ya fue descubierta la celda, no hay que revelarla.
  valor: int                             = tablero[f][c]
  nuevos_visitados: list[tuple[int,int]] = visitados + [(f, c)] # Agregamos una celda descubierta.
  nuevo_camino: list[tuple[int,int]]     = camino_actual + [(f, c)] # Actualizamos el nuevo camino.
  if valor > 0:
    caminos.append(nuevo_camino) # Guardamos el camino.
  elif valor == 0:
    revelados: int = 0 # Contamos cuantas celdas adyacentes conseguimos revelar.
    for fila in range(f-1,f+2): # Analizamos las posiciones adyacentes a la celda seleccionada (las filas).
      for columna in range(c-1,c+2): # Analizamos las posiciones adyacentes de cada fila (las columnas).
        if (fila != f or columna != c) and 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]): # Mira si es posición válida a revelar.
          if not (pertenece_lista(nuevo_camino, (fila, columna))) and tablero_visible[fila][columna] != BANDERA:
            if tablero[fila][columna] == 0:
              buscar_camino(tablero, tablero_visible, fila, columna, nuevo_camino, caminos, nuevos_visitados) # Recursión a posición adyacente.
              revelados += 1
            elif tablero[fila][columna] > 0:
              caminos.append(nuevo_camino + [(fila, columna)]) # Si la celda es > 0 solo revelamos esa celda (sin recursión).
    if revelados == 0:
      caminos.append(nuevo_camino) # Aunque no hayamos revelado ninguna celda, debemos guardar el camino, pues es una secuencia válida.

def pertenece_lista(l: list[tuple[int,int]], t: tuple[int,int]) -> bool:
  """
  Chequea si la tupla dada esta en una lista de tuplas.
  Args:
    l: list[tuple[int, int]]. Lista de tuplas a comparar. 
    t: tuple[int, int]. tupla que se compara.
  Returns:
    bool: True si la tupla pertenece a l. False en el caso contrario.
  """
  for fila, columna in l:
    if fila == t[0] and columna == t[1]:
      return True
  return False
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 7 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def verificar_victoria(estado: EstadoJuego) -> bool:
  """
  Verifica si se descubrieron todas las minas en el tablero visible.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
  Returns:
    bool: True si todas se ganó el juego, False en el caso contrario.
  """
  res: bool = False
  if todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']) == True:
    res = True
  return res

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 8 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def reiniciar_juego(estado: EstadoJuego) -> None:
  """
  Actualiza todos los valores de estado con la misma cantidad de filas, columnas y minas, pero con las minas distribuidas aleatoriamente de
  una forma distinta y con el valor estado['juego_terminado'] = False.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
  """
  filas: int                     = estado['filas']
  columnas: int                  = estado['columnas']
  minas: int                     = estado['minas']                       # Convocamos los elementos del diccionario.
  nuevo_tablero: list[list[int]] = colocar_minas(filas, columnas, minas) # Creamos un nuevo tablero.
  calcular_numeros(nuevo_tablero)
  while son_iguales_tableros(nuevo_tablero, estado['tablero']):          # Si crea un tablero igual a tablero@pre => vuelve a crear tableros.
    nuevo_tablero = colocar_minas(filas, columnas, minas)
    calcular_numeros(nuevo_tablero)
  estado['tablero'] = nuevo_tablero                                      # Reiniciamos el tablero con el nuevo tablero.
  estado['tablero_visible'] = vaciar_matriz(nuevo_tablero)
  estado['juego_terminado'] = False

#———————————————————————————————————————————————————————————————————————————————————————
# Función Auxiliar #
#———————————————————————————————————————————————————————————————————————————————————————
def son_iguales_tableros(tablero_original: list[list[int]], tablero_nuevo: list[list[int]]) -> bool:
  """
  Compara dos tableros y chequea que no sean iguales.
  Args:
    tablero_original: list[list[int]]. Tablero del juego que acaba de terminar.
    tablero_nuevo: list[list[int]]. Tablero generado.
  Returns:
    bool: True si ambos tableros son iguales, False en caso contrario.
  """
  for i in range(len(tablero_original)):
    for j in range(len(tablero_original[i])):
      if tablero_original[i][j] != tablero_nuevo[i][j]:
        return False
  return True
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 9 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def guardar_estado(estado: EstadoJuego, ruta_directorio: str) -> None:
  """
  Crea los archivos de texto 'tablero.txt' y 'tablero_visible.txt' si aún no existen, y sino los sobreescribe.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    ruta_directorio: str. ruta de acceso del archivo.
  """
  columnas: int                 = estado['columnas']
  ruta_tablero_txt: str         = os.path.join(ruta_directorio, 'tablero.txt')         # Establece el directorio del archivo tablero.txt
  ruta_tablero_visible_txt: str = os.path.join(ruta_directorio, 'tablero_visible.txt') # Establece el directorio archivo tablero_visible.txt
  guardar_tablero(estado, ruta_tablero_txt, columnas)
  guardar_tablero_visible(estado, ruta_tablero_visible_txt, columnas)
  
#———————————————————————————————————————————————————————————————————————————————————————
# Funciones Auxiliares #
#———————————————————————————————————————————————————————————————————————————————————————
def guardar_tablero(estado: EstadoJuego, ruta_tablero_txt: str, columnas: int) -> None:
  """
  Actualiza (si no existe, lo crea) los valores del archivo de texto tablero.txt
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    ruta_tablero_txt: str. Directorio donde se encuentra el archivo tablero.txt
    columnas: int. Cantidad de columnas del tablero.
  """
  archivo_tablero = open(ruta_tablero_txt, 'w') # Abrimos el archivo para escribir
  for fila in estado['tablero']:
    for i in range(columnas):
      archivo_tablero.write(str(fila[i]))   # Escribimos en el txt cada valor del tablero.
      if i < columnas - 1:                  # Si el numero no es el ultimo de la fila, agrega una coma a su derecha.
        archivo_tablero.write(',')
    archivo_tablero.write('\n')               # Cuando se termina la fila, pasa a la siguiente.
  archivo_tablero.close()
  
def guardar_tablero_visible(estado: EstadoJuego, ruta_tablero_visible_txt: str, columnas: int) -> None:
  """
  Actualiza (si no existe, lo crea) los valores del archivo de texto tablero_visible.txt
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    ruta_tablero_visible_txt: str. Directorio donde se encuentra el archivo tablero_visible.txt
    columnas: int. Cantidad de columnas del tablero.
  """
  archivo_tablero_visible = open(ruta_tablero_visible_txt, 'w') # Abrimos el archivo para escribir.
  for fila in estado['tablero_visible']:
    for i in range(columnas):
      if fila[i] == BANDERA:                 # Por el valor de la columna de cada fila, se fija si es BANDERA o VACIO y pone el valor adecuado.
        archivo_tablero_visible.write('*')
      elif fila[i] == VACIO:
        archivo_tablero_visible.write('?')
      else:
        archivo_tablero_visible.write(str(fila[i]))
      if i < columnas - 1:
        archivo_tablero_visible.write(',') # Si el numero no es el ultimo de la fila, agrega una coma a su derecha.
    archivo_tablero_visible.write('\n')        # Cuando se termina la fila, pasa a la siguiente.
  archivo_tablero_visible.close()
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 10 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def cargar_estado(estado: EstadoJuego, ruta_directorio: str) -> bool:
  """
  Carga un estado de juego desde los archivos "tablero.txt" y "tablero_visible.txt" ubicados en el directorio dado.
  Args:
    estado: EstadoJuego. Parametros del juego actual
    ruta_directorio: str.  Ruta a la carpeta que contiene los archivos.
  Returns:
    bool: True si se cargó exitosamente los archivos. False en el caso contrario
  Nota: logramos que esta función se limite a verificar condiciones y delegar el trabajo a funciones auxiliares, lo que mejora la
  legibilidad y modularidad, haciendo que ahora sea más directa.
  """
  res: bool = False
  if (not existe_archivo(ruta_directorio, "tablero.txt")) or (not existe_archivo(ruta_directorio, "tablero_visible.txt")): # Veo existencia.
    return res
  tablero: list[str] = lectura_tablero(ruta_directorio) # Leemos el contenido de los archivos.
  tablero_visible: list[str] = lectura_tablero_visible(ruta_directorio)
  if not chequeo_dimensiones(tablero, tablero_visible): # Comprobamos que ambos tableros tengan las mismas dimensiones y no estén vacíos.
    return res
  columnas: int = contar_columnas(tablero[0]) # Cuento columnas del tablero (si el programa no terminó => la matriz es cuadrada).
  tableros: tuple[list[list[int]],list[list[str]],int,bool] = armado_de_tableros(tablero, tablero_visible, columnas) # Armo tableros a la vez.
  if not tableros[3] or tableros[2] == 0 or not tablero_valido_minas(tableros[0]): # Compruebo que sean tableros válidos.
    return res
  actualiza_estado(estado, tableros[0], tableros[1], tableros[2], columnas) # Actualizo el estado para cargar datos en el dicc 'estado'.
  if estado_valido(estado): # Finalmente verificamos que el estado resultante cumpla todas las postcondiciones.
    res = True
    return res
  else:
    return res

#———————————————————————————————————————————————————————————————————————————————————————
# Funciones Auxiliares #
#———————————————————————————————————————————————————————————————————————————————————————
def linea_valida(linea: str) -> bool:
  """
  Chequea si una linea de text contiene algo distinto a saltos de línea o espacios. 
  Args:
    linea: str. Linea de texto para chequear.
  Returns:
    bool: True si contiene algo distinto. False en caso contrario.
  """
  i: int = 0
  while i < len(linea):
    if linea[i] != '\n' and linea[i] != ' ':
      return True
    i += 1
  return False

def contar_columnas(linea: str) -> int:
  """
  Devuelve la cantidad de columnas que debe de tener el tablero.
  Args:
    linea: str. Linea de texto para chequear.
  """
  res: int = 1 # Inicializamos en 1, ya que la cantidad de ',' es una menos que la cantidad de columnas en una fila.
  i: int   = 0
  while i < len(linea):
    if linea[i] == ',':
      res += 1
    i += 1
  return res

def armar_linea(linea: str) -> list[str]:
  """
  Separa un string en una lista de strings con la coma como separador. 
  Args:
    linea: str. Linea de texto a separar.
  Returns:
    list[str]:  variable linea separada por las comas y sin el salto de linea.
  """
  res: list[str]  = []
  contenedor: str = ''
  i: int = 0
  while i < len(linea): # Leo bien las bombas (-1) y un elemento de la lista como '-1', no como '-', '1'.
    if linea[i] == ',':
      res.append(contenedor)
      contenedor = ''
    elif linea[i] != '\n':
      contenedor += linea[i]
    i += 1
  res.append(contenedor)
  return res

def cantidad_minas_adyacentes(tablero: list[list[int]], f: int, c: int, filas: int, columnas: int) -> int:
  """
  Devuelve cuántas minas hay alrededor de una celda con posicion (f, c).
  Args:
    tablero: list[list[int]]. Matriz con minas (-1) y casillas con numeros del 0 al 8. 
    f: int. fila de la posicion seleccionada.
    c: int. columna de la aposicion seleccionada.
    filas: int. Cantidad de filas del tablero.
    columnas: int. Cantidad de columnas del tablero.
  """
  cantidad: int = 0
  posiciones_adyacentes: list[tuple[int, int]] = [(f-1, c-1), (f-1, c), (f-1, c+1), # Posiciones adyacentes de la fila superior del tablero.
                                                  (f  , c-1),           (f,   c+1), # Posiciones adyacentes en la misma fila.
                                                  (f+1, c-1), (f+1, c), (f+1, c+1)] # Posiciones adyacentes en la fila inferior.
  i: int = 0
  while i < 8:                                                                      # Hay como mucho 8 posiciones adyacentes por celda.
    pos_actual: tuple[int, int] = posiciones_adyacentes[i]
    if 0 <= pos_actual[0] < filas and 0 <= pos_actual[1] < columnas:
      if tablero[pos_actual[0]][pos_actual[1]] == -1:
        cantidad += 1
    i += 1
  return cantidad

def tablero_valido_minas(tablero: list[list[int]]) -> bool:
  """
  Verifica que cada celda numérica tenga el valor correcto según la cantidad de minas adyacentes.
  Args:
    tablero: list[list[int]].  tablero con minas (-1) y casillas con numeros del 0 al 8.
  Returns:
    bool: True si todas las celdas coinciden con el valor esperado de minas adyacentes. False en el caso contrario.
  """
  filas: int    = len(tablero)
  columnas: int = len(tablero[0])
  i: int = 0
  while i < filas:
    j: int = 0
    while j < columnas:
      if tablero[i][j] != -1:
        minas_adyacentes: int = cantidad_minas_adyacentes(tablero, i, j, filas, columnas)
        if tablero[i][j] != minas_adyacentes: # Si el número en el tablero no coincide con la cantidad real, el tablero no es válido
          return False
      j += 1
    i += 1
  return True

def estado_valido(estado: EstadoJuego) -> bool:
  """
  Verifica que estaado sea coherente: cantidad de minas correcta, visibilidad consistente, y que el estado de 'juego_terminado' coincida con
  la realidad del tablero.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
  Returns:
    bool: True si no se encuentra ninguna incoherencia en estado.
  """
  minas_totales: int = 0
  for i in range(len(estado['tablero'])):
    for j in range(len(estado['tablero'][i])):
      if estado['tablero'][i][j] == -1:
        minas_totales += 1 # Voy contando las minas que haya.
  if estructura_y_tipos_validos(estado) == False: # Si EstadoJuego esta formada incorrectamente.
    return False
  if minas_totales != estado['minas']: # Si no concuerdan la cantidad de minas previstas con las que hay en el tablero.
    return False
  if todas_celdas_seguras_descubiertas(estado['tablero'],estado['tablero_visible']) and not (estado['juego_terminado']): # Gana y estado incorrecto.
    return False
  for i in range(len(estado['tablero_visible'])):
    for j in range(len(estado['tablero_visible'][i])):
      elem: str = estado['tablero_visible'][i][j]
      valor_real: int = estado['tablero'][i][j]
      if ((elem == BOMBA) and (estado['juego_terminado'] == False)):
        return False
      if ((elem == BOMBA) and (valor_real != -1)):
        return False
      if ((elem not in [BOMBA,VACIO,BANDERA]) and (elem != str(valor_real))):
        return False
  if not todas_celdas_seguras_descubiertas(estado['tablero'], estado['tablero_visible']) and estado['juego_terminado']:
    return False
  return True
"""Nota: La condición estado['tablero'] = calcular_numeros(tablero) que pide el asegura de la especificación ya está automáticamente
asegurada por la función crear_juego."""

def lectura_tablero(ruta_directorio: str) -> list[str]:
  """
  Devuelve las lineas de tablero.txt sin los saltos de linea.
  Args:
    ruta_directorio: str. Directorio donde se encuentra tablero.txt
  Returns:
    list[str]: lineas de tablero.txt sin los saltos de linea.
  """
  archivo = open(os.path.join(ruta_directorio, "tablero.txt"), "r")
  res: list[str] = []
  for linea in archivo:
    if linea_valida(linea):
      sin_salto: str = ""
      i: int = 0
      while i < len(linea):
        if linea[i] != '\n':
          sin_salto += linea[i]
        i += 1
      res.append(sin_salto)
  archivo.close()
  return res

def lectura_tablero_visible(ruta_directorio: str) -> list[str]:
  """
  Devuelve las lineas de tablero_visible.txt sin los saltos de linea.
  Args:
    ruta_directorio: str. Directorio de tablero_visible.txt
  Returns:
    list[str]: lista de strings con las lineas de tablero_visible.txt sin los saltos de linea.
  """
  archivo = open(os.path.join(ruta_directorio, "tablero_visible.txt"), "r")
  res: list[str] = []
  for linea in archivo:
    if linea_valida(linea):
      sin_salto: str = ""
      i: int = 0
      while i < len(linea):
        if linea[i] != '\n':
          sin_salto += linea[i]
        i += 1
      res.append(sin_salto)
  archivo.close()
  return res

def chequeo_dimensiones(tablero: list[list[str]], tablero_visible: list[list[str]]) -> bool:
  """
  Verifica que ambos tableros coincidan a como tendrian que ser.
  Args:
    tablero: list[list[str]]. matriz con minas (-1) y casillas con numeros del 0 al 8.
    tablero_visible: list[list[str]]. matriz con los elementos VACIO, BANDERA o BOMBA.
  Returns:
    bool:  True si ambos tableros tienen las mismas dimensiones y que no esten vacios. False en caso contrario.
  """
  if len(tablero) != len(tablero_visible) or len(tablero) == 0: # Si las longitudes son distintas ó son iguales a 0 => no puedo cargar estado.
    return False
  columnas: int = contar_columnas(tablero[0])
  i: int = 0
  while i < len(tablero): # verificamos que todas las filas de ambos archivos tengan la misma cantidad de columnas.
    if contar_columnas(tablero[i]) != columnas:
      return False
    if contar_columnas(tablero_visible[i]) != columnas:
      return False
    i += 1
  return True

# Lista de números válidos que pueden aparecer en el tablero (distintos de minas). La usamos para simplificar validaciones 
# y evitar anidar condiciones con múltiples comparaciones. En armado_de_tableros se accede a las celdas de ambos tableros 
# y se verifica, mediante pertenece_lista_2, si el valor entero de cada celda está dentro de esta lista.
numeros_validos: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8] 

def armado_de_tableros(tablero: list[list[str]], tablero_visible: list[list[str]], columnas: int
                       ) -> tuple[list[list[int]], list[list[str]], int, bool]:
  # Agregamos esta función auxiliar que es una pieza clave que arma y valida ambos tableros simultáneamente.
  """
  Valida y convierte los tableros de entrada de strings a los valores necesarios para el juego.
  Args:
    tablero: list[list[str]]. matriz con minas ("-1") y casillas con strings del 0 al 8.
    tablero_visible: list[list[str]] matriz con los elementos VACIO, BANDERA o BOMBA.
    columnas: int. Cantidad de columnas del tablero.
  Returns:
    tuple:
      - list[list[int]]: matriz con minas (-1) y casillas con numeros del 0 al 8.
      - list[list[str]] matriz con los elementos VACIO, BANDERA o BOMBA.
      - int: cantidad de minas.
      - bool: True si el armado del tablero fue valido, False si no fue así.
  """
  nuevo_tablero: list[list[int]] = [] # Armamos nuevos tableros con los archivos de tablero y tablero visible ya revisados.
  nuevo_tablero_visible: list[list[str]] = []
  minas: int = 0
  i: int = 0
  while i < len(tablero): # Armamos los nuevos tableros, iterando primero por los caracteres de tablero.
    fila_tablero: list[int] = []
    fila_tablero_visible: list[str] = []
    linea_tablero: list[str] = armar_linea(tablero[i])
    linea_visible: list[str] = armar_linea(tablero_visible[i])
    j: int = 0
    while j < columnas:
      celda_tablero_str: str = linea_tablero[j]
      if celda_tablero_str == "-1": # Convertimos la celda a entero según corresponda. Puede ser "-1" (mina) o un número válido.
        celda: int = -1
      elif pertenece_lista_2(int(celda_tablero_str), numeros_validos):
        celda: int = int(celda_tablero_str)
      else:
        return [], [], 0, False # En caso de no reconocer el caracter, no es válido, se descarta todo.
      if celda == -1:
        minas += 1
      elif celda < 0 or celda > 8: # Si el número esta fuera del rango esperado, no es válido el tablero.
        return [], [], 0, False
      fila_tablero.append(celda)
      celda_tablero_visible_str: str = linea_visible[j] # Celda del tablero visible. Repito pero para ese punto.
      if celda_tablero_visible_str == BOMBA:
        if celda != -1: # No puede mostrarse una bomba si no hay una mina.
          return [], [], 0, False
        fila_tablero_visible.append(BOMBA)
      elif celda_tablero_visible_str == BANDERA or celda_tablero_visible_str == "*":
        fila_tablero_visible.append(BANDERA)
      elif celda_tablero_visible_str == VACIO or celda_tablero_visible_str == "?":
        fila_tablero_visible.append(VACIO)
      else:
        num_valido: bool = True # Hacemos un chequeo verificar si el string representa un número válido para convertir a int.
        if len(celda_tablero_visible_str) == 0: # Un string vacío no tipa con int ().
          num_valido = False
        else:
          k: int = 0
          if celda_tablero_visible_str[0] == '-': # Si el número es negativo (bomba), permitimos que el primer caracter sea '-'.
            if len(celda_tablero_visible_str) > 1:
              k = 1
            else:
              num_valido = False # Si el número es negativo (empieza con '-') pero su longitud es == 1, entonces no es válido.
          while num_valido and k < len(celda_tablero_visible_str):
            if celda_tablero_visible_str[k] < '0' or celda_tablero_visible_str[k] > '9': # Si hay algún caracter no numérico, no es válido.
              num_valido = False
            k += 1
        if num_valido:
          numero: int = int(celda_tablero_visible_str)
          if pertenece_lista_2(numero, numeros_validos):
            if numero != celda:  # El número en el tablero visible debe coincidir con el del tablero real.
              return [], [], 0, False
            fila_tablero_visible.append(celda_tablero_visible_str)
          else:
            return [], [], 0, False
        else:
          return [], [], 0, False
      j += 1
    nuevo_tablero.append(fila_tablero) # Recopilamos la fila completa y repetimos el proceso hasta que no haya filas por armar.
    nuevo_tablero_visible.append(fila_tablero_visible)
    i += 1
  return nuevo_tablero, nuevo_tablero_visible, minas, True

# La diferencia entre pertenece_lista_1 y pertenece_lista_2, radica en los tipos de parámetros de entrada. 
# La primera trabaja con listas de tuplas y una tupla, mientras que la segunda con listas de enteros y un entero.
def pertenece_lista_2(n: int, l: list[int]) -> bool: # Se usa en armado_de_tableros para verificar si los valores procesados son válidos.
  """
  Busca un numero en una lista.
  Args:
    n: int. numero que se busca en la lista.
    l: list[int]. Lista donde se busca el numero.
  Returns:
    bool: True si n esta en la lista l.
  """
  for elem in l:
    if elem == n:
      return True
  return False

def actualiza_estado(estado: EstadoJuego, tablero: list[list[int]], visible: list[list[str]], minas: int, columnas: int) -> None:
  """
  Actualiza el diccionario 'estado' con los nuevos valores del tablero, tablero visible, cantidad de minas, cantidad de columnas y si el
  juego ya fue ganado.
  Args:
    estado: EstadoJuego. Parametros del juego actual.
    tablero: list[list[int]]. matriz con minas (-1) y casillas con numeros del 0 al 8.
    visible: list[list[str]]. matriz con los elementos VACIO, BANDERA o BOMBA.
    minas: int. Cantidad de minas del juego nuevo o cargado.
    columnas: int. Cantidad de columnas del juego nuevo o cargado.
  """
  # Utilizamos esta función auxiliar para acortar el código en cargar_estado (llama a la función dentro de cargar_estado).
  estado["filas"] = len(tablero)
  estado["columnas"] = columnas
  estado["minas"] = minas
  estado["tablero"] = tablero
  estado["tablero_visible"] = visible
  estado["juego_terminado"] = todas_celdas_seguras_descubiertas(tablero, visible)
  return

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————