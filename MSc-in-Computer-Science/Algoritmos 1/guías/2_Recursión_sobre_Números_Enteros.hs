
-- ==========================================================================================================================================
-- Práctica 4: Recursión sobre Números Enteros
-- ==========================================================================================================================================

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 1 -- Implementar la función fibonacci :: Integer -> Integer que devuelve el i-ésimo número de Fibonacci.
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Recordar que la secuencia de Fibonacci se define como:
-- fib(n) = 0 si n=0   ;    1 si n=1  ;    fib(n-1) + fib(n-2) else

-- Usamos Pattern-Matching fácilmente:
fibonacci::Integer -> Integer
fibonacci 0 = 0                               -- CB 1
fibonacci 1 = 1                               -- CB 2
fibonacci n = fibonacci(n-1) + fibonacci(n-2) -- Paso recursivo

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 2 -- Implementar una función parteEntera :: Float -> Integer según la siguiente especificación:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema parteEntera (x : R) : Z {
     requiere: {x ≥ 0}
     asegura: {resultado ≤ x < resultado + 1.}
}--}

{--Este problema nos está pidiendo que dado un número real x que contiene decimales, la función devuelva el entero más cercano a éste y que
sea menor que el número, es decir, la función redondea el número x hacia abajo siempre.
Ejemplo:
     parteEntera 12.141567 = 12
     parteEntera 98.983125 = 98--}

{--Veamos el caso n-ésimo:
     parteEntera 1.5 = 1 (por ej. tomo 1.5)
     parteEntera 2.5 = 2
     ...
     parteEntera n = 1 + parteEntera (n-1)
Vemos que la relación entre el paso n-ésimo y el anterior es únicamente sumar 1.--}

parteEntera::Float -> Integer
parteEntera x | (x < 1)   = 0                    -- CB: Asumimos que x >= 0
              | otherwise = 1 + parteEntera(x-1) -- Sumamos 1

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 3 -- 
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar la función esDivisible :: Integer -> Integer -> Bool que dados dos números naturales determina si el primero es
-- divisible por el segundo. No está permitido utilizar las funciones mod ni div.

{-- Especificación:
problema esDivisible (n : Z, m : Z) : Bool {
     requiere: {Los números n y m son mayores a cero (n > 0 y m > 0), y el primer número es mayor que el segundo (n >= m).}
     asegura: {res indica si es verdadero o no que el segundo número (m) divide al primero (n), es decir, \ex k \in \bb{Z} : n = k . m}
}--}

{--Queremos saber si el número n es divisible por m para algún valor k. Esto indica que debemos recorrer los valores de k empezando por 0 ó 1.
Ejemplo: Supongamos que quiero resolver  esDivisible 18 3. Podemos resolverlo si hacemos lo siguiente. Arrancamos por dichos valores de n y m,
y le vamos quitando a n el valor m:
     esDivisible (18-3) 3
     esDivisible (15-3) 3
     esDivisible (12-3) 3
     esDivisible (9-3) 3
     esDivisible (6-3) 3
     esDivisible (3-3) 3
     esDivisible 0 3     => 0 es divisible por cualquier número => 18 es divisible por 3 => TRUE.
Si n fuera un número no divisible por 3 (por ej. 19), el valor de n será siempre menor que m => FALSE, pues un número no es divisible por un
número mayor que él.--}

esDivisible::Integer->Integer -> Bool
esDivisible n m | (n == 0)  = True                -- CB 1: Existe un k tal que substraer k-veces el número m a n, nos da 0 (n = k*m)
                | (n < m)   = False               -- CB 2: No existe un k que cumpla lo pedido (\nex k : n = k*m)
                | otherwise = esDivisible (n-m) m -- Paso recursivo

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 4 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar la función sumaImpares :: Integer -> Integer que dados n \in \bb{N} sume los primeros n números impares. Por ej.,
-- sumaImpares 3 -> 1 + 3 + 5 = 9.

{-- Especificación:
problema sumaImpares (n : Z) : Z {
     requiere: {El número n es un número natural mayor o igual a 1.}
     asegura: {res indica únicamente la suma de los primeros n-números naturales impares.}
}--}

{--Veamos:
     1         = sumaImpares (1)
     1         = sumaImpares (2) = sumaImpares (1)
     1 + 3     = sumaImpares (3) = sumaImpares (2) + 3
     1 + 3     = sumaImpares (4) = sumaImpares (3)
     1 + 3 + 5 = sumaImpares (5) = sumaImpares (4) + 5
     ...,
     Es decir, se cumple que:

     sumaImpares (n) = sumaImpares (n-1) + n    <=> n es impar,
     sumaImpares (n) = sumaImpares (n-1)        <=> n es par.--}

sumaImpares::Integer -> Integer
sumaImpares n | (n == 1) = 1                          -- CB.
              | (mod n 2 == 0) = sumaImpares(n-1)     -- Condición n par.
              | (mod n 2 /= 0) = n + sumaImpares(n-1) -- Condición n impar.

{--Si quisiéramos en cambio:
     0         = sumaPares(0)
     0         = sumaPares(1) = sumaPares(0)
     2         = sumaPares(2) = sumaPares(1) + 2
     2         = sumaPares(3) = sumaPares(2)
     2 + 4     = sumaPares(4) = sumaPares(3) + 4
     2 + 4     = sumaPares(5) = sumaPares(4)
     2 + 4 + 6 = sumaPares(6) = sumaPares(5) + 6
Tenemos que sumar n cuando n es par, y no sumarlo cuando n es impar (al revés):--}

sumaPares::Integer -> Integer
sumaPares n | (n == 0) = 0
            | (mod n 2 /= 0) = sumaPares(n-1)
            | (mod n 2 == 0) = sumaPares(n-1) + n

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 5 -- Implementar la función medioFactorial :: Integer -> Integer que dado n \in \bb{N} calcula n!! = n(n−2)(n−4)...
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

{--problema medioFactorial (n : Z) : Z {
     requiere: {n ≥ 0}
     asegura: {resultado = \prod_{i=0}^{\floor{(n-1)/2}} (n-2i)}
}
Por ejemplo:
     medioFactorial 10 -> 10*8*6*4*2 -> 3840.
     medioFactorial 9 -> 9*7*5*3*1 -> 945. 
     medioFactorial 0 -> 1.--}

-- Uso Pattern-Matching (solo por gusto):
factorial::Integer -> Integer
factorial 0 = 1                -- Caso especial
factorial 1 = 1                -- Caso base
factorial n = n*factorial(n-1) -- Paso recursivo

medioFactorial::Integer -> Integer
medioFactorial 0 = 1                     -- Caso especial
medioFactorial 1 = 1                     -- Caso Base
medioFactorial n = n*medioFactorial(n-2) -- Paso recursivo

-- La única diferencia de la función factorial con la función medio factorial es que entre el paso n-ésimo y el paso anterior, una (factorial)
-- resta 1, y la otra (medioFactorial) resta 2, independientemente de si el número n es par o impar.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 6 -- Implementar la función todosDigitosIguales :: Integer -> Bool, cuya especificación es de la forma:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

{--problema todosDigitosIguales (n: Z) : B {
     requiere: {n > 0}
     asegura: {resultado = True si y solo si todos los dígitos de n son iguales.}
}--}

{-- Podemos ver que, dado n un número entero:
     1. Si hacemos (mod n 10), podemos obtener el último dígito del número n.
     2. Si hacemos (div n 10), podemos quitarle el último dígito al número n.--}

{--Ejemplo:
     todosDigitosIguales 2111 -> 1
     todosDigitosIguales 211  -> 1 =  1 => True
     todosDigitosIguales 21   -> 1 =  1 => True
     todosDigitosIguales 2    -> 2 /= 1 => False.--}

todosDigitosIguales::Integer -> Bool
todosDigitosIguales n | (n < 10) = True                           -- Si n tiene un solo dígito, los dígitos son iguales (hay uno solo).
                      | (mod n 10 /= mod (div n 10) 10) = False   -- Si el 1° dígito no es igual al 2° dígito -> False.
                      | otherwise = todosDigitosIguales(div n 10) -- Si no fue False, fue True => le quitamos el 1° dígito a n y repetimos.

{-- Si llegamos a la tercera guarda, quiere decir lo siguiente. Se cumplió que n > 10, y no se cumplió que 1° /= 2° dígito, es decir, el primer
dígito y el segundo son iguales => not False = TRUE. Como el primer y el segundo dígito coinciden, ahora queremos seguir probando si el resto
de dígitos coinciden con el primero y el segundo => otherwise = todosDigitosIguales (div n 10) está quitando el 1° dígito del número para
chequear recursivamente el 2° con el 3°, y luego el 3° con el 4°, y así sucesivamente hasta llegar al caso base n < 10.--}

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 7 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar la función iesimoDigito :: Integer -> Integer -> Integer que dado un n (n\in\bb{Z}) mayor o igual a cero y un i (i\in\bb{Z})
--mayor o igual a 1 y menor o igual a la cantidad de dígitos de n, devuelve el i-ésimo dígito de n. Las especificaciones son:

{--problema iesimoDigito (n: Z, i: Z) : Z {
     requiere: {n ≥ 0 ∧ 1 ≤ i ≤ cantidadDigitos(n)}
     asegura: {res = (n div 10^{cantidadDigitos(n)−i}) mod 10}
}
problema cantidadDigitos (n: Z) : N {
     requiere: {n ≥ 0}
     asegura: {n = 0 → resultado = 1}
     asegura: {n = 0 → (n div 10^{res−1} > 0 ∧ n div 10^{res} = 0)}
}--}

-- Considerando que contamos desde 1 en adelante (hasta cantidadDigitos(n)), y que lo hacemos desde izquierda a derecha, podemos escribir,
--utilizando la función auxiliar cantidadDigitos, a la función iesimoDigito de la forma:
iesimoDigito::Integer->Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantidadDigitos(n) - i))) 10

cantidadDigitos::Integer -> Integer
cantidadDigitos n | (n < 10)  = 1                             -- CB
                  | otherwise = 1 + cantidadDigitos(div n 10) -- Si n tiene más de 1 dígito, calculo cantDígitos(n con 1 díg. menos) y sumo 1.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 8 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar la función sumaDigitos :: Integer -> Integer que calcula la suma de dígitos de un número natural. Para esta
--función pueden utilizar div y mod.

{--problema sumaDigitos (n: Z) : Z {
     requiere: {n es un número natural.}
     asegura: {res es la operación de sumar todos los dígitos del número natural n.}
}--}

sumaDigitos::Integer -> Integer
sumaDigitos n | (n < 10)  = n                                  -- CB: Si n tiene un solo dígito, ése es el dígito.
              | otherwise = (mod n 10) + sumaDigitos(div n 10) -- Si no, obtengo el 1° dígito (mod n 10), y calculo sumaDigitos(n menos el 1°).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 9 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar una función esCapicua :: Integer -> Bool que dado n \in \bb{N}_{>=0} determina si n es un número capicúa.

{--problema esCapicua (n: Z) : B {
     requiere: {n es un número natural mayor o igual a cero.}
     asegura: {res determina si es verdadero o no que el número n es capicúa.}
}--}

esCapicua::Integer -> Bool
esCapicua n | (cantidadDigitos n < 2) = True                                       -- CB: Si el número tiene 1 dígito ya es capicúa.
            | (iesimoDigito n 1 /= iesimoDigito n (cantidadDigitos n)) = False     -- Si el 1° dígito no coincide con el último => no capicúa.
            | otherwise = esCapicua(div (mod n (10^((cantidadDigitos n) - 1))) 10) -- Si el 1° dígito = último, los quito y repito.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 10 -- Especificar, implementar y dar el tipo de las siguientes funciones:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- A) f1(n)   = \S{i=0}{n}{2^i}  \ptd n \in \bb{N}_0
-- B) f2(n,q) = \S{i=1}{n}{q^i}  \ptd n \in \bb{N}, q \in \bb{R}
-- C) f3(n,q) = \S{i=1}{2n}{q^i} \ptd n \in \bb{N}_0, q \in \bb{R}
-- D) f4(n,q) = \S{i=n}{2n}{q^i} \ptd n \in \bb{N}_0, q \in \bb{R}

-- A) Especificación:
{--problema f1 (n : Z) : Z {
     requiere: {n es un número natural mayor o igual a cero.}
     asegura: {res es la sumatoria \S{i=0}{n}{2^i}.}
}--}

{--\S{i=0}{n}{2^i} = 2^0 + 2^1 + 2^2 + ... + 2^n
                   =   1 +   2 +   4 + ... + 2^n--}

f1::Integer -> Integer
f1 n | (n == 0)  = 2^0           -- CB: si n = 0 -> 2^0 = 1.
     | otherwise = 2^n + f1(n-1) -- Si no, el resultado es 2^n + los términos más pequeños (efectuamos n-1 con recursión).

-- B) Especificación:
{--problema f2 (n : Z, q: R) : R {
     requiere: {n es un número natural mayor o igual a uno.}
     asegura: {res es la sumatoria \S{i=1}{n}{q^i}.}
}--}

{--\S{i=1}{n}{q^i} = q^1 + q^2 + q^3 + ... + q^n
                   =   q + q^2 + q^3 + ... + q^n--}

f2::Integer->Float -> Float
f2 n q | (n == 1)  = q^1
       | otherwise = q^n + f2 (n-1) q

-- C) Especificación:
{--problema f3 (n : Z, q: R) : R {
     requiere: {n es un número natural mayor o igual a cero.}
     asegura: {res es la sumatoria \S{i=1}{2n}{q^i}.}
}--}

{--\S{i=1}{2n}{q^i} = q^1 + q^2 + q^3 + ... + q^{2n}
                    =   q + q^2 + q^3 + ... + q^{2n}--}

f3::Integer->Float -> Float
f3 n q | (n == 1)  = q^1
       | otherwise = q^(2*n) + f3 (n-1) q

-- Notar que en el LHS, n representa la ''última iteración'', pero en el RHS, colocamos 2*n, para que efectúe la suma hasta 2*n.
-- Notar que luego, f3 q (n-1) representa la iteración anterior a q^(2*n), que sería ''q^(2*n-1)''.

-- D) Especificación:
{--problema f4 (n : Z, q: R) : R {
     requiere: {n es un número natural mayor o igual a cero.}
     asegura: {res es la sumatoria \S{i=n}{2n}{q^i}.}
}--}

{--\S{i=n}{2n}{q^i} = q^n + q^{n+1} + q^{n+2} + ... + q^{2n-1} + q^{2n}
                    = q^n (1 + q + q^2 + ... + q^{n-1} + q^n)
                    = q^n . \S{i=0}{n}{q^i}

Tratmos de hallar la relación entre el paso n-ésimo y el (n-1)-ésimo:
     q^n . \S{i=0}{n}{q^i} = q^{2n} + q . (q^{n-1} . \S{i=0}{n-1}{q^i})
Tuvimos que agregar el término que falta q^{2n}, y multiplicar por q el caso anterior, entonces:--}

f4::Integer->Float -> Float
f4 n q | (n == 0)  = 0                        -- CB: si n=0 q^0 = 0 y la sumatoria se anula.
       | otherwise = q^(2*n) + q*(f4 (n-1) q) -- Si no, la recursión será q^{2n} + q*(el paso anterior)

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 11 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
--A) Especificar e implementar una función eAprox :: Integer -> Float que aproxime el valor del número e a partir de la siguiente sumatoria:
-- e(n) = \S{i=0}{n}{\fr{1}{i!}}

{--problema eAprox (n : Z) : R {
     requiere: {True}
     asegura: {res representa a la suma \S{i=0}{n}{\fr{1}{i!}}}
}--}

factorialFloat::Float -> Float
factorialFloat x | (x == 0) = 1
                 | otherwise = x * factorialFloat(x-1)

eAprox::Float -> Float
eAprox n | (n == 0)  = 1                                   -- CB: 1/0! = 1/1 = 1
         | otherwise = 1/(factorialFloat n) + eAprox (n-1) -- Recursión: 1/n! + 1/(n-1)! + ...

-- Para evitar problemas de tipado, convertí todas los tipos a Float. De esta forma, si escribimos eAprox n, donde n es un número Integer,
-- la computadora nos entregará el resultado de todas formas, por lo tanto funciona al tomar como argumento Integer.

-- B) Definir la constante e :: Float como la aproximación de e a partir de los primeros 10 términos de la serie anterior:

e::Float
e = eAprox 10

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 12 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--Para n \in \bb{N} N se define la sucesión:    a_n = 2 + ( 1 / (2 + 1 / (2 + 1 / (... 2 + 1/2)))) (el número 2 aparece n-veces). Lo cual
resulta en la siguiente definición recursiva:   a_1 = 2  ;    a_n = 2 + \fr{1}{a_{n−1}}
Utilizando esta sucesión, especificar e implementar una función raizDe2Aprox :: Integer -> Float que dado n \in\bb{N} devuelva la
aproximación de \sqrt{2} definida por \sqrt{2} \apxig a_n − 1.--}
{--Por ejemplo:
     raizDe2Aprox 1 -> 1
     raizDe2Aprox 2 -> 1.5
     raizDe2Aprox 3 -> 1.4.--}

{--problema raizDe2Aprox (n : Z) : R {
     requiere: {True}
     asegura: {res representa la aproximación de la raíz de 2, definida por a_n - 1, donde n es el parámetro Integer que recibe la función.}
     asegura: {si n=1, res = 2, y si n > 1 res = 2 + \fr{1}{a_{n-1}} - 1}
}--}

{--a_n - 1 = (2 + 1/a_{n-1}) - 1
           = 1 + 1/{2 + f_{n-1} - 1}
           = 1 + 1/{1 + f_{n-1}}--}

raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1                              -- CB: sqrt(2) \apxig a_1 - 1 = 2 - 1 = 1.
raizDe2Aprox n = 1 + 1/(1 + raizDe2Aprox (n-1)) -- Caso recursivo: 

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 13 -- Especificar e implementar la siguiente función: f(n,m) = \sum_{i=1}^n \sum_{j=1}^m i^j
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

{--problema sumaExponente (n : Z, m : Z) : Z {
     requiere: {n y m son dos números naturales mayores o iguales que uno.}
     asegura: {res representa el resultado de la doble sumatoria \sum_{i=1}^n \sum_{j=1}^m i^j .}
}--}

{-- Veamos qué pinta tiene el resultado de la sumatoria:
\sum_{i=1}^n \sum_{j=1}^m i^j = 1^1 + 1^2 + 1^3 + ... + 1^m
                              + 2^1 + 2^2 + 2^3 + ... + 2^m
                              + 3^1 + 3^2 + 3^3 + ... + 3^m
                              + ... +
                              + n^1 + n^2 + n^3 + ... + n^m--}

-- Creo primero una función sumaM que realiza la recursión sobre m, para un dado n fijo (una fila entera):
sumaM::Integer->Integer -> Integer
sumaM n m | (m == 1)  = n^1                 -- CB: Si m = 1 -> n^1 = n
          | otherwise = n^m + sumaM n (m-1) -- Paso recursivo: n^m + n^{m-1} + n^{m-2} + ...

-- Ahora creo la función que haga la recursión sobre n, y para todos los m (las columnas):
sumaExponente::Integer->Integer -> Integer
sumaExponente n m | (n == 1)  = sumaM 1 m                         -- CB: Si n = 1 -> suma 1^1 + 1^2 + ... + 1^m
                  | otherwise = sumaM n m + sumaExponente (n-1) m -- Si no, suma para todos los n (y los m).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 14 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar una función sumaPotencias :: Integer -> Integer -> Integer -> Integer que dados tres naturales q, n, m sume
-- todas las potencias de la forma:  q^{a+b} con 1 <= a <= n y 1 <= b <= m.

{--problema sumaPotencias (q : Z, n : Z, m : Z) : Z {
     requiere: {q,n y m son números naturales mayores o iguales que 1.}
     asegura: {res representa el resultado de la sumatoria \sum_{a=1}^n \sum_{b=1}^m q^{a+b}}
}--}

{--Veamos qué forma tiene el resultado de la sumatoria:
\sum_{a=1}^n \sum_{b=1}^m q^{a+b} = q^{1+1} + q^{1+2} + q^{1+3} + ... + q^{1+m}
                                   + q^{2+1} + q^{2+2} + q^{2+3} + ... + q^{2+m}
                                   + q^{3+1} + q^{3+2} + q^{3+3} + ... + q^{3+m}
                                   + ... +
                                   + q^{n+1} + q^{n+2} + q^{n+3} + ... + q^{n+m}--}

-- Creo primero una función sumaPotenciasM que realiza la recursión sobre m, para un dado n fijo (una fila entera):
sumaPotenciasM::Integer->Integer->Integer -> Integer
sumaPotenciasM q n m | (m == 1)  = q^(n + 1)                            -- CB: Si m = 1 -> q^{n+1}
                     | otherwise = q^(n + m) + sumaPotenciasM q n (m-1) -- Si no, q^{n+m} + q^{n+(m-1)} + ...

-- Ahora creo la función que haga la recursión sobre n, y para todos los m (las columnas):
sumaPotencias::Integer->Integer->Integer -> Integer
sumaPotencias q n m | (n == 1)  = sumaPotenciasM q 1 m                           -- CB: Si n = 1 solo hay una fila.
                    | otherwise = sumaPotenciasM q n m + sumaPotencias q (n-1) m -- Si no, sumo para todos los n (y los m).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 15 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Implementar una función sumaRacionales :: Integer -> Integer -> Float que dados dos naturales n,m sume todos los números racionales de la
-- forma p/q con 1 <= p <= n y 1 <= q <= m, es decir:

{--problema sumaRacionales (n : N, m : N) : R {
     requiere: {True}
     asegura: {res = \sum_{p=1}^n \sum{q=1}^m \fr{p}{q}.}
}--}

{-- Veamos qué pinta tiene el resultado de la sumatoria:
\sum_{p=1}^n \sum_{q=1}^m \fr{p}{q} = 1/1 + 1/2 + 1/3 + ... + 1/m
                                    + 2/1 + 2/2 + 2/3 + ... + 2/m
                                    + 3/1 + 3/2 + 3/3 + ... + 3/m
                                    + ... +
                                    + n/1 + n/2 + n/3 + ... + n/m--}

-- Creo primero una función sumaRacionalesM que realiza la recursión sobre m, para un dado n fijo (una fila entera):
sumaRacionalesM::Integer->Integer -> Float
sumaRacionalesM n m | (m == 1)  = (fromIntegral n)/1                                          -- CB: Si m = 1 -> 1/1
                    | otherwise = (fromIntegral n)/(fromIntegral m) + sumaRacionalesM n (m-1) -- Si no, n/m + n/(m-1) + ...

-- Ahora creo la función que haga la recursión sobre n, y para todos los m (las columnas):
sumaRacionales::Integer->Integer -> Float
sumaRacionales n m | (n == 1)  = sumaRacionalesM 1 m -- CB: Si n=1 -> sumo solo la fila con n=1.
                   | otherwise = sumaRacionalesM n m + sumaRacionales (n-1) m -- Si no, sumo todos los n (y los m).

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 16 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Recordando que un entero p > 1 es primo si y solo si no existe un entero k tal que 1 < k < p y k divida a p, resuelva los siguientes
-- problemas:

--A) Implementar menorDivisor :: Integer -> Integer que calcule el menor divisor (mayor que 1) de un natural n pasado como parámetro.

buscarDivisor::Integer->Integer -> Integer
buscarDivisor n i | (mod n i == 0) = i                     -- CB: Si el número i divide listo.
                  | otherwise      = buscarDivisor n (i+1) -- Si no, busco hacia arriba (aumentamos i). Si no divide ninguno, termina en n.

menorDivisor::Integer -> Integer
menorDivisor 1 = 1                 -- CB: 1 se divide a si mismo.
menorDivisor n = buscarDivisor n 2 -- Empezamos a buscar divisores desde 2 (no desde 1). Si no hay ninguno => -n divide a n y termina.

--B) Implementar la función esPrimo :: Integer -> Bool que indica si un número natural pasado como parámetro es primo.

esPrimo::Integer -> Bool
esPrimo 1 = False
esPrimo n = (menorDivisor n == n) -- Si el menor divisor de n es si mismo => es primo.

--C) Implementar la función sonCoprimos :: Integer -> Integer -> Bool que dados dos números naturales indica si no tienen algún divisor en
-- común mayor estricto que 1.

-- Primero creo una función que calcule el Máximo Común Divisor (MCD) entre dos números a y b:
maximoComunDivisor::Integer->Integer -> Integer
maximoComunDivisor a 0 = a                              -- CB: Todos los números dividen a cero (0).
maximoComunDivisor a b = maximoComunDivisor b (mod a b) -- Uso el algoritmo de Euclides.

sonCoprimos::Integer->Integer -> Bool
sonCoprimos a b = (maximoComunDivisor a b == 1) -- (a:b) = 1 <=> el máximo común divisor entre ellos es igual a 1.

--D) Implementar la función nEsimoPrimo :: Integer -> Integer que devuelve el n-ésimo primo (n >= 1). Recordar que el primer primo es 2,
-- el segundo es el 3, el tercero es el 5, etc.

-- Creamos una función auxiliar que dado un número n, devuelva el primo más cercano a n hacia arriba (sumando):
siguientePrimo::Integer -> Integer
siguientePrimo n | esPrimo n = n                    -- Si es primo listo! -> n es el siguiente.
                 | otherwise = siguientePrimo (n+1) -- Si no, hago recursión hacia arriba (sigo buscando hasta llegar a un primo).

nEsimoPrimo::Integer -> Integer
nEsimoPrimo 1 = 2                                     -- CB: El primer primo es 2.
nEsimoPrimo n = siguientePrimo (nEsimoPrimo(n-1) + 1) -- Buscamos el próximo primo sumando 1 recursivamente al primo anterior.

{--El funcionamiento es el siguiente. Si conocemos un primo n-1, tomamos este número y le sumamos 1. Para este nuevo número, si es primo
entonces es nuestro n-ésimo primo, y sino, sumamos 1 recursivamente con siguientePrimo hasta hallarlo. Cuando lo hallemos, lo devuelve.
Ahora el nEsimoPrimo será n. Si necesitaramos el siguiente empieza desde n, suma 1, etc. (se repite el proceso).--}

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 17 -- Implementar la función esFibonacci :: Integer -> Bool según la siguiente especificación:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema esFibonacci (n: Z) : B {
     requiere: {n >= 0}
     asegura: {res = True si y solo si n es algún valor de la secuencia de Fibonacci definida en el ejercicio 1.}
}--}

esFibonacciAux::Integer->Integer -> Bool
esFibonacciAux n i | (fibonacci i == n) = True                   -- Si n es un número de fibonacci -> True.
                   | (fibonacci i  > n) = False                  -- Si no, si n se pasó, no es de fibonacci -> False.
                   | otherwise          = esFibonacciAux n (i+1) -- Realizo la recursión sumando 1 hacia arriba en la variable i auxiliar.

esFibonacci::Integer -> Bool
esFibonacci n = esFibonacciAux n 0 -- Comienzo sumando el for desde 0.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 18 -- Implementar una función mayorDigitoPar :: Integer -> Integer según la siguiente especificación:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema mayorDigitoPar (n: N) : N {
     requiere: {True}
     asegura: {res es el mayor de los dígitos pares de n. Si n no tiene ningún dígito par, entonces resultado es -1.}
}--}

mayorDigitoPar::Integer -> Integer
mayorDigitoPar 0 = -1                                              -- CB: Si la cantidad de dígitos = 0 y no encontré ningún par => res = -1.
mayorDigitoPar n | ((mod x 2 == 0) && x > mayorDigitoPar cola) = x -- Si x par, y mayor que el mayor dígito par de cola => Listo! x es el máx.
                 | otherwise            = mayorDigitoPar cola      -- Si no, busco mayor dígito par de la cola (si es el 1° listo, sino sigo).
                 where
                    x    = mod n 10    -- x es el 1° dígito del número.
                    cola = div n 10 -- cola son todo el resto de dígitos del número.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 19 -- Implementar la función esSumaInicialDePrimos :: Integer -> Bool según la siguiente especificación:
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
{--problema esSumaInicialDePrimos (n: Z) : B {
     requiere: {n >= 0}
     asegura: {res = True si y solo si n es igual a la suma de los m primeros números primos, para algún m.}
}--}

{-- Vemos que:
     sumaPrimos 1 = 2
     sumaPrimos 2 = 2 + 3         = sumaPrimos 1 + nEsimoPrimo 2
     sumaPrimos 3 = 2 + 3 + 5     = sumaPrimos 2 + nEsimoPrimo 3
     sumaPrimos 4 = 2 + 3 + 5 + 7 = sumaPrimos 3 + nEsimoPrimo 4, entonces:--}
sumaPrimos::Integer -> Integer
sumaPrimos 1 = 2
sumaPrimos n = sumaPrimos (n-1) + nEsimoPrimo n

esSumaInicialDePrimosAux::Integer->Integer -> Bool
esSumaInicialDePrimosAux 2 1 = True -- CB: Si m = 1, sumaPrimos 1 = 2 -> True.
esSumaInicialDePrimosAux n m | ((sumaPrimos m) == n) = True                             -- Si n es suma de primos => TRUE.
                             | ((sumaPrimos m)  > n) = False                            -- Si la suma de primos se pasó (mayor a n) => FALSE.
                             | otherwise             = esSumaInicialDePrimosAux n (m+1) -- Hago recursión subiendo en m hacia arriba.

esSumaInicialDePrimos::Integer -> Bool
esSumaInicialDePrimos 2 = True                         -- CB: 2 es suma inicial del primer primo 2 con cero.
esSumaInicialDePrimos s = esSumaInicialDePrimosAux s 1 -- Busco si es suma inicial empezando desde 1

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 20 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar la función tomaValorMax :: Integer -> Integer -> Integer que dado un número entero n_1 >= 1 y un n_2 >= n_1
-- devuelve algún m entre n_1 y n_2 tal que sumaDivisores(m) = máx{sumaDivisores(i) : n_1 ≤ i ≤ n_2}:

{--problema tomaValorMax (n_1, n_2 : Z) : Z {
     requiere: {n_1 >= 1 y n_2 >= n_1}
     asegura: {res es el número m perteneciente al intervalo [n_1,n_2] cuya suma de divisores es la máxima respecto de la suma de divisores
               de todo el resto de números que pertenecen al intervalo [n_1,n_2].}
}--}

divisoresAux::Integer->Integer -> [Integer]
divisoresAux n 1 = [1]                                          -- CB: Si i=1, el único divisor de 1 es uno.
divisoresAux n i | (mod n i == 0) = divisoresAux n (i-1) ++ [i] -- Si i divide, lo agrego a la lista.
                 | otherwise      = divisoresAux n (i-1)        -- Si no, voy bajando en i hasta llegar a 1 (mi caso base).

divisores::Integer -> [Integer]
divisores n = divisoresAux n n -- divisores devuelve una lista con todos los divisores de n (incluyendo n mismo)

sumaDivisores::Integer -> Integer
sumaDivisores n = sumaLista(divisores n) -- Devuelve la suma de divisores de n (res es un número natural).

maxDivisores::[Integer] -> Integer
maxDivisores [x] = sumaDivisores x                                                    -- Si la lista tiene 1 elem => res=sumaDivisores(elem).
maxDivisores (x:y:cola) | (sumaDivisores x > sumaDivisores y) = maxDivisores (x:cola) -- Comparo de a 2 y quito el número cuya suma es menor.
                        | (sumaDivisores x < sumaDivisores y) = maxDivisores (y:cola)
                        | otherwise                           = maxDivisores (x:cola) -- Si la suma es igual, me quedo con el primero.

tomaValorMax::Integer->Integer -> Integer
tomaValorMax n1 n2 | ((maxDivisores (generarLista n1 n2)) == sumaDivisores n1) = n1                     -- Si valor max = n1, listo!
                   | otherwise                                                 = tomaValorMax (n1+1) n2 -- Si no, sumo 1 hasta llegar a n2.

-- —————————————————————————————————————————————————————————————————————————————————————
-- Funciones Auxiliares:
-- —————————————————————————————————————————————————————————————————————————————————————
-- Creo una función auxiliar que suma los elementos de una lista
sumaLista::[Integer] -> Integer
sumaLista [] = 0
sumaLista (x:cola) = x + sumaLista cola

-- Creo una función auxiliar que dados dos enteros n1 y n2, genera una lista de enteros en el intervalo [n1,n2], es decir, [n1,n1+1,...,n2]:
generarListaAux::Integer->Integer->Integer -> [Integer]
generarListaAux n1 n2 j | (j <= n2) = j : generarListaAux n1 n2 (j+1)
                        | otherwise = []

generarLista::Integer->Integer -> [Integer]
generarLista n1 n2 = generarListaAux n1 n2 n1
-- —————————————————————————————————————————————————————————————————————————————————————

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Ejercicio 21 --
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- Especificar e implementar una función pitagoras :: Integer -> Integer -> Integer -> Integer que dados m, n, r \in \bb{N}_0 cuente cuántos
-- pares (p,q) con 0 <= p <= n y 0 <= q <= m satisfacen que p^2 + q^2 <= r^2.

{--Por ejemplo:
     pitagoras 3 4 5 -> 20,
     pitagoras 3 4 2 -> 6.--}

-- Creo una función auxiliar que haga recursión sobre p desde 0 hasta n:
pitagorasP::Integer->Integer->Integer -> Integer
pitagorasP (-1) q r = 0                                            -- CB: p va desde 0 hasta n -> uso (-1) para incluir al cero.
pitagorasP p q r | ((p^2 + q^2) <= r^2) = 1 + pitagorasP (p-1) q r -- Si se cumple la condición, sumo 1 y hago recursión.
                 | otherwise            =     pitagorasP (p-1) q r -- Si no, hago recursión.

-- Ahora hago la recursión en q desde 0 hasta m, y para cada valor de ellos contemplo la recursión sobre p de pitagorasP:
pitagoras::Integer->Integer->Integer -> Integer
pitagoras n (-1) r = 0                                      -- CB: q va desde 0 hasta m -> uso (-1) para incluir al cero.
pitagoras n m r    = pitagorasP n m r + pitagoras n (m-1) r -- Sumo las contribuciones de la recursión sobre p, y hago recursión sobre q.

-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
-- ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————