
//============================================================================================================================================
// Taller 4 // Árboles Binarios de Búsqueda (ABB's)
//============================================================================================================================================

/*En este taller obligatorio implementaremos un tipo de datos Conjunto mediante Árboles Binarios de Búsqueda.
En un Árbol Binario de Búsqueda (ABB), cada nodo contiene un valor y la referencia a sus nodos descendientes izquierdo y derecho. Los ABB
respetan la siguiente restricción: el valor de todos los nodo del árbol izquierdo debe ser menor al valor del nodo actual, y el valor de todos
los nodo del árbol derecho debe ser mayor al valor del nodo actual. Para facilitar los algoritmos, se recomienda que los nodos también apunten
a su padre.
El ABB debe soportar cualquier tipo de datos comparables (como Integer, String, Byte). Todos los tipos de datos comparables tienen definido el
método compareTo(). Sean elem1 y elem2 dos instancias de un mismo tipo de datos comparable, luego elem1.compareTo(elem2) devuelve un entero:
  1) mayor a 0 si elem1 > elem2.
  2) menor a 0 si elem1 < elem2.
  3) 0 si elem1 = elem2.
Para resolver el taller cuentan con tres archivos: Conjunto.java, Iterador.java, y ABB.java. El primero define la interfaz de una Conjunto<T>,
mientras que el segundo define la interfaz de un iterador Iterador<T>. Estos dos archivos definen los métodos a implementar. El tercero
corresponde a su implementación, bajo la clase ABB<T>, la cual debe respetar la estructura de representación de un ABB y constituye el archivo
que deben completar.*/

/* Ejemplo:
 * ========                8
 *                      /     \
 *                    3        10
 *                   / \        \
 *                  1   6        14
 *                     / \      /
 *                    4   7    13
 */

package aed;
import java.util.*;
import aed.ABB.ABB_Iterador;

// Parte 1: ABB
//—————————————
// Todos los tipos de datos "Comparables" tienen el método compareTo(): x.compareTo(y) devuelve un entero.

public class ABB<T extends Comparable<T>> implements Conjunto<T> {

  private Nodo _raiz;       // Declaro mis atributos privados: "_raiz" es el Nodo de arriba de todo,
  private int _cardinal;    // y "_cardinal" representa la cantidad de elementos del ABB.
  private class Nodo {      // Creo la clase Nodo, que es un atributo privado deL ABB.
    T valor;                // Tiene un valor de tipo T,
    Nodo padre, izq, der;   // y puede tener solamente un nodo padre y/o solo dos hijos debajo, uno a izquierda y uno a derecha.
    Nodo(T valor) {         // Creo el constructor del Nodo, que contiene un valor de tipo T (representa un Nodo i-ésimo del ABB).
      this.valor = valor;   // Su valor será el valor pasado por parámetro,
      this.padre = null;    // y se inicializa con todos sus nodos en null.
      this.izq   = null;
      this.der   = null;
    }
  }

  public ABB() {           // Constructor por defecto de la clase ABB. Construye un conjunto ABB vacío.
    this._raiz     = null; // Inicializa la raíz con valor nulo
    this._cardinal = 0;    // y por ende, su cantidad de nodos es cero.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 1 // Devuelve la cantidad de elementos que tiene el conjunto.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public int cardinal() {
    return _cardinal;     // El cardinal() de un ABB será simplemente el valor del int _cardinal (atributo de la clase ABB).
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 2 // Devuelve el menor elemento del conjunto.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public T minimo(){
    if (_raiz == null) return null;  // Si _raiz es nula, no hay mínimo.
    Nodo j = _raiz;                  // Si no, creo un nodo auxiliar que representará un nodo j-ésimo (inicialmente es la _raiz).
    while (j.izq != null) j = j.izq; // Mientras pueda moverme hacia mi hijo izquierdo, lo hago.
    return j.valor;                  // Si ya no puedo moverme más -> listo! -> encontré el mínimo -> devuelvo su valor de tipo T.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 3 // Devuelve el mayor elemento del conjunto.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public T maximo(){
    if (_raiz == null) return null;  // Si _raiz es nula, no hay máximo.
    Nodo j = _raiz;                  // Si no, creo un nodo auxiliar que representará un nodo j-ésimo (inicialmente es la _raiz).
    while (j.der != null) j = j.der; // Mientras pueda moverme hacia mi hijo derecho, lo hago.
    return j.valor;                  // Si ya no puedo moverme más -> listo! -> encontré el máximo -> devuelvo su valor de tipo T.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 4 // Determina si un elemento pertenece al conjunto.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public boolean pertenece(T elem){
    Nodo j = _raiz;                                    // Creo un Nodo auxiliar llamado "j" igual al nodo _raíz.
    while (j != null) {                                // Mientras que j no sea null, chequeo:
      if (elem.compareTo(j.valor) == 0) return true;   // Si el valor del Nodo j = elem, -> True! el elemento "elem" pertenece al ABB.
      else if (elem.compareTo(j.valor) > 0) j = j.der; // Si elem > _raiz.valor -> j = hijo_der del que había antes (recursión sub-árbol der)
      else if (elem.compareTo(j.valor) < 0) j = j.izq; // Si elem < _raiz.valor -> j = hijo_izq del que había antes (recursión sub-árbol izq)
    }
    return false;                                      // Si _raiz = null o se llegó a que j = null => False! (elem no pertenece al ABB).
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Inserta un elemento en el conjunto. Si este ya existe, el conjunto no se modifica.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void insertar(T elem){
    if (_raiz == null) {_raiz = new Nodo(elem); _cardinal = 1; return;} // Si el ABB=vacío -> creo el Nodo(T:elem), actualizo _card=1 y salgo.
    Nodo j = _raiz;                                                     // Creo un Nodo aux que representa un nodo j-ésimo (arranca en _raiz).
    while (true) {                                                      // Chequear siempre:
      if (elem.compareTo(j.valor) == 0) return;                         // Si el nodo j actual = elem -> ya existe -> no hago nada -> return.
      if (elem.compareTo(j.valor) > 0) {                                // Si elem > j.valor -> debo ir al sub-árbol derecho:
        if (j.der == null) {                                            // Si no hay nadie a mi derecha -> listo!
          j.der = new Nodo(elem);                                       // creo un nuevo nodo de valor elem en j.der,
          j.der.padre = j;                                              // cuyo padre es j,
          _cardinal++; return;                                          // -> incremento _cardinal en 1 -> termino -> return.
        }
        j = j.der;                                                      // si había o no hijo_der -> actualizo (sigo buscando) -> voy a j.der.
      } else {                                                          // Si elem < j.valor -> debo ir al sub-árbol izquierdo:
        if (j.izq == null) {                                            // Si no hay nadie a mi izquierda -> listo!
          j.izq = new Nodo(elem);                                       // creo un nuevo nodo de valor elem en j.izq,
          j.izq.padre = j;                                              // cuyo padre es j,
          _cardinal++; return;                                          // -> incremente _cardinal en 1 -> termino -> return.
        }
        j = j.izq;                                                      // Si había o no hijo_izq -> actualizo (sigo buscando) -> voy a j.izq.
      }                                                                 // Eventualmente me encontraré si o si en alguno de esos 3 casos.
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Elimina un elemento del conjunto. Si este no existe, el conjunto no se modifica.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void eliminar(T elem){
    Nodo j = _raiz;                                           // Creo un nodo auxiliar que representará un nodo j-ésimo del ABB.
    while (j != null && elem.compareTo(j.valor) != 0) {
      if (elem.compareTo(j.valor) > 0) j = j.der;             // Si "elem" > j.valor -> me muevo a j.derecha.
      if (elem.compareTo(j.valor) < 0) j = j.izq;             // Si "elem" < j.valor -> me muevo a j.izquierda.
    }
    if (j == null) return;                                    // CASO 0: El elemento no existe (llegué a null -> no lo encontré).
    if (j.izq == null && j.der == null) {                     // CASO 1: El nodo no tiene hijos.
      if      (j.padre == null)  _raiz       = null;          // Si j no tiene padre (es _raiz) -> el ABB tenía 1 nodo -> elimino.
      else if (j.padre.izq == j) j.padre.izq = null;          // Si j es hijo_izq, -> elimino el hijo_izq de mi padre.
      else if (j.padre.der == j) j.padre.der = null;          // Si j es hijo_der, -> elimino el hijo_der de mi padre.
    }
    else if (j.izq == null && j.der != null) {                // CASO 2: El nodo tiene un solo hijo a su derecha.
      if      (j.padre == null)  _raiz       = j.der;         // Si j no tiene padre -> raíz nueva será hijo j (der).
      else if (j.padre.izq == j) j.padre.izq = j.der;         // Si soy hijo_izq de padre -> padre apunta al hijo j (der).
      else if (j.padre.der == j) j.padre.der = j.der;         // Si soy hijo_der de padre -> padre apunta al hijo j (der).
      j.der.padre = j.padre;                                  // Actualizo el padre de j.der como el padre de j.
    }
    else if (j.der == null && j.izq != null) {                // CASO 3: El nodo tiene un solo hijo a su izquierda.
      if      (j.padre == null)  _raiz       = j.izq;         // Si j no tiene padre -> raíz nueva será hijo j (izq).
      else if (j.padre.izq == j) j.padre.izq = j.izq;         // Si soy hijo_izq de padre -> padre apunta al hijo j (izq).
      else if (j.padre.der == j) j.padre.der = j.izq;         // Si soy hijo_der de padre -> padre apunta al hijo j (izq).
      j.izq.padre = j.padre;                                  // Actualizo el padre de j.izq como el padre de j.
    }
    else if (j.der != null && j.izq != null) {                // CASO 4: El nodo tiene dos hijos, uno a izquierda y uno a derecha.
      Nodo suc = j.der;                                       // Creo un nodo auxiliar "suc" que representará el sucesor.
      while (suc.izq != null) {                               // Si todavía tengo un hijo_izq, aún no llegué al mín del sub-árbol_der,
        suc = suc.izq;                                        // -> voy redefiniendo mi sucesor como su hijo_izq.
      }                                                       // Si suc.izq=null -> listo! -> encontré el mín -> encontré el suc de j.
      j.valor = suc.valor;                                    // El nodo j no lo toco, solo reemplazo su valor por el de sucesor.
      if      (suc.padre.izq == suc) suc.padre.izq = suc.der; // Si sucesor es un hijo izquierdo, mi hijo_der pasa a ser hijo_izq de mi padre.
      else if (suc.padre.der == suc) suc.padre.der = suc.der; // Si sucesor es un hijo derecho, mi hijo_der pasa a ser hijo_der de mi padre.
      if (suc.der != null) suc.der.padre = suc.padre;         // Si tengo hijo_der -> el nuevo padre de mi hijo será mi padre.
    }
    _cardinal--;                                              // A menos que elem no exista (cuyo caso da return), saco 1 a _cardinal del ABB.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Devuelve un String con los elementos del conjunto de la forma (Por ej.: {1, 3, 4, 6, 10}).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  @Override
  public String toString() {
    String res = "{";                      // Creo una variable auxiliar de tipo String denominada res e inicializada en "{".
    if (_raiz == null) {return res + "}";} // Si no hay siquiera raiz -> res = "{}" -> completo res y salgo -> return.
    Nodo j = _raiz;                        // Si no, creo un nodo auxiliar que representará el nodo j-ésimo (inicializado en _raiz).
    while (j.izq != null) {                // Mientras haya hijo_izq ->
      j = j.izq;                           // busco.
    }
    boolean primero = true;                // Cuando llegué al último (el mínimo) -> defino un booleano "primero"=true (pues estoy en el 1°).
    while (j != null) {                    // Mientras j no sea null, voy buscando mis sucesores.
      if (!primero) {res += ",";}          // A menos que sea el primero, appendeo una coma a res,
      res += j.valor.toString();           // y agrego el valor actual (de tipo T) del j que haya obtenido de mi loop (en formato String).
      primero = false;                     // Si ya pasé por acá -> ya no soy el primero.
      if (j.der != null) {                 // Si tengo hijo_der -> mi sucesor estará debajo en mi sub-arbol derecho,
        j = j.der;                         // así que arranco con j = mi hijo_der.
        while (j.izq != null) {            // Busco el mínimo de este sub-árbol derecho -> mientras el nuevo j tenga hijo_izq,
          j = j.izq;                       // actualizo mi j a ese hijo_izq hasta hallar el mínimo (el sucesor).
        }
      } else {                             // Si no, mi sucesor estará por encima de mí -> busco hacia arriba mediante:
        Nodo p = j.padre;                  // un nodo auxiliar que representará un padre p-ésimo.
        while (p != null && j == p.der) {  // Mientras tenga padre, y j sea un hijo_der de dicho padre,
          j = p;                           // actualizo el j como el padre,
          p = p.padre;                     // y sigo buscando el padre.
        }                                  // Si p=null o he encontrado que j es un hijo_izq de padre -> encontré el sucesor,
        j = p;                             // -> actualizo el j para appendearlo al reiniciar el loop.
      }
    }                                      // Si terminé de hallar todos,
    return res + "}";                      // salgo -> agrego "}" -> return.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public ABB_Iterador iterador() {  // Constructor del iterador.
    return new ABB_Iterador(_raiz); // El iterador arrancará con su parámetro inicio = al Nodo _raiz.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

  // Parte 2: Iterador
  //——————————————————
  public class ABB_Iterador implements Iterador<T> {
    
    private Nodo _iter, _prox;  // Declaro los atributos privados, dos nodos _iter (un nodo i-ésimo) y _prox (el (i+1)-ésimo) (su siguiente).

    public ABB_Iterador(Nodo inicio) { // Constructor del iterador.
      this._iter = null;               // El nodo _iter arranca nulo.
      Nodo j = inicio;                 // Creo un nodo auxiliar j-ésimo de inicio.
      while (j.izq != null) j = j.izq; // Mientras j tenga hijo_izq -> actualizo j hasta llegar al mínimo.
      this._prox = j;                  // -> el nodo _prox arrancará siendo el mínimo (el próximo del nodo _iter).
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 9 // Devuelve true si hay un elemento siguiente al iterador, y false en caso contrario.
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public boolean haySiguiente() {
      boolean res = (_prox != null); // Creo una variable auxiliar booleana llamada res, cuyo valor de verdad indicará si existe un _prox.
      return res;                    // y devuelvo dicho valor de verdad.
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 10 // Devuelve el elemento siguiente al iterador (y avanza al iterador a la posición siguiente).
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public T siguiente() {
      T res = null;                             // Creo una variable auxiliar llamada res de tipo T inicializada en null.
      if (haySiguiente()) {                     // Si hay siguiente,
        _iter = _prox;                          // actualizo al Nodo _iter por el próximo,
        res = _iter.valor;                      // y -> el valor de res será el de dicho próximo (el nuevo _iter)

        if (_prox.der != null) {                // Si el próximo (_prox) tiene un hijo a su derecha -> busco sub-árbol derecho.
          _prox = _prox.der;                    // Actualizo al _prox como dicho prox_der
          while (_prox.izq != null) {           // Mientras dicho hijo derecho tenga elementos a su izquierda,
            _prox = _prox.izq;                  // busco hasta hallar el mín -> listo!, _prox estará actualizado en el valor del próximo.
          }
        } else {                                // Si _prox no tiene hijo_der -> debo buscar el siguiente hacia arriba (padres)
          Nodo p = _prox.padre;                 // -> defino un nodo auxiliar p-ésimo como el padre de _prox.
          while (p != null && _prox == p.der) { // Misma lógica para buscar sucesores que utilizamos en el método toString()
            _prox = p;
            p = p.padre;
          }
          _prox = p;
        }
        return res;                             // Devuelvo _iter.valor, pero _prox se habrá actualizado con el sucesor correspondiente.
      }
      return res;                               // Si no hay siguiente -> devuelve null.
    }
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————