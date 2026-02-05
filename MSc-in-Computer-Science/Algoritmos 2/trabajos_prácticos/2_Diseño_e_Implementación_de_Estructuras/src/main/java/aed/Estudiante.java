
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

package aed;
import java.util.ArrayList;

public class Estudiante<T> {
  /*Esta clase contiene todos los métodos que caracterizan a un estudiante de la instancia Edr.*/
  private int   _id;               // ATRIBUTOS PRIVADOS: un estudiante se identifica unívocamente por su _id (un entero positivo),
  private int[] _respuestas;       // por un arreglo de enteros _respuestas, que representa los ejercicios del examen que resuelve,
  private Handle<NotaFinal> _nota; // una _nota, que se actualiza en todo momento de tipo Handle<T>,
  private boolean _sospechoso;     // y los estados booleanos de si resulta sospechoso de copiarse o no,
  private boolean _entregado;      // y si ha entregado o no su examen.
  
  public int id() {return _id;}    // Constructores de los atributos privados.

  public int[] respuestas() {
    int[] copia = new int[_respuestas.length];
    for (int i = 0; i < _respuestas.length; i++) {
        copia[i] = _respuestas[i];
    }
    return copia;
  }

  public Handle<NotaFinal> nota() {return _nota;}       //
  public boolean     sospechoso() {return _sospechoso;} //
  public boolean      entregado() {return _entregado;}  //

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Constructor de la clase Estudiante<T>:
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public Estudiante(int id, int[] respuestas, Handle<NotaFinal> nota, boolean sospechoso, boolean entregado){
    this._id         = id;         // Inicializa la instancia de acuerdo a sus atributos privados.
    this._respuestas = respuestas;
    this._nota       = nota;
    this._sospechoso = sospechoso;
    this._entregado  = entregado;
  }
  
  public void cambiarNota(Handle<NotaFinal> nuevaNota) {
    /*El método cambiar nota actualiza el atributo privado del estudiante _nota por una nueva nota de tipo Handle<T>. No devuelve nada.*/
    this._nota = nuevaNota;
  }

  public void cambiarRespuestas(int[] respuestas){
    /*La función cambiar respuestas, actualiza todas las respuestas de un estudiante dado mediante el arreglo de enteros "respuestas" que
    recibe como parámetro. No devuelve nada.*/
    this._respuestas = new int[respuestas.length];
    for(int j=0; j < respuestas.length; j++){
      this._respuestas[j] = respuestas[j];
    }
  }

  public void cambiarEntregado(boolean entregado) {
    /*El método cambiar entregado, actualiza el estado del atributo booleano _entregado de un estudiante dado. No devuelve nada.*/
    this._entregado = entregado;
  }

  public void cambiarSospechoso(boolean sospechoso){
    /*El método cambiar entregado, actualiza el estado del atributo booleano _sospechoso de un estudiante dado. No devuelve nada.*/
    this._sospechoso = sospechoso;
  }

  public void responderConsigna(int nroEjercicio, int valorRespuesta, double puntaje) {
    /*El método responder consigna, recibe el ejercicio al respuesta que cambia y la nueva nota, que ya fue calculada en edr que tiene el
    examen canonico para hacerlo.*/
    NotaFinal nuevaNota = new NotaFinal(puntaje, this.id());
    this.nota().modificar(nuevaNota);
    this._respuestas[nroEjercicio] = valorRespuesta;
    this._nota = this.nota();
  }

  public void reemplazarExamen(int[] nuevasRespuestas, Handle<NotaFinal> nuevaNota) {
    /*El método reemplazar examen, recibe las nuevas repsuestas y la nuevanota a la que va a puntar el handle, y cambia el examen entero.*/
    int[] copia = new int[nuevasRespuestas.length];     // Hago copia para evitar aliasing (cambiar nuevasRespuestas no afecta respuestas).
    for (int i = 0; i < nuevasRespuestas.length; i++) {
        copia[i] = nuevasRespuestas[i];
    }
    this._respuestas = copia; 
    this._nota = nuevaNota;
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————