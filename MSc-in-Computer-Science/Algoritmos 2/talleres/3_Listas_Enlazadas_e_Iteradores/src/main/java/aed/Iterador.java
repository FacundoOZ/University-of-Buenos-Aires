
//============================================================================================================================================
// Taller 3 // Listas Enlazadas e Iteradores
//============================================================================================================================================

package aed;

interface Iterador<T> {
  /*La interfaz Iterador<T> es una interfaz de elementos de tipo T, que se utilizará en el archivo ListaEnlazada.java, y que declara los
  siguientes métodos públicos:*/

  public boolean haySiguiente(); // Devuelve true si hay un elemento siguiente al iterador, y false en caso contrario.
  public boolean hayAnterior();  // Devuelve true si hay un elemento anterior al iterador, y false en caso contrario.
  public T siguiente();          // Devuelve el elemento siguiente al iterador y avanza al iterador a la posición siguiente.
  public T anterior();           // Devuelve el elemento anterior al iterador y retrocede al iterador a la posición anterior.
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————