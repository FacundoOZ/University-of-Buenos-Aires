
//============================================================================================================================================
// Taller 4 // Árboles Binarios de Búsqueda (ABB's)
//============================================================================================================================================

package aed;

interface Conjunto<T> {
  /*La interfaz Conjunto<T> declara los siguientes métodos:*/

  public int cardinal();            // Devuelve la cantidad de elementos del conjunto.
  public T minimo();                // Devuelve el menor elemento del conjunto.
  public T maximo();                // Devuelve el mayor elemento del conjunto.
  public boolean pertenece(T elem); // Devuelve verdadero si el elemento pertenece al conjunto.
  public void insertar(T elem);     // Agrega un elemento al conjunto.
  public void eliminar(T elem);     // Elimina el elemento del donjunto.
  public String toString();         // Imprime el conjunto.
  // public ABB<T> copiar();        // Retorna un conjunto con los mismos elementos.
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————