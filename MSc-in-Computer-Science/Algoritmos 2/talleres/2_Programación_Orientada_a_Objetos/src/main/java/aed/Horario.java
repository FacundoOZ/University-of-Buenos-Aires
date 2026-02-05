
// Parte 1.2: Horario
//———————————————————

package aed;

public class Horario {

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Implementar el constructor Horario(int, int) y los métodos hora y minutos de la clase Horario.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El constructor Horario(int, int) recibe por parámetro la hora y los minutos del horario a construir.
  El método hora devuelve la hora del horario.
  El método minutos devuelve los minutos del horario.*/

  private int _hora;    // Declaro los atributos de la clase.
  private int _minutos;

  public Horario(int hora, int minutos) { // Constructor Horario. Recibe (int hora, int minutos) y no devuelve nada.
    _hora    = hora;                      // Asigno a los atributos _hora y _minutos, los parámetros hora y minutos del constructor Horario.
    _minutos = minutos;
  }

  public int hora() { // El método hora devuelve la hora de Horario.
    return _hora;
  }

  public int minutos() { // El método minutos devuelve los minutos del Horario.
    return _minutos;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Implementar el método toString de la clase Horario.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método toString debe retornar un String con el formato h:m. Por ejemplo, 10:5 corresponde a las 10:05 hs.
  Notar que el método toString ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.*/

  @Override                        // Sobreescribimos el método toString pre-existente
  public String toString() {
    return _hora + ":" + _minutos; // Devolvemos un string con el valor de _hora y _minutos en formato "h:m".
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Implementar el método equals de la clase Horario.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método equals debe retornar verdadero si el objeto recibido por parámetro es un horario y es igual al horario original.
  Notar que el método equals ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.
  Notar que el método recibe como parámetro cualquier objeto, no necesariamente un Horario.*/

  @Override
  public boolean equals(Object otro) {
    if ((otro == null) || (otro.getClass() != this.getClass())) {                  // Si otra es vacío, o no pertenece a la clase Fecha,
      return false;                                                                // no son iguales.
    } else {                                                                       // Si no,
      Horario otroHorario = (Horario) otro;                                        // Casting: Cambio tipo del objeto "otro" a tipo Horario.
      return ((otroHorario._hora == _hora) && (otroHorario._minutos == _minutos)); // Accedo a sus variables _hora/_minutos y comparo.
    }
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————