
//============================================================================================================================================
// Taller 2 // Programación Orientada a Objetos
//============================================================================================================================================

// Segunda parte: Arreglo Redimensionable de Recordatorios
//————————————————————————————————————————————————————————
/*El objetivo de esta sección es implementar la clase ArregloRedimensionableDeRecordatorios. El ArregloRedimensionableDeRecordatorios es una
implementación sencilla de una secuencia de recordatorios. La implementación se basa en guardar los elementos en un arreglo. Cuando el arreglo
se llena, lo que debe hacerse es crear un nuevo arreglo más grande, copiar los elementos del antiguo arreglo al nuevo, y reemplazar el arreglo
viejo por el nuevo.*/

package aed;

class ArregloRedimensionableDeRecordatorios {

  private Recordatorio[] _arreglo; // Declaro los atributos de la clase.
  private int _longitud;

  public ArregloRedimensionableDeRecordatorios() {
    _arreglo  = new Recordatorio[0];               // Inicializo el array que contendrá los recordatorios, es decir, _arreglo = []
    _longitud = 0;                                 // La cantidad de recordatorios que haya en mi arreglo, será inicialmente cero (0). 
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 11 // Implementar los métodos longitud, agregarAtras y obtener de la clase ArregloRedimensionableDeRecordatorios.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método longitud devuelve la cantidad de elementos en la secuencia.
  El método agregarAtras, extiende la secuencia con el elemento recibido por parámetro.
  El método obtener devuelve el elemento en la posición i.*/

  public int longitud() { // El método longitud devuelve la cantidad de recordatorios que haya en mi arreglo.
    return _longitud;
  }

  public void agregarAtras(Recordatorio i) {
    Recordatorio[] nuevoArreglo = new Recordatorio[_arreglo.length + 1]; // Creo un nuevo arreglo con un elemento más que el actual.
    for (int j = 0; j < _arreglo.length; j++) {                          // Para cada elemento desde 0 a len(arreglo)-1,
      nuevoArreglo[j] = _arreglo[j];                                     // coloco el que había originalmente.
    }
    nuevoArreglo[_arreglo.length] = i;                                   // En la nueva posición (el último), agrego el nuevo recordatorio.
    _arreglo = nuevoArreglo;                                             // Actualizo el arreglo,
    _longitud++;                                                         // y la longitud.
  }

  public Recordatorio obtener(int i) {
    return _arreglo[i];                // Devuelvo el elemento i-ésimo del arreglo de recordatorios.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 12 // Implementar el método quitarAtras de la clase ArregloRedimensionableDeRecordatorios.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método quitarAtras elimina el último elemento de la secuencia.*/

  public void quitarAtras() {
    Recordatorio[] nuevoArreglo = new Recordatorio[_arreglo.length - 1]; // Creo un nuevo arreglo con un elemento menos que el actual.
    for (int i = 0; i < (_arreglo.length - 1); i++) {                    // Para cada elemento desde 0 a len(arreglo)-2 (no agrego el último),
      nuevoArreglo[i] = _arreglo[i];                                     // coloco el que había originalmente.
    }
    _arreglo = nuevoArreglo;                                             // Actualizo el arreglo,
    _longitud--;                                                         // y la longitud.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 13 // Implementar el método modificarPosicion de la clase ArregloRedimensionableDeRecordatorios.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método modificarPosicion guarda el valor recibido por parámetro en la posición indicada del arreglo.*/

  public void modificarPosicion(int indice, Recordatorio valor) {
    _arreglo[indice] = valor;                                     // En la posición "indice" actualizo el Recordatorio "valor".
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 14 // 
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*Implementar el constructor por copia de la clase ArregloRedimensionableDeRecordatorios. El constructor por copia de una clase es el que
  toma como único parámetro otra instancia de la misma clase y lo usa para construir una copia.
  No debe haber aliasing entre los dos arreglos.
  ¿Cuantás veces se reserva memoria para el arreglo en una invocación del constructor por copia? Dicho de otra forma, ¿cuántas operaciones
  new se realizan?*/

  public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) { // Vector tiene toda la información de Arreglo.
    _longitud = vector._longitud;                                                              // Copio lo que haya en vector en _longitud, y
    _arreglo  = new Recordatorio[vector._arreglo.length];                                      // lo de _arreglo.length en nuevo _arreglo.
    for (int i = 0; i < _longitud; i++) {                                                      // Para i de 0 a _longitud en vector._arreglo,
      _arreglo[i] = vector._arreglo[i];                                                        // lo copiamos en el nuevo _arreglo.
    }
  }

  // Se realiza solo una única operación new.

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 15 // Implementar el método copiar de la clase ArregloRedimensionableDeRecordatorios.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método copiar retorna un nuevo arreglo igual al original.
  No debe haber aliasing entre los dos arreglos.
  ¿Cuantás veces se reserva memoria para el arreglo en una invocación del método copiar? Dicho de otra forma, ¿cuántas operaciones new se
  realizan?
  Si no usaste el constructor por copia, pensar la manera de hacerlo usandolo.*/

  public ArregloRedimensionableDeRecordatorios copiar() {
    ArregloRedimensionableDeRecordatorios copia = new ArregloRedimensionableDeRecordatorios(); // Creamos una copia de ArregloRedim...
    copia._longitud = this._longitud;                                                          // Pido que la longitud de copia sea la actual,
    copia._arreglo  = new Recordatorio[this._arreglo.length];                                  // y para elementos de arreglo (evito Aliasing)
    for (int i = 0; i < this._longitud; i++) {
      copia._arreglo[i] = this._arreglo[i];                                                    // Ya copié la longitud, ahora sus elementos.
    }
    return copia;                                                                              // Devuelvo la copia.
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————