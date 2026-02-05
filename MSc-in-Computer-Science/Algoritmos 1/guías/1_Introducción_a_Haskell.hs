
-- ==========================================================================================================================================
-- Práctica 3: Introducción a Haskell
-- ==========================================================================================================================================

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 1 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
--A) Implementar la función parcial f :: Integer -> Integer definida por:    f(1) = 8    ;    f(4) = 131    ;    f(16) = 16,
-- cuya especificación es de la forma:
{--problema f (n : Z) : Z {
  requiere: {n=1 ∨ n=4 ∨ n=16}
  asegura: {(n=1 → res = 8) ∧ (n=4 → res = 131) ∧ (n=16 → res = 16)}
}--}

f::Integer -> Integer  -- Definición utilizando pattern-matching
f 1  = 8
f 4  = 131
f 16 = 16

--B) Análogamente, especificar e implementar la función g :: Integer -> Integer dada por:    g(8) = 16    ;    g(16) = 4    ;    g(131) = 1.
{--problema g (n : Z) : Z {
  requiere: {n=8 ∨ n=16 ∨ n=131}
  asegura: {(n=8 → res = 16) ∧ (n=16 → res = 4) ∧ (n=131 → res = 1)}
}--}

g::Integer -> Integer
g 8   = 16
g 16  = 4
g 131 = 1

--C) A partir de las funciones definidas en los ítems a) y b), implementar las funciones parciales h = f o g y k = g o f.

-- Recuerdo que h = f o g = f[g(x)]
h::Integer -> Integer
h 8   = f (g 8)
h 16  = f (g 16)
h 131 = f (g 131)

-- Recuerdo que k = g o f = g[f(x)]
k::Integer -> Integer
k 1  = g (f 1)
k 4  = g (f 4)
k 16 = g (f 16)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 2 -- Especificar e implementar las siguientes funciones, incluyendo su signatura:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
--A) Función 'absoluto': calcula el valor absoluto de un número entero.

{--problema absoluto (n : Z) : Z {
  requiere: {True}
  asegura: {si n es mayor o igual a cero res = n, y si n es menor a cero res = -n}
}--}

absoluto::Integer -> Integer
absoluto n | (n >= 0) = n
           | (n < 0)  = -n

--B) Función 'maximoAbsoluto': devuelve el máximo entre el valor absoluto de dos números enteros.

{--problema maximoAbsoluto (n : Z, m : Z) : Z {
  requiere: {True}
  asegura: {res es el número más grande entre el valor absoluto de n y m}
}--}

maximoAbsoluto::Integer->Integer -> Integer
maximoAbsoluto n m | (absoluto n > absoluto m) = absoluto n
                   | (absoluto m > absoluto n) = absoluto m

--C) Función 'maximo3': devuelve el máximo entre tres números enteros.

{--problema maximo3 (n : Z, m : Z, l : Z) : Z {
  requiere: {True}
  asegura: {res es el número más grande entre los tres números n, m, y l.}
}--}

maximo3::Integer->Integer->Integer -> Integer
maximo3 n m l | (n >= m && n >= l) = n
              | (m >= n && m >= l) = m
              | (l >= n && l >= m) = l

--D) Función 'algunoEsCero': dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching).

{--problema algunoEsCero (a : Q, b : Q) : Bool {
  requiere: {True}
  asegura: {res indica si es verdadero o no que al menos uno de los dos numeros a o b es nulo.}
}--}

algunoEsCero::Float->Float -> Bool
algunoEsCero a b = (a == 0 || b == 0)

--E) Función 'ambosSonCero': dados dos números racionales, decide si ambos son iguales a 0 (resolverlo con y sin pattern matching).

{--problema ambosSonCero (a : Q, b : Q) : Bool {
  requiere: {True}
  asegura: {res indica si es verdadero o no que tanto a como b son nulos.}
}--}

ambosSonCero::Float->Float -> Bool
ambosSonCero a b = (a == 0 && b == 0)

--F) Función 'enMismoIntervalo': dados dos números reales, indica si están relacionados por la relación de equivalencia en R cuyas clases de
-- equivalencia son: (−∞,3],(3,7] y (7,∞), o dicho de otra manera, si pertenecen al mismo intervalo.

{--problema enMismoIntervalo (a : R, b : R) : Bool {
  requiere: {True}
  asegura: {res indica si es verdadero que los reales a y b pertenecen simultáneamente a los intervalos (-inf,3], (3,7] o (7,inf).}
}--}

enMismoIntervalo::Float->Float -> Bool
enMismoIntervalo a b = (a <= 3 && b <= 3) || ((a > 3 && a <= 7) && (b > 3 && b <= 7)) || (a > 7 && b > 7)

--G) Función 'sumaDistintos': que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).

{--problema sumaDistintos (n : Z, m : Z, l : Z) : Z {
  requiere: {True}
  asegura: {si n, m y l son todos distintos, res indica la suma de n + m + l.}
  asegura: {si hay 1 o más números repetidos entre n, m y l, dicho número solo se tendrá en cuenta una vez a la hora de efectuar la suma.}
}--}

sumaDistintos::Integer->Integer->Integer -> Integer
sumaDistintos n m l | (n == m && n == l) = n           -- ó (m) ó (l)
                    | (n == m && n /= l) = n + l       -- ó (m + l)
                    | (n == l && n /= m) = m + l       -- ó (n + m)
                    | (m == l && m /= n) = n + m       -- ó (n + l)
                    | otherwise          = n + m + l

--H) Función 'esMultiploDe': dados dos números naturales, decide si el primero es múltiplo del segundo.

{--problema esMultiploDe (n : Z, m : Z) : Bool {
  requiere: {True}
  asegura: {res indica se es verdadero o no que el primer número natural (n) es múltiplo del segundo número natural (m).}
}--}

esMultiploDe::Integer->Integer -> Bool
esMultiploDe n m = (n > 0 && m > 0 && mod n m == 0)

--I) Función 'digitoUnidades': dado un número entero, extrae su dígito de las unidades.

{--problema digitoUnidades (n : Z) : Z {
  requiere: {True}
  asegura: {res representa el valor del dígito de las unidades del número n.}
}--}

digitoUnidades::Integer -> Integer
digitoUnidades n = (mod n 10)

--J) Función 'digitoDecenas': dado un número entero mayor a 9, extrae su dígito de las decenas.

{--problema digitoDecenas (n : Z) : Z {
  requiere: {True}
  asegura: {res representa el valor del dígito de las decenas del número n.}
}--}

digitoDecenas::Integer -> Integer
digitoDecenas n = (mod (div n 10) 10)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 3 -- Implementar una función estanRelacionados :: Integer -> Integer -> Bool cuya especificación está dada por:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema estanRelacionados (a : Z, b : Z) : Bool {
  requiere: {a y b son distintos de 0}
  asegura: {(res = True) si y solo si (a*a + a*b*k = 0 para algún k en Z con k distinto de 0).}
}
Ejemplo:
  estanRelacionados 8 2 ⇝ True porque existe k = −4 tal que 82 + 8x2x(−4) = 0.
  estanRelacionados 7 3 ⇝ False porque no existe un k entero tal que 72 + 7x3xk = 0.--}

{--Podemos ver que:
a^2 + abk = 0
a (a + bk) = 0
sii a = 0    ó    a + bk = 0
sii a = 0    ó    a = k'b
(donde k' = -k),
y como:
mod a b = 0    sii    a = kb,
entonces:--}

estanRelacionados::Integer->Integer -> Bool
estanRelacionados a b = (a == 0 || (mod a b == 0))

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 4 -- Especificar e implementar las siguientes funciones utilizando tuplas para representar pares y ternas de números.
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
--A) Función 'productoInterno': calcula el producto interno entre dos tuplas de R x R.

{--problema productoInterno (t1, t2 : R x R) : R {
  requiere: {True}
  asegura: {dadas t1 = (x1,y1) y t2 = (x2,y2) dos tuplas de R x R, res es la operación dada por x1*x2 + y1*y2.}
}--}

productoInterno::(Float,Float)->(Float,Float) -> Float
productoInterno (x1,y1) (x2,y2) = x1*x2 + y1*y2

--B) Función 'esParMenor': dadas dos tuplas de R x R, decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente
-- de la segunda tupla.

{--problema esParMenor (t1, t2 : R x R) : Bool {
  requiere: {True}
  asegura: {dadas t1 = (x1,y1) y t2 = (x2,y2) dos tuplas de R x R, res decide si es verdadero o no que cada coordenada de la primera tupla
            es menor a cada coordenada de la segunda, respectivamente.}
}--}

esParMenor::(Float,Float)->(Float,Float) -> Bool
esParMenor (x1,y1) (x2,y2) = (x1 < x2 && y1 < y2)

--C) Función 'distancia': calcula la distancia euclídea entre dos puntos de R^2.

{--problema distancia (t1, t2 : R x R) : R {
  requiere: {true}
  asegura: {dadas t1 = (x1,y1) y t2 = (x2,y2) dos tuplas de R x R, res es la operación raíz de la suma (x2-x1)^2 + (y2-y1)^2, cuyo valor
            mayor o igual a cero.}
}--}

distancia::(Float,Float)->(Float,Float) -> Float
distancia (x1,y1) (x2,y2) = sqrt((x2-x1)^2 + (y2-y1)^2)

--D) Función 'sumaTerna': dada una terna de enteros, calcula la suma de sus tres elementos.

{--problema sumaTerna (t : Z x Z x Z) : Z {
  requiere: {True}
  asegura: {dada una terna de enteros t = (i,j,k), res es la suma de todos ellos.}
}--}

sumaTerna::(Integer,Integer,Integer) -> Integer
sumaTerna (i,j,k) = i + j + k

--E) Función 'sumarSoloMultiplos': dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que
-- son múltiplos del número natural.

{--problema sumarSoloMultiplos (t : Z x Z x Z, n : Z) : Z {
  requiere: {el número n es un número entero mayor o igual a uno}
  asegura: {res es la suma de todos los números enteros de la terna t = (i,j,k) que son múltiplos del número natural n.}
}
Ejemplo:
  sumarSoloMultiplos (10, -8,-5) 2 ⇝ 2.
  sumarSoloMultiplos (66, 21, 4) 5 ⇝ 0.
  sumarSoloMultiplos (-30, 2,12) 3 ⇝ -18.--}

sumarSoloMultiplos::(Integer,Integer,Integer)->Integer -> Integer
sumarSoloMultiplos (i,j,k) n | (mod i n == 0 && mod j n /= 0 && mod k n /= 0) = i
                             | (mod i n /= 0 && mod j n == 0 && mod k n /= 0) = j
                             | (mod i n /= 0 && mod j n /= 0 && mod k n == 0) = k
                             | (mod i n == 0 && mod j n == 0 && mod k n /= 0) = i + j
                             | (mod i n == 0 && mod j n /= 0 && mod k n == 0) = i + k
                             | (mod i n /= 0 && mod j n == 0 && mod k n == 0) = j + k
                             | (mod i n == 0 && mod j n == 0 && mod k n == 0) = i + j + k
                             | otherwise                                      = 0

--F) Función 'posPrimerPar': dada una terna de enteros, devuelve la posición del primer número par si es que hay alguno, o devuelve 4
-- si son todos impares.

{--problema posPrimerPar (t : Z x Z x Z) : Z {
  requiere: {True}
  asegura: {res es un número entero 1, 2 o 3, que corresponde a la posición del primer elemento que sea par de la terna t = (i,j,k).}
  asegura: {si no hay ningún número entero par en la terna t = (i,j,k), entonces res es igual a cuatro (4).}
}--}

posPrimerPar::(Integer,Integer,Integer) -> Integer
posPrimerPar (i,j,k) | (mod i 2 == 0) = 1
                     | (mod i 2 /= 0 && mod j 2 == 0) = 2
                     | (mod i 2 /= 0 && mod j 2 /= 0 && mod k 2 == 0) = 3
                     | otherwise = 4

--G) Función 'crearPar' (crearPar :: a -> b -> (a,b)): a partir de dos componentes, crea un par con esos valores. Debe funcionar para
-- elementos de cualquier tipo.

{--problema crearPar (a, b) : (a,b) {
  requiere: {True}
  asegura: {res es una tupla formada a partir de los elementos a y b de la forma (a,b) donde a y b pueden ser elementos de cualquier tipo.}
}--}

crearPar::a->b -> (a,b)
crearPar a b = (a,b)

--H) Función 'invertir' (invertir :: (a,b) -> (b,a)): invierte los elementos del par pasado como parámetro. Debe funcionar para elementos
-- de cualquier tipo.

{--problema invertir (a,b) : (b,a) {
  requiere: {True}
  asegura: {res es la operación de invertir los componentes de la tupla (a,b) en (b,a).}
}--}

invertir::(a,b) -> (b,a)
invertir (a,b) = (b,a)

--I) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos:
type R2 = (Float, Float)

productoInternoR2::R2->R2 -> Float
productoInternoR2 (x1,y1) (x2,y2) = x1*x2 + y1*y2

esParMenorR2::R2->R2 -> Bool
esParMenorR2 (x1,y1) (x2,y2) = (x1 < x2 && y1 < y2)

distanciaR2::R2->R2 -> Float
distanciaR2 (x1,y1) (x2,y2) = sqrt((x2-x1)^2 + (y2-y1)^2)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 5 -- Implementar la función todosMenores :: (Integer,Integer,Integer) -> Bool, dada por las especificaciones:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema todosMenores (t : ZxZxZ) : Bool {
  requiere: {True}
  asegura: {(res = true) sii ((p(t0) > q(t0)) y (p(t1) > q(t1)) y (p(t2) > q(t2))).}
}--}
{--problema p (n : Z) : Z {
  requiere: {True}
  asegura: {(n <= 7 entonces res = n^2) y (n > 7 entonces res = 2n−1).}
}--}
{--problema q (n : Z) : Z {
  requiere: {True}
  asegura: {Si n es un número par entonces res = n/2, en caso contrario, res = 3n+1.}
}--}

p::Integer -> Integer
p n | (n <= 7) = n^2
    | (n > 7)  = 2*n-1

q::Integer -> Integer
q n | (mod n 2 == 0) = (div n 2)   -- Usamos div para que el resultado sea un Integer (si usáramos n/2, el resultado es Float)
    | otherwise      = 3*n+1

todosMenores::(Integer,Integer,Integer) -> Bool
todosMenores (t0,t1,t2) = ((p t0 > q t0) && (p t1 > q t1) && (p t2 > q t2))

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 6 -- Programar la función bisiesto :: Anio -> EsBisiesto según la siguiente especificación:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
type Anio = Integer
type EsBisiesto = Bool

{--problema bisiesto (año : Z) : Bool {
  requiere: {True}
  asegura: {(res = false) sii (año no es múltiplo de 4, o bien, año es múltiplo de 100 pero no de 400).}
}--}

bisiesto::Anio -> EsBisiesto
bisiesto n = ((mod n 4 == 0) && (mod n 100 /= 0)) || (mod n 400 == 0)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 7 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- A) Implementar la función: distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float, dada por la especificación:

{--problema distanciaManhattan (p : R x R x R, q : R x R x R) : R {
  requiere: {True}
  asegura: {res = \sum_{i=0}^2 |p_i − q_i|.}
}
Ejemplo:
  distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9.
  distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8.--}

absFloat::Float -> Float      -- Debo crear otra función absoluto ya que la del ejercicio 2 utilizaba Integers
absFloat x | (x >= 0) = x
           | (x < 0)  = -x

distanciaManhattan::(Float,Float,Float)->(Float,Float,Float) -> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2) = absFloat (x2-x1) + absFloat (y2-y1) + absFloat (z2-z1)

-- B) Reimplementar la función teniendo en cuenta el siguiente tipo:
type R3 = (Float, Float, Float)

distanciaManhattanR3::R3->R3 -> Float
distanciaManhattanR3 (x1,y1,z1) (x2,y2,z2) = absFloat (x2-x1) + absFloat (y2-y1) + absFloat (z2-z1)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 8 -- Implementar la función comparar :: Integer -> Integer -> Integer, dada por las especificaciones:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema comparar (a : Z, b : Z) : Z {
  requiere: {True}
  asegura: {(res = 1)  sii (sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
  asegura: {(res = −1) sii (sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
  asegura: {(res = 0)  sii (sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
}--}

{--problema sumaUltimosDosDigitos (x : Z) : Z {
  requiere: {True}
  asegura: {res = (|x| mod 10) + ( floor(|x|/10) mod 10)}
}
Ejemplo:
  comparar 45 312 ⇝-1 porque 45 ≺ 312 y 4+5>1+2.
  comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1+2<0+7.
  comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45.--}

sumaUltimosDosDigitos::Integer -> Integer
sumaUltimosDosDigitos n = (mod (absoluto n) 10) + mod (div (absoluto n) 10) 10

comparar::Integer->Integer -> Integer
comparar a b | (sumaUltimosDosDigitos a < sumaUltimosDosDigitos b) = 1
             | (sumaUltimosDosDigitos a > sumaUltimosDosDigitos b) = -1
             | otherwise = 0

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 9 -- A partir de las siguientes implementaciones en Haskell:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- A)
f9_1::Float->Float
f9_1 n | (n == 0)  = 1
       | otherwise = 0

-- B)
f9_2::Float->Float
f9_2 n | (n == 1)  = 15
       | (n == -1) = -15

-- C)
f9_3::Float->Float
f9_3 n | (n <= 9) = 7
       | (n >= 3) = 5

-- D)
f9_4::Float->Float->Float
f9_4 x y = (x+y)/2

-- E)
f9_5::(Float, Float)->Float
f9_5 (x,y) = (x+y)/2

-- F)
f9_6::Float->Int->Bool
f9_6 a b = (truncate a == b)

-- Describir en lenguaje natural qué hacen y especificarlas.

-- A) Esta función es como una ''delta de Dirac'', pero que no vale infinito, sino que vale 1 en la posición n=0, para cualquier otro valor
-- es nula. Una posible especificación es de la forma:
{--problema f9_1 (n : R) : R {
  requiere: {True}
  asegura: {res es 0 para todo valor de n, salvo cuando n = 0, que vale 1.}
}--}

-- B) Esta función es como dos funciones f9_1, donde la imagen puede tomar el valor positivo 15, o negativo -15, pero ningún otro valor.
-- Una posible especificación es de la forma:
{--problema f9_2 (n : R) : R {
  requiere: {True}
  asegura: {res vale 15 cuando n = 1, y -15 cuando n = -1. Para todo otro valor de n, res no está definido.}
}--}

-- C) Esta función es una función partida en el intervalo (-inf,9] U (9,inf) que es constante en ambos intervalos. Una posible especificación
-- es de la forma:
{--problema f9_3 (n : R) : R {
  requiere: {True}
  asegura: {res es igual a 7 para todo n <= 9, y es igual a 5 para todo n > 9.}
}--}

-- D) Esta función es una función que toma dos números reales y calcula su promedio. Una posible especificación es de la forma:
{--problema f9_4 (x, y : R) : R {
  requiere: {True}
  asegura: {res es igual al promedio de x e y.}
}--}

-- E) Esta función es una función que recibe una tupla de entradas (x,y) y devuelve el promedio entre dichas entradas. Una posible
-- especificación es de la forma:
{--problema f9_5 (n : R x R) : R {
  requiere: {True}
  asegura: {res es igual a la suma de las entradas de la tupla x + y dividida entre 2.}
}--}

-- F) Esta función es una función que recibe dos números a y b, tal que dado el número real a, determina si es cierto o no que al truncar
-- dicho número se obtiene el número entero b. Una posible especificación es de la forma:
{--problema f9_6 (a : R, b : Z) : R {
  requiere: {True}
  asegura: {res es True únicamente cuando al truncar el número real a se obtiene el número entero b (esto sucede cuando la diferencia entre
            a y b es < 0.0000001).}
}--}

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————