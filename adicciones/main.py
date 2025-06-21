from collections import Counter
import matplotlib.pyplot as plt

DICCTIONARY_ADDICTION = {
    1: "Tabaquismo",
    2: "Alcoholismo",
    3: "Otras drogas",
    4: "Televisión/Videojuegos",
    5: "Refrescos/Comida chatarra",
    6: "Otras"
}

LIST_ADDICTIONS = [[5],[6],[6],[5],[6],[],[],[6],[6],[6],[1,5],[],[],[1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[1],[1],[1,2],[2],[6],[6],[],[1,2],[1,2],[1,2,4,5],[2],[6],[2,5],[1,2],[4],[],[4],[],[2,5],[5],[],[],[],[],[],[4],[],[],[],[],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[],[],[],[1],[],[1],[],[],[1],[],[],[1],[],[],[],[],[],[],[],[6],[1],[1],[1,2],[2],[6],[6],[],[1,2],[1,2],[1,2],[],[],[],[],[],[],[],[],[],[]]

# Total de pacientes
total_pacientes = len(LIST_ADDICTIONS)

# Pacientes sin adicciones
sin_adicciones = [p for p in LIST_ADDICTIONS if len(p) == 0]
num_sin_adicciones = len(sin_adicciones)

# Pacientes con al menos una adicción
con_adicciones = [p for p in LIST_ADDICTIONS if len(p) > 0]
num_con_adicciones = len(con_adicciones)

# Número promedio de adicciones por paciente
total_adicciones = sum(len(p) for p in LIST_ADDICTIONS)
promedio_todos = total_adicciones / total_pacientes

# Promedio considerando solo pacientes con adicciones
promedio_con_adicciones = (
    total_adicciones / num_con_adicciones if num_con_adicciones > 0 else 0
)

# Frecuencia de cada adicción
todas_adicciones = [adiccion for sublist in LIST_ADDICTIONS for adiccion in sublist]
conteo = Counter(todas_adicciones)

# Moda (adicción más frecuente)
moda = conteo.most_common(1)[0]

# Resultados
print("🔹 Total de pacientes:", total_pacientes)
print("🔹 Pacientes sin adicciones:", num_sin_adicciones)
print("🔹 Pacientes con al menos una adicción:", num_con_adicciones)
print("🔹 Promedio de adicciones (todos):", round(promedio_todos, 2))
print("🔹 Promedio de adicciones (solo con adicciones):", round(promedio_con_adicciones, 2))
print("🔹 Moda de adicciones:", DICCTIONARY_ADDICTION[moda[0]], f"({moda[1]} pacientes)")

print("\n🔹 Frecuencia de cada adicción:")
for adiccion, cantidad in conteo.items():
    nombre = DICCTIONARY_ADDICTION.get(adiccion, "Desconocida")
    print(f"  - {nombre}: {cantidad}")

# --- Configuración de Colores para Gráficos ---
# Colores para el gráfico de pastel (Pacientes con/sin adicciones)
PIE_CHART_COLORS = ["#ff9999", "#66b3ff"] # Ejemplo: [Color para "Con adicciones", Color para "Sin adicciones"]

# Colores para el gráfico de barras (Frecuencia de cada adicción)
# Define una lista de colores. Matplotlib ciclará a través de ellos si hay más barras que colores.
BAR_CHART_COLORS = ["#4CAF50", "#FFC107", "#2196F3", "#E91E63", "#795548", "#00BCD4"]


# Pie chart: pacientes con y sin adicciones
labels_pie = ["Con adicciones", "Sin adicciones"]
sizes_pie = [num_con_adicciones, num_sin_adicciones]

plt.figure(figsize=(6,6))
# Capturar wedges, texts (para labels_pie) y autotexts (para porcentajes)
wedges, texts, autotexts = plt.pie(
    sizes_pie,
    labels=None,                 # Etiquetas principales
    autopct=lambda p: f'{p:0.1f}%' if p >= 1 else '',                 # Formato de los porcentajes
    colors=PIE_CHART_COLORS,
    startangle=140,
    pctdistance=0.5,                   # Distancia de los porcentajes desde el centro (ej. 0.8 para estar más afuera que las etiquetas)
    labeldistance=0.8,                 # Distancia de las etiquetas desde el centro (<1 para estar dentro, ej. 0.5)
    textprops={'fontsize': 12, 'horizontalalignment': 'center', 'verticalalignment': 'center'} # Propiedades para el texto de las etiquetas
    
)


# Ajusta el tamaño y color de los porcentajes y centraliza el texto
for autotext in autotexts:
    autotext.set_color('white')  # Cambia el color del texto de porcentaje
    autotext.set_fontsize(18)     # Cambia el tamaño de fuente del texto de porcentaje
    autotext.set_fontweight('bold')  # Hace el texto de porcentaje en negrita
    # autotext.set_horizontalalignment('center')  # Centra el texto horizontalmente
    autotext.set_verticalalignment('center')    # Centra el texto verticalmente

plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.title("Pacientes con / sin adicciones", fontsize=22, pad=20)



# Modificado para incluir el porcentaje en la etiqueta de la leyenda
import matplotlib.patches as mpatches

# Añadir leyenda
plt.legend(
    # handles=legend_patches,
    handles=[mpatches.Patch(color=PIE_CHART_COLORS[0], label="Con adicciones"), mpatches.Patch(color=PIE_CHART_COLORS[1], label="Sin adicciones")],
    title="Adicciones",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=12,
    title_fontsize=14
)

plt.tight_layout()
plt.show()

total_adicciones = sum(len(p) for p in LIST_ADDICTIONS)
print(f"\n🔹 Total de adicciones registradas: {total_adicciones}")


# Gráfico de pastel: distribución de cada tipo de adicción
def plot_addiction_pie_chart():
    """Genera un gráfico de pastel mostrando la distribución de cada tipo de adicción."""
    # Ordenar los datos por la clave de la adicción para consistencia
    sorted_items = sorted(conteo.items())
    
    # Preparar los datos para el gráfico
    labels = [DICCTIONARY_ADDICTION.get(k, str(k)) for k, v in sorted_items]
    sizes = [v for k, v in sorted_items]
    # Usar los colores definidos en BAR_CHART_COLORS
    colors = BAR_CHART_COLORS[:len(labels)]

    plt.figure(figsize=(12, 8))
    
    wedges, texts, autotexts = plt.pie(
        sizes,
        autopct='%1.1f%%', # Mostrar porcentaje dentro de cada porción
        startangle=140,
        colors=colors,
        pctdistance=0.75,
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
    )

    # Estilo para el texto del porcentaje
    plt.setp(autotexts, size=12, weight="bold", color="white")

    plt.title("Distribución de Tipos de Adicción", fontsize=22, pad=20)
    plt.axis('equal')  # Asegura que el gráfico sea un círculo.

    # Crear leyenda con el nombre y el porcentaje de cada adicción
    legend_patches = [mpatches.Patch(color=color, label=f'{label}:({size/total_adicciones*100:.1f}%)') 
                      for label, color, size in zip(labels, colors, sizes)]

    plt.legend(handles=legend_patches, title="Tipos de Adicción", loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=12, title_fontsize=14)
    plt.tight_layout(rect=[0, 0, 0.8, 1]) # Ajustar para dejar espacio a la leyenda
    plt.show()

# Gráfico de barras: frecuencia de cada adicción
def plot_bar_chart():
    # Ordenar las adicciones por su clave (ID) para una visualización consistente
    sorted_items = sorted(conteo.items())
    adicciones_labels = [DICCTIONARY_ADDICTION.get(k, str(k)) for k, v in sorted_items]
    frecuencias = [v for k, v in sorted_items]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(adicciones_labels, frecuencias, color=BAR_CHART_COLORS, edgecolor='black')

    # Etiquetas sobre cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, yval, ha='center', va='bottom', fontsize=10, fontweight='bold')
            
    plt.xlabel("Tipo de Adicción", fontsize=12)
    plt.ylabel("Cantidad de Pacientes", fontsize=12)
    plt.title("Frecuencia de Cada Adicción", fontsize=16, fontweight='bold')
    plt.xticks(rotation=45, ha="right") # Rotar etiquetas para mejor legibilidad
    plt.ylim(0, max(frecuencias) + 5) # Añadir espacio en la parte superior

    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout() # Ajustar diseño para que todo encaje

    plt.show()

# --- Generar Gráfico de Barras ---
plot_bar_chart()

# --- Generar Gráfico de Pastel (Distribución de Adicciones) ---
plot_addiction_pie_chart()
