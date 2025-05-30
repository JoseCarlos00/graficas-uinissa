import matplotlib.pyplot as plt # type: ignore

import barras as barras # type: ignore
import estadisticas as estadisticas # type: ignore


DICTIONARY_LEVEL_EDUCATION = {
  1: "ANALFABETA",
  2: "SABE LEER  Y ESCRIBIR",
  3: "PREESCOLAR",
  4: "PRIMARIA",
  5: "EDUCACIÓN ESPECIAL",
  6: "SECUNDARIA",
  7: "BACHILLERATO",
  8: "CARRERA TÉCNICA",
  9: "LICENCIATURA",
  10: "POSGRADO",
}

ESCOLARIDAD_LIST = [6,2,4,5,1,4,4,4,6,2,6,5,6,5,7,7,5,6,6,6,5,4,7,4,7,5,4,5,4,5,4,4,5,6,6,5,7,6,6,5,5,5,7,4,6,8,4,4,6,8,2,6,5,6,6,4,4,6,4,6,5,7,4,7,6,8,1,6,7,5,4,5,7,6,6,5,5,5,5,5,4,5,5,6,4,6,8,5,4,5,5,5,7,7,7,5,5,6,7,5,3,8,5,6,5,5,4,3,7,4]



if __name__ == "__main__":
 
    print("\n--- Medidas Estadísticas ---")
    estadisticas.medidas_estadisticas(ESCOLARIDAD_LIST, DICTIONARY_LEVEL_EDUCATION)

   
    print("\n--- Gráfico de Barras (Frecuencia de Niveles Educativos) ---")
    barras.plot_education_level(ESCOLARIDAD_LIST, DICTIONARY_LEVEL_EDUCATION)
    