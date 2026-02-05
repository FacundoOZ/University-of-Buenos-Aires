
//============================================================================================================================================
// Taller 5 // Estructuras Enlazadas
//============================================================================================================================================

/*En este taller, modificaremos la implementación de la clase ABB para que utilice handles. Un handle es un objeto que actúa como referencia
a otro objeto, permitiendo acceder y modificar el objeto referenciado de manera indirecta en O(1). En este caso, el handle será un objeto que
contiene un puntero al nodo de la lista enlazada. De esta manera, podremos acceder y modificar los elementos de la lista sin necesidad de
recorrerla.
Luego, implementaremos una clase que combina una lista enlazada con un árbol binario de búsqueda para almacenar pedidos de comida rápida,
permitiendo acceder a los pedidos tanto por orden de llegada (usando la lista enlazada) como por su identificador (usando el árbol binario de
búsqueda). Se puede asumir que los identificadores siguen una distribución aleatoria, por lo que el árbol binario de búsqueda se mantendrá
balanceado en promedio.
Para resolver el taller, deben modificar la clase ABB<T> (dentro del archivo ABB.java) de manera tal que devuelva un handle al agregar un
elemento y permitia eliminar elementos a través de él.
Implementar la clase SistemaPedidos (en el archivo SistemaPedidos.java) de manera tal que permita agregar pedidos, obtener el pedido con
menor identificador, quitar pedidos por orden de llegada y listarlos tanto por su orden de llegada como por su identificador. Recordar que
los identificadores siguen una distribución aleatoria, por lo que la complejidad promedio de las operaciones sobre el árbol binario de
búsqueda es O(log n).*/

package aed;

// Parte 2: Sistema de Pedidos
//————————————————————————————
/*Implementar la clase SistemaPedidos (en el archivo SistemaPedidos.java) de manera tal que permita agregar pedidos, obtener el pedido con
menor identificador, quitar pedidos por orden de llegada y listarlos tanto por su orden de llegada como por su identificador. Recordar que los
identificadores siguen una distribución aleatoria, por lo que la complejidad promedio de las operaciones sobre el árbol binario de búsqueda es
O(log n).*/

public class SistemaPedidos {

  // Declaro los atributos privados:
  private ListaEnlazada<Pedido> _lista; // "_lista", representará mi lista enlazada donde los nodos serán los pedidos (de tipo "Pedido")
  private ABB<Pedido> _abb;             // "_abb", representará mi ABB, donde los nodos serán los pedidos (también de tipo "Pedido")

  public SistemaPedidos(){               // Constructor del sistema de pedidos.
    this._lista = new ListaEnlazada<>(); // Inicializo los atributos _lista y 
    this._abb   = new ABB<>();           // _abb como mi lista enlazada y mi ABB vacíos, respectivamente.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Agrega un pedido al sistema con complejidad O(log n) en promedio.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void agregarPedido(Pedido pedido){
    _lista.agregarAtras(pedido);            // Agregar un pedido consiste en reciclar los métodos "agregarAtras()" (agrega último),
    _abb.insertar(pedido);                  // e "insertar()" (inserta un elemento) de ListaEnlazada.java y ABB.java, para un pedido.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Devuelve el próximo pedido por orden de llegada y lo elimina del sistema con complejidad O(log n).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public Pedido proximoPedido(){
    if (_lista.longitud() == 0) return null; // Si la lista es vacía -> no hay ningún próximo pedido -> devuelvo null.
    Pedido res = _lista.obtener(0);          // Si no, obtengo el primer elemento de _lista (próximo Pedido), y lo guardo en una variable res.
    _lista.eliminar(0);                      // Ahora que lo tengo, lo elimino tanto de la lista enlazada,
    _abb.eliminar(res);                      // como del ABB, ya que lo pedía el enunciado.
    return res;                              // -> devuelvo res, que representa el pedido que estaba próximo en mi sistema de pedidos.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Devuelve el pedido con menor identificador con complejidad O(log n) en promedio.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public Pedido pedidoMenorId(){
    if (_abb.cardinal() == 0) return null; // Si el ABB no tiene ningún elemento -> no hay ningún pedido -> devuelvo null.
    Pedido res = _abb.minimo();            // Si no, obtengo el mínimo del árbol y lo guardo en una variable res de tipo "Pedido".
    return res;                            // -> devuelvo res.
  }
  // Observación: Utilicé el ABB porque tiene mínimo, pero la lista no, y no elimino el mínimo del árbol porque no lo pide el enunciado.

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8 // Devuelve un string con los pedidos en orden de llegada en O(n) (por ej.: [28, 71, 17, 261, 21])
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public String obtenerPedidosEnOrdenDeLlegada(){ // Solo importa el orden (no el sucesor) -> uso la lista y no el ABB.
    if (_lista.longitud() == 0) return "[]";      // Si la lista es vacía -> devuelvo []:
    String res = "[";                             // Si no, inicializo una variable res de tipo String en "[".
    int j = 0;                                    // Inicializo un entero j en cero para un while.
    while (j < _lista.longitud()) {               // Mientras j se encuentre en la longitud de "_lista",
        res += _lista.obtener(j).toString();      // obtengo los pedidos en orden de llegada -> los convierto a String -> los agrego a res.
        if (j < _lista.longitud()-1) res +=", ";  // Si j no es el último => agrego coma (vendrá otro), pues ya agregué el pedido j-ésimo.
        j++;                                      // Sumo 1 a mi iterador j, y repito el proceso.
    }                                             // Si es el último -> no entré al if -> salgo del while.
    res += "]";                                   // Cierro la lista,
    return res;                                   // y devuelvo res.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 9 // Retorna un string con los pedidos ordenados por su identificador en O(n) (por ej.: {17, 21, 28, 71, 261}).
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public String obtenerPedidosOrdenadosPorId() {  // Ahora, necesito arrancar del mínimo y recorrer de forma creciente -> debo usar el ABB!
    if (_abb.cardinal() == 0) return "{}";        // Si el ABB no tiene ningún nodo -> devuelvo {}.
    String res = "{";                             // Si no, inicializo una variable res de tipo String en "{".
    ABB<Pedido>.ABB_Iterador j = _abb.iterador(); // Tengo la clase iterador del ABB que busca el sucesor! => inicio iterador (lo llamo j)
    boolean primero = true;                       // Si estoy justo en el primero, inicializo esta variable "primero" booleana en True.
    while (j.haySiguiente()) {                    // Mientras haya nodo siguiente (reciclo "boolean haySiguiente()" del iterador del ABB),
      if (!primero) res += ", ";                  // Si soy el primero -> no entro al if -> no agrego ", " a res. Si no, agrego ", " a res.
      Pedido p = j.siguiente();                   // Creo variable p que guarde el siguiente pedido (reciclo "T siguiente()" de iterador ABB),
      res += p.toString();                        // y agrego dicha variable p en formato String.
      primero = false;                            // Si llego acá, "primero" pasa a false => será false para todo el while => agrego ","
    }                                             // Cuando llegué al último, no entro al while => no agregué ", " incorrectamente.
    res += "}";                                   // -> cierro la llave del string res.
    return res;                                   // -> devuelvo res.
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————