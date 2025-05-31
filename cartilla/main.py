import sys
import os

# Añadir el directorio padre (graficas-uinissa) a sys.path
# Esto permite que Python encuentre el paquete 'escolaridad'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import servicios_de_salud.pastel as pastel # Importar el nuevo módulo de pastelimport servicios_de_salud.pastel as pastel # Importar el nuevo módulo de pastel
import servicios_de_salud.estadisticas as estadisticas # Importar el módulo de estadísticas

CARTILLA_MAP = {
  1: "SI",
  2: "NO"
}


DATA_SET_LIST = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

COLOR_BY_LEVEL_PASTEL = {
    1: "#32CD32",     # verde
    2: "#6A5ACD",     # púrpura
}

if __name__ == "__main__":
    print("\n--- Gráfico de Pastel (Cartilla de Vacunación) ---")

    # pastel.plot_pie_chart(
    #     data_list=DATA_SET_LIST,
    #     category_labels_dict=CARTILLA_MAP,
    #     color_map=COLOR_BY_LEVEL_PASTEL,  # Reutilizar el mapa de colores de barras.py
    #     title="Distribución de Pacientes " + "\n" + " con Cartilla de Vacunación",
    #     special_mappings={}  # No hay mapeos especiales en este caso
    # )
    
    print("\n--- Estadísticas de Pacientes ---")
    
    estadisticas.calcular_estadisticas_servicios(
    data_list=DATA_SET_LIST,
    category_labels_dict=CARTILLA_MAP,
    special_mappings={'1-2': 9},
    title="Análisis Estadístico de Afiliación a Servicios de Salud"
)

  
