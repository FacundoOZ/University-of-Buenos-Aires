
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

package aed;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.util.ArrayList;
import java.util.Arrays;

class testsHeap {
  Integer[] arreglo;
  Heap<Integer> heap;

  @BeforeEach
  void heapPredeterminado(){
    arreglo = new Integer[]{5,1,3,7,8,9,2};
    heap    = new Heap<>(arreglo);
  }

  @Test
  void minimosYMaximosCorrectos() {
    arreglo = new Integer[]{1,4,7,12,16,293}; // al principio
    heap    = new Heap<>(arreglo);
    assertEquals(1, heap.minimo());
    assertEquals(293, heap.maximo());

    arreglo = new Integer[]{14,11,8,7,3};     // al final
    heap    = new Heap<>(arreglo);
    assertEquals(3, heap.minimo());
    assertEquals(14, heap.maximo());

    arreglo = new Integer[]{9,5,2,11,3,7,6};   // al medio
    heap    = new Heap<>(arreglo);
    assertEquals(2, heap.minimo());
    assertEquals(11, heap.maximo());

    arreglo = new Integer[]{24};               // Son el mismo
    heap    = new Heap<>(arreglo);
    assertEquals(24, heap.minimo());
    assertEquals(24, heap.maximo());
  }

  Double[] lista_float;
  Heap<Double> heap_double;
  @Test
  void heapDeDoubles() {
    lista_float = new Double[]{12.0, 14.0, 19823000.0, -142.0, 987345.0};
    heap_double = new Heap<>(lista_float);
    assertEquals(-142.0, heap_double.minimo().doubleValue());
    assertEquals(19823000.0, heap_double.maximo().doubleValue());
  }

  String[] lista_string;
  Heap<String> heap_string;
  @Test
  void heapDeString() {
    lista_string = new String[]{"hola", "mundo", "!"};
    heap_string = new Heap<>(lista_string);
    assertEquals("!", heap_string.minimo());
    assertEquals("mundo", heap_string.maximo());
  }

  @Test
  void longitudesCorrectas() {
    arreglo = new Integer[]{1,3,6,9,10};
    heap    = new Heap<>(arreglo);
    assertEquals(5, heap.longitud());

    arreglo = new Integer[]{};
    heap    = new Heap<>(arreglo);
    assertEquals(0, heap.longitud());
  }

  @Test
  void encolarElementos() {
    Heap<Integer> h = new Heap<Integer>();
    assertEquals(0, h.longitud());
    h.encolar(10);
    h.encolar(3);
    h.encolar(7);
    assertEquals(3, h.minimo());
    assertEquals(3, h.longitud());
    assertEquals(10, h.maximo());
  }

  @Test
  void desencolarHeapVacio() {
    Heap<Integer> h = new Heap<Integer>();
    assertEquals(null, h.desencolarMinimo());
  }

  @Test
  void desencolarElementos() {
    Heap<Integer> h = new Heap<Integer>(new Integer[]{9,6,2,3});
    assertEquals(4, h.longitud());         // la longitud disminuye sucesivamente

    assertEquals(2, h.desencolarMinimo()); // obtengo el mínimo correspondiente
    assertEquals(3, h.longitud());

    assertEquals(3, h.desencolarMinimo()); // voy obteniendo los elementos en orden creciente
    assertEquals(2, h.longitud());

    assertEquals(6, h.desencolarMinimo());
    assertEquals(1, h.longitud());

    assertEquals(9, h.desencolarMinimo());
    assertEquals(0, h.longitud());
  }

  @Test
  void desencolarHeapConRepetidos() {
    Heap<Integer> h = new Heap<Integer>(new Integer[]{9,9,9,9});
    assertEquals(4, h.longitud());

    assertEquals(9, h.desencolarMinimo()); // obtengo siempre el mismo
    assertEquals(9, h.desencolarMinimo());
    assertEquals(9, h.desencolarMinimo());
    assertEquals(9, h.desencolarMinimo());

    assertEquals(0, h.longitud());
  }

  //————————————————————————————————————————————————————————————————————————————————————
  // HANDLE:
  //————————————————————————————————————————————————————————————————————————————————————
  @Test
  void modificarActualizaMinimo() { // SiftUp
    ArrayList<Handle<Integer>> handles = heap.devolverHandles(); // Obtengo los handles del heap, del heap [5,1,3,7,8,9,2] del beforeEach
    Heap<Integer>.HandleHeap h = (Heap<Integer>.HandleHeap) handles.get(3); // Obtengo s[3] (el "7")
    assertEquals(9, heap.maximo());
    h.modificar(-23);                         // El valor modificado se volvió el mínimo -> hubo SiftUp
    assertEquals(-23, heap.minimo());
    assertEquals(9, heap.maximo()); // Máximo queda igual
  }

  @Test
  void modificarActualizaMaximo() {
    ArrayList<Handle<Integer>> handles = heap.devolverHandles(); // Obtengo el [5,1,3,7,8,9,2]
    Heap<Integer>.HandleHeap h = (Heap<Integer>.HandleHeap) handles.get(2); // Agarro cualquiera (el "3")

    assertEquals(9, heap.maximo());
    h.modificar(1000);               // El valor modificado se volvió el máximo -> hubo SiftDown
    assertEquals(1000, heap.maximo()); // Máximo cambia
    assertEquals(1, heap.minimo());    // Mínimo queda igual
  }

  @Test
  void handleEliminaElementoCorrecto() {
    ArrayList<Handle<Integer>> handles = heap.devolverHandles(); // Obtengo el [5,1,3,7,8,9,2]
    Heap<Integer>.HandleHeap h = (Heap<Integer>.HandleHeap) handles.get(4); // Agarro cualquiera (el "8")

    int val = h.valor(); // Obtengo y guardo el valor de tipo T (int) de dicho índice, es decir, el 8.
    h.eliminar();        // Lo elimino

    ArrayList<Integer> resto = new ArrayList<>();                   // Creo un nuevo array,
    while (heap.longitud() > 0) resto.add(heap.desencolarMinimo()); // Desencolo todos los demás y los pongo en el array,
    assertFalse(resto.contains(val));                               // Chequeamos que el que eliminamos efectivamente se borró.
  }

  @Test
  void eliminarEsAbsurdo() {
    Heap<Integer>.HandleHeap h = (Heap<Integer>.HandleHeap) heap.devolverHandles().get(0); // Obtengo el primero en h (el "5")
    h.eliminar(); // Elimino el "5"
    assertThrows(IllegalStateException.class, h::eliminar); // no hay más -> no puedo eliminar lo que no existe
  }

  @Test
  void eliminarVariasVeces() {
    arreglo = new Integer[]{4,4,4,4};
    heap    = new Heap<>(arreglo);
    ArrayList<Handle<Integer>> handles = heap.devolverHandles(); // Obtengo los handles de [4,4,4,4]
    Heap<Integer>.HandleHeap A = (Heap<Integer>.HandleHeap) handles.get(0);
    A.eliminar();                                                                 // Los puedo eliminar correctamente
    Heap<Integer>.HandleHeap B = (Heap<Integer>.HandleHeap) handles.get(1);
    B.eliminar();                                                                 // Los puedo eliminar correctamente
    Heap<Integer>.HandleHeap C = (Heap<Integer>.HandleHeap) handles.get(2);
    C.eliminar();                                                                 // Los puedo eliminar correctamente
    Heap<Integer>.HandleHeap D = (Heap<Integer>.HandleHeap) handles.get(3);
    D.eliminar();                                                                 // Los puedo eliminar correctamente
  }    
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————