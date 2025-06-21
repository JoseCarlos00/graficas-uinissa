import sys
import os

# Añadir el directorio padre (graficas-uinissa) a sys.path
# Esto permite que Python encuentre el paquete 'escolaridad'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import servicios_de_salud.pastel as pastel # Importar el nuevo módulo de pastel
# import servicios_de_salud.anillo as anillo # Importar el nuevo módulo de anillo
import servicios_de_salud.estadisticas as estadisticas # Importar el módulo de estadísticas

import escolaridad.barras as barras # Importar el módulo de barras



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

print("\n--- Gráfico de Pastel (Servicios de Salud) ---")

# Colores personalizados por cada nivel de escolaridad
COLOR_BY_LEVEL_PASTEL = {
    0: "#C0C0C0",     # Gris (para Ninguno)
    1: "#C45693",     # rojo oscuro (para Secretaría de Salud)
    2: "#B22222",     # rojo (para IMSS)
    3: "#FF8C00",     # naranja
    4: "#1639D4",     # dorado
    5: "#9ACD32",     # verde oliva
    6: "#32CD32",     # verde
    7: "#00CED1",     # turquesa
    8: "#1E90FF",     # azul
    9: "#6A5ACD",     # púrpura
}

# # Generar gráfico de pastel original
# pastel.plot_pie_chart(
#         data_list=LIST_SERVICES_DE_SALUD,
#         category_labels_dict=DICIONARY_SERVICIOS_DE_SALUD,
#         color_map=COLOR_BY_LEVEL_PASTEL,
#         title="Distribución de Pacientes\npor Servicio de Salud",
#     )

print("\n--- Gráfico de Barra de Pastel (Servicios de Salud) ---")

# Datos para el gráfico de "bar of pie" basados en los porcentajes solicitados.
# Rebanadas principales del pastel
main_ratios_data = {
    DICIONARY_SERVICIOS_DE_SALUD[1]: 65.0,  # "Secretaría de Salud"
    DICIONARY_SERVICIOS_DE_SALUD[2]: 12.0,  # "IMSS"
    DICIONARY_SERVICIOS_DE_SALUD[8]: 9.0,   # "OTRO(S)"
    DICIONARY_SERVICIOS_DE_SALUD[0]: 8.0,   # "Ninguno"
}

# Desglose para la barra (la rebanada que se "explota")
sub_ratios_data = {
    DICIONARY_SERVICIOS_DE_SALUD[3]: 4.0,   # "ISSSTE"
    DICIONARY_SERVICIOS_DE_SALUD[5]: 1.0,   # "MARINA"
    DICIONARY_SERVICIOS_DE_SALUD[7]: 1.0,   # "Seguro Medico"
}

# Mapeo inverso para encontrar la clave numérica de una etiqueta de texto
label_to_key = {v: k for k, v in DICIONARY_SERVICIOS_DE_SALUD.items()}

# Crear los diccionarios de colores requeridos por la nueva función
main_colors_map = {label: COLOR_BY_LEVEL_PASTEL[label_to_key[label]] for label in main_ratios_data.keys()}
sub_colors_map = {label: COLOR_BY_LEVEL_PASTEL[label_to_key[label]] for label in sub_ratios_data.keys()}

# Llamar a la nueva función para generar el gráfico
pastel.plot_bar_of_pie_chart(main_ratios=main_ratios_data, sub_ratios=sub_ratios_data, main_colors=main_colors_map, sub_colors=sub_colors_map, title="Distribución de Pacientes por Servicio de Salud")
# print("\n--- Gráfico de Anillo (Servicios de Salud) ---")
# anillo.plot_donut_chart(
#     data_list=LIST_SERVICES_DE_SALUD,
#     category_labels_dict=DICIONARY_SERVICIOS_DE_SALUD,
#     color_map=COLOR_BY_LEVEL_PASTEL, # Puedes usar el mismo mapa de colores
#     title="Distribución de Pacientes por Servicio de Salud (Anillo)",
#     special_mappings={'1-2': 9},
#     donut_hole_ratio=0.45 # Ajusta el tamaño del agujero como prefieras
# )

print("\n--- Medidas Estadísticas (Servicios de Salud) ---")
estadisticas.calcular_estadisticas_servicios(
    data_list=LIST_SERVICES_DE_SALUD,
    category_labels_dict=DICIONARY_SERVICIOS_DE_SALUD,
    special_mappings={'1-2': 9},
    title="Análisis Estadístico de Afiliación a Servicios de Salud"
)

# print("\n--- Gráfico de Barras (Servicios de Salud) ---")
# barras.plot_education_level(
#     data_list=LIST_SERVICES_DE_SALUD,
#     category_labels_dict=DICIONARY_SERVICIOS_DE_SALUD,
#     color_map=COLOR_BY_LEVEL_PASTEL,  # Reutilizar el mapa de colores de pastel.py
#     title="Distribución de Pacientes por Servicio de Salud",
#     special_mappings={'1-2': 9} # Mapeo específico para este conjunto de datos
# )
