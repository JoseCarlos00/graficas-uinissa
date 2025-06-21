import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # type: ignore
from collections import Counter

# Añadir el directorio padre (graficas-uinissa) a sys.path para encontrar otros módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import servicios_publicos.pastel as pastel

# Cada fila es un servicio y cada elemento indica si el paciente tiene acceso (1) o no (0)
# 1 = tiene acceso ("x"), 0 = no tiene acceso (vacío)

servicios = [
    # Agua entubada
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  
    
    # Drenaje
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],  
    
    # Basura
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1], 
     
    # Gas
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1], 
     
    # Luz eléctrica
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],  
    
    # Teléfono
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1], 
    
    # Internet
    [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]   
]

servicios_nombres = [
    "Agua Entubada",
    "Drenaje",
    "Basura",
    "Gas",
    "Luz Eléctrica",
    "Teléfono",
    "Internet"
]


# Convertimos a matriz NumPy para facilitar cálculos
data = np.array(servicios)

# Frecuencia de acceso por servicio
acceso_por_servicio = np.sum(data, axis=1)

# Frecuencia de acceso por paciente
acceso_por_paciente = np.sum(data, axis=0)

# Porcentaje de acceso por servicio
porcentaje_servicio = (acceso_por_servicio / data.shape[1]) * 100


# Total de pacientes
total_pacientes = data.shape[1]



# Resultados
print("🔹 Total de pacientes:", total_pacientes)
print("🔹 Frecuencia de acceso por servicio:")
for i, servicio in enumerate(servicios_nombres):
    print(f"  - {servicio}: {acceso_por_servicio[i]} pacientes ({porcentaje_servicio[i]:.1f}%)")

# --- Gráfico de Barras para Porcentaje de Acceso por Servicio ---

# Colores personalizados por cada nivel de escolaridad
COLOR_BY_LEVEL = [
 "#D94274",     # rojo (para IMSS)
 "#FF8C00",     # naranja
 "#FFD700",     # dorado
 "#9ACD32",     # verde oliva
 "#281FD3",     # verde
 "#00CED1",     # turquesa
 "#6A5ACD",     # púrpura
]


# Crear gráfico de barras
def create_bar_chart():
    plt.figure(figsize=(12, 7)) # Ajustar el tamaño de la figura para mejor visualización

    # Crear las barras
    bars = plt.bar(servicios_nombres, porcentaje_servicio, color=COLOR_BY_LEVEL, edgecolor='black')

    # Añadir etiquetas de porcentaje encima de cada barra para mayor claridad
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.xlabel("Servicio Público", fontsize=12)
    plt.ylabel("Porcentaje de Acceso (%)", fontsize=12)
    plt.title("Porcentaje de Acceso a Servicios Públicos por Paciente", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha="right", fontsize=10) # Rotar etiquetas del eje X para evitar superposición
    plt.yticks(fontsize=10)
    plt.ylim(0, max(porcentaje_servicio) + 10) # Ajustar límite del eje Y para dar espacio a las etiquetas y mejorar la estética
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Añadir una rejilla horizontal sutil
    plt.tight_layout() # Ajustar el layout para que todo encaje bien
    plt.show()
    

# Gráfico de barras horizontales
def create_horizontal_bar_chart():
    plt.figure(figsize=(10, 6))
    plt.barh(servicios_nombres, porcentaje_servicio, color=COLOR_BY_LEVEL)
    plt.xlabel("Porcentaje de acceso (%)", fontsize=12)
    plt.title("Acceso a Servicios Públicos por Pacientes", fontsize=16, fontweight="bold")
    plt.xlim(0, 100)

    # Mostrar los valores al final de cada barra
    for i, v in enumerate(porcentaje_servicio):
        plt.text(v + 0.5, i, f"{v:.1f}%", va='center', fontsize=10)

    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

# Ya tienes esto:
acceso_por_servicio = np.sum(data, axis=1)  # accesos por servicio
print("🔹 Acceso por servicio:", acceso_por_servicio)

def create_pie_chart():
    # El problema es que los porcentajes se calculaban sobre bases distintas.
    # `plt.pie` calcula el porcentaje de cada rebanada respecto a la SUMA de los datos que se le pasan.
    # La leyenda, sin embargo, usaba un porcentaje pre-calculado que se basaba en el total de accesos *posibles*, no en el total de accesos *reales*.
    # Para que coincidan, debemos usar la misma base para ambos cálculos: el total de accesos reales.

    # Crear gráfico de pastela
    plt.figure(figsize=(10, 10))  # Tamaño cuadrado para un pastel más simétrico
    wedges, texts, autotexts = plt.pie(
        acceso_por_servicio, # Pasamos los conteos directos. Matplotlib calculará el porcentaje.
        labels=None,
        autopct='%1.1f%%',
        startangle=140,
        colors=COLOR_BY_LEVEL,
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
    )
    # Estilo para el texto del porcentaje
    plt.setp(autotexts, size=12, weight="bold", color="white")

    plt.title("Distribución de Acceso\na Servicios Públicos", fontsize=22, pad=20)
    plt.axis('equal')  # Asegura que el gráfico sea un círculo.
    
    # Para que la leyenda coincida, calculamos el porcentaje sobre la misma base que el gráfico:
    # la suma total de accesos reales.
    total_accesos_reales = np.sum(acceso_por_servicio)
    legend_patches = [mpatches.Patch(color=color, label=f'{label}: {(size/total_accesos_reales*100):.1f}%')
                      for label, color, size in zip(servicios_nombres, COLOR_BY_LEVEL, acceso_por_servicio)]
    
    plt.legend(handles=legend_patches, title="Servicios Públicos", loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=12, title_fontsize=14)
    plt.tight_layout(rect=[0, 0, 0.8, 1])  # Ajustar para dejar espacio a la leyenda
    plt.show()
    
    
# Llamar a las funciones para crear los gráficos
create_pie_chart()

print('acceso_por_servicio', acceso_por_servicio)
