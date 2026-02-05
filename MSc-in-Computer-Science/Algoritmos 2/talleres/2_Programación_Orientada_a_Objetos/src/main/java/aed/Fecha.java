
// Parte 1.1: Fecha
//—————————————————
// En el contexto del ejercicio, una fecha representa un día del año. Permite recuperar el mes y el día.

package aed;

public class Fecha {

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 1 // Implementar el constructor Fecha(int, int) y los métodos dia y mes de la clase Fecha.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El constructor Fecha(int, int) recibe por parámetro el día y el mes de la fecha a construir.
  El método dia devuelve el día de la fecha.
  El método mes devuelve el número de mes de la fecha.*/

  private int _dia; // Declaro los atributos de la clase.
  private int _mes;

  public Fecha(int dia, int mes) { // Constructor Fecha. Recibe (int dia, int mes) y no devuelve nada.
    _dia = dia;                    // Asigno a los atributos _dia y _mes, los parámetros dia y mes del constructor Fecha.
    _mes = mes;
  }

  public Fecha(Fecha fecha) { // Constructor de copia.
    this._dia = fecha._dia;   // Al objeto Fecha, le asigno los valores de _dia y _mes del objeto fecha.
    this._mes = fecha._mes;
  }

  public Integer dia() { // El método día devuelve el día de la fecha.
    return _dia;
  }

  public Integer mes() { // El método mes devuelve el mes de la fecha.
    return _mes;
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 2 // Implementar el método toString de la clase Fecha.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método toString debe retornar un String con el formato d/m. Por ejemplo, 12/6 corresponde al 12 de junio.
  Notar que el método toString ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.*/

  @Override                   // Sobreescribimos el método toString pre-existente
  public String toString() {
    return _dia + "/" + _mes; // Devolvemos un string con el valor de _dia y _mes en formato "d/m".
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 3 // Implementar el método incrementarDia de la clase Fecha.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método incrementarDia debe incrementar en un día la fecha (ignorando años bisiestos).
  Pueden aprovechar el método provisto diasEnMes.*/

  private int diasEnMes(int mes) { // Método diasEnMes, me dice cuántos días en total tiene cada mes del año.
    int dias[] = {
      31, 28, 31, 30, 31, 30,      // ene, feb, mar, abr, may, jun
      31, 31, 30, 31, 30, 31       // jul, ago, sep, oct, nov, dic
    };
    return dias[mes - 1];
  }

  public void incrementarDia() {          // 'void' => no retorno nada. Solo actualizaremos la variable _dia (y _mes cuando corresponda)
    if ((_dia == 31) && (_mes == 12)) {   // Si es justo "31/12" => debo cambiar _dia y _mes => "1/1"
      _dia = 1;
      _mes = 1;
    } else if (_dia == diasEnMes(_mes)) { // Si no, si _dia es el último (por ej. "28/2"), entonces:
      _dia = 1;                           // _dia = 1, y 
      _mes = _mes + 1;                    // _mes -> _mes + 1 (cambio de mes).
    } else {
      _dia = _dia + 1;                    // Si no, solo aumenta un día del mismo mes.
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 4 // Implementar el método equals de la clase Fecha.
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  /*El método equals debe retornar verdadero si el objeto recibido por parámetro es una fecha y es igual a la fecha original.
  Notar que el método equals ya tiene una implementación por defecto y lo que debe hacerse es una sobrecarga (override) de la misma.
  Notar que el método recibe como parámetro cualquier objeto, no necesariamente una Fecha.*/

  @Override
  public boolean equals(Object otra) {
    if ((otra == null) || (otra.getClass() != this.getClass())) {    // Si otra es vacío, o no pertenece a la clase Fecha,
      return false;                                                  // no son iguales.
    } else {                                                         // Si no,
      Fecha otraFecha = (Fecha) otra;                                // Casting: Cambiamos el tipo del objeto "otra" a tipo Fecha.
      return ((otraFecha._dia == _dia) && (otraFecha._mes == _mes)); // Así, puedo acceder a variables _dia/_mes y realizar la comparación.
    }
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————