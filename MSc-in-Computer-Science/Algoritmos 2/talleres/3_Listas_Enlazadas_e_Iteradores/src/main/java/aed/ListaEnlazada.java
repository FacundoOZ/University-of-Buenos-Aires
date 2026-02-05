
//============================================================================================================================================
// Taller 3 // Listas Enlazadas e Iteradores
//============================================================================================================================================

/*En este taller deben implementar una lista doblemente enlazada con su correspondiente iterador.
En una lista enlazada, cada nodo apunta únicamente al nodo siguiente de la lista, mientras que en una lista doblemente enlazada cada nodo
apunta, además, al nodo anterior. Por otro lado, una lista doblemente enlazada tiene un puntero al primer elemento y un puntero al último
elemento. En la Figura 1 se puede ver un diagrama de la lista a implementar.
Para resolver el taller cuentan con tres archivos: Secuencia.java, Iterador.java, y ListaEnlazada.java. El primero define la interfaz de una
Secuencia<T>, mientras que el segundo define la interfaz de un iterador Iterador<T>. Estos dos archivos definen los métodos a implementar.
El tercero corresponde a su implementación, bajo la clase ListaEnlazada<T>, la cual debe respetar la estructura de representación de una
lista doblemente enlazada y constituye el archivo que deben completar.*/

package aed;

// Parte 1: Secuencia
//———————————————————

public class ListaEnlazada<T> implements Secuencia<T> {

  // Declaro los siguientes atributos privados (características de la lita enlazada):
  private Nodo _primero, _ultimo; // representan el primer y último elemento de la lista, respectivamente.
  private int _len;               // representa la cantidad de elementos de la lista.
  private class Nodo {            // Nodo es una característica (clase) de la lista enlazada.
    T valor;                      // Tiene un valor de tipo T,
    Nodo sig, ant;                // un nodo siguiente y un nodo anterior como atributos (ambos de tipo Nodo).
    Nodo(T valor) {               // Un nodo, tiene un valor de tipo T, este valor representa el elemento de la lista en la posición i.
        this.valor = valor;       // El valor de un nodo será el de esta clase.
    }
  }

  public ListaEnlazada() { // ListaEnlazada() inicializa la lista.
    this._primero = null;  // No tiene elemento primero,
    this._ultimo  = null;  // ni último, y por lo tanto
    this._len     = 0;     // su longitud es cero.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 1 // Devuelve la cantidad de elementos que contiene la Secuencia.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public int longitud() {
    return _len;          // Su valor es simplemente el valor que tome nuestro atributo privado entero "len".
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 2 // Agrega un elemento al principio de la Secuencia.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void agregarAdelante(T elem) {
    Nodo nuevo = new Nodo(elem);        // Creo un nuevo nodo llamado "nuevo" que será el primero y cuyo valor es "elem" (de tipo T).
    nuevo.ant = null;                   // Como nuevo será el primero -> no existe un nodo anterior,
    nuevo.sig = _primero;               // y el nodo siguiente será el que antes era el_ primero.

    if (_primero == null) {             // Si la lista estaba vacía, ahora tendrá un solo elemento,
      _ultimo = nuevo;                  // por lo que el nuevo nodo será único, y será el primero y el último simultáneamente.
    } else {                            // Si no,
      _primero.ant = nuevo;             // el nodo primero que había antes ahora tendrá un anterior, que es el nuevo nodo.
    }
    _primero = nuevo;                   // Sea cual sea el caso, ahora el primer nodo, será el nuevo nodo creado de valor "elem".
    _len++;                             // Finalmente, la longitud será len_final = len_inicial + 1.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 3 // Agrega un elemento al final de la Secuencia.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void agregarAtras(T elem) {
    Nodo nuevo = new Nodo(elem);     // Creo un nuevo nodo llamado "nuevo" que será el último y cuyo valor es "elem" (de tipo T).
    nuevo.ant = _ultimo;             // Como nuevo será el último, entonces su anterior, será el nodo que era originalmente el último,
    nuevo.sig = null;                // y su siguiente será nulo.

    if (_primero == null) {          // Si la lista es vacía,
      _primero = nuevo;              // El primero será el nuevo, que además será el último.
    } else {
      _ultimo.sig = nuevo;           // Si no, actualizo la lista: ahora el último tendrá un siguiente, que será el nuevo.
    }
    _ultimo = nuevo;                 // Sea cual sea el caso, finalmente el nuevo último será el nuevo nodo "nuevo".
    _len++;                          // Y la longitud de la lista se incrementará en 1.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 4 // Devuelve una referencia al elemento en la i-ésima posición de la Secuencia.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public T obtener(int i) {
    if (i < 0 || i >= _len) {     // Si el i < 0 ó es mayor que la longitud de la lista,
      return null;                // devuelve null, ya que es absurdo.
    }
    Nodo aux = _primero;          // Creo un nodo auxiliar que comienza siendo igual que el primero.
    for (int j = 0; j < i; j++) { // Mientras un entero j se encuentre en el intervalo [0,i),
      aux = aux.sig;              // voy moviéndome al siguiente nodo a la par que el j incrementa en 1.
    }                             // Si i == j, me salgo del for,
    return aux.valor;             // y devuelvo el valor que tiene auxiliar, que es una copia del nodo en la i-ésima posición.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Elimina el i-ésimo elemento de la Secuencia.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void eliminar(int i) {
    Nodo aux     = _primero;          // Creo dos nodos auxiliares (i), e (i+1), inicializados en primero,
    Nodo aux_sig = _primero.sig;      // y en primero.sig.
    if (i == 0) {                     // Si tengo que eliminar el primero,
      _primero = aux.sig;             // el nuevo primero será entonces el siguiente.
    } else {                          // Si no,
      for (int j = 0; j < i-1; j++) { // Para j entre [0,i-1),
        aux     = aux.sig;            // Voy incrementando aux,
        aux_sig = aux_sig.sig;        // y aux_sig
      }                               // Si j = i-1, salgo del for, y entonces
      aux.sig = aux_sig.sig;          // actualizo: el siguiente del que era i-1, será el siguiente del que era i (me salteo el i).
    }
    _len--;                           // La longitud de la lista se ve disminuida en uno.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Reemplaza al elemento i-ésimo de la Secuencia por el elemento pasado por parámetro.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void modificarPosicion(int indice, T elem) {
    Nodo aux = _primero;                              // Creo un nodo auxiliar que comienza siendo igual que el primero.
    for (int j = 0; j < indice; j++) {                // Mientras j se encuentre en el intervalo [0,indice),
      aux = aux.sig;                                  // voy moviéndome al siguiente nodo a la par que el j incrementa en 1.
    }                                                 // Si j == indice, me salgo del for,
    aux.valor = elem;                                 // y actualizo: el valor de aux será ahora "elem" de tipo T.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Constructor por copia de la lista pasada por parámetro.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public ListaEnlazada(ListaEnlazada<T> lista) {
    this();                                      // Copio los atributos this.primero=null; this.ultimo=null y this.len=0.
    Nodo aux = lista._primero;                   // Creo un nodo auxiliar que comienza siendo igual al primero de "lista".
    while (aux != null) {                        // Mientras éste no sea vacío,
      agregarAtras(aux.valor);                   // voy agregando el valor de tipo T que tenga éste (el valor del i-ésimo nodo),
      aux = aux.sig;                             // y voy incrementando el nodo auxiliar para barrer toda la lista.
    }                                            // Cuando llegue al que está después de "último" (o sea, null), termina el while.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8 // Convierte los elementos de la Secuencia a un string de la forma (Por ej.: [7, 4, 2]).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  @Override
  public String toString() {
    String res = "[";              // Creo una variable res de tipo string inicializada con "[",
    Nodo aux = _primero;           // y un nodo auxiliar inicializado por el primer nodo.
    while (aux != null) {          // Mientras el nodo no sea vacío,
      res += aux.valor.toString(); // convierto el valor de tipo T de aux (aux.valor) a string, y lo appendeo a res.
      if (aux.sig != null) {       // Solo si el siguiente tampoco es null,
        res += ",";                // entonces agrego una coma y un espacio.
      }
      aux = aux.sig;               // Incremento el nodo del while (que es mi contador del loop)
    }
    res += "]";                    // Finalmente, agrego el último char "]". Esto funciona incluso en listas vacías.
    return res;                    // Devuelvo res.
  }
  
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 9
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public ListaIterador iterador() {     // El comando .iterador() inicializará el sistema
    return new ListaIterador(_primero); // Llama a la función public ListaIterador(Nodo inicio) de la public class ListaIterador
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

  // Parte 2: Iterador
  //——————————————————
  public class ListaIterador implements Iterador<T> {

    // Declaro los atributos privados del iterador de tipo T, que serán dos nodos de tipo "Nodo"
    private Nodo _iter, _prox; // "iter" y "prox" representarán Nodos en una posición i-ésima e (i+1)-ésima, respectivamente.

    public ListaIterador(Nodo inicio) { // Constructor que inicia el iterador, recibe un nodo de tipo "Nodo" llamado "inicio"
      this._iter = null;                // el nodo "iter" será el nodo cero (null) que se encuentra antes de comenzar la lista enlazada.
      this._prox = inicio;              // el nodo "prox" será el próximo a "iter", y estará al inicio de la lista (antes del 1er valor).
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 10 // Devuelve true si hay un elemento siguiente al iterador, y false en caso contrario.
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public boolean haySiguiente() {
      boolean res = false;          // Creo una variable llamada "res" de tipo boolean inicializada en false.
      if (_prox != null) {          // Si el Nodo prox no es null, entonces no me encuentro al final de la lista,
        res = true;                 // y por lo tanto existe el siguiente -> actualizo res a true.
      }                             // Si no, el prox es null -> estoy al final de la lista -> no hago nada -> res=false.
      return res;                   // Devuelvo res.
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 11 // Devuelve true si hay un elemento anterior al iterador, y false en caso contrario.
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public boolean hayAnterior() {
      boolean res = false;         // Idem a haySiguiente().
      if (_iter != null) {         // Ahora, si el Nodo iter no es null, entonces no me encuentro al principio de la lista,
        res = true;                // y por lo tanto existe el anterior -> actualizo res a true.
      }                            // Si no, el iter es null -> estoy al principio de la lista -> no hago nada -> res=false.
      return res;                  // Devuelvo res.
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 12 // Devuelve el elemento siguiente al iterador y avanza al iterador a la posición siguiente.
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public T siguiente() {
      if (haySiguiente()) { // Si hay siguiente,
        _iter = _prox;      // actualizo iter a la proxima posición (paso de i a i+1),
        _prox = _prox.sig;  // actualizo prox a la proxima posición (paso de i+1 a i+2),
        return _iter.valor; // y devuelvo iter.valor (es decir, el que antes era prox.valor, pues incrementé en 1).
      }
      return null;          // Si no hay siguiente, devuelvo null, pues estoy al final de la lista.
    }

    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    // Ejercicio 13 // Devuelve el elemento anterior al iterador y retrocede al iterador a la posición anterior.
    //————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    public T anterior() {
      if (hayAnterior()) {  // Si hay anterio,
        _prox = _iter;      // actualizo prox a la posición anterior (paso de i+1 a i),
        _iter = _iter.ant;  // actualizo iter a la posición anterior (paso de i a i-1),
        return _prox.valor; // y devuelvo prox.valor (es decir, el que antes era iter.valor, pues disminuí en 1).
      }
      return null;          // Si no hay anterior, devuelvo null, pues estoy al principio de la lista.
    }
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————