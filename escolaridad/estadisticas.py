import numpy as np
from collections import Counter

def medidas_estadisticas(education_list: list[int], DICTIONARY_LEVEL_EDUCATION: dict[int, str]) -> None:
     # --- Medidas Estadísticas ---
    data_array = np.array(education_list)

    mean_val = np.mean(data_array)
    median_val = np.median(data_array)
    
    # Calcular la moda (puede haber múltiples modas)
    counts = Counter(education_list)
    max_count = counts.most_common(1)[0][1]
    mode_val_numeric = [item for item, count in counts.most_common() if count == max_count]
    mode_val_descriptive = [DICTIONARY_LEVEL_EDUCATION[m] for m in mode_val_numeric]

    std_dev = np.std(data_array)
    variance = np.var(data_array)
    min_val = np.min(data_array)
    min_val_desc = DICTIONARY_LEVEL_EDUCATION[min_val]
    max_val = np.max(data_array)
    max_val_desc = DICTIONARY_LEVEL_EDUCATION[max_val]
    
    q1 = np.percentile(data_array, 25)
    q2 = np.percentile(data_array, 50) # Igual a la mediana
    q3 = np.percentile(data_array, 75)
    iqr = q3 - q1

    print("--- Medidas Estadísticas Descriptivas ---")
    print(f"Lista de datos (niveles numéricos): {education_list}")
    print(f"Número total de registros: {len(education_list)}")
    
    # Media: Promedio de los niveles de escolaridad.
    # Puede ser un valor decimal; lo redondeamos para buscar una descripción aproximada.
    mean_desc = DICTIONARY_LEVEL_EDUCATION.get(round(mean_val), f"Entre niveles (valor {mean_val:.2f})")
    print(f"Media: {mean_val:.2f} (Nivel educativo promedio aproximado: {mean_desc})")
    
    # Mediana: Valor central que divide los datos en dos mitades iguales.
    # Es robusta a valores extremos.
    print(f"Mediana: {median_val} (Nivel educativo: {DICTIONARY_LEVEL_EDUCATION[int(median_val)]})")
    
    # Moda: Nivel(es) de escolaridad más frecuente(s).
    if len(mode_val_numeric) == 1:
        print(f"Moda: {mode_val_numeric[0]} (Nivel educativo: {mode_val_descriptive[0]})")
    else:
        print(f"Modas: {mode_val_numeric} (Niveles educativos: {', '.join(mode_val_descriptive)})")
        
    print(f"Desviación Estándar: {std_dev:.2f}") # Mide la dispersión de los datos alrededor de la media.
    print(f"Varianza: {variance:.2f}") # Cuadrado de la desviación estándar.
    print(f"Mínimo: {min_val} (Nivel educativo: {min_val_desc})")
    print(f"Máximo: {max_val} (Nivel educativo: {max_val_desc})")
    print(f"Rango (Max - Min): {max_val - min_val}")
