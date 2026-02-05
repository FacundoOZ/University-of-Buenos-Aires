
//============================================================================================================================================
// Taller 3 // Listas Enlazadas e Iteradores
//============================================================================================================================================

package aed;

interface Secuencia<T> {
  /*La interfaz Secuencia<T> es una interfaz de elementos de tipo T, que se utilizará en el archivo ListaEnlazada.java, y que declara los
  siguientes métodos públicos:*/

  public int longitud();                              // Devuelve la cantidad de elementos que contiene la Secuencia.
  public void agregarAdelante(T elem);                // Agrega un elemento al principio de la Secuencia.
  public void agregarAtras(T elem);                   // Agrega un elemento al final de la Secuencia.
  public T obtener(int indice);                       // Devuelve una referencia al elemento en la i-ésima posición de la Secuencia.
  public void eliminar(int indice);                   // Elimina el i-ésimo elemento de la Secuencia.
  public void modificarPosicion(int indice, T valor); // Reemplaza al elemento i-ésimo de la Secuencia por el elemento pasado por parámetro.
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————