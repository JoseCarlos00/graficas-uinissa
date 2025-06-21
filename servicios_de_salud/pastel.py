import matplotlib.pyplot as plt # type: ignore
import matplotlib.patches as mpatches # type: ignore
from typing import List, Dict, Union

def plot_pie_chart(
    data_list: List[Union[int, str]],
    category_labels_dict: Dict[int, str],
    color_map: Dict[int, str],
    title: str = "Gráfico de Pastel"
) -> None:
    """
    Genera un gráfico de pastel a partir de una lista de datos categóricos.

    Args:
        data_list: Lista de datos con claves de categorías.
        category_labels_dict: Diccionario que mapea claves enteras a etiquetas de categorías.
        color_map: Diccionario que mapea claves enteras a colores hexadecimales.
        title: Título del gráfico.
    """
    # 1. Contar ocurrencias
    category_counts = {key: 0 for key in category_labels_dict.keys()}
    for category_key in data_list:
        if category_key in category_counts:
            category_counts[category_key] += 1

    # 2. Filtrar categorías con 0 pacientes y preparar datos para el pastel
    pie_labels_for_legend = []
    pie_counts = []
    pie_colors = []
    
    sorted_keys = sorted(category_labels_dict.keys())

    for key in sorted_keys:
        count = category_counts.get(key, 0)
        if count > 0:
            pie_labels_for_legend.append(category_labels_dict[key].title())
            pie_counts.append(count)
            pie_colors.append(color_map.get(key))

    if not pie_counts:
        print(f"No hay datos con recuentos positivos para graficar en '{title}'.")
        return

    # Calcular porcentajes para la leyenda
    total_count = sum(pie_counts)
    pie_percentages = [(count / total_count) * 100 for count in pie_counts]

    # 3. Crear gráfico de pastel
    plt.figure(figsize=(12, 8))
    
    wedges, texts_pie, autotexts = plt.pie(
        pie_counts,
        labels=None,
        autopct=lambda p: f'{p:.1f}%' if p >= 2 else '', # Esto es para el porcentaje dentro de la rebanada
        startangle=140,
        colors=pie_colors,
        pctdistance=0.85, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
    )

    plt.setp(autotexts, size=12, weight="bold", color="white") # Ajusta el tamaño del texto del porcentaje en la rebanada
    plt.title(title.title(), fontsize=22, pad=20) # Mantiene el tamaño de fuente del título original
    plt.axis('equal')

    # 4. Añadir leyenda
    # Modificado para incluir el porcentaje en la etiqueta de la leyenda
    legend_patches = [mpatches.Patch(color=color, label=f'{label} ({percentage:.1f}%)') 
                      for label, color, percentage in zip(pie_labels_for_legend, pie_colors, pie_percentages)]

    plt.legend(
        handles=legend_patches,
        title="Nivel de Escolaridad",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=12,
        title_fontsize=14
    )

    plt.tight_layout(rect=[0, 0, 0.8, 1])
    plt.show()
