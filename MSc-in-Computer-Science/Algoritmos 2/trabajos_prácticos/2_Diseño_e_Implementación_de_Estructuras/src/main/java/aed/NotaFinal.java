
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

package aed;

public class NotaFinal implements Comparable<NotaFinal> {
  /*Esta clase contiene todos los métodos que contiene las características de un estudiante tanto en el ArrayList _aula como en el MinHeap
  _heapNotas que se encuentran en el archivo principal Edr.java.*/

  // Atributos Públicos:
  public double _nota; // _nota de tipo double
  public int    _id;   // y el _id del estudiante de tipo entero (será positivo)

  public int    id()   {return this._id;}   // Constructores de los atributos públicos _id (a utilizar en otros archivos .java)
  public double nota() {return this._nota;} // y _nota.

  public NotaFinal(double nota, int id){ // Constructor de la clase NotaFinal
    this._nota = nota;
    this._id   = id;
  }

  public int compareTo(NotaFinal otra){
    int res = Double.compare(this._nota, otra._nota); // Compara primero por id,
    if (res != 0) return res;                         // Si res no es cero, devuelvo res (es > 0 si this > otra, y viceversa)
    return this._id - otra._id;                       // Si las notas coinciden => desempato por id => misma lógica.
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) return true;                                                   // Chequeo si es el mismo objeto.
    if (obj == null || getClass() != obj.getClass()) return false;                  // Chequeo si es nulo o de una clase diferente.
    NotaFinal otra = (NotaFinal) obj;                                               // Convierto el objeto y comparo los campos.
    return (this._id == otra._id) && (Double.compare(this._nota, otra._nota) == 0); // Compara el id Y la nota.
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————