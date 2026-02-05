
//============================================================================================================================================
// Taller 2 // Programación Orientada a Objetos
//============================================================================================================================================

// Primera parte: Agenda
//——————————————————————
/*Vamos a programar un pequeño sistema para manejar recordatorios. Nos interesa que el sistema permita agendar recordatorios para una fecha
y una hora dada considerando solo el lapso de un año. El sistema debe imprimir los recordatorios de la fecha actual. La Agenda mantiene la
fecha actual y el conjunto de recordatorios.*/

package aed;

public class Agenda {

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 16 // Implementar el constructor Agenda(Fecha) y el método fechaActual de la clase Agenda.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El constructor Agenda(Fecha) recibe por parámetro la fecha del día de hoy.
  El método fechaActual devuelve la fecha del día de hoy según la agenda. No debe haber aliasing entre la fecha devuelta y la instancia de
  Agenda.*/

  private Fecha _fecha;                                         // Declaro los atributos que voy a utilizar.
  private ArregloRedimensionableDeRecordatorios _recordatorios;

  public Agenda(Fecha fechaActual) {
    _fecha = new Fecha(fechaActual);                              // fechaActual será una nueva instancia de _fecha (para evitar aliasing),
    _recordatorios = new ArregloRedimensionableDeRecordatorios(); // e inicializo el arreglo redimensionable, también evitando aliasing.
  }

  public Fecha fechaActual() {
    Fecha copiaFecha = new Fecha(_fecha); // Creo una copia de tipo Fecha, que sea una nueva instancia de _fecha,
    return copiaFecha;                    // y la devuelvo.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 17 // Implementar el método agregarRecordatorio y toString de la clase Agenda.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método agregarRecordatorio agrega un recordatorio a la agenda.
  El método toString debe retornar un String que contenga los recordatorios de la fecha actual, con formato como el del ejemplo:

      10/5
      =====
      Clase Algo @ 10/5 9:0
      Labo Algo @ 10/5 11:0

  Notar que se imprime primero la fecha actual, luego un separador de cinco = y finalmente un recordatorio por línea.
  Notar que el método toString ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.*/

  public void agregarRecordatorio(Recordatorio recordatorio) {
    _recordatorios.agregarAtras(recordatorio);                // Mediante la función anterior, agrego "recordatorio" al final de lista actual.
  }

  @Override
  public String toString() {
    String res = "";                                      // Inicializo una variable String: res, como un string vacío "".
    res += _fecha.toString() + "\n" + "=====" + "\n";     // Le agrego la fecha (en formato string) y los 5 iguales, con nuevo rengloón (\n).
    for (int i = 0; i < _recordatorios.longitud(); i++) { // Luego, para cada elemento que haya en recordatorios,
      Recordatorio x = _recordatorios.obtener(i);         // lo obtengo y lo guardo en una variable x,
      if (x.fecha().equals(_fecha)) {                     // y si la fecha de este recordatorio coincide con _fecha (la actual),
        res += x.toString() + "\n";                       // lo agrego a res, hago nuevo renglón, y repito el procedimiento.
      }
    }
    return res;                                           // Devuelvo res.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 18 // Implementar el método incrementarDia de la clase Agenda.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método incrementarDia incrementa en un dia la fecha actual de la agenda.*/

  public void incrementarDia() {
    _fecha.incrementarDia();     // El método incrementar día, debe aumentar la fecha en 1 (no devuelve nada).
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————