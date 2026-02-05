
//============================================================================================================================================
// Taller 1 // Introducción a la Programación Imperativa en Java
//============================================================================================================================================

package aed;

class Funciones {
  /*public static void main(String[] args) { // Creamos una instancia para la clase Funciones (nuestro archivo)
    // Funciones f = new Funciones();
    // int[] lista = {7,4,0}; // Ejemplo
    // System.out.println("Probando f: " + f.todosPositivos(lista)); // Usamos system.out.printIn para probar casos manualmente.
  }*/

// Primera parte: Funciones en java
//—————————————————————————————————
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 1 // Implementar la función cuadrado, que devuelve el resultado de multiplicar a un número por si mismo.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc cuadrado (in x: Z) : Z {
    requiere {true}
    asegura {res = x∗x}
  }*/

  int cuadrado(int x) {
    int res = x*x;      // Creamos la variable entera res = x*x, y la retornamos
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 2 // Implementar la función distancia, que dadas las coordenadas (x,y) ∈ R2, devuelve la distancia al origen de coordenadas.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc distancia (in x: R, in y: R) : R {
    requiere {true}
    asegura {res = √(x∗x+y∗y)}
  }*/

  double distancia(double x, double y) {
    double res = Math.sqrt(x*x + y*y);   // Usamos la función raíz cuadrada de Math (viene con Java)
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 3 // Implementar la función esPar, que determina si un número natural es par.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc esPar (in n: N) : Bool {
    requiere {true}
    asegura {res = true ↔ divideA(2,n)}
    pred divideA (d: N, n: N) {
      (∃k : N) (n = d∗k)
    }
  }
  Si hicieron este ejercicio usando if, for o while, piensen cómo hacerlo sin usarlo.*/

  boolean divideA(int d, int n) { // Creamos la función auxiliar que devuelve un booleano si n es divisible por d.
    return (n % d == 0);          // Como el output es booleano, podemos nos ahorramos usar condicionales.
  }

  boolean esPar(int n) {
    boolean res = divideA(2,n); // res, será la operación de dividir a n entre 2 (usando la f aux divideA)
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 4 // Implementar la función esBisiesto, que determina si un año es bisiesto.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Los años bisiestos son los múltiplos de 4 que no son múltiplos de 100. Esta regla tiene una excepción: los años múltiplo de 400 se
  // consideran bisiestos de todos modos.
  /*proc esBisiesto (in n: N) : Bool {
    requiere {true}
    asegura {res = true ↔ (divideA(4,n)∧¬divideA(100,n)) ∨ divideA(400,n)}
  }
  Si hicieron este ejercicio usando if, for o while, piensen cómo hacerlo sin usarlo.*/

  boolean esBisiesto(int n) {
    boolean res = ((divideA(4,n) && !divideA(100,n)) || divideA(400,n)); // Transcribimos la especificación a código directamente.
    return res;                                                                 // Evitamos usar condicionales nuevamente.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Implementar la función factorial, que calcula el factorial de un número natural. Recordar que 0! = 1 por definición.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc factorial (in n: N) : N {
    requiere {true}
    asegura {res = \prod_{i=1}^n i}
  }
  Pensar tanto una solución recursiva como una iterativa.*/

  int factorialIterativo(int n) {
    int res = 1;                     // Hago los casos base e inicializo el for simultáneamente.
    if (n == 0 || n == 1) {          // Caso especial y caso base: 0! = 1! = 1
      return res;
    } else {
      for (int j = 2; j <= n; j++) { // En otro caso: n! = 1.2.3. ... .n, cuando n > 1
        res *= j;
      }
      return res;
    }
  }

  int factorialRecursivo(int n) {
    int res = 1;                       // Ídem
    if (n == 0 || n == 1) {
      return res;
    } else {
      res = n*factorialRecursivo(n-1); // Ahora hago recursión usando que: n! = n . (n-1)!
    }
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Implementar la función esPrimo, que determina si un número natural es primo (tiene exactamente dos divisores).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc esPrimo (in n: N) : Bool {
    requiere {true}
    asegura {res = true ↔ primo(n)}
    pred primo (n: N) {
      ( \sum_{i=1}^n {if divideA(i,n) then 1 else 0 fi} )  =  2
    }
  }*/

  boolean primo(int n) {
    int res = 0;                   // Inicializamos res
    for (int j = 1; j <= n; j++) { // Sumamos la cantidad de números 1 <= j <= n tales que j divide a n.
      if (divideA(j,n)) {
        res += 1;
      }
    }
    if (res == 2) {                // Si res = 2 => n solo fue dividido por 1 y por sí mismo => primo!
      return true;
    }
    return false;                  // Sino, no.
  }

  boolean esPrimo(int n) {
    boolean res = primo(n); // res será el valor booleano que tome primo(n)
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Implementar la función sumatoria, que dado un arreglo de números enteros, calcula la suma de sus elementos.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc sumatoria (in l: seq⟨Z⟩) : Z {
    requiere {true}
    asegura {res = \sum_{i=0}^{|l|-1} {l[i]}}
  }*/

  int sumatoria(int[] numeros) {
    int res = 0;                 // Inicializo res en cero:
    for (int elem : numeros) {   // Para cada elemento de numeros,
      res += elem;               // lo agrego (sumo) a res.
    }
    return res;
  }

  // Observación: si la lista es vacía, como inicializamos res en 0 y numeros no tiene elementos => sumatoria({}) = 0.

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8 //
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Implementar la función busqueda, que dado un arreglo de números enteros l y un número buscado, devuelve alguna de las posiciones del
  // arreglo en las que se encuentra el número buscado.
  /*proc busqueda (in l: seq⟨Z⟩, in buscado: Z) : N {
    requiere {(∃i : N) (i<|l| ∧_L l[i] = buscado)}
    asegura {l[res] = buscado}
  }*/

  int busqueda(int[] numeros, int buscado) {
    int res = 0;                               // Inicializo res en cero (primer índice de numeros)
    for (int j = 0; j < numeros.length; j++) { // Para cada índice j=0,1,...,|l|-1,
      if (numeros[j] == buscado) {             // si el elemento de numeros en ese j es el buscado,
        res = j;                               // => res = j
        break;                                 // Listo! no quiero seguir loopeando (prefiero que res me dé la primera aparición de índice)
      }
    }
    return res;                                // Devuelvo res.
  }

  // Observación: por la especificación, en la lista de enteros 'numeros' EXISTE algún elemento igual al buscado.

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 9 // Implementar la función tienePrimo, que determina si un arreglo de números naturales contiene un número primo.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc tienePrimo (in l: seq⟨N⟩) : Bool {
    requiere {true}
    asegura {res = true ↔ (∃i : N) ( i<|l| ∧_L primo(l[i]) ) }
  }*/

  boolean tienePrimo(int[] numeros) {
    boolean res = false;              // res será falsa a menos que encontremos un primo.
    for (int elem : numeros) {        // Para cada elemento de numeros,
      if (primo(elem)) {              // si el elemento es primo, primo(elem)=true,
        res = true;                   // => res = true.
        break;                        // Listo! ya no busco.
      }
    }
    return res;                       // Devuelvo res.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 10 // Implementar la función todosPares, que determina si todos los números de un arreglo de números son pares.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc todosPares (in l: seq⟨Z⟩) : Bool {
    requiere {true}
    asegura {res = true ↔ (∀i : N) ( i<|l| −→_L divideA(2,l[i]) ) }
  }*/

  boolean todosPares(int[] numeros) {
    boolean res = true;               // Vamos a inicializar astutamente res en true.
    for (int elem : numeros) {        // Para cada elemento de numeros,
      if (!divideA(2,elem)) {       // Si alguno no es par (divisible por 2)
        res = false;                  // res = false.
        break;                        // Listo! encontramos un impar.
      }
    }
    return res;                       // Si todos pasaron, res = true (todos pares)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 11 // Implementar la función esPrefijo, que dados dos strings determina si el primero es prefijo del segundo.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc esPrefijo (in s1: String, in s2: String) : Bool {
    requiere {true}
    asegura {res = true ↔ (∀i : N) ( i<|s1| −→_L (i<|s2| ∧_L s1[i]=s2[i]) ) }
  }*/

  boolean esPrefijo(String s1, String s2) {
    boolean res = true;                       // Otra vez, arrancamos con res=true.
    if (s1.length() > s2.length()) {          // Si |s1|>|s2| => IMPOSIBLE.
      res = false;                            // res = false, y listo!
    } else {                                  // Si no,
      for (int j = 0; j < s1.length(); j++) { // desde j=0 hasta la longitud que tiene s1,
        if (s1.charAt(j) != s2.charAt(j)) {   // si s1[j] != s2[j],
          res = false;                        // res = false,
          break;                              // Listo! ya no es prefijo.
        }
      }
    }
    return res;                               // Si se cumplieron todas las condiciones (es prefijo) => res = true!
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 12 // Implementar la función esSufijo, que dados dos strings determina si el primero es sufijo del segundo.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc esSufijo (in s1: String, in s2: String) : Bool {
    requiere {true}
    asegura {res = true ↔ (∀i : N) ( i<|s1| −→_L (i<|s2| ∧_L s1[|s1|−i−1]=s2[|s2|−i−1]) ) }
  }
  Si la solución no usa esPrefijo, pensar una solución que lo use.*/

  String invertir(String s) {                 // Para usar esPrefijo, creo una función auxiliar que invierte un string s dado.
    String res = "";                          // Arrancamos con res = "" (string vacío)
    for (int j = s.length()-1; j >= 0; j--) { // Para cada posición j de s, contando de derecha a izquierda (j va desde len(s)-1,...,0),
      res += s.charAt(j);                     // agrego el elemento s[j] a res (de izq a der => lo estoy invirtiendo).
    }
    return res;                               // Devuelvo res.
  }

  boolean esSufijo(String s1, String s2) {
    boolean res = esPrefijo(invertir(s1),invertir(s2)); // s1 será sufijo de s2 si inv(s1) es prefijo de inv(s2) (pues esPrefijo retorna bool)
    return res;                                         // Devuelvo res.
  }

// Segunda parte: Debugging
//—————————————————————————
// Los siguientes ejercicios tienen ya un código que los implementa, aunque con algunos errores. Su objetivo es encontrar estos errores y
// arreglarlos para que pasen los tests.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 13 // Debuggear el código que implementa el operador xor (que se simboliza con ⊻).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Este operador representa un “o excluyente”:
  // A ⊻ B es verdadero cuando A ó B es verdadero, pero no ambos. Cumple la siguiente tabla de verdad:

        /*-------------------
          | A | B | A xor B |
          |-----------------|
          | F | F |    F    |
          | F | T |    T    |
          | T | F |    T    |
          | T | T |    F    |
          -------------------*/

  boolean xor(boolean a, boolean b) {
    return (a || b) && !(a && b);     // Faltaban los paréntesis en a || b ===> (a || b)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 14 // Debuggear el código que implementa la función iguales, que determina si dos arreglos de número enteros son iguales.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc iguales (in xs: seq⟨Z⟩, in ys: seq⟨Z⟩) : Bool {
    requiere {true}
    asegura {res = true ↔ |xs|=|ys| ∧_L (∀i : N) (i<|xs| −→_L xs[i]=ys[i]) }
  }*/

  boolean iguales(int[] xs, int[] ys) {
    boolean res = true;
    if (xs.length != ys.length) {           // Faltaba agregar esta condición, si las longitudes no son iguales => res = false!
      res = false;
    } else {
      for (int i = 0; i < xs.length; i++) {
        if (xs[i] != ys[i]) {
          res = false;
          break;                            // Faltaba el break. Sin él, el loop sigue y res podría terminar dando true incluso si hubo false.
        }
      }
    }
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 15 // Debuggear el código que implementa la función todosPositivos (determina si los valores de un arreglo de enteros son > 0).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc todosPositivos (in xs: seq⟨Z⟩) : Bool {
    requiere {true}
    asegura {res = true ↔ (∀x : N) (x ∈ xs −→ 0 < x)}
  }*/

  boolean todosPositivos(int[] xs) {
    boolean res = true;              // Es más eficiente comenzar con res=true.
    for (int x : xs) {               // Para cada elemento de xs,
      if (x <= 0) {                  // Si alguno es menor o igual a cero,
        res = false;                 // => res = false
        break;                       // Listo! ya no tengo que seguir (faltaba el break)
      }
    }
    return res;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 16 // Debuggear el código que implementa la función maximo, que devuelve el máximo valor de un arreglo de números enteros.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc maximo (in xs: seq⟨Z⟩) : Z {
    requiere {|xs| > 0}
    asegura {res ∈ xs ∧ (∀x : Z) (x ∈ xs −→ x ≤ res)}
  }*/

  int maximo(int[] xs) {
    int res = xs[0];                      // res debe pertenecer a xs => no puedo inventarme res=0, si no, arranco por el 1° elemento de xs.
    for (int i = 0; i < xs.length; i++) { // i < xs.length, no menor o igual (pues i=0,1,...,|xs|-1)
      if (xs[i] > res) {
        res = xs[i];                      // Por la especificación res pertenece a xs, es decir, es un elemento de xs (no el índice)
      }
    }
    return res;
  }

  // Observación: debido a que en este ejercicio no se requería utilizar el índice i en absoluto, era más conveniente escribir
  // for (int elem : xs) {...}.

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 17 // Debuggear el código que implementa la función ordenado (determina si un arreglo de enteros está ordenado crecientemente).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*proc ordenado (in xs: seq⟨Z⟩) : Bool {
    requiere {true}
    asegura {res = true ↔ (∀i,j : N) (i<j ∧ j<|xs| −→_L xs[i]≤xs[j]) }
  }*/

  boolean ordenado(int[] xs) {
    boolean res = true;
    for (int i = 0; i < (xs.length - 1); i++) { // Si voy a comparar i e i+1, => debo iterar desde 0 hasta |xs|-2 pues i=0,1,...,|xs|-1(-1)
      if (xs[i] > xs [i+1]) {
        res = false;
        break;                                  // Listo! ya no debo iterar más, y debo devolver res = false, sino podría caer en errores.
      }
    }
    return res;
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————