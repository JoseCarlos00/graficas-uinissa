import streamlit as st # type: ignore
import matplotlib.pyplot as plt


INITIAL_COLORS_FROM_FILE = {
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

# Placeholder de la función de graficado (deberías usar la tuya, modificada)
def plot_education_level_placeholder(education_list, dictionary_education, color_map, upper_case):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    levels = sorted(list(dictionary_education.keys()))
    level_counts_data = {key: 0 for key in dictionary_education.keys()}
    for edu_level in education_list:
        if edu_level in level_counts_data:
            level_counts_data[edu_level] += 1
            
    counts = [level_counts_data.get(level,0) for level in levels]
    colors = [color_map.get(level, "#CCCCCC") for level in levels]
    labels = [(dictionary_education[level].upper() if upper_case else dictionary_education[level].title()) for level in levels]

    ax.bar(range(len(levels)), counts, color=colors, edgecolor='black', alpha=0.85)
    for i, count_val in enumerate(counts):
        if count_val > 0:
            ax.text(i, count_val + 0.5, str(count_val), ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Nivel de Escolaridad')
    ax.set_ylabel('Pacientes')
    ax.set_title('Escolaridad')
    ax.set_xticks(range(len(levels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig

DICTIONARY_LEVEL_EDUCATION = {
  1: "ANALFABETA",
  2: "SABE LEER  Y ESCRIBIR",
  3: "PREESCOLAR",
  4: "PRIMARIA",
  5: "EDUCACIÓN ESPECIAL",
  6: "SECUNDARIA",
  7: "BACHILLERATO",
  8: "CARRERA TÉCNICA",
  9: "LICENCIATURA",
  10: "POSGRADO",
}

ESCOLARIDAD_LIST = [6,2,4,5,1,4,4,4,6,2,6,5,6,5,7,7,5,6,6,6,5,4,7,4,7,5,4,5,4,5,4,4,5,6,6,5,7,6,6,5,5,5,7,4,6,8,4,4,6,8,2,6,5,6,6,4,4,6,4,6,5,7,4,7,6,8,1,6,7,5,4,5,7,6,6,5,5,5,5,5,4,5,5,6,4,6,8,5,4,5,5,5,7,7,7,5,5,6,7,5,3,8,5,6,5,5,4,3,7,4]


st.title("Visualizador Interactivo de Escolaridad")

st.sidebar.header("Editar Colores por Nivel")
current_custom_color_map = {}

# Usar DICTIONARY_LEVEL_EDUCATION_EXAMPLE para crear los selectores de color
for level_code, level_name in DICTIONARY_LEVEL_EDUCATION.items():
    default_color = INITIAL_COLORS_FROM_FILE.get(level_code, "#FFFFFF")
    # La 'key' es importante para que Streamlit identifique cada widget de forma única
    color = st.sidebar.color_picker(
        f"Color para {level_name}", 
        value=default_color, 
        key=f"color_{level_code}"
    )
    current_custom_color_map[level_code] = color

upper_case = st.sidebar.checkbox("Mostrar etiquetas en mayúsculas", value=False)

st.subheader("Gráfico de Escolaridad")

# Llama a tu función de graficado (idealmente una que devuelva la figura)
fig = plot_education_level_placeholder( # Reemplaza con tu función real
    ESCOLARIDAD_LIST,
    DICTIONARY_LEVEL_EDUCATION,
    current_custom_color_map,
    upper_case
)
st.pyplot(fig)

# Para ejecutar: guarda este código como streamlit_app.py y corre `streamlit run streamlit_app.py` en tu terminal.
# Nota: Asegúrate de que matplotlib y streamlit estén instalados en tu entorno.
