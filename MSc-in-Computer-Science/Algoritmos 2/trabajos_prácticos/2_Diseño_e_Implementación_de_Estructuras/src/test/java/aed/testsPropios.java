
//============================================================================================================================================
// Trabajo Práctico 2 // Diseño e Implementación de Estructuras (tests propios)
//============================================================================================================================================

package aed;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import java.util.Arrays;

class testsPropios {
  Edr edr;
  int d_aula;
  int cant_alumnos;
  int[] solucion;

  @BeforeEach
  void setUp(){
    d_aula = 5;
    cant_alumnos = 4;
    solucion = new int[]{0,1,2,3,4,5,6,7,8,9};
    edr = new Edr(d_aula, cant_alumnos, solucion);
  }

  @Test
  void nuevoEdrAula4x4() {
    int d_aula_4x4 = 4; 
    int cantAlumnos = 10;
    solucion = new int[]{0,1,2,3,4,5,6,7,8,9};
    IllegalStateException exception = assertThrows(IllegalStateException.class, () -> {
    new Edr(d_aula_4x4, cantAlumnos, solucion);
    });
    assertEquals("EdR inválido.", exception.getMessage());
  }

  @Test
  void nuevoEdrAula3x3() {
    int d_aula_3x3 = 3; 
    int cantAlumnos = 7;
    solucion = new int[]{0,1,2,3,4,5,6,7,8,9};
    IllegalStateException exception = assertThrows(IllegalStateException.class, () -> {
      new Edr(d_aula_3x3, cantAlumnos, solucion);
    });
    assertEquals("EdR inválido.", exception.getMessage());

  }

  @Test
  void copiarseCasoBordeVecinosParciales() {
    edr = new Edr(5, 4, solucion); 
    edr.resolver(1, 0, 0); 
    edr.resolver(3, 9, 9); 
    double[] notas_esperadas_inicial = new double[]{0.0, 10.0, 0.0, 10.0};
    assertTrue(Arrays.equals(notas_esperadas_inicial, edr.notas()));
    edr.copiarse(1);
    double[] notas_esperadas_final = new double[]{0.0, 10.0, 0.0, 10.0};
    assertTrue(Arrays.equals(notas_esperadas_final, edr.notas()));
  }

  @Test
  void copiarseCasoBordeVecinoCompleto() {
    for (int i = 0; i < 9; i++) {
      edr.resolver(1, i, i); 
    }
    for (int i = 0; i <= 9; i++) {
      edr.resolver(2, i, i); 
    }
    double[] notas_esperadas_inicial = new double[]{0.0, 90.0, 100.0, 0.0};
    assertTrue(Arrays.equals(notas_esperadas_inicial, edr.notas()));
    edr.copiarse(1);
    double[] notas_esperadas_final = new double[]{0.0, 100.0, 100.0, 0.0};
    assertTrue(Arrays.equals(notas_esperadas_final, edr.notas()));
  }

  @Test
  void copiarseNoPuedeNadieHizoNada() {
    // caso borde se quiere copiar pero no puede, nadie hizo nada.
    edr.copiarse(1);
    edr.copiarse(2);
    edr.copiarse(3);
    edr.copiarse(4);
    double[] notas_esperadas = new double[]{0.0, 0.0, 0.0, 0.0};
    assertTrue(Arrays.equals(notas_esperadas, edr.notas()));
  }

  @Test
  void darkWebConAlumnosEntregados() {
    edr.entregar(2);
    edr.entregar(3);
    edr.consultarDarkWeb(2, solucion);
    double[] notas = edr.notas();
    double[] notas_esperadas = new double[4];
    notas_esperadas[0] = 100.0; // CopiaDW
    notas_esperadas[1] = 100.0; // CopiaDW
    notas_esperadas[2] = 0.0;
    notas_esperadas[3] = 0.0;
    assertTrue(Arrays.equals(notas_esperadas, notas));
  }

  @Test
  void darkWebNadieEntrego() {
    edr.consultarDarkWeb(4, solucion);
    double[] notas = edr.notas();
    double[] notas_esperadas = new double[4];
    Arrays.fill(notas_esperadas, 100.0);
    assertTrue(Arrays.equals(notas_esperadas, notas));
  }

  @Test
  void notasTodosIguales() {
    for(int i = 0; i < 4; i++) {
      for (int p = 0; p < 5; p++) {
        edr.resolver(i, p, p);
      }
    }
    double[] notas = edr.notas();
    double[] notas_esperadas = new double[]{50.0, 50.0, 50.0, 50.0};
    assertTrue(Arrays.equals(notas_esperadas, notas));
  }

  @Test
  void EscandaloTotalTodosCopian() {
    for (int p = 0; p < 10; p++) {
      edr.resolver(0, p, 1); 
      edr.resolver(1, p, 1);
      edr.resolver(2, p, 1);
      edr.resolver(3, p, 1);
    }
    for(int i = 0; i < 4; i++) {
      edr.entregar(i);
    }
    int[] copiones = edr.chequearCopias();
    int[] copiones_esperados = new int[]{0, 1, 2, 3};
    assertTrue(Arrays.equals(copiones_esperados, copiones));
    NotaFinal[] notas_finales = edr.corregir();
    NotaFinal[] notas_finales_esperadas = new NotaFinal[0];
    assertTrue(Arrays.equals(notas_finales_esperadas, notas_finales));
  }

  // Ejercicio 7
  @Test
  void revisar_copias_no_todos_entregaron() {
    edr.entregar(0);
    edr.entregar(1);
    edr.entregar(2);
    IllegalStateException exception = assertThrows(IllegalStateException.class, () -> {
    edr.chequearCopias();
  });
    assertEquals("Faltan estudiantes por entregar.", exception.getMessage());
  }

  // Ejercicio 8
  @Test
  void corregir_sin_chequear_copias() {
    for(int i = 0; i < cant_alumnos; i++) {
      edr.entregar(i);
    }
    IllegalStateException exception = assertThrows(IllegalStateException.class, () -> {
    edr.corregir();
    });
    assertEquals("Falta realizar el chequeado de copias.", exception.getMessage());
  }

  @Test
  void corregir_sin_examen_terminado() {
  for(int i = 0; i < cant_alumnos - 1; i++) {
    edr.entregar(i);
  }
  IllegalStateException exception = assertThrows(IllegalStateException.class, () -> {
    edr.corregir();
  });
  assertEquals("Faltan estudiantes por entregar su examen.", exception.getMessage());
  }
}

//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
//————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————