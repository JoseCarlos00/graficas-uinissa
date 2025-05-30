import sys
import os

# Añadir el directorio padre (graficas-uinissa) a sys.path
# Esto permite que Python encuentre el paquete 'escolaridad'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import barras.barras as barras # type: ignore
import servicios_de_salud.pastel as pastel # Importar el nuevo módulo de pastel
# import escolaridad.estadisticas as estadisticas # type: ignore

DICIONARY_SERVICIOS_DE_SALUD = {
  0: "Ninguno",
  1: "Secretaría de Salud",
  2: "IMSS",
  3: "ISSSTE",
  4: "PEMEX",
  5: "MARINA",
  6: "SEDENA",
  7: "Seguro Medico",
  8: "OTRO(S)",
  9: "Secretaria - IMMS",
}

LIST_SERVICES_DE_SALUD = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,5,7,8,8,8,8,8,8,8,8,8,'1-2','1-2','1-2','1-2','1-2','1-2','1-2','1-2','1-2','1-2']

print("\n--- Gráfico de Barras (Servicios de Salud) ---")
barras.plot_education_level(LIST_SERVICES_DE_SALUD, DICIONARY_SERVICIOS_DE_SALUD)

print("\n--- Gráfico de Pastel (Servicios de Salud) ---")

# Colores personalizados por cada nivel de escolaridad
COLOR_BY_LEVEL_PASTEL = {
    0: "#C0C0C0",     # Gris (para Ninguno)
    1: "#C45693",     # rojo oscuro (para Secretaría de Salud)
    2: "#B22222",     # rojo (para IMSS)
    3: "#FF8C00",     # naranja
    4: "#FFD700",     # dorado
    5: "#9ACD32",     # verde oliva
    6: "#32CD32",     # verde
    7: "#00CED1",     # turquesa
    8: "#1E90FF",     # azul
    9: "#6A5ACD",     # púrpura
}


pastel.plot_pie_chart(
    data_list=LIST_SERVICES_DE_SALUD,
    category_labels_dict=DICIONARY_SERVICIOS_DE_SALUD,
    color_map=COLOR_BY_LEVEL_PASTEL,  # Reutilizar el mapa de colores de barras.py
    title="Distribución de Pacientes por Servicio de Salud",
    special_mappings={'1-2': 9} # Mapeo específico para este conjunto de datos
)
print("\n--- Medidas Estadísticas (Servicios de Salud) ---")
# estadisticas.medidas_estadisticas(LIST_SERVICES_DE_SALUD, DICIONARY_SERVICIOS_DE_SALUD)
