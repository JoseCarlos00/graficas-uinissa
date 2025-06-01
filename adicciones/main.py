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
    labels=labels_pie,                 # Etiquetas principales
    autopct='%1.1f%%',                 # Formato de los porcentajes
    colors=PIE_CHART_COLORS,
    startangle=140,
    pctdistance=0.8,                   # Distancia de los porcentajes desde el centro (ej. 0.8 para estar más afuera que las etiquetas)
    labeldistance=0.5,                 # Distancia de las etiquetas desde el centro (<1 para estar dentro, ej. 0.5)
    textprops={'fontsize': 12, 'horizontalalignment': 'center', 'verticalalignment': 'center'} # Propiedades para el texto de las etiquetas
)

# Ajustar tamaño de fuente para los porcentajes (autotexts)
for autotext in autotexts:
    autotext.set_fontsize(18) # Ajusta el tamaño de la fuente del porcentaje aquí
    
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.title("Pacientes con / sin adicciones")
plt.show()

# Gráfico de barras: frecuencia de cada adicción
adicciones_labels = [DICCTIONARY_ADDICTION.get(k, str(k)) for k in conteo.keys()] 
frecuencias = list(conteo.values())

plt.figure(figsize=(8,5))
bars = plt.bar(adicciones_labels, frecuencias, color=BAR_CHART_COLORS, edgecolor='black')

# Etiquetas sobre cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontsize=10)
        
plt.xlabel("Adicción").set_fontsize(14)
plt.ylabel("Cantidad de pacientes")
plt.title("Frecuencia de cada adicción")
plt.xticks(rotation=45, ha="right") # Rotar etiquetas para mejor legibilidad

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout() # Ajustar diseño para que todo encaje

plt.show()
