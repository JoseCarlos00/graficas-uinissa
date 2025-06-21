import matplotlib.pyplot as plt # type: ignore

import barras as barras # type: ignore
import estadisticas as estadisticas # type: ignore
import pastel as pastel # type: ignore


DICTIONARY_LEVEL_EDUCATION = {
  1: "ANALFABETA",
  2: "SABE LEER  Y ESCRIBIR",
  3: "PREESCOLAR",
  4: "PRIMARIA",
  5: "SECUNDARIA",
  6: "BACHILLERATO",
  7: "CARRERA TÉCNICA",
  8: "LICENCIATURA",
  9: "POSGRADO"
}

# Colores para los gráficos, consistentes con otros módulos
COLOR_BY_LEVEL = {
    1: "#8B0000",     # rojo oscuro
    2: "#B22222",     # rojo
    3: "#FF8C00",     # naranja
    4: "#FFD700",     # dorado
    5: "#4B0082",    # índigo
    6: "#DB7095",     # verde
    7: "#00CED1",     # turquesa
    8: "#1E90FF",     # azul
    9: "#6A5ACD",     # púrpura
}

ESCOLARIDAD_LIST = [5,7,7,4,7,5,4,5,4,4,6,2,4,5,1,4,4,4,6,2,6,3,2,2,3,2,2,2,2,7,4,4,5,6,6,5,7,6,6,4,8,2,6,5,6,6,4,4,6,4,5,5,5,7,4,6,8,4,4,6,6,5,7,4,7,6,8,1,6,7,5,4,5,7,6,6,5,5,5,5,5,4,5,5,6,4,6,8,5,4,1,8,5,5,8,5,5,6,2,7,5,5,5,7,7,7,5,5,6,7]


if __name__ == "__main__":
 
    print("\n--- Medidas Estadísticas ---")
    estadisticas.medidas_estadisticas(ESCOLARIDAD_LIST, DICTIONARY_LEVEL_EDUCATION)
   
    print("\n--- Gráfico de Pastel (Distribución por Escolaridad) ---")
    pastel.plot_pie_chart(
        data_list=ESCOLARIDAD_LIST,
        category_labels_dict=DICTIONARY_LEVEL_EDUCATION,
        color_map=COLOR_BY_LEVEL,
        title="Distribución de Pacientes\npor Nivel de Escolaridad"
    )
    
    # print("\n--- Gráfico de Barras (Frecuencia de Niveles Educativos) ---")
    barras.plot_education_level(ESCOLARIDAD_LIST, DICTIONARY_LEVEL_EDUCATION)
