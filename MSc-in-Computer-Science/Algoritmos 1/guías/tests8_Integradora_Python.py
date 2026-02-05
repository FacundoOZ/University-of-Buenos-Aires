
#============================================================================================================================================
# Práctica Especial: Ejercicios Integradores de Python (tests)
#============================================================================================================================================

import unittest
from queue import Queue as Cola
from Guía8_Integradora_Python import (maximas_cantidades_consecutivos, maxima_cantidad_primos, tuplas_positivas_y_negativas, resolver_cuenta)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 18 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class Ej18Test(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(Ej18Test, self).__init__(*args, **kwargs)
    self.method = maximas_cantidades_consecutivos
  def test_sec_vacia(self):
    entrada = []
    entrada_copia = entrada.copy()
    self.assertEqual(maximas_cantidades_consecutivos(entrada), {})
    self.assertEqual(entrada, entrada_copia)
  def test_todos_aparecen_una_sola_vez(self):
    entrada = list(range(0, 10))
    entrada_copia = entrada.copy()
    salida_esperada = {0:1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    # self.assertEqual(entrada, entrada_copia)
  def test_un_unico_elemento(self):
    entrada = [1]*20
    entrada_copia = entrada.copy()
    salida_esperada = {1: 20}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    # self.assertEqual(entrada, entrada_copia)
  def test_maxima_aparicion_al_final(self):
    entrada = [1, 1, 1, 2, 1, 1, 1, 1]
    entrada_copia = entrada.copy()
    salida_esperada = {1: 4, 2: 1}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    # self.assertEqual(entrada, entrada_copia)
  def test_maxima_aparicion_al_medio(self):
    entrada = [1, 1, 1, 97, 1, 1, 1, 1, 54, 54, 101]
    entrada_copia = entrada.copy()
    salida_esperada = {1: 4, 54: 2, 97: 1, 101: 1}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_maxima_aparicion_al_inicio(self):
    entrada = [30, 30, 30, 30, 2, 30, 30, 30]
    entrada_copia = entrada.copy()
    salida_esperada = {30: 4, 2: 1}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_multiples_sec_con_igual_longitud(self):
    entrada = [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2]
    entrada_copia = entrada.copy()
    salida_esperada = {1: 4, 2: 2}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_numeros_negativos(self):
    entrada = [-1, -2, -2, -3, -3, -1, -1]
    entrada_copia = entrada.copy()
    salida_esperada = {-1: 2, -2: 2, -3: 2}
    self.assertEqual(maximas_cantidades_consecutivos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 19 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class Ej19Test(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(Ej19Test, self).__init__(*args, **kwargs)
    self.method = maxima_cantidad_primos
  def test_matriz_con_un_primo(self):
    entrada = [[2]]
    entrada_copia = entrada.copy()
    salida_esperada = 1
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_matriz_con_un_no_primo(self):
    entrada = [[4]]
    entrada_copia = entrada.copy()
    salida_esperada = 0
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_matriz_cuadrada(self):
    entrada = [[1, 2], 
               [1, 2]]
    entrada_copia = entrada.copy()
    salida_esperada = 2
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_columnas_con_distinta_longitud_que_fila(self):
    entrada = [[1, 2, 3], 
                [1, 1, 1]]
    entrada_copia = entrada.copy()
    salida_esperada = 1
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_unica_columna(self):
    entrada = [[1],
                [2],
                [3], 
                [121]]
    entrada_copia = entrada.copy()
    salida_esperada = 2
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_unica_fila_con_primos(self):
    entrada = [[4, 6, 7, 14, 121, 5]]
    entrada_copia = entrada.copy()
    salida_esperada = 1
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_unica_fila_sin_primos(self):
    entrada = [[4, 6, 8, 14, 9, 21]]
    entrada_copia = entrada.copy()
    salida_esperada = 0
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_negativos(self):
    entrada = [[-2, 4, 5], 
               [-5, 3, 2], 
               [-7, 1, 1]]
    entrada_copia = entrada.copy()
    salida_esperada = 2
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_max_primos_en_el_medio(self):
    entrada = [[1, 2, 3, 4], 
               [6, 6, 7, 8], 
               [9, 10, 11, 12], 
               [5, 14, 13, 16],
               [0, 0, 0, 0]]
    entrada_copia = entrada.copy()
    salida_esperada = 4
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)
  def test_max_primos_en_el_medio_en_2_columas(self):
    entrada = [[1, 2, 3, 4], 
               [6, 6, 7, 8], 
               [9, 7, 11, 12], 
               [5, 14, 12, 16],
               [0, 19, 0, 0]]
    entrada_copia = entrada.copy()
    salida_esperada = 3
    self.assertEqual(maxima_cantidad_primos(entrada), salida_esperada)
    self.assertEqual(entrada, entrada_copia)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 20 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class Ej20Test(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(Ej20Test, self).__init__(*args, **kwargs)
    self.method = tuplas_positivas_y_negativas
  def test_elimina_tuplas_nulas(self):
    entrada = construir_cola_con_elementos([(-1,-1),(0,0), (1,1), (0,4), (-2,1)])
    salida_esperada = construir_cola_con_elementos([(-1,-1),(1,1), (-2,1)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_todas_positivas_queda_igual(self):
    entrada = construir_cola_con_elementos([(1,1),(1,2),(3,4)])
    salida_esperada = construir_cola_con_elementos([(1,1),(1,2),(3,4)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_todas_neativas_queda_igual(self):
    entrada = construir_cola_con_elementos([(1,-1),(-1,2),(-3,4)])
    salida_esperada = construir_cola_con_elementos([(1,-1),(-1,2),(-3,4)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_todas_nulas(self):
    entrada = construir_cola_con_elementos([(0,0)])
    salida_esperada = Cola()
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_tuplas_negativas_antes_que_positivas(self):
    entrada = construir_cola_con_elementos([(-1,2),(-1,-1),(1,-2),(2,2)])
    salida_esperada = construir_cola_con_elementos([(-1,-1),(2,2),(-1,2),(1,-2)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_tuplas_negativas_antes_que_positivas_y_nulas(self):
    entrada = construir_cola_con_elementos([(-1,2),(-1,-1),(1,-2),(0,0),(2,2)])
    salida_esperada = construir_cola_con_elementos([(-1,-1),(2,2),(-1,2),(1,-2)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_tuplas_intercaladas(self):
    entrada = Cola([(1,2),(1,-2),(-1,-2),(1,0),(0,2),(0,0),(3,2)])
    salida_esperada = Cola([(1,2),(3, 2),(1,-2),(-1,-2)])
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)
  def test_vacio(self):
    entrada = Cola()
    salida_esperada = Cola()
    tuplas_positivas_y_negativas(entrada)
    self.assertEqual(entrada.queue, salida_esperada.queue)

#———————————————————————————————————————————————————————————————————————————————————————
# Función Auxiliar
#———————————————————————————————————————————————————————————————————————————————————————
def construir_cola_con_elementos(elementos: list[tuple[int, int]]) -> Cola[tuple[int, int]]:
  res: Cola = Cola()
  for elem in elementos:
    res.put(elem)
  return res
#———————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Ejercicio 21 #
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class Ej21Test(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(Ej21Test, self).__init__(*args, **kwargs)
    self.method = resolver_cuenta
  def test_cuenta_comienza_con_caracter_negativo(self):
    result = resolver_cuenta('-1.1')
    self.assertAlmostEqual(result, -1.1)
  def test_cuenta_comienza_con_caracter_positivo(self):
    result = resolver_cuenta('+1.17')
    self.assertAlmostEqual(result, 1.17)
  def test_cuenta_comienza_con_digito(self):
    result = resolver_cuenta('4')
    self.assertAlmostEqual(result, 4.0)
  def test_cuenta_con_operacion_punto_con_multiple_digitos(self):
    result = resolver_cuenta('0.00007+1')
    self.assertAlmostEqual(result, 1.00007)
  def test_cuenta_resultado_positivo(self):
    result = resolver_cuenta('-10+15.5-23.5+23.4')
    self.assertAlmostEqual(result, 5.4)
  def test_cuenta_resultado_negativo(self):
    result = resolver_cuenta('+30-100+120.03-1000')
    self.assertAlmostEqual(result, -949.97)
  def test_cuenta_solo_sumas(self):
    result = resolver_cuenta('50+50+100')
    self.assertAlmostEqual(result, 200)
  def test_cuenta_solo_sumas_decimales(self):
    result = resolver_cuenta('50.25+50.255+100.277')
    self.assertAlmostEqual(result, 200.78199999999998)
  def test_cuenta_solo_restas(self):
    result = resolver_cuenta('-5010-90-900')
    self.assertAlmostEqual(result, -6000)
  def test_cuenta_solo_restas_decimales(self):
    result = resolver_cuenta('-500.12309-1250.5430-78894.4331')
    resultado_esperado = -80645.09919
    self.assertAlmostEqual(result, resultado_esperado)

if __name__ == '__main__':
  unittest.main(verbosity=2)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————