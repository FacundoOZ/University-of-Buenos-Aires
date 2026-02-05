
// Parte 1.3: Recordatorio
//————————————————————————

package aed;

public class Recordatorio {

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8 // Implementar el constructor Recordatorio(String,Fecha,Horario) y métodos mensaje, fecha, horario de la clase Recordatorio.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El constructor Recordatorio(String, Fecha, Horario) recibe por parámetro el mensaje del recordatorio, la fecha y el horario en que ocurre
  el evento.
  El método fecha devuelve la fecha del recordatorio. No debe haber aliasing entre la fecha devuelta y la instancia del Recordatorio (se debe
  devolver una copia).
  El método horario devuelve el horario del recordatorio.
  El método mensaje devuelve el mensaje del recordatorio.*/

  private String _mensaje;  // Declaro los atributos de la clase.
  private Fecha _fecha;
  private Horario _horario;

  public Recordatorio(String mensaje, Fecha fecha, Horario horario) { // Constructor. Recibe mensaje, fecha, horario y no devuelve nada.
    _mensaje = mensaje;                                               // Asigno a los atributos _..., los parámetros del constructor.
    _fecha   = new Fecha(fecha);                                      // Evito Aliasing inicializando una nueva instancia.
    _horario = horario;
  }

  public Fecha fecha() {                  // El método fecha devuelve la fecha (una copia) del recordatorio.
    Fecha copiaFecha = new Fecha(_fecha); // Evito Aliasing.
    return copiaFecha;
  }

  public Horario horario() { // El método horario devuelve el horario del recordatorio.
    return _horario;
  }

  public String mensaje() { // El método mensaje devuelve el mensaje del recordatorio.
    return _mensaje;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 9 // Implementar el método toString de la clase Recordatorio.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método toString debe retornar un String con el formato mensaje @ fecha horario. Por ejemplo, Cumple Agustin @ 6/12 17:30 corresponde al
  recodatorio con mensaje “Cumple Agustin”, fecha 6/12 y horario 17:30 hs.
  Notar que el método toString ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.*/

  @Override                                            // Sobreescribo el método toString.
  public String toString() {
    return _mensaje + " @ " + _fecha + " " + _horario; // Devuelvo el string solicitado.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 10 // Implementar el método equals de la clase Recordatorio.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método equals debe retornar verdadero si el objeto recibido por parámetro es un recordatorio y es igual al recordatorio original.
  Notar que el método equals ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.
  Notar que el método recibe como parámetro cualquier objeto, no necesariamente una Recordatorio.*/

  @Override
  public boolean equals(Object otro) {
    if ((otro == null) || (otro.getClass() != this.getClass())) { // Si otro es vacío, o no pertenece a la clase Fecha,
      return false;                                               // no son iguales.
    } else {                                                      // Si no,
      Recordatorio otroRecordatorio = (Recordatorio) otro;        // Casting: Cambiamos el tipo del objeto "otro" a tipo Recordatorio.
      return ((_mensaje.equals(otroRecordatorio._mensaje))        // Así, accedo a sus variables y comparo:
           && (_fecha.equals(otroRecordatorio._fecha))
           && (_horario.equals(otroRecordatorio._horario)));
    }
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————