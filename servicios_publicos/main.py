import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

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
 "#32CD32",     # verde
 "#00CED1",     # turquesa
 "#6A5ACD",     # púrpura
]


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
