
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

/*Algoritmos y Estructuras de Datos
  —————————————————————————————————
  Grupo: Java Haters
  ——————————————————

  Integrantes             LU        Correo electrónico
  ————————————————————————————————————————————————————————————
  Burunov, Celina          23/25    celinaburunov@gmail.com
  Doublier, Galo          629/25    galodoublier@gmail.com
  Otero Zappa, Facundo    339/20    facuotero20.88@outlook.com

  Operaciones a implementar:
    Las operaciones se deben implementar respetando las complejidades temporales indicadas. Usaremos las siguientes variables para
    expresar las complejidades: 
    
    E: cantidad total de estudiantes.
    R: cantidad total de respuestas del examen.*/

package aed;
import java.util.ArrayList;

public class Edr {
  /*Esta clase contiene todos los métodos (ejercicios) del trabajo práctico, que implementa la estructura del MinHeap, y que utiliza las
  clases Estudiante.java, NotaFinal.java, con sus respectivos métodos y atributos. El MinHeap incorpora su propio Handle.*/

  // Atributos Privados:
  private ArrayList<Estudiante<NotaFinal>> _aula; // ArrayList de estudiantes llamado _aula,
  private Heap<NotaFinal> _heapNotas;             // Nuestro Heap.java cuyos elementos son tipo NotaFinal llamado _heapNotas
  private int[] _examenCanonico;                  // El _examenCanonico es un array de enteros positivos, representa la solución del examen.
  private int _ladoAula;                          // El entero positivo _ladoAula representa el tamaño de la matriz cuadrada del aula.
  private EstadoEdR _estado;                      // En _estado, guardamos el estado del examen y chequeo de copias.
  
  private class EstadoEdR {                       // Hago un struct chiquito para no hacer una clase estadoEDR solo para dos cosas.
    boolean examenTerminado;
    boolean chequeadoDeCopias;
    EstadoEdR() {                                 // El constructor la inicializa
      this.examenTerminado = false;
      this.chequeadoDeCopias = false;
    }
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 1 // Complejidad: O(E*R)
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public Edr(int ladoAula, int cantEstudiantes, int[] examenCanonico) { // COMPLEJIDAD O(E*R)
    /*Inicializa el sistema EdR. Recibe el lado del aula, que representará a una matriz cuadrada, la cantidad de estudiantes en el aula
    (que es estrictamente menor que el aula para lado>1), y un examen canónico que representa la solución del examen.*/
    boolean estado_valido = (                                                // Chequeamos que parámetros de entrada sean coherentes. // O(1)
      (ladoAula % 2 == 0 && cantEstudiantes <= (ladoAula/2)) ||              // Aula par   => habrá máximo (lado/2)-estudiantes. // O(1)
      (ladoAula % 2 != 0 && cantEstudiantes <= (ladoAula*(ladoAula+1))/2));  // Aula impar => máximo ((lado^2+lado)/2)-estudiantes. // O(1)
      if (!estado_valido) throw new IllegalStateException("EdR inválido.");// Si no estamos en esas condiciones -> inválido! // O(1)
    NotaFinal[] notas               = new NotaFinal[cantEstudiantes];        // Creamos un array de notas, // O(1)
    ArrayList<Estudiante<NotaFinal>> estudiantes = new ArrayList<>();        // y un ArrayList de estudiantes // O(1)
    for(int i = 0; i < cantEstudiantes; i++){                                // Para cada i-estudiante, // O(E*R)
      int [] resp = new int[examenCanonico.length];                          // Creo array de respuestas de longitud=examenCanonico, // O(1)
      for(int j = 0; j < resp.length; j++) resp[j] = -1;                     // con todas las respuestas en valor inicializado en -1 // O(R)
      notas[i] = new NotaFinal(0.0, i);                                      // Las notas de todos los estudiantes arrancan en 0. // O(1)
      Estudiante<NotaFinal> estudiante = new Estudiante<>(i, resp, null, false, false); // Creamos al estudiante. // O(1)
      estudiantes.add(estudiante);                                           // Agrego estudiante a nuestra ArrayList de estudiantes. // O(1)
    }
    this._ladoAula       = ladoAula;                                         // Inicializamos los atributos privados de la clase EDR. // O(1)
    this._examenCanonico = examenCanonico;                                   // O(1)
    this._estado         = new EstadoEdR();                                  // O(1)
    this._heapNotas      = new Heap<>(notas);                                // O(E)
    _aula                = new ArrayList<>();                                // Creo el ArrayList _aula // O(1)
    ArrayList<Handle<NotaFinal>> handles = _heapNotas.devolverHandles();     // Creo ArrayList de handles (devolver es método interno) // O(1)
    for(int j = 0 ; j < cantEstudiantes; j++){                               // Para cada estudiante,  // O(E)
      estudiantes.get(j).cambiarNota(handles.get(j));                        // actualizo su nota mediante el handle, // O(1)
      _aula.add(estudiantes.get(j));}                                        // Agrego el estudiante al aula. // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 2 // Complejidad: O(R + log(E))
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void copiarse(int estudiante) { // COMPLEJIDAD O(R + LOG E)
    /*El/la estudiante se copia del vecino que más respuestas completadas tenga que el/ella no tenga; se copia solamente la primera de esas
    respuestas. Desempata por id mayor. Recibe el entero positivo "estudiante", que representa su id.*/
    int k = mejorVecino(estudiante);                                // En la variable k guardo al mejor vecino, del cual me copiaré. // O(R)
    if (k == -1) return;                                            // Si no hay ninguno o no hay nada para copiar, no me copio. // O(1)
    int[] resp_j = _aula.get(estudiante).respuestas();              // Obtengo las respuestas mías, // O(1)
    int[] resp_k = _aula.get(k).respuestas();                       // y las del vecino k que me voy a copiar. // O(1)
    int ejAcopiar = -1;                                             // me hago unas variables para guardar el ejercicio y rta a copiar.
    int respAcopiar = -1;
    for (int i = 0; i < _examenCanonico.length; i++) {              // busco si elvecino k tiene algun ejercicio copiable. O(R)
        if (resp_j[i] == -1 && resp_k[i] >= 0 && resp_k[i] <= 9) {
            ejAcopiar = i;
            respAcopiar = resp_k[i];
            break;
        }
    }
    if (ejAcopiar != -1) resolver(estudiante,ejAcopiar,respAcopiar); // Complejidad de resolver: O(R + log E)
  }
  
  //————————————————————————————————————————————————————————————————————————————————————
  // Funciones Auxiliares:
  //————————————————————————————————————————————————————————————————————————————————————
  private boolean esVecino(int j, int k, int ladoAula) { // COMPLEJIDAD O(1)
    /*La función esVecino, recibe dos enteros positivos j y k que representan los id's de dos estudiantes en _aula, cuyo tamaño es ladoAula
    pasado por parámetro. La función devuelve true si se cumple que k es un vecino de j, es decir, si k se encuentra a dos asientos de 
    distancia por izquierda o derecha en la misma fila que j, o justo en el asiento de enfrente en la misma columna.*/
    if (j<0 || k<0 || j>=_aula.size() || k>=_aula.size()) return false; // Si j ó k son más grandes que el aula, false.
    int alumnos_por_fila = (ladoAula + 1) / 2;                          // Java usa floor(a/b) => funciona para ladoAula par/impar. // O(1)
    int fila_j = j / alumnos_por_fila;                                  // j/alumnos_por_fila da la fila en la que se encuentra j. // O(1)
    int fila_k = k / alumnos_por_fila;                                  // Ídem para k. // O(1)
    int col_j  = j % alumnos_por_fila;                                  // El resto de dividir j por alumnos_por_fila=columna par j. // O(1)
    int col_k  = k % alumnos_por_fila;                                  // Ídem para k. // O(1)
    if ((fila_k == fila_j)   && (col_k == col_j-1)) return true;        // Si hay vecino izquierdo -> return true. // O(1)
    if ((fila_k == fila_j)   && (col_k == col_j+1)) return true;        // Si hay vecino derecho -> return true. // O(1)
    if ((fila_k == fila_j-1) && (col_j ==   col_k)) return true;        // Si hay vecino delantero -> return true. // O(1)
    return false;                                                       // Si no, false. // O(1)
  }

  private int cantRespuestasVecinoQueNoTengo(int j, int k) { // COMPLEJIDAD O(R)
    /*Recibe dos enteros positivos que representan los id's de dos estudiantes vecinos, y devuelve un entero que representa la cantidad de
    ejercicios completados que tiene el alumno con id=k respecto del alumno con id=j, y que éste último no tiene hecho.*/
    if (!esVecino(j, k, _ladoAula)) return 0;                  // Si no es vecino -> 0 (no hay respuestas para copiarse). // O(1)
    int[] resp_j = _aula.get(j).respuestas();                  // Obtengo mis respuestas (soy el j-ésimo). // O(1)
    int[] resp_k = _aula.get(k).respuestas();                  // Obtengo las del vecino k. // O(1)
    int res = 0;                                               // Creo la variable entera positiva res = 0. // O(1)
    for (int i = 0; i < _examenCanonico.length; i++) {         // Para cada respuesta de examen canónico, // O(1)
      boolean j_no_tiene = (resp_j[i] == -1);                  // Creo los booleanos: j_no_tiene (no la respondí), // O(1)
      boolean k_tiene    = (resp_k[i] >= 0 && resp_k[i] <= 9); // k_tiene (mi vecino la respondió) (está entre 0 y 9). // O(1)
      if (j_no_tiene && k_tiene) res++;                        // Si se cumplen las dos condiciones, -> sumo 1 a res. // O(1)
    }                                                          // Repito para todas las respuestas. // O(R)
    return res;                                                // Devuelvo res. // O(1)
  }

  private int mejorVecino(int j) { // COMPLEJIDAD O(R)
    /*La función mejorVecino, recibe un estudiante con id=j-ésimo y determina cual de los 3 vecinos que tiene (si es que tiene) es el mejor
    vecino del cual puedo copiarme, es decir, tiene más respuestas respondidas que j no tiene, que cualquier otro vecino de j. Devuelve el id
    de dicho mejor vecino.*/
    int n = _examenCanonico.length;                         // N = cantidad de consignas del examen (longitud). // O(1)
    int[] lista_vecinos;                                    // Inicializo una lista de id's de vecinos a completar. // O(1)
    if (_ladoAula % 2 == 0) {                               // Si el lado del aula es par, // O(1)
      int mitad = _ladoAula / 2;                            // creo la variable auxiliar mitad, // O(1)
      lista_vecinos = new int[] {j-1, j+1, j-mitad};        // y mis vecinos serán los de la fila y j-mitad. // O(1)
    } else {                                                // Si el lado del aula es impar, // O(1)
      int mitad = (_ladoAula + 1) / 2;                      // la variable mitad cambia, // O(1)
      lista_vecinos = new int[] {j-1, j+1, j-mitad};}       // y mis vecinos son los de la fila y j-mitad nueva. // O(1)
    int res = -1;                                           // Inicializo las variables res (mejor vecino) // O(1)
    int cant_max = -1;                                      // y cant_max (el que tiene mayor respuestas que yo no) // O(1)
    for (int k : lista_vecinos) {                           // Para cada candidato (como máx son 3) // O(3R)
      if (k >= 0 && k < n && esVecino(j, k, _ladoAula)) {   // Si el id es valido, y además es un vecino válido, // O(1)
        int resp = cantRespuestasVecinoQueNoTengo(j, k);    // creo una variable donde guardo sus respuestas. // O(R)
        if (resp>cant_max || (resp==cant_max && k > res)) { // Si resp > al máximo, o es igual pero su id es mayor, // O(1)
          cant_max = resp;                                  // entonces resp es el máximo, // O(1)
          res = k;                                          // y el mejor vecino tiene id=k. // O(1)
        }
      }
    }                                                       // Peor caso -> O(1)
    return res;                                             // Devuelvo res (mejor vecino, si no hay vecinos da -1). // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 3 // Complejidad: O(log(E))
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void resolver(int estudiante, int nroEjercicio, int respuestaEjercicio) { // COMPLEJIDAD O(LOG E)
    /*El/la estudiante resuelve un ejercicio. Recibe un id="estudiante", un número de ejercicio que debe pertenecer a la longitud del examen
    canónico (atributo) y una respuesta que debe encontrarse entre 0 y 9 inclusive. No devuelve nada.*/
    if (estudiante < 0 || estudiante >= _aula.size()) {                   // Si el id < 0 ó > cant_estudiantes, entonces // O(1)
        throw new IndexOutOfBoundsException("ID inválido.");}           // es absurdo. // O(1)
    if (respuestaEjercicio < 0 || respuestaEjercicio > 9) {               // Si la respuesta < 0 ó > 9, // O(1)
        throw new IllegalArgumentException("Respuesta inválida.");}     // es inválida. // O(1)
    Estudiante<NotaFinal> est = _aula.get(estudiante);                    // Obtengo el Estudiante<NotaFinal> con su id=estudiante. // O(1)
    int[] respuestas = est.respuestas();                                  // esto es una copia de respuesats para evitar aliasing
    respuestas[nroEjercicio] = respuestaEjercicio;                        // Obtengo todas sus respuestas. // O(1)
    double nuevoPuntaje = calcularPuntaje(respuestas);                    // Calculo nuevopuntaje, donde está el examen canonico.
    est.responderConsigna(nroEjercicio, respuestaEjercicio, nuevoPuntaje);// Paso el ej, la rta y el handle de Heap a actualizar la nota.
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 4 // Complejidad: O(k*(R + log(E)))
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void consultarDarkWeb(int k, int[] examenDW) { // COMPLEJIDAD O(k*(R + LOG E))
    /*Los/as k estudiantes que tengan el peor puntaje (hasta el momento) reemplazan completamente su examen por el examenDW.
    Nota: en caso de empate en el puntaje, se desempata por menor id de estudiante.*/
    ArrayList<NotaFinal> peor_nota = new ArrayList<>();                    // Guardo las peores notas en un ArrayList. // O(1)
    double puntos = calcularPuntaje(examenDW);                             // Calculo nota de examenDW una vez.
    for (int i = 0; i < k; i++) {                                          // Para cada elemento hasta la cantidad k, // O(1)
        peor_nota.add(_heapNotas.desencolarMinimo());}                     // desencolamos la peor nota del MinHeap de notas. // O(K*logE)
    for (NotaFinal peor_NotaFinal : peor_nota) {                           // Recorro cada nota de peores notas O(K*R)
        int id_est                       = peor_NotaFinal._id;             // Me guardo el id del estudiante, // O(1)
        Estudiante<NotaFinal> estudiante = _aula.get(id_est);              // el estudiante de tipo Estudiante<NotaFinal>, // O(1)
        NotaFinal nueva_nota             = new NotaFinal(puntos, id_est);  // el nuevo tipo NotaFinal, // O(1)
        Handle<NotaFinal> nuevo_handle   = _heapNotas.encolar(nueva_nota); // y el nuevo handle. // O(LOG E)
        estudiante.reemplazarExamen(examenDW, nuevo_handle);
    }
  }

  //————————————————————————————————————————————————————————————————————————————————————
  // Función Auxiliar:
  //————————————————————————————————————————————————————————————————————————————————————
  private double calcularPuntaje(int[] respuestas){ // COMPLEJIDAD O(R)
    /*Recibe un arreglo de enteros "respuestas", y calcula el puntaje del examen en base a éste. Compara las respuestas con el atributo
    examen canónico, y devuelve el resultado en porcentaje (100 %) de tipo double.*/
    int correctas = 0;                                      // Inicializamos la variable entera positiva correctas. // O(1)
    int R = _examenCanonico.length;                         // Calculamos la longitud del examen (cant de ejercicios). // O(1)
    if (R == 0) return 0.0;                                 // Si la longitud es cero el examen no tiene ejercicios. // O(1)
    for (int i = 0; i<R; i++) {                             // Para cada ejercicio i en el examen, // O(1)
      if (respuestas[i] == _examenCanonico[i]) correctas++; // Si respuesta coincide con la de examenCanónico es correcta -> suma 1. // O(1)
    }                                                       // Calculo para todo el examen. // O(R)
    double porcentaje = ((double)correctas*100)/(double)R;  // Calculo el porcentaje de tipo double. // O(1)
    return Math.floor(porcentaje);                          // Devuelvo el porcentaje (la nota final) de acuerdo a las respuestas. // O(1)
  }
  //————————————————————————————————————————————————————————————————————————————————————
  
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 5 // Complejidad: O(E)
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public double[] notas(){ // COMPLEJIDAD O(E)
    /*Devuelve una secuencia de las notas de todos los estudiantes del _aula ordenada por id.*/
    int cant_estudiantes = _aula.size();                 // Obtengo la cantidad de estudiantes. // O(1)
    double[] res         = new double[cant_estudiantes]; // Inicializo res: un array de double's de longitud cant_estudiantes. // O(1)
    for (Estudiante<NotaFinal> estudiante : _aula) {     // Para cada estudiante que haya en aula,
      int id         = estudiante.id();                  // Obtengo el ID del estudiante, // O(1)
      NotaFinal nota = estudiante.nota().valor();        // Para acceder a nota => Estudiante.nota()=Handle<NotaFinal> => uso .valor() // O(1)
      res[id]        = nota._nota;                       // Agrego en pos j=ID, la nota correspondiente (uso NotaFinal._nota (double)) // O(1)
    }                                                    // Recorro todos los estudiantes -> O(E)
    return res;                                          // Devuelvo res // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 6 // Complejidad: O(log(E))
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public void entregar(int estudiante) {
    /*El/la estudiante entrega su examen. Recibe el entero positivo "estudiante" que representa su id, y convierte su estado del examen a
    "Terminado". No devuelve nada. Todo estudiante solo puede entregar una vez.*/
    Estudiante<NotaFinal> estAentregar = _aula.get(estudiante);       // Busco al estudiante con ese id. // O(1)
    if(estAentregar.entregado() == true){                             // Si ya había entregado, // O(1)
      throw new IllegalStateException("El estudiante ya entregó.");}// No puede volver a entregar. // O(1)
    Handle<NotaFinal> nodoAeliminar = estAentregar.nota();            // Consigo el nodo a eliminar del heapNotas // O(1)
    nodoAeliminar.eliminar();                                         // Elimino y reordeno en el heap. // O(log E)
    estAentregar.cambiarEntregado(true);                              // Actualizo el estado a entregado. // O(1)
    if(_heapNotas.longitud() == 0){                                   // Si no quedan Notas en el heap significa que entregaron todos, // O(1)
      _estado.examenTerminado = true;}                                // por lo tanto el examen terminó. // O(1)
  }

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 7 // Complejidad: O(E*R)
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public int[] chequearCopias() { // COMPLEJIDAD O(E*R)
    /*Devuelve la lista de los estudiantes sospechosos de haberse copiado ordenada por id de estudiante.*/
    examenTerminadoValido();                                 // Chequeo examen válido. // O(1)
    int E = _aula.size();                                    // Guardo la cantidad de estudiantes, // O(1)
    if (E <= 1) return new int[0];                           // Si hay uno solo, no puede copiarse. // O(1)
    int R = _examenCanonico.length;                          // Guardo la cantidad de respuestas, // O(1)
    int[][] frecuencia_opciones = construirFrecuencias(E,R); // y la frecuencia de las opciones. // O(E*R)
    double minimo = 0.25*(E-1);                              // Calculo el 25% sin el estudiante que estoy revisando. // O(1)
    ArrayList<Integer> sospechosos = new ArrayList<>();      // Creo un ArrayList de sospechosos. // O(1)
    for (int i = 0; i < E; i++) {                            // Para cada estudiante, // O(E)
      if (esSospechoso(i, frecuencia_opciones, minimo)) {    // Si es sospechoso, // O(R)
        sospechosos.add(_aula.get(i).id());                  // lo agrego a la lista de sospechosos, // O(1)
        _aula.get(i).cambiarSospechoso(true);}               // y le cambio el atributo de su estado a sospechoso. // O(1)
    }
    _estado.chequeadoDeCopias = true;
    return convertirArray(sospechosos);                      // Devuelvo los sospechosos en formato array de enteros. // O(1)
  }

  //————————————————————————————————————————————————————————————————————————————————————
  // Funciones Auxiliares:
  //————————————————————————————————————————————————————————————————————————————————————
  private void examenTerminadoValido() { // COMPLEJIDAD O(1)
    /*Chequea si el estado total del aula es correcto, es decir, si entregaron todos los estudiantes. No devuelve nada.*/
    if (!_estado.examenTerminado)                                            // O(1)
      throw new IllegalStateException("Faltan estudiantes por entregar."); // O(1)
  }

  private int[] convertirArray(ArrayList<Integer> lista) { // COMPLEJIDAD O(1)
    /*Convierte un ArrayList de enteros llamado lista en un arreglo de enteros.*/
    int[] res = new int[lista.size()];       // Inicio arreglo de ints "res" con longitud de la lista pasada por parámetro. // O(1)
    for (int j = 0; j < lista.size(); j++) { // Para cada índice j en dicha lista, // O(1)
      res[j] = lista.get(j);                 // le asigno a dicha posición en res, el valor de lista. // O(1)
    }
    return res;                              // Devuelvo res. // O(1)
  }
  
  private int[][] construirFrecuencias(int E, int R) { // COMPLEJIDAD O(E*R)
    /*Para cada estudiante, recorre sus respuestas y cuenta cuantas opciones hay de cada una.*/
    int[][] frecuencias = new int[R][10];     // Inicializo una variable frecuencias en un arreglo de enteros, // O(1)
    for (int i = 0; i < E; i++) {             // Para cada estudiante, // O(E)
      int[] resp = _aula.get(i).respuestas(); // creo una variable resp, donde obtengo todas sus respuestas. // O(1)
      for (int j = 0; j < R; j++) {           // Y para cada respuesta, // O(R)
        int op = resp[j];                     // guardo la opción marcada por el estudiante. // O(1)
        if (op != -1) frecuencias[j][op]++;   // Si la opción no es -1, sumo al arreglo de frecuencias. // O(1)
      }
    }
    return frecuencias;                       // Devuelvo el arreglo de enteros de frecuencias. // O(1)
  }

  private boolean esSospechoso(int i, int[][] frecuencia, double minimo) { // COMPLEJIDAD O(R)
    /*Recibe un entero positivo que representa el id de un estudiante dado, la frecuencia de las opciones en general, y si esta es mayor al
    25% devuelve true.*/
    int[] resp = _aula.get(i).respuestas(); // Obtengo las respuestas del alumno con id=i, y las guardo en resp. // O(1)
    boolean respondio = false;              // Inicializo una variable a actualizar "respondió" en false. // O(1)
    for (int j = 0; j < resp.length; j++) { // Para cada respuesta en la lista de respuestas, // O(R)
      int op = resp[j];                     // guardo el ejercicio en el que me encuentro en una variable op. // O(1)
      if (op == -1) continue;               // Si no respondión nada, paso al siguiente ejercicio. // O(1)
      respondio = true;                     // Si no, respondió es true, y entonces // O(1)
      int conteo = frecuencia[j][op] - 1;   // No se incluye a si mismo como estudiante en las opciones // O(1)
      if (conteo < minimo) return false;    // Si el conteo es menor al 25% -> devuelve false. // O(1)
    }                                       // Recorro todas las respuestas -> O(R)
    return respondio;                       // Devuelve su estado booleano de sospechoso en base a sus respuestas. // O(1)
  }
  //————————————————————————————————————————————————————————————————————————————————————

  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  // Ejercicio 8 // Complejidad: O(E*log(E))
  //——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
  public NotaFinal[] corregir() {
    /*Devuelve las notas de los examenes de los estudiantes que no se hayan copiado ordenada por NotaFinal.nota de forma decreciente. En caso
    de empate, se desempata por mayor NotaFinal.id de estudiante.*/
    if(!_estado.examenTerminado){                              // Me fijo que haya terminado el examen, que todos hayan entregado. O(1)
      throw new IllegalStateException("Faltan estudiantes por entregar su examen.");}
    if(!_estado.chequeadoDeCopias){                            // Me fijo que se haya hecho el chequeo de copias. O(1)
      throw new IllegalStateException("Falta realizar el chequeado de copias.");}
    ArrayList<NotaFinal> alumnosAcorregir = new ArrayList<>(); //
    for(Estudiante<NotaFinal> estudiante : _aula){             // Agrego a todos los estudiantes que no se hayan copiado. O(E)
      if(estudiante.sospechoso() == false){                    //
        Handle<NotaFinal> handleNota = estudiante.nota();      //
        NotaFinal notaFinal = handleNota.valor();              //
        alumnosAcorregir.add(notaFinal);}                      //
    }
    buildMinHeap(alumnosAcorregir, alumnosAcorregir.size());   // "Creo" el minHeap con la secuecia de alumnos a corregir (heapify). O(E)
    for (int i = alumnosAcorregir.size() - 1; i > 0; i--) {    // Ahora lo que hago, es voy desencolando el maximo E veces, // O(E*log E) 
      swap(alumnosAcorregir, 0, i);                         // es decir, pongo la raiz al final del "heap"
      siftDownMin(alumnosAcorregir, 0, i);                  // Arreglar el heap, con sift down para un min heap.
    }
    NotaFinal[] res = new NotaFinal[alumnosAcorregir.size()];  // Ahora lo paso de un ArrayList a un arreglo. // O(E)
    alumnosAcorregir.toArray(res);                             // Uso la funcion to array de ArrayList que recibe el arreglo con el tamaño.
    return res;                                                // Devuelvo res. // O(1)
  }

  //————————————————————————————————————————————————————————————————————————————————————
  // Funciones Auxiliares:
  //————————————————————————————————————————————————————————————————————————————————————
  private int compararNotaMin(NotaFinal a, NotaFinal b) { // COMPLEJIDAD O(1)
    /*Método de comparación nuevo para la nota final con máximo.*/
    int res = Double.compare(a.nota(), b.nota());      // < 0 si a>b
    if (res != 0) return res;                          // > 0 si a<b
    return Integer.compare(a.id(), b.id());
  }

  private void buildMinHeap(ArrayList<NotaFinal> lista, int k) { // COMPLEJIDAD O(E) (heapify)
    /*Recibe un ArrayList con elementos de tipo NotaFinal llamado lista, y un entero positivo k que representa el tamaño. Construye
    un MinHeap de dicho tamaño con dichos elementos. No devuelve nada.*/
    int ultimoPadre = (k / 2) - 1; // busco el ultimo padre del heap con matematica
    for (int i = ultimoPadre; i >= 0; i--) { // ahora voy haciendo sift down desde el ultimo padre hasta arriba a la raiz
      siftDownMin(lista, i, k);
    }
  }

  private void siftDownMin(ArrayList<NotaFinal> lista, int j, int n) { // COMPLEJIDAD O(LOG E)
    /*Recibe un ArrayList de elementos NotaFinal llamado lista, la longitud del heap n, y un elemento j del heap al cual se le realizará la 
    operación siftDown, que fue reciclada del archivo Heap.java pero se aplicará en este MinHeap. No devuelve nada.*/
    while (true) {                                                     // Itero como máximo todas las filas del Heap // O(log E)
      int i = 2*j + 1;
      int d = 2*j + 2;
      int m = j;                                                       // Creo una variable para guardar el menor.
      if (i<n && compararNotaMin(lista.get(i), lista.get(m)) < 0) m=i; // Si izq es menor al j-ésimo, el menor (por ahora) es izq. // O(1)
      if (d<n && compararNotaMin(lista.get(d), lista.get(m)) < 0) m=d; // Si der < menor actual (puede ser j ó izq) => menor es der. // O(1)
      if (m == j) break;                                               // Si menor=j => no pasó nada => no se rompe el Heap => break!
      swap(lista, j, m);                                               // Intercambio los nodos del heap, actualizo índices, // O(1)
      j = m;                                                           // y me muevo hacia abajo para seguir iterando hasta algún break.
    }
  }

  private void swap(ArrayList<NotaFinal> lista, int i, int j) { // COMPLEJIDAD O(1)
    /*Recibe un ArrayList de elementos NotaFinal llamado lista, y dos elementos i y j, a los cuales intercambiará entre sí en el Array.
    No devuelve nada.*/
    NotaFinal nota = lista.get(i);
    lista.set(i, lista.get(j));
    lista.set(j, nota);
  }
  //————————————————————————————————————————————————————————————————————————————————————

}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————