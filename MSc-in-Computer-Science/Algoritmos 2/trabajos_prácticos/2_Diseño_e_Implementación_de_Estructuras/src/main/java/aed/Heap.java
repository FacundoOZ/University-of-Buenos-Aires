
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

/*Utilizando ArrayLists, contamos con los métodos de ayuda:
    isEmpty() add() remove() size() get() set() indexOf() contains()*/

package aed;
import java.util.ArrayList;

public class Heap<T extends Comparable <T>> {
  /*Esta clase contiene todos los métodos de un MinHeap, incluyendo su respectivo Handle.*/

  // Atributos Privados:
  private ArrayList<Nodo>      _heap;        // _heap es un ArrayList de objetos de clase Nodo.
  private ArrayList<Handle<T>> _handles;     // _handles es un ArrayList de objetos de clase Handle.
  private int padre(int j) {return (j-1)/2;} // Mediante los métodos privados 'padre', 'izq' y 'der', podemos obtener el índice del padre,
  private int   izq(int j) {return 2*j+1;}   // del hijo izquierdo, o del hijo derecho,
  private int   der(int j) {return 2*j+2;}   // respecto del índice de un nodo j cualquiera de un array, cuya forma representa un MinHeap.
  private class Nodo {                       // Nodo del Heap
    T   valor;                               // Cada nodo tiene un valor de tipo T,
    int indice;                              // y un índice.
    HandleHeap handle;                       // un handle,
    Nodo(T v) {                              // Constructor del nodo con sus atributos.
      this.valor  = v;
      this.handle = null;                    // Seteamos el handle inicialmente en null.
      this.indice = -1;                      // Seteamos el índice inicialmente en -1.
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Constructores:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public Heap() { // COMPLEJIDAD O(1)
    /*Constructor vacío del MinHeap.*/
    this._heap    = new ArrayList<>(); // En el heap inicializo un nuevo arraylist,
    this._handles = new ArrayList<>(); // la longitud del heap será la longitud del array
  }

  public Heap(T[] arreglo) { // COMPLEJIDAD O(N)
    /*Constructor del MinHeap cuando recibe un arreglo de tipo T.*/
    this();                                          // Contiene los elementos del constructor Heap() vacío.
    for (int j = 0; j < arreglo.length; j++) {       // Para cada índice j entre 0 y longitud(arreglo), // O(N)
      Nodo n   = new Nodo(arreglo[j]);               // Creo un Nodo n que contiene al elemento j-ésimo del arreglo, // O(1)
      n.indice = j;                                  // y por lo tanto defino su índice = j. // O(1)
      n.handle = new HandleHeap(n);                  // Creo el handle asociado a dicho nodo. // O(1)
      _heap.add(n);                                  // Agrego el nodo al ArrayList de nodos '_heap', // O(1)
      _handles.add(n.handle);                        // y al ArrayList de Handles de tipo T '_handles'. // O(1)
    }
    if (_heap.isEmpty()) return;
    for (int k = padre(_heap.size()-1); k>=0; k--) { // Ahora tengo elementos del array en el heap, pero necesito ordenarlos correctamente.
      siftDown(k);                                   // Transformo el arreglo recibido en uno de la forma MinHeap con siftDown. // O(N)
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Operaciones:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public int longitud(){ // COMPLEJIDAD O(1)
    /*Devuelve un entero positivo que representa la longitud del MinHeap.*/
    return _heap.size(); // Devuelve el tamaño del heap. // O(1)
  }

  public T minimo() { // COMPLEJIDAD O(1)
    /*La función mínimo devuelve el mínimo valor de tipo T del MinHeap.*/
    if (_heap.isEmpty()) throw new IllegalStateException("Heap vacío.");
    return _heap.get(0).valor;                                       // MinHeap => el valor de raíz es mínimo (el 1° elemento) // O(1)
  }

  public T maximo() { // COMPLEJIDAD O(N)
    /*La función máximo devuelve el máximo valor de tipo T del MinHeap.*/
    if (_heap.isEmpty()) throw new IllegalStateException("Heap vacío."); // Si longitud=0, el heap está vacío. // O(1)
    T max = _heap.get(0).valor;                                   // Creo valor auxiliar inicializado en primer nodo del heap. // O(1)
    for (Nodo actual : _heap) {                                         // Para cada nodo j-ésimo (lo llamo "actual") en el heap de nodos,
      if (actual.valor.compareTo(max) > 0) max = actual.valor;          // Si actual.valor > max.valor actualizo valor de mi máximo. // O(1)
    }                                                                   // Recorre toda la lista // O(N)
    return max;                                                         // Devuelve el valor máximo hallado del Heap (arraylist). // O(1)
  }

  public HandleHeap encolar(T elem) { // COMPLEJIDAD O(LOG N)
    /*La función encolar agrega un elemento de tipo T al heap (en particular al Handle).*/
    Nodo nuevo   = new Nodo(elem);        // Creo mi nuevo nodo // O(1)
    nuevo.indice = _heap.size();          // Le asigno el indice // O(1)
    nuevo.handle = new HandleHeap(nuevo); // Creo el handle para mi nuevo nodo // O(1)
    _heap.add(nuevo);                     // Agrego el nuevo nodo a la lista _heap, // O(1)
    _handles.add(nuevo.handle);           // y su handle a la lista _handles. // O(1)
    siftUp(nuevo.indice);                 // Arreglo el orden del heap // O(log n)
    return nuevo.handle;                  // Devuelvo el handle de mi nuevo nodo // O(1)
  }

  public T desencolarMinimo() { // COMPLEJIDAD O(LOG N)
    /*La función desencolarMínimo, quita el mínimo del MinHeap (el nodo raíz!) y devuelve su valor de tipo T.*/
    if(_heap.isEmpty()) return null; // Si el Heap está vacío no hay mínimo -> no devuelvo nada. // O(1)
    Nodo raiz = _heap.get(0);  // Obtengo y guardo el primer nodo del ArrayList _heap en la variable 'raiz' // O(1)
    T res     = raiz.valor;          // Guardo su valor de tipo T antes de eliminarlo. // O(1)
    eliminarNodo(raiz);              // Eliminamos el nodo, // O(LOG N)
    return res;                      // y devolvemos el valor de tipo T guardado en res. // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Estructura del MinHeap:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  private void siftUp(int j) { // COMPLEJIDAD O(LOG N)
    /*La función siftUp recibe un índice j asociado a un nodo del array MinHeap, y ejecuta siftUp, no devuelve nada.*/
    while (j > 0) {                                  // O(LOG N)
      int j_padre = padre(j);                        // Obtengo y guardo el índice del padre, // O(1)
      Nodo actual = _heap.get(j);                    // el Nodo actual en la posición j-ésima del array (del heap), // O(1)
      Nodo padre  = _heap.get(j_padre);              // y el Nodo padre del nodo actual que se encuentra en la posición j-ésima. // O(1)
      if (actual.valor.compareTo(padre.valor) < 0) { // Si valor del nodo actual < valor del padre -> se rompe el MinHeap, entonces // O(1)
        intercambiar(j, j_padre);                    // los intercambio entre sí, // O(1)
        j = j_padre;                                 // y me muevo hacia arriba para poder seguir iterando el while. // O(1)
      } else break;                                  // Si no se rompe el MinHeap (incrementa hacia abajo) => correcto => break! (salgo)
    }
  }

  private void siftDown(int j) { // COMPLEJIDAD O(LOG N)
    /*La función siftUp recibe un índice j asociado a un nodo del array MinHeap, y ejecuta siftDown, no devuelve nada.*/
    int n = _heap.size();                                                 // Guardo la longitud del array (cantidad de elementos del Heap)
    while (true) {                                                        // Itero como máximo todas las filas del Heap // O(log n)
      int i = izq(j);                                                     // Dado un índice j pasado por parámetro, guardo los de sus hijos.
      int d = der(j);
      int m = j;                                                          // Creo una variable para guardar el menor (j/hijo_izq/hijo_der).
      if (i<n && _heap.get(i).valor.compareTo(_heap.get(m).valor)<0) m=i; // Si izq es menor al j, el menor (por ahora) es izq. // O(1)
      if (d<n && _heap.get(d).valor.compareTo(_heap.get(m).valor)<0) m=d; // Si der<menor actual (puede ser j ó izq) => menor es der. // O(1)
      if (m == j) break;                                                  // Si menor=j => no pasó nada => no se rompe el Heap => break!
      intercambiar(j, m);                                                 // Intercambio los nodos del heap, actualizo índices, // O(1)
      j = m;                                                              // y me muevo hacia abajo para seguir iterando hasta algún break.
    }
  }

  //————————————————————————————————————————————————————————————————————————————————————
  // Función Auxiliar:
  //————————————————————————————————————————————————————————————————————————————————————
  private void intercambiar(int i, int j){ // COMPLEJIDAD O(1)
    /*La función aux intercambiar, dados dos índices i, y j asociados a dos nodos del array MinHeap, los permuta entre sí, no devuelve nada.*/
    Nodo nodo_i = _heap.get(i); // Guardo el nodo i // O(1)
    Nodo nodo_j = _heap.get(j); // Guardo el nodo j // O(1)
    _heap.set(i, nodo_j);       // Guardo en i el nodo j // O(1)
    _heap.set(j, nodo_i);       // Guardo en j el nodo i // O(1)
    nodo_i.indice = j;          // Cambio el índice del nodo_i por j // O(1)
    nodo_j.indice = i;          // Cambio el índice del nodo_j por i // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Modificaciones del Heap:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  private void eliminarNodo(Nodo n) { // COMPLEJIDAD O(LOG N) (peor caso)
    /*La función eliminarNodo recibe un nodo asociado al array del MinHeap, lo elimina, y reacomoda el heap para que preserve su estructura.
    El nodo debe pertenecer a este heap, y por lo tanto, tener un índice entre (0,longitud(_heap)). No devuelve nada.*/
    int j     = n.indice;                                                    // Obtengo el índice del nodo a elimianr. // O(1)
    int j_ult = _heap.size() - 1;                                            // y el del último nodo. // O(1)
    if (j<0 || j>j_ult) throw new IllegalArgumentException("Nodo inválido"); // Si el índice es absurdo -> nodo invalido. // O(1)
    if (n.handle != null) _handles.remove(n.handle);                         // Si no, si el nodo tiene handle lo eliminamos. // O(1)
    if (j == j_ult) {                                                        // Si el nodo es el último,
      _heap.remove(j_ult);                                                   // lo eliminamos -> listo! (no se rompe el heap),
      n.indice = -1;                                                         // pero debo volver a setear el índice en menos 1.
      return;                                                                // Salgo.
    }
    Nodo ultimo = _heap.remove(j_ult);                                       // Si no, me guardo el último nodo y lo elimino. // O(1)
    _heap.set(j, ultimo);                                                    // Ahora coloco último nodo en la pos j donde estaba n, // O(1)
    ultimo.indice = j;                                                       // y le coloco el índice j. // O(1)
    if (j > 0) {                                                             // Si aún no llegué a la raíz, // O(1)
      T valor_padre = _heap.get(padre(j)).valor;                             // obtengo el valor de mi padre, y si éste // O(1)
      if (ultimo.valor.compareTo(valor_padre) < 0) {siftUp(j); return;}      // es mayor que ultimo => hago siftUp. Luego salgo. // O(1)
    }                                                                        //
    siftDown(j);                                                             // Si no, hacemos siftDown.
  }

  private void modificarNodo(Nodo nodo, T nuevoValor){ // COMPLEJIDAD O(LOG N)
    /*La función modificarNodo recibe un nodo del array MinHeap y un valor de tipo T y modifica su valor con dicho elemento de tipo T.
    No devuelve nada.*/
    T valor_actual = nodo.valor;                         // Guardo el valor del nodo pasado por parámetro, // O(1)
    int j          = nodo.indice;                        // y su índice // O(1)
    nodo.valor     = nuevoValor;                         // Actualizo su valor por nuevoValor, // O(1)
    if (nuevoValor.compareTo(valor_actual) < 0) {        // y si este es menor que el que había antes, // O(1)
      siftUp(j);                                         // hago siftUp // O(LOG N) 
    } else if (nuevoValor.compareTo(valor_actual) > 0) { // Si no,
      siftDown(j);                                       // hago siftDown // O(LOG N)
    }
  }

  public ArrayList<Handle<T>> devolverHandles() { // O(N)
    /*La función devolverHandles devuelve un ArrayList de Handles (que son de tipo T), que es una lista de los handles asociados al ArrayList
    _heap, que es el array cuya estructura representa el MinHeap.*/
    ArrayList<Handle<T>> res = new ArrayList<>(); // Creo un ArrayList de objetos Handle<T> vacío llamado res, // O(1)
    for (Nodo n : _heap) {                        // y para cada nodo que haya en el heap, // O(1)
      res.add(n.handle);                          // agrego a res sus handles, // O(1) 
    }                                             // Recorro todo el _heap // O(N)
    return res;                                   // Devuelvo res.
  }
  
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Handle del MinHeap:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public class HandleHeap implements Handle<T> {
    /*La clase HandleHeap es la clase que implementa los métodos que se encuentran en la interfaz Handle<T> del archivo Handle.java, y que
    actualiza el handle del MinHeap en caso de eliminación o modificación de sus objetos.*/
    private Nodo _elemento;      // ATRIBUTO PRIVADO: _elemento representa el 'Nodo' al cual el Handle apunta, del Heap.

    private HandleHeap(Nodo n) { // Constructor del Handle dentro del HandleHeap
      this._elemento = n;
    }
    
    public T valor() {
      /*La función valor, devuelve el valor del elemento del handle.*/
      return _elemento.valor; // Devuelvo el valor de tipo T del nodo _elemento (al cual el Handle apunta).
    }

    public void eliminar() {
      /*La función eliminar, al ser llamada, elimina el nodo al cual el Handle apunta. No devuelve nada.*/
      if (_elemento.indice < 0 || _elemento.indice >= _heap.size() || _heap.get(_elemento.indice) != _elemento) {
        throw new IllegalStateException("Handle inválido.");
      }
      eliminarNodo(this._elemento); // Accedo directamente a la función del MinHeap eliminarNodo. // O(LOG N)
    }

    public void modificar(T nuevoValor){
      /*La función modificar, modifica el valor del nodo al cual el Handle apunta. No devuelve nada.*/
      if (_elemento.indice < 0 || _elemento.indice >= _heap.size() || _heap.get(_elemento.indice) != _elemento) {
        throw new IllegalStateException("Handle inválido.");
      }
      modificarNodo(this._elemento, nuevoValor); // Accedo directamente a la función del MinHeap modificarNodo. // O(LOG N)
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————