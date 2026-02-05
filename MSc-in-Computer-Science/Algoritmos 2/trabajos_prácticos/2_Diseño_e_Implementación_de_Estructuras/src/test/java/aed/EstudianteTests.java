
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras
//============================================================================================================================================

package aed;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.lang.reflect.Array;
import java.util.Arrays;

class HandlePrueba<T> implements Handle<T>{
  private T valor;

  public HandlePrueba(T v){
    this.valor=v;
  }
  @Override
  public T valor() { return this.valor; }

  @Override
  public void eliminar() { /* No hace nada */ }

  @Override
  public void modificar(T nuevoValor) { this.valor = nuevoValor; }
}

public class EstudianteTests {
  Estudiante<NotaFinal>estudiante;
  HandlePrueba<NotaFinal> handle;
  NotaFinal nota;
  int id;
  int[] respuestas;
  @BeforeEach
  void setUp(){
    id=6;
    nota=new NotaFinal(50.0,id);
    handle = new HandlePrueba<>(nota);
    respuestas = new int[]{1,2,3,-1,5,-1};
    boolean sospechoso = false;
    boolean entregado = false;
    estudiante= new Estudiante<>(id, respuestas, handle, sospechoso, entregado);
  }
  @Test
  void inicializarCorrectamente(){
    assertEquals(6,estudiante.id());
    assertEquals(50.0,estudiante.nota().valor().nota());
    assertFalse(estudiante.sospechoso());
    assertFalse(estudiante.entregado());
    assertTrue(Arrays.equals(respuestas,estudiante.respuestas()));
    
  }
  @Test
  void cambiarSospechoso(){
    estudiante.cambiarSospechoso(true);
    assertTrue(estudiante.sospechoso());

  }
  @Test
  void cambiarEntregado(){
    estudiante.cambiarEntregado(true);
    assertTrue(estudiante.entregado());

  }
  @Test
  void cambiarNota(){

  }
  @Test
  void cambiarRespuesta(){
    int[] nuevasRespuestas = new int[]{-1,0,2,3};
    estudiante.cambiarRespuestas(nuevasRespuestas);
    assertTrue(Arrays.equals(nuevasRespuestas,estudiante.respuestas()));
    nuevasRespuestas[0]=5;
    assertEquals(-1, estudiante.respuestas()[0]);
    assertEquals(4, estudiante.respuestas().length);
  }
  @Test 
  void obtenerRespuestas(){
    int []respuestasIniciales=estudiante.respuestas();
    respuestasIniciales[0]=0;
    int[]respuestasActuales=estudiante.respuestas();
    assertEquals(1,respuestasActuales[0]);
  }
  @Test
  void accederAnota(){

  }
  @Test
  void respuestasVacias(){
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————