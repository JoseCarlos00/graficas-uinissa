import matplotlib.pyplot as plt # type: ignore
from typing import List, Dict, Union

# Colores personalizados por cada nivel de escolaridad
COLOR_BY_LEVEL = {
    0: "#C0C0C0",     # Gris (para Ninguno)
    1: "#8B0000",     # rojo oscuro (para Secretaría de Salud)
    2: "#B22222",     # rojo (para IMSS)
    3: "#FF8C00",     # naranja
    4: "#FFD700",     # dorado
    5: "#9ACD32",     # verde oliva
    6: "#32CD32",     # verde
    7: "#00CED1",     # turquesa
    8: "#1E90FF",     # azul
    9: "#6A5ACD",     # púrpura
}

def plot_education_level(education_list: List[Union[int, str]], DICTIONARY_LEVEL_EDUCATION: Dict[int, str], upperCase: bool = False) -> None:
    # Preprocesar la lista de entrada para mapear '1-2' a la clave 9
    processed_education_list = []
    for item in education_list:
        if item == "1-2":  # Si el item es la cadena '1-2'
            processed_education_list.append(9)  # Mapear a la clave 9 ("Secretaria - IMMS")
        elif isinstance(item, int):
            processed_education_list.append(item)
        else:
            # Opcional: manejar o registrar elementos inesperados si es necesario
            print(f"Advertencia: Elemento inesperado '{item}' de tipo {type(item)} en la lista de datos. Será ignorado.")
            continue

    # Contar ocurrencias
    level_counts = {key: 0 for key in DICTIONARY_LEVEL_EDUCATION.keys()}
    for level in processed_education_list: # Usar la lista procesada
        if level in level_counts:
            level_counts[level] += 1
            
    # Datos para graficar
    levels = list(level_counts.keys())
    counts = list(level_counts.values())
    
    print("Datos para graficar:")
    for level, count in zip(levels, counts):
        print(f"{DICTIONARY_LEVEL_EDUCATION[level]}: {count} pacientes")
    # Verificar si hay datos para graficar
    if not any(counts):
        print("No hay pacientes para graficar.")
        return
    # Verificar si hay niveles de escolaridad
    if not levels or len(levels) == 0:
        print("No hay niveles de escolaridad definidos.")
        return
    # Verificar si hay datos para graficar
    if not counts or len(counts) == 0:
        print("No hay datos para graficar.")
        return

    if not levels:
        print("No hay datos para graficar.")
        return
    # Asignar colores a cada nivel
    if len(levels) > len(COLOR_BY_LEVEL):
        print("Error: Hay más niveles de escolaridad que colores definidos.")
        return
    if any(level not in COLOR_BY_LEVEL for level in levels):
        missing_colors = [level for level in levels if level not in COLOR_BY_LEVEL]
        print(f"Error: Los siguientes niveles de escolaridad no tienen un color definido en COLOR_BY_LEVEL:")
        for level_key in missing_colors:
            label = DICTIONARY_LEVEL_EDUCATION.get(level_key, f"Clave {level_key}")
            print(f"  - Nivel {level_key}: '{label}'")
        return    
    
    colors = [COLOR_BY_LEVEL[level] for level in levels]

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    bars = plt.bar(levels, counts, color=colors, edgecolor='black', alpha=0.85)

    # Etiquetas sobre cada barra
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 str(counts[i]), ha='center', va='bottom', fontsize=9)

    # Configuración del gráfico
    plt.xlabel('Nivel de Escolaridad')
    plt.ylabel('Pacientes')
    plt.title('Escolaridad')
    plt.xticks(levels, [DICTIONARY_LEVEL_EDUCATION[level] if upperCase else (DICTIONARY_LEVEL_EDUCATION[level].title()) for level in levels], rotation=45, ha='right')
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()
