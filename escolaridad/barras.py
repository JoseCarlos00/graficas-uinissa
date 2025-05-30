import matplotlib.pyplot as plt # type: ignore

# Colores personalizados por cada nivel de escolaridad
COLOR_BY_LEVEL = {
    1: "#8B0000",     # rojo oscuro
    2: "#B22222",     # rojo
    3: "#FF8C00",     # naranja
    4: "#FFD700",     # dorado
    5: "#9ACD32",     # verde oliva
    6: "#32CD32",     # verde
    7: "#00CED1",     # turquesa
    8: "#1E90FF",     # azul
    9: "#6A5ACD",     # púrpura
    10: "#4B0082",    # índigo
}

def plot_education_level(education_list: list[int], DICTIONARY_LEVEL_EDUCATION: dict[int, str], upperCase: bool = False) -> None:
    # Contar ocurrencias
    level_counts = {key: 0 for key in DICTIONARY_LEVEL_EDUCATION.keys()}
    for level in education_list:
        if level in level_counts:
            level_counts[level] += 1

    # Datos para graficar
    levels = list(level_counts.keys())
    counts = list(level_counts.values())
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
    plt.xticks(levels, [DICTIONARY_LEVEL_EDUCATION[level] if upperCase else (DICTIONARY_LEVEL_EDUCATION[level].title) for level in levels], rotation=45, ha='right')
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()
