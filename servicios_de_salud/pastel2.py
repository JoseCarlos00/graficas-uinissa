import matplotlib.pyplot as plt # type: ignore
import matplotlib.patches as mpatches # type: ignore
from typing import List, Dict, Union, Any
from matplotlib.patches import ConnectionPatch # type: ignore
import numpy as np

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
        autopct=lambda p: f'{p:.1f}%' if p >= 1 else '', # Esto es para el porcentaje dentro de la rebanada
        startangle=140,
        colors=pie_colors,
        pctdistance=0.85, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
    )

    plt.setp(autotexts, size=12, weight="bold", color="white") # Ajusta el tamaño del texto del porcentaje en la rebanada
    plt.title(title.title(), fontsize=16, pad=20) # Mantiene el tamaño de fuente del título original
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

def plot_bar_of_pie_chart(
    main_ratios: Dict[str, float],
    sub_ratios: Dict[str, float],
    main_colors: Dict[str, str],
    sub_colors: Dict[str, str],
    title: str = "Distribución de Pacientes"
) -> None:
    """
    Genera un gráfico de "bar of pie" para mostrar un desglose de una porción.

    Args:
        main_ratios: Diccionario con etiquetas y porcentajes para las rebanadas principales del pastel.
        sub_ratios: Diccionario con etiquetas y porcentajes para las barras (el desglose).
        main_colors: Diccionario de colores para las rebanadas principales.
        sub_colors: Diccionario de colores para las barras.
        title: Título del gráfico.
    """
    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))
    fig.subplots_adjust(wspace=0)

    # --- Pie Chart ---
    # 1. Combinar los sub-ratios en una única rebanada "agrupada" para el pastel
    group_sum = sum(sub_ratios.values())
    
    # 2. Preparar datos para el gráfico de pastel. La rebanada a explotar va primero.
    # El orden es importante para que ConnectionPatch funcione en wedges[0]
    pie_labels_ordered = ['Otros Servicios', *main_ratios.keys()]
    pie_ratios_ordered = [group_sum, *main_ratios.values()]
    
    # Usar un color neutral para la rebanada combinada
    pie_colors_ordered = ['#B0B0B0', *main_colors.values()] 
    
    explode = [0.1] + [0] * len(main_ratios)
    
    # Rotar para que la primera rebanada quede dividida por el eje x para la conexión
    angle = -180 * (pie_ratios_ordered[0] / sum(pie_ratios_ordered))

    wedges, texts, autotexts = ax1.pie(
        pie_ratios_ordered, 
        autopct='%1.1f%%', 
        startangle=angle,
        labels=[label.title() for label in pie_labels_ordered], 
        explode=explode,
        colors=pie_colors_ordered,
        pctdistance=0.8,
        textprops={'fontsize': 9}
    )
    # Poner el texto del porcentaje en blanco y negrita para mejor visibilidad
    plt.setp(autotexts, size=10, weight="bold", color="w")
    ax1.set_title(title.title(), fontsize=16, pad=20)

    # --- Gráfico de Barras (Detalle de la Rebanada Explotada) ---
    bar_labels = list(sub_ratios.keys())
    # Los ratios para el gráfico de barras deben ser relativos a su propia suma
    bar_ratios_relative = [r / group_sum for r in sub_ratios.values()]
    bar_colors = list(sub_colors.values())

    bottom = 1
    width = .35 # Un poco más ancho para mejor visibilidad de las etiquetas

    # Añadir desde arriba coincide con la leyenda
    for j, (height, label, color) in enumerate(reversed([*zip(bar_ratios_relative, bar_labels, bar_colors)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color=color, label=label.title(),
                     alpha=0.9, edgecolor='black', linewidth=0.5)
        ax2.bar_label(bc, labels=[f"{height:.1%}"], label_type='center', color='w', weight='bold', fontsize=9)

    ax2.set_title('Detalle de Otros Servicios')
    ax2.legend(title="Servicios", loc="upper right")
    ax2.axis('off')
    ax2.set_xlim(- 2 * width, 2 * width)

    # --- Líneas de Conexión ---
    # Usar ConnectionPatch para dibujar líneas entre los dos gráficos
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(bar_ratios_relative) # Esto es 1.0

    # Dibujar línea de conexión superior
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(1.5)
    ax2.add_artist(con)

    # Dibujar línea de conexión inferior
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(1.5)

    plt.show()
