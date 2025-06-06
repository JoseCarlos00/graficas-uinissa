import matplotlib.pyplot as plt # type: ignore
import matplotlib.patches as mpatches # type: ignore
from typing import List, Dict, Union, Optional

def plot_donut_chart(
    data_list: List[Union[int, str]],
    category_labels_dict: Dict[int, str],
    color_map: Dict[int, str],
    title: str = "Gráfico de Anillo",
    special_mappings: Optional[Dict[str, int]] = None,
    donut_hole_ratio: float = 0.4
) -> None:
    """
    Genera un gráfico de anillo a partir de una lista de datos categóricos.

    Args:
        data_list: Lista de datos, puede contener enteros (claves de categorías)
                   o cadenas (que pueden ser mapeadas a claves a través de special_mappings).
        category_labels_dict: Diccionario que mapea claves enteras a etiquetas de categorías.
        color_map: Diccionario que mapea claves enteras a colores hexadecimales.
        title: Título del gráfico.
        special_mappings: Diccionario opcional para mapear valores de cadena especiales
                          en data_list a claves enteras. Ej: {"1-2": 9}
        donut_hole_ratio: Proporción del radio para el agujero del gráfico de anillo.
    """
    if special_mappings is None:
        special_mappings = {}

    # 1. Preprocesar la lista de entrada
    processed_data_list = []
    for item in data_list:
        if isinstance(item, str) and item in special_mappings:
            processed_data_list.append(special_mappings[item])
        elif isinstance(item, int):
            processed_data_list.append(item)
        else:
            print(f"Advertencia: Elemento inesperado '{item}' de tipo {type(item)} en la lista de datos. Será ignorado.")
            continue

    # 2. Contar ocurrencias
    category_counts = {key: 0 for key in category_labels_dict.keys()}
    for category_key in processed_data_list:
        if category_key in category_counts:
            category_counts[category_key] += 1

    # 3. Filtrar categorías con 0 pacientes y preparar datos para el gráfico
    pie_labels_for_legend = []
    pie_counts = []
    pie_colors = []
    
    sorted_keys = sorted(category_labels_dict.keys())

    for key in sorted_keys:
        count = category_counts.get(key, 0)
        if count > 0:
            pie_labels_for_legend.append(category_labels_dict[key].title())
            pie_counts.append(count)
            if key in color_map:
                pie_colors.append(color_map[key])
            else:
                print(f"Advertencia: No se encontró color para la categoría '{category_labels_dict[key]}' (clave {key}). Se usará color por defecto.")
                pie_colors.append(None)

    if not pie_counts:
        print(f"No hay datos con recuentos positivos para graficar en '{title}'.")
        return

    # 4. Opcional: Destacar la porción más grande (explode)
    explode_slices = [0] * len(pie_counts)
    if pie_counts:
        max_count_index = pie_counts.index(max(pie_counts))
        explode_slices[max_count_index] = 0.05

    # 5. Crear gráfico de pastel base
    plt.figure(figsize=(12, 8))
    
    wedges, texts_pie, autotexts = plt.pie(
        pie_counts,
        explode=explode_slices,
        labels=None,
        autopct=lambda p: '{:.1f}%'.format(p) if p >= 1 else '',
        startangle=140,
        colors=pie_colors,
        pctdistance=0.85, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
    )

    plt.setp(autotexts, size=9, weight="bold", color="white")
    for i, at_text in enumerate(autotexts):
        if pie_counts[i] / sum(pie_counts) < 0.02:
            at_text.set_text('')

    plt.title(title.title(), fontsize=16, pad=20)
    plt.axis('equal')

    # 5.1. Dibujar el círculo central para crear el efecto de anillo
    centre_circle = plt.Circle((0,0), donut_hole_ratio, fc='white', linewidth=0)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # 6. Añadir leyenda
    legend_patches = [mpatches.Patch(color=color if color else 'grey', label=label) 
                      for label, color in zip(pie_labels_for_legend, pie_colors)]
    plt.legend(handles=legend_patches, title="Servicios de Salud", loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize='medium')
    plt.tight_layout(rect=[0, 0, 0.82, 1])
    plt.show()

    # 7. Nota sobre categorías con cero pacientes
    categorias_cero_info = [category_labels_dict[key].title() for key in sorted_keys if category_counts.get(key, 0) == 0]
    if categorias_cero_info:
        print(f"\nNota: Las siguientes categorías tienen 0 pacientes y no se muestran en el gráfico '{title}': {', '.join(categorias_cero_info)}")
