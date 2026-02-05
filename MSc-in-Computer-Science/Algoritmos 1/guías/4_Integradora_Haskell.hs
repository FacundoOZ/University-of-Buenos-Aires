
-- ==========================================================================================================================================
-- Práctica Especial: Ejercicios Integradores de Haskell
-- ==========================================================================================================================================

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 1 -- Sistema de Stock
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{-- Una reconocida empresa de comercio electrónico nos pide desarrollar un sistema de stock de mercadería. La mercadería de la empresa va a
ser representada como una secuencia de nombres de los productos, donde puede haber productos repetidos. El stock va a ser representado como
una secuencia de tuplas de dos elementos, donde el primero es el nombre del producto y el segundo es la cantidad que hay en stock (en este
caso no hay nombre de productos repetidos). También se cuenta con una lista de precios de productos representada como una secuencia de tuplas
de dos elementos, donde el primero es el nombre del producto y el segundo es el precio. Para implementar este sistema nos enviaron las
siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las
funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA). Implementar la función
generarStock :: [String] -> [(String, Integer)] dada por la siguiente especificación:--}

{--problema generarStock(mercadería: seq⟨String⟩) : seq⟨String x Z⟩ {
  requiere: {True}
  asegura: {La longitud de res es igual a la cantidad de productos distintos que hay en mercadería.}
  asegura: {Para cada producto que pertenece a mercadería, existe un i tal que 0 ≤ i < |res| y res[i]0=producto y res[i]1 es igual a la
            cantidad de veces que aparece producto en mercadería.}
}--}

quitar::String->[String] -> [String]
quitar _ [] = []
quitar nombre (x:cola) | (x == nombre) = quitar nombre cola
                       | otherwise     = x : quitar nombre cola

contar::String->[String] -> Integer
contar _ [] = 0
contar nombre (x:cola) | (x == nombre) = 1 + contar nombre cola
                       | otherwise     = contar nombre cola

pertenece::String->[String] -> Bool
pertenece _ [] = False
pertenece nombre (x:cola) | (x == nombre) = True
                          | otherwise     = pertenece nombre cola

generarStock::[String] -> [(String,Integer)]
generarStock [] = []
generarStock (x:cola) | (pertenece x cola) = (x, 1 + contar x cola) : generarStock(quitar x cola)
                      | otherwise          = (x, 1) : generarStock cola

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 2 -- Sistema de Stock
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función stockDeProducto :: [(String, Integer)] -> String -> Integer dada por la siguiente especificación:

{--problema stockDeProducto(stock: seq⟨String x Z⟩, producto: String) : Z {
  requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock.}
  requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero.}
  asegura: {si no existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a 0.}
  asegura: {si existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a stock[i]1.}
}--}

stockDeProducto::[(String,Integer)]->String -> Integer
stockDeProducto [] _ = 0
stockDeProducto ((x,y):cola) producto | (x == producto) = y
                                      | otherwise       = stockDeProducto cola producto

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 3 -- Sistema de Stock
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función dineroEnStock :: [(String, Integer))] -> [(String, Float)] -> Float dada por la siguiente especificación:

{--problema dineroEnStock(stock: seq⟨String x Z⟩, precios: seq⟨String x R⟩ ) : R {
  requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock.}
  requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios.}
  requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero.}
  requiere: {Todos los precios (segundas componentes) de precios son mayores a cero.}
  requiere: {Todo producto de stock aparece en la lista de precios.}
  asegura: {res es igual a la suma de los precios de todos los productos que están en stock multiplicado por la cantidad de cada producto
            que hay en stock.}
}
Nota: Para resolver este ejercicio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Integer devuelve
su equivalente de tipo Float.--}

buscarPrecio::String->[(String,Float)] -> Float
buscarPrecio producto ((x,y):cola) | (x == producto) = y
                                   | otherwise       = buscarPrecio producto cola

dineroEnStock::[(String,Integer)]->[(String,Float)] -> Float
dineroEnStock [] [] = 0.0
dineroEnStock ((x,y):cola) precios = (buscarPrecio x precios)*(fromIntegral y) + dineroEnStock cola precios

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 4 -- Sistema de Stock
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función aplicarOferta :: [(String, Integer)] -> [(String, Float)] -> [(String,Float)] dada por la siguiente especificación:

{--problema aplicarOferta(stock: seq⟨String x Z⟩, precios: seq⟨String x R⟩ ) : seq⟨String x R⟩ {
  requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock.}
  requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios.}
  requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero.}
  requiere: {Todos los precios (segundas componentes) de precios son mayores a cero.}
  requiere: {Todo producto de stock aparece en la lista de precios.}
  asegura: {|res| = |precios|}
  asegura: {Para todo 0≤i<|precios|, si stockDeProducto(stock,precios[i]0) > 10, entonces res[i]0=precios[i]0 y res[i]1 = 0,8*precios[i]1.}
  asegura: {Para todo 0≤i<|precios|, si stockDeProducto(stock,precios[i]0) ≤ 10, entonces res[i]0=precios[i]0 y res[i]1 = precios[i]1.}
}--}

aplicarOferta::[(String,Integer)]->[(String,Float)] -> [(String,Float)]
aplicarOferta [] [] = []
aplicarOferta stock ((x,y):cola) | ((stockDeProducto stock x) > 10) = (x,y*0.8) : aplicarOferta stock cola
                                 | otherwise                        =     (x,y) : aplicarOferta stock cola

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 5 -- Sopa de Números
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{-- Una sopa de números es un juego que consiste en descubrir propiedades de un tablero de dimensiones n x m con n y m>0, en los que en cada
posición hay un número entero positivo. Cada posición se identifica con una dupla (i,j) en el cual la primera componente corresponde a una
fila y la segunda a una columna. A modo de ejemplo, la siguiente figura muestra un tablero de 5 x 4 en el que el número 13 aparece en la
posición (1,1) y el número 5 aparece en la posición (4,3). Notar que tanto la numeración de las filas como la de las columnas comienzan en 1.

13   12     6     4
 1    1    32    25
 9    2    14     7
 7    3     5    16
27    2     8    18

--Un camino en un tablero está dado por una secuencia de posiciones adyacentes en la que solo es posible desplazarse desde una posición dada
hacia la posición de su derecha o hacia la que se encuentra debajo. En otras palabras, un camino de longitud l en un tablero se define como
una secuencia con l posiciones, ordenadas de manera tal que el elemento i-ésimo es la posición resultante de haberse movido hacia la derecha
o hacia abajo desde la posición (i-1)-ésima. Siguiendo con el ejemplo, a continuación puede observarse un camino de longitud 5 que representa
la sucesión Fibonacci y que empieza en la posición (2,1) y termina en (4,3) del tablero.

13   12     6     4
 1 -> 1 |  32    25
 9    2 |  14     7
 7    3 |-> 5    16
27    2     8    18

--Para manipular las sopas de números en Haskell vamos a representar el tablero como una lista de filas de igual longitud. A su vez, cada
fila vamos a representarla como una lista de enteros positivos. Las posiciones vamos a representarlas con tuplas de dos números enteros
positivos y un camino va a estar dado por una lista de posiciones. Para implementar esta sopa de números nos enviaron las siguientes
especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones
que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA). Asumimos los siguientes renombres
de tipos de datos en las especificaciones de los ejercicios:

--- Fila = seq⟨Z⟩
--- Tablero = seq⟨Fila⟩
--- Posicion = ZxZ -Observación: las posiciones son: (fila, columna)
--- Camino = seq⟨Posicion⟩--}

-- Implementar la función maximo :: Tablero -> Integer dada por la siguiente especificación:

{--problema minimo(t: Tablero) : Z {
  requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al menos un elemento.}
  requiere: {Existe al menos una columna en el tablero t.}
  requiere: {El tablero t no es vacío, todos los números del tablero son positivos, mayor estricto a 0.}
  asegura: {res es igual al número más pequeño del tablero t.}
}--}

minim::[Integer] -> Integer
minim [x] = x
minim (x:y:cola) | (x <= y)  = minim (x:cola)
                 | otherwise = minim (y:cola)

minimo::[[Integer]] -> Integer
minimo [x] = minim x
minimo (x:y:cola) | (minim x <= minim y) = minimo (x:cola)
                  | otherwise            = minimo (y:cola)

{--problema maximo(t: Tablero) : Z {
  requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al menos un elemento.}
  requiere: {Existe al menos una columna en el tablero t.}
  requiere: {El tablero t no es vacío, todos los números del tablero son positivos, mayor estricto a 0.}
  asegura: {res es igual al número más grande del tablero t.}
}--}

maxim::[Integer] -> Integer
maxim [x] = x
maxim (x:y:cola) | (x >= y)  = maxim (x:cola)
                 | otherwise = maxim (y:cola)

maximo::[[Integer]] -> Integer
maximo [x] = maxim x
maximo (x:y:cola) | (maxim x >= maxim y) = maximo (x:cola)
                  | otherwise            = maximo (y:cola)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 6 -- Sopa de Números
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función masRepetido :: Tablero -> Integer dada por la siguiente especificación:

{--problema repetidos(t: Tablero) : seq⟨Z⟩ {
  requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al menos un elemento.}
  requiere: {Existe al menos una columna en el tablero t.}
  requiere: {El tablero t no es vacío, todos los números del tablero son positivos, mayor estricto a 0.}
  asegura: {res es igual a las secuencias de números que aparecen al menos 2 veces en el tablero.}
  asegura: {res no tiene repetidos.}
}--}

quitarEntero::Integer->[Integer] -> [Integer]
quitarEntero _ [] = []
quitarEntero elem (x:cola) | (x == elem) = quitarEntero elem cola
                           | otherwise   = x : quitarEntero elem cola

perteneceEntero::Integer->[Integer] -> Bool
perteneceEntero _ [] = False
perteneceEntero elem (x:cola) | (elem == x) = True
                              | otherwise   = perteneceEntero elem cola

repet::[Integer] -> [Integer]
repet []  = []
repet [x] = [] -- Caso especial: Si hay un solo elemento, éste no se repite -> los repetidos será una lista vacía.
repet (x:y:cola) | (x == y)                 = x : repet(quitarEntero x cola)     -- Si x=y, quito 'x' de 'y' y 'cola', y lo appendeo primero.
                 | (perteneceEntero x cola) = x : repet(y:(quitarEntero x cola)) -- Si x/=y pero x en cola, quito los x de cola y lo appendeo.
                 | otherwise                = x : repet(y:cola)                  -- Si x es el único en toda la lista, lo apendeo y repito.

repetidos::[[Integer]] -> [Integer]
repetidos [x]      = repet x
repetidos (x:cola) = repet x ++ repetidos cola

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 7 -- Sopa de Números
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función valoresDeCamino :: Tablero -> Camino -> [Integer] dada por la siguiente especificación:

{--problema valoresDeCamino(t: Tablero, c: Camino) : seq⟨Z⟩ {
  requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al menos un elemento.}
  requiere: {Existe al menos una columna en el tablero t.}
  requiere: {El tablero t no es vacío, todos los números del tablero son positivos, mayores estrictos a 0.}
  requiere: {El camino c es un camino válido, es decir, secuencia de posiciones adyacentes en la que solo es posible desplazarse hacia la
             posición de la derecha o hacia abajo y todas las posiciones están dentro de los limites del tablero t.}
  asegura: {res es igual a la secuencia de números que están en el camino c, ordenados de la misma forma que aparecen las posiciones
            correspondientes en el camino.}
}--}

elemLista::Integer->[Integer] -> Integer
elemLista 1    (x:cola) = x
elemLista elem (x:cola) = elemLista (elem-1) cola

filaMatriz::Integer->[[Integer]] -> [Integer]
filaMatriz 1 (x:cola) = x
filaMatriz filM (x:cola) = filaMatriz (filM-1) cola

elemMatriz::(Integer,Integer)->[[Integer]] -> Integer
elemMatriz (i,j) matriz = elemLista j (filaMatriz i matriz)

valoresDeCamino::[[Integer]]->[(Integer,Integer)] -> [Integer]
valoresDeCamino [] _ = []
valoresDeCamino _ [] = [] 
valoresDeCamino matriz ((i,j):cola) = (elemMatriz (i,j) matriz) : (valoresDeCamino matriz cola)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 8 -- Perfectos Amigos
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--El Departamento de Matemática (DM) de la FCEyN-UBA nos ha encargado que desarrollemos un sistema para el tratamiento de números naturales.
Específicamente les interesa conocer cuándo un número es perfecto y cuándo dos números son amigos. Aunque por ahí no lo sabías, estos
conceptos existen y se definen como:
1. Un número natural es perfecto cuando la suma de sus divisores propios (números que lo dividen menores a él) es igual al mismo número.
Por ejemplo, 6 es un número perfecto porque la suma de sus divisores propios (1,2 y 3) es igual a 6.
2. Dos números naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del otro. Por ejemplo, 220 y 284
son amigos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110 que sumados dan 284 y los divisores propios de
284 son 1, 2 , 4, 71, 142 que sumados dan 220.

Para implementar este sistema nos enviaron las siguientes especificaciones en lenguaje semiformal y nos pidieron que hagamos el desarrollo
enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia
Algoritmos y Estructuras de Datos I.--}

--Implementar la función divisoresPropios :: Integer -> [Integer] dada por la siguiente especificación:

{--problema divisoresPropios(n: Z) : seq⟨Z⟩ {
  requiere: {n > 0}
  asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor.}
  asegura: {res no tiene elementos repetidos.}
  asegura: {res no contiene a ningún elemento que no sea un divisor propio de n.}
}--}

-- Creo una función auxiliar que recibe un número n, y un índice i. Si el índice divide a n lo agrega a una lista sino no.
contarDivisores::Integer->Integer -> [Integer]
contarDivisores n 1 = [1]
contarDivisores n i | (mod n i == 0) = contarDivisores n (i-1) ++ [i]
                    | otherwise      = contarDivisores n (i-1)

divisoresPropios::Integer -> [Integer]
divisoresPropios n = contarDivisores n (n-1) -- No contemplo al último número como divisor (de acuerdo al enunciado).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 9 -- Perfectos Amigos
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función sonAmigos :: Integer -> Integer -> Bool dada por la siguiente especificación:

{--problema sonAmigos(n,m: Z) : Bool {
  requiere: {n > 0}
  requiere: {m > 0}
  asegura: {res = True ⇔ n y m son números amigos.}
}--}

sumaLista::[Integer] -> Integer
sumaLista [] = 0
sumaLista (x:cola) = x + sumaLista cola

sonAmigos::Integer->Integer -> Bool
sonAmigos 1 1 = True
sonAmigos n m | ((sumaLista(divisoresPropios n) == m) && (sumaLista(divisoresPropios m) == n)) = True
              | otherwise = False

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 10 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema maxMovilN(lista: seq⟨Z⟩, n: Z) : Z {
  requiere: {|lista| > 0}
  requiere: {n > 0 y n es menor a la longitud de la lista.}
  asegura: {res es el máximo de los últimos n elementos de la lista.}
}--}

ultimo::[Integer]->Integer
ultimo [x] = x
ultimo (x:cola) = ultimo cola

listaSinUltimo::[Integer]->[Integer]
listaSinUltimo [x] = []
listaSinUltimo (x:cola) = x : listaSinUltimo cola

ultimosNAux::[Integer]->Integer->Integer -> [Integer]
ultimosNAux lista n 1 = [ultimo (lista)]
ultimosNAux lista n j | (j <= n) = ultimosNAux (listaSinUltimo lista) n (j-1) ++ [ultimo (lista)]
                      | otherwise = []

ultimosN::[Integer]->Integer -> [Integer]
ultimosN lista n = ultimosNAux lista n n

maxLista::[Integer]-> Integer
maxLista [x] = x
maxLista (x:y:cola) | (x >= y) = maxLista (x:cola)
                    | otherwise = maxLista (y:cola)

maxMovilN::[Integer]->Integer -> Integer
maxMovilN lista n = maxLista (ultimosN lista n)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 11 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema promedioPrimo(n: Z) : Float {
  requiere: {n > 1}
  asegura: {res es el promedio de todos los factores primos de n (distintos o no).}
}
Nota: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3].--}

listaDivisores::Integer->Integer -> [Integer]
listaDivisores n 1 = [1]
listaDivisores n j | (mod n j == 0) = listaDivisores n (j-1) ++ [j]
                   | otherwise = listaDivisores n (j-1)

lenLista::[Integer] -> Integer
lenLista [] = 0
lenLista (x:cola) = 1 + lenLista cola

esPrimo::Integer -> Bool
esPrimo 0 = False
esPrimo 1 = False
esPrimo n | (lenLista(listaDivisores n n) > 2) = False
          | otherwise = True

factoresPrimos::Integer->Integer -> [Integer]
factoresPrimos 1 _ = []
factoresPrimos n j | mod n j == 0 && esPrimo j = j : factoresPrimos (div n j) j
                   | j > n = []
                   | otherwise = factoresPrimos n (j + 1)

sumLista::[Integer] -> Integer
sumLista [] = 0
sumLista (x:cola) = x + sumLista cola

promedioPrimo::Integer -> Float
promedioPrimo n = (fromIntegral (sumLista(factoresPrimos n 2)))/(fromIntegral (lenLista(factoresPrimos n 2)))

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 12 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema letrasIguales(palabra: seq⟨Char⟩) : Z {
  requiere: {True}
  asegura: {res es la cantidad de caracteres no blancos repetidos en palabra.}
}--}

iesimo::[Char]->Integer -> Char
iesimo (x:cola) 1 = x
iesimo (x:cola) j = iesimo cola (j-1)

len::[Char] -> Integer
len [] = 0
len [x] = 1
len (x:cola) = 1 + len cola

repsLetraAux::[Char]->Char->Integer -> Integer
repsLetraAux _ _ 0 = 0
repsLetraAux palabra letra j | ((j <= len(palabra)) && ((iesimo palabra j) == letra)) = 1 + repsLetraAux palabra letra (j-1)
                             | otherwise = repsLetraAux palabra letra (j-1)

repsLetra::[Char]->Char -> Integer
repsLetra palabra letra = (repsLetraAux palabra letra (len(palabra)))

quitaLetrasRep::[Char]->Char -> [Char]
quitaLetrasRep [] _ = []
quitaLetrasRep (x:cola) letra | (x == letra) = quitaLetrasRep cola letra
                              | otherwise = x : quitaLetrasRep cola letra

letrasAux::[Char]->Integer -> Integer
letrasAux palab 1 = 0
letrasAux palab j | (j <= len(palab) && repsLetra palab (iesimo palab j) >= 2) = 1 + letrasAux (quitaLetrasRep palab (iesimo palab j)) (j-1) 
                  | otherwise = letrasAux palab (j-1)

letrasIguales::[Char] -> Integer
letrasIguales palabra = letrasAux palabra (len(palabra))

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 13 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema cuantosIguales(palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Z {
  requiere: {True}
  asegura: {res es igual a la cantidad de caracteres no blancos y distintos que palabra1 y palabra2 tienen en común.}
}--}

-- Tomo una letra de palabra1, y me fijo si está en palabra 2. quito todos los reps de palabra 1 y 2 de dicha letra y repito para mas letras

letrasDistintas::[Char]->Integer -> [Char]
letrasDistintas [x] 1 = [x]
letrasDistintas palabra j | (j <= len(palabra)) = letrasDistintas (quitaLetrasRep palabra (iesimo palabra j)) (j-1) ++ [iesimo palabra j]
                          | otherwise = letrasDistintas (palabra) (j-1)

enPalabraAux::[Char]->Char->Integer -> Bool
enPalabraAux _ _ 0 = False
enPalabraAux palabra letra j | (letra == (iesimo palabra j)) = True
                             | otherwise = enPalabraAux palabra letra (j-1)

letraPerteneceAPalabra::[Char]->Char -> Bool
letraPerteneceAPalabra palabra letra = enPalabraAux palabra letra (len(palabra))

cuantosIgualesAux::[Char]->[Char]->Integer -> Integer
cuantosIgualesAux _ _ 0 = 0
cuantosIgualesAux palabra1 palabra2 j | (letraPerteneceAPalabra palabra2 (iesimo (letras1) j)) = 1 + cuantosIgualesAux palabra1 palabra2 (j-1)
                                      | otherwise = cuantosIgualesAux palabra1 palabra2 (j-1)
                                   where
                                        letras1 = letrasDistintas palabra1 (len(palabra1))

cuantosIguales::[Char]->[Char] -> Integer
cuantosIguales palabra1 palabra2 = cuantosIgualesAux palabra1 palabra2 (len(letrasDistintas palabra1 (len(palabra1))))

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 14 -- Codificar
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{-- La codificación por sustitución es una de las técnicas de cifrado más simples, en el que un caracter en el texto original es reemplazado
por otro caracter dependiendo de un mapeo. Este mapeo puede representarse con una secuencia de tuplas de dos caracteres, donde la primera
componente de la tupla representa el caracter original y la segunda componente el caracter por el cual se lo va a sustituir. Por simplicidad,
en este problema codificaremos solo los caracteres que aparecen en el mapeo dado. Todos los restantes caracteres quedan inalterados en el
mensaje codificado.
Para implementar este sistema de codificación nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo
enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia
Algoritmos y Estructuras de Datos I.--}

{--problema codificar (c: Char, mapeo: seq⟨Char x Char⟩ ) : Bool {
  requiere: {No hay elementos repetidos entre las primeras o segundas componentes de mapeo.}
  asegura: {res = true <=> c es igual a la primera componente de alguna tupla de mapeo.}
}--}

codificar::Char->[(Char,Char)] -> Bool
codificar c [] = False
codificar c ((x,_):cola) | (c == x) = True
                         | otherwise = codificar c cola

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 15 -- Codificar
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema cantCodificaciones(c: Char, frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Z {
  requiere: {No hay elementos repetidos entre las primeras o segundas componentes de mapeo.}
  requiere: {|frase| > 0 }
  requiere: {c pertenece a frase.}
  asegura: {(res = 0 y codificar (c, mapeo) = false) o (res = cantidad de veces que c aparece en frase y codificar (c, mapeo) = true).}
}--}

apariciones::Char->[Char] -> Integer
apariciones c [] = 0
apariciones c (x:cola) | (x == c) = 1 + apariciones c cola
                       | otherwise = apariciones c cola

cantCodificaciones::Char->[Char]->[(Char,Char)] -> Integer
cantCodificaciones c frase mapeo | ((codificar c mapeo) == False) = 0
                                 | ((codificar c mapeo) == True) = apariciones c frase

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 16 -- Codificar
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema maxCodificacion(frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩) : Char {
  requiere: {No hay elementos repetidos entre las primeras o segundas componentes de mapeo.}
  requiere: {|frase| > 0}
  requiere: {Existe al menos un c que pertenece a frase y codificar(c, mapeo)=true.}
  asegura: {res=c donde c es el caracter tal que cantCodificaciones(c,frase,mapeo) es mayor a cualquier otro caracter perteneciente a frase.}
  asegura: {Si existen más de un caracter c que cumple la condición anterior, devuelve el que aparece primero en frase.}
}--}

maxCodificacion::[Char]->[(Char,Char)] -> Char
maxCodificacion [x] _ = x
maxCodificacion (x:y:cola) map | (cantCodificaciones x (x:y:cola) map > cantCodificaciones y (x:y:cola) map) = maxCodificacion (x:cola) map
                               | (cantCodificaciones x (x:y:cola) map < cantCodificaciones y (x:y:cola) map) = maxCodificacion (y:cola) map
                               | otherwise = maxCodificacion (x:cola) map

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 17 -- Codificar
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema codificarFrase(frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : seq ⟨Char⟩ {
  requiere: {No hay elementos repetidos entre las primeras o segundas componentes de mapeo.}
  requiere: {|frase| > 0 }
  asegura: {|res| = | frase|}
  asegura: {Para todo 0<=i<|frase| si codificar(frase[i],mapeo)=True y (mapeo[j])0=frase[i] => res[i]=(mapeo[j])1, para un j tal que
            0 <= j < |mapeo|.}
  asegura: {Para todo 0<=i<|frase| si codificar(frase[i],mapeo)=False => res[i]=frase[i].}
}--}

buscarClave::Char->[(Char,Char)] -> Char
buscarClave x ((t0,t1):resto) | (x == t0) = t1
                              | (x /= t0) = buscarClave x resto

codificarFrase::[Char]->[(Char,Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase [x] [] = [x]
codificarFrase (x:cola) map | ((codificar x map)) = [buscarClave x map] ++ (codificarFrase cola map)-- Si i-ésimo de x en mapeo ((t0,t1):resto),
                                                                                                    -- busco codif, si encuentra devuelve map[j]1.
                            | ((codificar x map) == False) = x : codificarFrase cola map            -- Si el elem no está devuelvo x y repito.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 18 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Se dice que n es un número abundante si la suma de sus divisores propios es mayor que n. Los divisores propios de un número son todos los
-- divisores sin contar al número mismo. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6. La suma de los divisores propios de 12
-- es 1 + 2 + 3 + 4 + 6 = 16, que es mayor que 12. Por lo tanto, 12 es un número abundante. Se pide implementar abundantes:

{--problema abundantes(d: Z,h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números abundantes en el rango [d..h].}
}
Ejemplo: abundantes 12 24 debe devolver 4.--}

buscaDivisores::Integer->Integer -> [Integer]
buscaDivisores n 2 = [1,2]
buscaDivisores n i | (mod n i == 0) = buscaDivisores n (i-1) ++ [i]
                   | otherwise = buscaDivisores n (i-1)

divisores::Integer -> [Integer]
divisores 1 = [1]
divisores 2 = [1]
divisores n = buscaDivisores n (n-1)

sumaDivisoresPropios::Integer -> Integer
sumaDivisoresPropios n = sumaLista(divisores n)

esAbundante::Integer -> Bool
esAbundante n = ((sumaDivisoresPropios n) > n)

-- La función auxiliar tiene un índice i sobre el cual haré el loop desde d hasta h:
abundantesAux::Integer->Integer->Integer -> Integer
abundantesAux d h 0 = 0
abundantesAux d h i | (esAbundante i) = 1 + abundantesAux d h (i-1)
                    | otherwise = abundantesAux d h (i-1)

abundantes::Integer->Integer -> Integer
abundantes d h = abundantesAux d h h - abundantesAux d h (d-1)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 19 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Representaremos una cursada aprobada con una tupla String x Z x Z, donde:
  --1. La primera componente de la tupla contiene el nombre de una materia.
  --2. La segunda componente de la tupla contiene el año de aprobación de la cursada.
  --3. La tercera componente de la tupla contiene el cuatrimestre de aprobación de la cursada (el valor 0 representa un curso de verano).
--Se pide implementar cursadasVencidas, que dada una lista de cursadas devuelva aquellas materias cuya aprobación de la cursada ya venció,
-- y por lo tanto ya no se puede rendir el final.

{--problema cursadasVencidas(s: seq⟨String x Z x Z⟩) :seq⟨String⟩ {
  requiere: {s[i]1 ≥ 1993 para todo i tal que 0 ≤ i < |s|.}
  requiere: {0 ≤ s[i]2 ≤ 2 para todo i tal que 0 ≤ i < |s|.}
  asegura: {res no tiene elementos repetidos.}
  asegura: {res contiene los nombres de todas las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer
            cuatrimestre de 2021, inclusive.}
  asegura: {res contiene solamente los nombres de las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer
            cuatrimestre de 2021, inclusive.}
}
Ejemplo: cursadasVencidas [("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] debe devolver
["Algoritmos y Estructuras de Datos I"].--}

eliminaRepetidos::[String] -> [String]
eliminaRepetidos [x] = [x]
eliminaRepetidos (x:cola) | (pertenece x cola == False) = x : eliminaRepetidos (cola)
                          | otherwise = eliminaRepetidos(cola)

cursadasVencidasRep::[(String,Integer,Integer)] -> [String]
cursadasVencidasRep [] = []
cursadasVencidasRep ((materia,año,cuatri):cola) | (((año == 2021) && (cuatri == 0)) || (año <= 2020)) = materia : cursadasVencidasRep (cola)
                                                | otherwise = cursadasVencidasRep (cola)

cursadasVencidas::[(String,Integer,Integer)] -> [String]
cursadasVencidas lista = eliminaRepetidos (cursadasVencidasRep lista)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 20 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema saturaEnNegativo(s: seq⟨Z⟩, u: Z) : seq⟨Z⟩ {
  requiere: {u > 0}
  asegura: {La longitud de res es igual a la cantidad de elementos no negativos consecutivos desde el inicio de s.}
  asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que 0 ≤ s[i] ≤ u, se cumple que res[i] = s[i].}
  asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que s[i] > u, se cumple que res[i] = u.}
}
Ejemplo: saturaEnNegativo [3,8,5,0,7,-2,4] 5 debe devolver [3,5,5,0,5].--}

saturaEnNegativo::[Integer]->Integer -> [Integer]
saturaEnNegativo [] _ = []
saturaEnNegativo (x:cola) u | (x >= 0 && x <= u) = x : (saturaEnNegativo cola u)
                            | (x > u) = u : (saturaEnNegativo cola u)
                            | (x < 0) = []

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 21 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema cantidadParesColumna(matriz: seq⟨seq⟨Z⟩⟩, col: Z) : Z{
requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud.}
requiere: {|matriz| > 0}
requiere: {|matriz[0]| > 0}
requiere: {1 ≤ col ≤ |matriz[0]|}
asegura: {res es la cantidad de números pares de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz|.}
}
Ejemplo: cantidadParesColumna [[-9, 8, 2, 3],
                              [ 2, 7,-5, 3],
                              [-1, 0, 5, 6]] 2
debe devolver 2.--}

indiceLista::[Integer]->Integer -> Integer
indiceLista (x:cola) 0 = x
indiceLista (x:cola) elem = indiceLista cola (elem-1)

cantidadParesColumna::[[Integer]]->Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna ((x:cola):mat) col | (mod (indiceLista (x:cola) (col-1)) 2 == 0) = 1 + cantidadParesColumna mat col -- Si es par, sumo 1.
                                        | otherwise = cantidadParesColumna mat col                                       -- Si no, no.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 22 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Representaremos un producto con una tupla String x Z x seq⟨Z x Z⟩, donde:
-- La primera componente de la tupla contiene el nombre del producto.
-- La segunda componente de la tupla contiene el precio del producto en efectivo.
-- La tercera componente es una lista de tuplas (cada tupla es una opción para pagar en cuotas), para cada una de las cuales:
  --1. La primera componente de la tupla contiene el número de cuotas en las que se puede abonar el producto.
  --2. La segunda componente de la tupla contiene el precio de cada cuota.
-- Se pide implementar la función productosSinInteres dada por la siguiente especificación:
{--problema productosSinInteres(s: seq⟨String x Z x seq⟨Z x Z⟩⟩) : seq⟨String⟩ {
  requiere: {No hay elementos repetidos en las primeras componentes de s.}
  requiere: {Todos los números de las segundas componentes de s son positivos.}
  requiere: {Todos los números de cada tupla de las terceras componentes de s son positivos.}
  asegura: {res contiene los elementos s[i]0 tales que s[i]1 es igual al producto de (s[i]2)[j]0 por (s[i]2)[j]1 (para al menos un j).}
}
Ejemplo: productosSinInteres[("zapatillas",60000,[(3,20000),(6,12000)]),("alfajor",1500,[(6,300)]),("yate",2000000,[])] = ["zapatillas"].--}

productosSinInteres::[(String,Integer,[(Integer,Integer)])] -> [String]
productosSinInteres [] = []
productosSinInteres ((nombre,precio,lista):resto) | (buscarEnLista precio lista) = nombre : (productosSinInteres resto)
                                                  | otherwise                    =           productosSinInteres resto

buscarEnLista::Integer->[(Integer,Integer)] -> Bool
buscarEnLista x [] = False
buscarEnLista precio ((x,y):cola) | (x*y == precio) = True
                                  | otherwise       = buscarEnLista precio cola

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 23 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Decimos que n es un número cuadrado de un primo si existe un número primo p tal que p al cuadrado es igual a n. Se pide implementar
-- contarCuadradosDeUnPrimo dada por la siguiente especificación:

{--problema contarCuadradosDeUnPrimo(d: Z,h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números cuadrados de un primo en el rango [d..h].}
}
Ejemplo: contarCuadradosDeUnPrimo 3 30 debe devolver 3 (porque los números cuadrados de un primo en el rango [3..30] son 4, 9 y 25).--}

contarCuadradosDeUnPrimo::Integer->Integer -> Integer
contarCuadradosDeUnPrimo n m = (contarAux n m (lenLista(listaElementos n m)))

contarAux::Integer->Integer->Integer -> Integer
contarAux n m 0 = 0
contarAux n m j | ((j <= m) && (esCuadradoPrimo(iesimoInt (listaElementos n m) j))) = 1 + contarAux n m (j-1)
                | otherwise                                                         =     contarAux n m (j-1)

iesimoInt::[Integer]->Integer -> Integer
iesimoInt (x:cola) 1 = x
iesimoInt (x:cola) j = (iesimoInt cola (j-1))

listaElementos::Integer->Integer -> [Integer]
listaElementos n m = creaLista n m m

creaLista::Integer->Integer->Integer -> [Integer]
creaLista n _ 0 = []
creaLista n m j | (j == m)          = creaLista n m (j-1) ++ [j]
                | (j < m && j >= n) = creaLista n m (j-1) ++ [j]
                | otherwise         = []

esCuadradoPrimo::Integer -> Bool
esCuadradoPrimo 1 = False
esCuadradoPrimo 2 = False
esCuadradoPrimo 3 = False
esCuadradoPrimo 4 = True
esCuadradoPrimo n | (esPrimo(raiz n)) = True
                  | otherwise = False

raiz::Integer -> Integer
raiz 4 = 2
raiz n = esRaiz n n

esRaiz::Integer->Integer -> Integer
esRaiz n 0 = 0
esRaiz 4 2 = 2
esRaiz n j | (j*j == n) = j
           | (j*j /= n) = esRaiz n (j-1)
           | otherwise  = 0

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 24 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema menorPrimo (s: seq⟨Z⟩) : Z {
  requiere: {Existe algún elemento n que pertenece a s tal que n es primo.}
  asegura: {res es primo y pertenece a s.}
  asegura: {No hay ningún elemento de s que sea primo y que sea menor a res.}
}
Ejemplo: menorPrimo [4, 17, 5, 20, 8, 7]  debe devolver 5.--}

menorPrimo::[Integer] -> Integer
menorPrimo [] = 0
menorPrimo lista = minLista(listaPrimos lista)

listaPrimos::[Integer] -> [Integer]
listaPrimos [] = []
listaPrimos (x:cola) | (esPrimo x) = x : listaPrimos cola
                     | otherwise   = listaPrimos cola

minLista::[Integer] -> Integer
minLista [] = 0
minLista [x] = x
minLista (x:y:cola) | (x <= y) = minLista (x:cola)
                    | (y < x)  = minLista (y:cola)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 25 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema sumaDeMaximosPorColumna(matriz: seq⟨seq⟨Z⟩⟩) : Z {
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud.}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  asegura: {res es la suma de los máximos de cada columna de matriz.}
}
Ejemplo: sumaDeMaximosPorColumna [[10,2],[5,4]]  debe devolver 14.--}

sumaDeMaximosPorColumna::[[Integer]] -> Integer
sumaDeMaximosPorColumna [] = 0
sumaDeMaximosPorColumna m = sumaMaximosAux m (lenLista(fila m 1))

sumaMaximosAux::[[Integer]]->Integer -> Integer
sumaMaximosAux m 1 = maxLista(columna m 1)
sumaMaximosAux m j = maxLista(columna m j) + sumaMaximosAux m (j-1)

columna::[[Integer]]->Integer -> [Integer]
columna m j = columnaAux m (lenMatriz(m)) j -- Elijo la fila 1 como referencia. Si todas las filas no tienen la misma longitud -> no es matriz.
-- Observación: Vale para matrices cuadradas y no cuadradas.

columnaAux::[[Integer]]->Integer->Integer -> [Integer]
columnaAux m 0 j = []
columnaAux m i j | (i <= lenMatriz(m)) = columnaAux m (i-1) j ++ [(elementoMatriz m i j)]
                 | otherwise           = columnaAux m (i-1) j

lenMatriz::[[Integer]] -> Integer
lenMatriz [] = 0
lenMatriz (x:cola) = 1 + lenMatriz cola

elementoMatriz::[[Integer]]->Integer->Integer -> Integer
elementoMatriz (x:resto) i j = iesimoInt (fila (x:resto) i) j

fila::[[Integer]]->Integer -> [Integer]
fila (x:resto) 1 = x
fila (x:resto) j = fila resto (j-1)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Preguntas Teóricas: Indique la opción correcta:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--En Haskell, se dice que una función tiene transparencia referencial cuando:
  1. La función puede cambiar su resultado dependiendo del contexto en el que se evalúa.
  2. El valor de la función depende de su estado interno y puede cambiar durante la ejecución.
  3. La función devuelve siempre el mismo resultado para los mismos argumentos sin importar dónde o cuándo se evalúe.--}

-- La opción correcta es la 3.

{--Si un usuario no cumple con la precondición de la especificación de un programa y el programa no termina (se cuelga):
  1. El usuario tiene derecho a quejarse porque el programador debería haber contemplado ese caso.
  2. El usuario no tiene derecho a quejarse, pero el programa es incorrecto porque no debería colgarse.
  3. El usuario no tiene derecho a quejarse y no importa que el programa se cuelgue para este caso.--}

-- La opción correcta es la 3.

{--Qué ocurre si una definición por pattern matching no contempla todos los casos posibles?
  1. El programa no compila.
  2. Haskell elige un valor por defecto automáticamente.
  3. El programa puede lanzar un error en tiempo de ejecución si se invoca con un patrón no contemplado.--}

-- La opción correcta es la 3.

{--Dado un problema con parámetros c (de tipo Char) y s (de tipo String), cuya única precondición es (esVocal(c) ∨ longitud(s) > 3):
  1. La precondición garantiza que siempre se trabajará con strings no vacíos.
  2. Si c es una consonante y s tiene longitud igual a 2, no se garantiza el comportamiento correcto del programa.
  3. Cualquier combinación de valores de c y s es válida, porque la precondición es una disyunción en vez de una conjunción.--}

-- La opción correcta es la 2.

{--En una definición recursiva, si se omite el caso base:
  1. La función se comporta igual que si el caso base estuviera presente.
  2. El compilador lanza un error de sintaxis.
  3. El programa puede quedar atrapado en una recursión infinita.--}

-- La opción correcta es la 3.

{--Dado un problema con un parámetro s que es una secuencia de enteros, cuya única precondición es |s| > 0:
  1. Una implementación que falla cuando s es vacía puede seguir siendo considerada correcta.
  2. El programa debe verificar dentro del código que s no esté vacía.
  3. El testing debe incluir al menos un caso con s vacía para asegurar robustez.--}

-- La opción correcta es la 1.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————