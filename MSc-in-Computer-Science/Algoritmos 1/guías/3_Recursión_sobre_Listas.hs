
-- ==========================================================================================================================================
-- Práctica 5: Recursión sobre Listas
-- ==========================================================================================================================================

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 1 -- Definir las siguientes funciones sobre listas:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- 1. longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos:

longitud::[t] -> Integer
longitud []       = 0                  -- CB: Si la lista está vacía su longitud es cero
longitud (x:cola) = 1 + longitud(cola) -- Si no, su longitud es 1 + tail(lista) (hago recursión quitando head's)

-- 2. ultimo :: [t] -> t según la siguiente especificación:
{--problema ultimo(s: seq⟨T⟩) : T {
  requiere: {|s| > 0}
  asegura: {resultado = s[|s| − 1]}
}--}

primero::[t] -> t
primero (x:_) = x -- Obtengo el primer elemento (head)

ultimo::[t] -> t
ultimo [x]      = x            -- CB: Si la lista tiene 1 elemento, el último es ese.
ultimo (_:cola) = ultimo(cola) -- Si no, le quito head recursivamente hasta llegar al último.

-- 3. principio :: [t] -> [t] según la siguiente especificación:
{--problema principio(s: seq⟨T⟩) : seq⟨T⟩ {
  requiere: {|s| > 0}
  asegura: {resultado = subseq(s, 0, |s| − 1)}
}--}

principio::[t] -> [t]
principio [_]  = []                      -- CB: Cuando lleguemos al último (a la última head), no lo agregamos.
principio (x:cola) = x : principio(cola) -- Obtenemos head, y agregamos recursivamente más head's.

-- 4. reverso :: [t] -> [t] según la siguiente especificación:
{--problema reverso(s: seq⟨T⟩) : seq⟨T⟩ {
  requiere: {True}
  asegura: {resultado tiene los mismos elementos que s pero en orden inverso.}
}--}

reverso::[t] -> [t]
reverso [x]      = [x]                  -- CB: La inversa de una lista de un elemento es ella misma.
reverso (x:cola) = reverso(cola) ++ [x] -- Si no, obtengo head y la appendeo al final, tomando recursión de tail delante.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 2 -- Definir las siguientes funciones sobre listas:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- 1. pertenece :: (Eq t) => t -> [t] -> Bool según la siguiente especificación:
{--problema pertenece(n: T , s: seq⟨T⟩) : B {
  requiere: {True}
  asegura: {resultado = true ↔ n ∈ s}
}--}

pertenece::(Eq t)=>t->[t] -> Bool
pertenece n [] = False                                -- Caso especial: lista vacía
pertenece n (x:cola) | (x == n)  = True               -- Si el 1° pertenece listo!
                     | otherwise = pertenece n (cola) -- Si no, hago recursión para tail de s.

-- 2. todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero si y solo si todos sus elementos son iguales.

todosIguales::(Eq t)=>[t] -> Bool
todosIguales []  = True                                        -- Caso especial: lista vacía.
todosIguales [x] = True                                        -- CB: Un único elemento.
todosIguales (x:cola) | (x /= head(cola)) = False              -- Si el 1° no es igual al 2° -> False.
                      | otherwise         = todosIguales(cola) -- Si no, quito el primero y hago recursión.

-- 3. todosDistintos :: (Eq t) => [t] -> Bool según la siguiente especificación:
{--problema todosDistintos(s: seq⟨T⟩) : B {
  requiere: {True}
  asegura: {resultado = False ↔ existen dos posiciones distintas de s con igual valor.}
}--}

todosDistintos::(Eq t)=>[t] -> Bool
todosDistintos []  = True                                           -- Caso especial: lista vacía.
todosDistintos [x] = True                                           -- CB: Un único elemento.
todosDistintos (x:cola) | (pertenece x cola) = False                -- Si el primer elemento está en tail -> False.
                        | otherwise          = todosDistintos(cola) -- Si no, lo quito y hago recursión.

-- 4. hayRepetidos :: (Eq t) => [t] -> Bool según la siguiente especificación:
{--problema hayRepetidos(s: seq⟨T⟩) : B {
  requiere: {True}
  asegura: {resultado = true ↔ existen dos posiciones distintas de s con igual valor.}
}--}

hayRepetidos::(Eq t)=>[t] -> Bool
hayRepetidos []  = False                                        -- Caso especial: lista vacía.
hayRepetidos [x] = False                                        -- CB: Un único elemento.
hayRepetidos (x:cola) | (pertenece x cola) = True               -- Si el primer elemento está en tail -> True.
                      | otherwise          = hayRepetidos(cola) -- Si no, lo quito y hago recursión.

-- 5. quitar :: (Eq t) => t -> [t] -> [t], que dados un entero n y una lista xs, elimina la primera aparición de x en la lista xs (de haberla).

-- Esta función funcionará siempre que n pertenece a la lista:
nuevaLista::(Eq t)=>t->[t] -> [t]
nuevaLista n (x:cola) | (x == n)  = cola                    -- Si n es el primero, listo! el resultado es tail.
                      | otherwise = x : (nuevaLista n cola) -- Si no, agrego head al inicio y sumo como cola el proceso recursivo.

quitar::(Eq t)=>t->[t] -> [t]
quitar n [] = []                                               -- Caso especial: si la lista es vacía no hay nada que quitar.
quitar n lista | (not(pertenece n lista)) = lista              -- Si n no pertenece a la lista -> la lista queda igual.
               | otherwise                = nuevaLista n lista -- Si n sí pertenece a la lista, hacemos una nueva lista sin n.

-- 6. quitaTodo :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones de x en la lista xs
-- (de haberlas). Es decir:
{--problema quitaTodo(e: T, s: seq⟨T⟩) : seq⟨T⟩ {
  requiere: {True}
  asegura: {resultado es igual a s pero sin el elemento e.}
}--}

quitaTodo::(Eq t)=>t->[t] -> [t]
quitaTodo n [] = []                                                                    -- CB: si la lista es vacía no hay nada que quitar.
quitaTodo n lista | (not(pertenece n (quitar n lista))) = quitar n lista               -- Si al quitar n 1 vez, n ya no está en lista => listo!
                  | otherwise                           = quitaTodo n (quitar n lista) -- Si no, repito el proceso (ahora lista tiene 1 menos).

-- 7. quitaRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, eliminando las repeticiones adicionales.

quitaRepetidos::(Eq t)=>[t] -> [t]
quitaRepetidos [] = []                                                              -- CB: si la lista es vacía no hay nada que quitar.
quitaRepetidos (x:cola) | (pertenece x cola) = x : quitaRepetidos(quitaTodo x cola) -- Si x en cola lo obtengo, quito los demás y hago recursión.
                        | otherwise          = x : quitaRepetidos cola              -- Si no, hago [x,recursión(cola)] para ver otros elementos.

-- 8. mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero si y solo si ambas listas contienen los mismos
-- elementos, sin tener en cuenta repeticiones, es decir:
{--problema mismosElementos(s: seq⟨T⟩, r: seq⟨T⟩) : B {
  requiere: {True}
  asegura: {resultado = true ↔ todo elemento de s pertenece r y viceversa.}
}--}

-- Creo una función que determina si es cierto o no que todos los elementos de la primera lista están incluidos en la segunda lista:
estanTodos::(Eq t)=>[t]->[t] -> Bool
estanTodos [] _ = True                                      -- CB: Si la primera lista es vacía => el vacío está incluido en la segunda.
estanTodos l1 l2 | (not(pertenece (ultimo l1) l2)) = False  -- Si el 1° elemento de l1 no está en l2 -> False!
                 | otherwise = estanTodos (principio l1) l2 -- Si está, lo quito y repito (recursión).

mismosElementos::(Eq t)=>[t]->[t] -> Bool
mismosElementos l1 l2 = ((estanTodos l1 l2) && (estanTodos l2 l1))

-- 9. capicua :: (Eq t) => [t] -> Bool según la siguiente especificación:
{--problema capicua(s: seq⟨T⟩) : B {
  requiere: {True}
  asegura: {(resultado = true) ↔ (s = reverso(s))}
}
Por ejemplo capicua ['a','c','b','b','c','a'] es true, capicua ['a','c','b','d','a'] es false.--}

capicua::(Eq t)=>[t] -> Bool
capicua []  = True                                                               -- Caso Especial: consideramos lista vacía como capicua.
capicua [x] = True                                                               -- CB: Un único elemento es capicúa.
capicua lista | (primero lista == ultimo lista) = capicua(tail(principio lista)) -- Si el 1° elemento = al último, los quito y hago recursión.
              | otherwise                       = False                          -- Si alguno no coincidió, False!

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 3 -- Definir las siguientes funciones sobre listas de enteros:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
--1. sumatoria :: [Integer] -> Integer según la siguiente especificación:
{--problema sumatoria(s: seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: {resultado = \sum_{i=0}^{|s|-1} s[i]}
}--}

sumatoria::[Integer] -> Integer
sumatoria [] = 0                         -- CB: Si la lista es vacía, la suma es 0.
sumatoria (x:cola) = x + sumatoria(cola) -- Si no, sumo el 1° elemento y hago recursión sobre la cola.

-- 2. productoria :: [Integer] -> Integer según la siguiente especificación:
{--problema productoria(s: seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: {resultado = \prod_{i=0}^{|s|−1} s[i]}
}--}

productoria::[Integer] -> Integer
productoria [] = 1                         -- CB: Si la lista es vacía devuelve 1.
productoria (x:cola) = x*productoria(cola) -- Si no, multiplico el primero por productoria(cola) (recursión).

-- 3. maximo :: [Integer] -> Integer según la siguiente especificación:
{--problema maximo(s: seq⟨Z⟩) : Z {
  requiere: {|s| > 0}
  asegura: {resultado ∈ s ∧ todo elemento de s es menor o igual a resultado.}
}--}

maximo::[Integer] -> Integer
maximo []  = 0                                  -- CB: Si la lista es vacía devuelve 0.
maximo [x] = x                                  -- Si tiene un elemento, devuelve el elemento.
maximo (x:y:cola) | (x >= y)  = maximo (x:cola) -- Si el 1° >= 2° -> efectúa recursión entre el máximo (el primero: x) y la cola.
                  | otherwise = maximo (y:cola) -- Si no, efectúa recursión entre el máximo (el segundo: y) y la cola.

minimo::[Integer] -> Integer
minimo [] = 0                                   -- CB: Si la lista es vacía devuelve 0.
minimo [x] = x                                  -- Si tiene un elemento, devuelve el elemento.
minimo (x:y:cola) | (x <= y)  = minimo (x:cola) -- Si el 1° >= 2° -> efectúa recursión entre el máximo (el primero: x) y la cola.
                  | otherwise = minimo (y:cola) -- Si no, efectúa recursión entre el máximo (el segundo: y) y la cola.

-- 4. sumarN :: Integer -> [Integer] -> [Integer] según la siguiente especificación:
{--problema sumarN(n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {True}
  asegura: {|resultado| = |s| ∧ cada posición de resultado contiene el valor que hay en esa posición en s sumado n.}
}--}

sumarN::Integer->[Integer] -> [Integer]
sumarN n [] = []                              -- CB: Si la lista es vacía no puedo sumarle nada.
sumarN n (x:cola) = ((x+n) : (sumarN n cola)) -- Si no, le sumo n al 1° elemento y hago recursión con cola.

-- 5. sumarElPrimero :: [Integer] -> [Integer] según la siguiente especificación:
{--problema sumarElPrimero(s: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {|s| > 0}
  asegura: {resultado = sumarN (s[0], s)}
}
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4] --}

sumarElPrimero::[Integer] -> [Integer]
sumarElPrimero [] = []                      -- CB: Si la lista es vacía no hace nada.
sumarElPrimero (x:cola) = sumarN x (x:cola) -- Sumo el 1° elemento a toda la lista (x:cola).

-- 6. sumarElUltimo :: [Integer] -> [Integer] según la siguiente especificación:
{--problema sumarElUltimo(s: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {|s| > 0}
  asegura: {resultado = sumarN (s[|s| − 1], s)}
}
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6] --}

sumarElUltimo::[Integer] -> [Integer]
sumarElUltimo [] = []                             -- CB: Si la lista es vacía no hace nada.
sumarElUltimo lista = sumarN (ultimo lista) lista -- Sumo el último elemento de lista a toda la lista.

-- 7. pares :: [Integer] -> [Integer] según la siguiente especificación:
{--problema pares(s: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {True}
  asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones.}
}
Por ejemplo pares [1,2,3,5,8,2] da [2,8,2] --}

pares::[Integer] -> [Integer]
pares [] = []                                     -- CB: Si la lista está vacía es vacía.
pares (x:cola) | (mod x 2 == 0) = x : pares(cola) -- Si el 1° elemento es par, lo appendeo (en 1° lugar) a la lista de efectuar recursión(cola).
               | otherwise      = pares(cola)     -- Si el 1° elemento no es par, lo descarto, y hago recursión sobre la cola.

-- 8. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un número natural n distinto de cero y una lista xs, devuelve una lista con
-- los elementos de xs múltiplos de n.

multiplosDeN::Integer->[Integer] -> [Integer]
multiplosDeN n [] = []                                               -- CB: Si no hay elementos, la lista sigue vacía.
multiplosDeN n (x:cola) | (mod x n == 0) = x : multiplosDeN n (cola) -- Si el 1° elemento es múltiplo de n, lo appendeo y hago recursión(cola).
                        | otherwise      =     multiplosDeN n (cola) -- Si no, lo descarto y hago recursión sobre cola.

-- 9. ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente.

ordenar::[Integer] -> [Integer]
ordenar [] = []                                                       -- CB: Si la lista es vacía no hay nada que ordenar.
ordenar lista = minimo(lista) : ordenar(quitar (minimo(lista)) lista) -- Si no, coloco mín al principio y recursión sobre cola. En cola,
                                                                      -- ahora la lista tendrá un elemento menos, el mínimo.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 4 -- Definir las siguientes funciones sobre listas de Chars:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- 1. sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco
-- en la lista resultado.

sacarBlancosRepetidos::[Char] -> [Char]
sacarBlancosRepetidos []  = []                                                                -- CB: Si la lista es vacía no pasa nada.
sacarBlancosRepetidos [x] = [x]                                                               -- CB: Si hay un solo elmento queda igual.
sacarBlancosRepetidos (x:y:cola) | (x == ' ' && y == ' ') = sacarBlancosRepetidos(x:cola)     -- Si 1°=2°=' ' => quito 1 y hago recursión.
                                 | otherwise              = x : sacarBlancosRepetidos(y:cola) -- Si no, me quedo el 1° y pruebo recursión.

-- 2. contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.

contarPalabras::[Char] -> Integer
contarPalabras []  = 0                                                          -- CB: Lista vacía no tiene palabras.
contarPalabras " " = 0                                                          -- Caso especial 1: un espacio no es una palabra.
contarPalabras [x] = 1                                                          -- Caso especial 2: una palabra sola da 1.
contarPalabras (x:y:cola) | (x /= ' ' && y == ' ') = 1 + contarPalabras(cola)   -- Si 1°=letra y 2°=' ' cuento 1 palabra y hago recursión.
                          | otherwise              =     contarPalabras(y:cola) -- Si no, si x=y=letra, sigo probando => recursión(cola).

-- 3. palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.

palabras::[Char] -> [[Char]]
palabras [] = []                                        -- CB: Lista vacía no tiene palabras.
palabras (' ':cola) = palabras cola                     -- Si el primer char es un espacio, lo omitimos -> sigo con cola.
palabras cola = palabra : palabras resto                -- Si no, guardamos la primer palabra,
              where (palabra,resto) = tomarPalabra cola -- donde tomarPalabra extrae la primer palabra y devuelve el resto del string.

-- Creamos una función auxiliar que extrae la primer palabra de un string, y la devuelve junto al resto del string.
tomarPalabra::[Char] -> ([Char], [Char])
tomarPalabra [] = ([], [])                                      -- CB: Si la lista está vacía, ambas expresiones son vacías.
tomarPalabra (' ':cola) = ([],cola)                             -- Si el primer char= ' ', termino palabra actual y devuelvo resto del string.
tomarPalabra (x:cola) = (x : palabra,resto)                     -- Si no, agrego el char a la palabra actual y continuo procesando el string.
                      where (palabra,resto) = tomarPalabra cola -- Hago recursión sobre cola del string para armar palabra y obtengo el resto.

-- 4. palabraMasLarga :: [Char] -> [Char], que dada una lista de caracteres devuelve su palabra más larga.

-- Creo una función len que calcula la longitud de una palabra:
len::[Char] -> Integer
len [] = 0
len (x:cola) = 1 + len cola

-- Y una función auxiliar que recibe una lista de palabras y devuelve cual de ellas es la más larga:
palabraMasLargaAux::[[Char]] -> [Char]
palabraMasLargaAux []  = []                                                        -- CB: Lista vacía no tiene palabra más larga.
palabraMasLargaAux [x] = x                                                         -- Caso especial: listas con 1 palabra -> palabra única.
palabraMasLargaAux (x:y:cola) | ((len x) >= (len y)) = palabraMasLargaAux (x:cola) -- Si la primera > segunda recursión con primera:resto.
                              | otherwise            = palabraMasLargaAux (y:cola) -- Si no, recursión con segunda:resto.

palabraMasLarga::[Char] -> [Char]
palabraMasLarga palabra = palabraMasLargaAux(palabras palabra) -- Obtengo la palabra más larga.

-- 5. aplanar :: [[Char]] -> [Char], que a partir de una lista de palabras arma una lista de caracteres concatenándolas.

aplanar::[[Char]] -> [Char]
aplanar [] = []                      -- CB: No hay nada que aplanar.
aplanar (x:cola) = x ++ aplanar cola -- Concateno las palabras.

-- 6. texto :: [[Char]] -> [Char], que a partir de una lista de palabras, arma una lista de caracteres concatenándolas e insertando un blanco
-- entre cada palabra.

texto::[[Char]] -> [Char]
texto [] = []                                          -- CB: No hay nada en texto (ó, si ya no hay más palabras, no agrego nada).
texto (x:cola) | (cola /= []) = x ++ " " ++ texto cola -- Si en cola aún hay palabras, agrego un espacio entre palabras.
               | otherwise    = x        ++ texto cola -- Si no, no.

-- 7. textoConNespacios :: [[Char]] -> Integer -> [Char], que a partir de una lista de palabras y un entero n, arma una lista de caracteres
-- concatenándolas e insertando n blancos entre cada palabra (n debe ser no negativo).

-- Creo una función auxiliar que dado un número n, devuelve una "palabra" con n-cantidad de espacios.
nEspacios::Integer -> [Char]
nEspacios 0 = []                     -- CB: Si n=0 la lista es vacía.
nEspacios 1 = " "                    -- CB: Si n=1 solo hay 1 espacio.
nEspacios n = " " ++ nEspacios (n-1) -- Hago recursión hasta llegar a 0

textoConNespacios::[[Char]]->Integer -> [Char]
textoConNespacios [] _ = []                                                                  -- CB: Lista vacía no tiene palabras.
textoConNespacios (x:cola) n | (cola /= []) = x ++ (nEspacios n) ++ textoConNespacios cola n -- Mientras haya palabras, agrego n-espacios.
                             | otherwise    = x                  ++ textoConNespacios cola n -- Si ya no hay más palabras, no agrego espacio.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 5 -- Definir las siguientes funciones sobre listas:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- 1. sumaAcumulada :: (Num t) => [t] -> [t] según la siguiente especificación:
{--problema sumaAcumulada(s: seq⟨T⟩) : seq⟨T⟩ {
  requiere: {T es un tipo numérico}
  requiere: {cada elemento de s es mayor estricto que cero.}
  asegura: {|s| = |resultado| ∧ el valor en la posición i de resultado es \S{k=0}{i}{s[k]}.}
}
Por ejemplo sumaAcumulada [1, 2, 3, 4, 5] es [1, 3, 6, 10, 15].--}

-- Creo una función auxiliar que tiene un parámetro adicional que utilizamos para sumar de forma acumulada:
sumaAcumuladaAux::(Num t)=>t->[t] -> [t]
sumaAcumuladaAux _ [] = []                                            -- CB: Si la lista está vacía queda igual.
sumaAcumuladaAux n (x:cola) = (n + x) : sumaAcumuladaAux (n + x) cola -- Considerando n=0 -> Appendeo (0+x) : (0+x+proximo) recursivamente.

sumaAcumulada::(Num t)=>[t] -> [t]
sumaAcumulada lista = sumaAcumuladaAux 0 lista -- Arrancamos a sumar con n=0.

-- 2. descomponerEnPrimos :: [Integer] -> [[Integer]] según la siguiente especificación:
{--problema descomponerEnPrimos(s: seq⟨Z⟩) : seq⟨seq⟨Z⟩⟩ {
  requiere: {Todos los elementos de s son mayores a 2.}
  asegura: {|resultado| = |s|}
  asegura: {todos los valores en las listas de resultado son números primos.}
  asegura: {multiplicar todos los elementos en la lista en la posición i de resultado es igual al valor en la posición i de s.}
}
Por ejemplo descomponerEnPrimos [2, 10, 6] es [[2], [2, 5], [2, 3]].--}

listaDivisores::Integer->Integer -> [Integer] -- Primero, calculamos la lista de divisores de un número n
listaDivisores n 1 = [1]
listaDivisores n j | (mod n j == 0) = listaDivisores n (j-1) ++ [j]
                   | otherwise      = listaDivisores n (j-1)

lenLista::[Integer] -> Integer -- Creamos una función auxiliar que calcula la longitud de una lista
lenLista [] = 0
lenLista (x:cola) = 1 + lenLista cola

esPrimo::Integer -> Bool -- Creamos esPrimo, que usa lenLista y listaDivisores, y determina si n es primo.
esPrimo 0 = False
esPrimo 1 = False
esPrimo n | (lenLista(listaDivisores n n) > 2) = False
          | otherwise = True

factoresPrimos::Integer->Integer -> [Integer] -- Creamos una función que determina los factores primos de n
factoresPrimos 1 _ = []
factoresPrimos n j | ((mod n j == 0) && (esPrimo j)) = j : factoresPrimos (div n j) j
                   | j > n                           = []
                   | otherwise                       = factoresPrimos n (j+1)

iesimo::[Integer]->Integer -> Integer -- Creamos la función auxiliar iesimo, que devuelve el i-ésimo elemento de una lista
iesimo (x:cola) 1 = x
iesimo (x:cola) j = iesimo cola (j-1)

descomponerEnPrimosAux::[Integer]->Integer -> [[Integer]] -- Usamos una función auxiliar
descomponerEnPrimosAux _ 0 = []
descomponerEnPrimosAux lista j = descomponerEnPrimosAux lista (j-1) ++ [factoresPrimos (iesimo lista j) 2]

descomponerEnPrimos::[Integer] -> [[Integer]] -- Calculamos la descomposición en factores primos de los números de la lista de enteros.
descomponerEnPrimos lista = descomponerEnPrimosAux lista (lenLista lista)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 6 -- En este ejercicio trabajaremos con la lista de contactos del teléfono.
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
type Texto        = [Char]
type Nombre       = Texto
type Telefono     = Texto
type Contacto     = (Nombre, Telefono)
type ContactosTel = [Contacto]

{--Sugerencia: Implementar las funciones auxiliares elNombre y elTelefono para que dado un Contacto devuelva el dato del nombre y el teléfono
respectivamente.--}

-- A) Implementar una función que diga si una persona aparece en la lista de contactos del teléfono:
-- enContactos :: Nombre -> ContactosTel -> Bool

enContactos::Nombre->ContactosTel -> Bool -- Notar que el tipado es: [Char] -> [([Char],[Char])] -> Bool
enContactos _ [] = False                                                     -- CB: Si la lista está vacía, no está el contacto.
enContactos persona ((x,_):cola) | (x == persona) = True                     -- Si el 1° elem de la 1° tupla es persona -> listo! -> True
                                 | otherwise      = enContactos persona cola -- Si no, busco el 1° elem de la 2°,3°,... tupla (recursión(cola)).

-- B) Implementar una función que agregue una nueva persona a mis contactos, si esa persona está ya en mis contactos entonces actualiza el
-- teléfono. nuevoContacto :: Contacto -> ContactosTel -> ContactosTel

nuevoContacto::Contacto->ContactosTel -> ContactosTel
nuevoContacto (contacto,telefono) [] = [(contacto,telefono)]                                                         -- CB: Si no está lo agrego.
nuevoContacto (contacto,telefono) ((x,tel):cola) | (x == contacto) = (x,telefono) : cola                             -- Si está, actualizo tel.
                                                 | otherwise       = (x,tel):(nuevoContacto (contacto,telefono) cola)-- Si no, sigo buscando.

-- C) Implementar una función que dado un nombre, elimine un contacto de mis contactos. Si esa persona no está no hace nada.
-- eliminarContacto :: Nombre -> ContactosTel -> ContactosTel

eliminarContacto::Nombre->ContactosTel -> ContactosTel
eliminarContacto _ [] = []                                                                        -- CB: Si no hay contactos => nada a eliminar.
eliminarContacto nombre ((x,_):cola) | (x == nombre) = cola                                       -- Si encontré contacto, devuelvo lista sin él.
                                     | otherwise     = (x,numero) : (eliminarContacto nombre cola)-- Si no, sigo buscando (recursión con cola).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 7 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--En este ejercicio trabajaremos con lockers de una facultad. Para resolverlo usaremos un tipo MapaDelockers que será una secuencia de locker.
Cada locker es una tupla con la primera componente correspondiente al número de identificación, y la segunda componente el estado. El estado es
a su vez una tupla cuya primera componente dice si esta ocupado (False) o libre (True), y la segunda componente es un texto con el código de
ubicación del locker.

Por ejemplo, un posible mapa de lockers puede ser:
lockers = [
  (100,(False,"ZD39I")),
  (101,(True,"JAH3I")),
  (103,(True,"IQSA9")),
  (105,(True,"QOTSA")),
  (109,(False,"893JJ")),
  (110,(False,"99292"))
]--}

type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

-- A) Implementar existeLocker :: Identificacion -> MapaDeLockers -> Bool, una función para saber si un locker existe en la facultad.

existeLocker::Identificacion->MapaDeLockers -> Bool
existeLocker _ [] = False                                                 -- CB: Si no hay lockers, no hay identificación.
existeLocker id ((numero,_):cola) | (numero == id) = True                 -- Si el la identificación coincide con algún número, existe!
                                  | otherwise      = existeLocker id cola -- Si no, seguimos buscando (recursión sobre cola)

-- B) Implementar ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion, una función que dado un locker que existe en la facultad,
-- me dice la ubicación del mismo.

ubicacionDelLocker::Identificacion->MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = ""                                                            -- CB: Si no hay lockers, no hay ubicación.
ubicacionDelLocker id ((x,(_,ubicacion)):cola) | (x == id) = ubicacion                  -- Si la id es locker actual => devuelvo la ubicación.
                                               | otherwise = ubicacionDelLocker id cola -- Si no, sigo buscando en mapa de lockers (recursión).

-- C) Implementar libreLocker :: Identificacion -> MapaDeLockers -> Bool, una función que dado un locker que existe en la facultad, me devuelve
-- Verdadero si esta libre.

libreLocker::Identificacion->MapaDeLockers -> Bool
libreLocker _ [] = False                                               -- CB: Si no hay lockers, no hay ninguno disponible.
libreLocker id ((x,(estado,_)):cola) | (x == id) = estado              -- Si la id es locker actual, devuelve disponibilidad (true ó false).
                                     | otherwise = libreLocker id cola -- Si no, sigue buscando en el mapa de lockers (recursión sobre cola).

-- D) Implementar usarLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers, una función que dado un locker que existe en la facultad, y
-- está libre, lo ocupa.

usarLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
usarLocker _ [] = []                                                                               -- CB: Sin lockers => nada para ocupar.
usarLocker id ((x,(False,ubicacion)):cola) = (x,(False,ubicacion)) : usarLocker id cola            -- CB: Si está ocupado, no puede usarse.
usarLocker id ((x,(True, ubicacion)):cola) | (x == id) = (x,(False,ubicacion)) : cola              -- Si la id es locker libre actual, lo uso.
                                           | otherwise = (x,(True, ubicacion)) : usarLocker id cola-- Si no, sigo buscando (recursión cola).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————