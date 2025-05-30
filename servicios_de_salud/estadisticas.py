from typing import List, Dict, Union, Optional
from collections import Counter

def calcular_estadisticas_servicios(
    data_list: List[Union[int, str]],
    category_labels_dict: Dict[int, str],
    special_mappings: Optional[Dict[str, int]] = None,
    title: str = "Estadísticas de Servicios de Salud"
) -> None:
    """
    Calcula y muestra estadísticas descriptivas para los datos de servicios de salud.

    Args:
        data_list: Lista de datos, puede contener enteros (claves de categorías)
                   o cadenas (que pueden ser mapeadas a claves a través de special_mappings).
        category_labels_dict: Diccionario que mapea claves enteras a etiquetas de categorías.
        special_mappings: Diccionario opcional para mapear valores de cadena especiales
                          en data_list a claves enteras. Ej: {"1-2": 9}
        title: Título para la sección de estadísticas.
    """
    if special_mappings is None:
        special_mappings = {}

    # 1. Preprocesar la lista de entrada
    processed_data_list = []
    for item in data_list:
        if isinstance(item, str) and item in special_mappings:
            processed_data_list.append(special_mappings[item])
        elif isinstance(item, int) and item in category_labels_dict: # Asegurar que la clave entera sea válida
            processed_data_list.append(item)
        elif isinstance(item, int): # Clave entera no en el diccionario
            print(f"Advertencia: Clave numérica '{item}' no encontrada en category_labels_dict. Será ignorada.")
            continue
        else:
            print(f"Advertencia: Elemento inesperado '{item}' de tipo {type(item)} en la lista de datos. Será ignorado.")
            continue

    if not processed_data_list:
        print(f"No hay datos válidos para calcular estadísticas en '{title}'.")
        return

    # 2. Contar ocurrencias (Frecuencias Absolutas)
    counts = Counter(processed_data_list)
    total_pacientes = len(processed_data_list)

    print(f"\n--- {title.upper()} ---")
    print(f"Total de Pacientes Analizados: {total_pacientes}\n")

    print("Tabla de Frecuencias:")
    print("----------------------------------------------------------")
    print(f"{'Servicio de Salud':<35} | {'Frec. Absoluta':<15} | {'Frec. Relativa (%)':<18}")
    print("----------------------------------------------------------")

    sorted_categories = sorted(category_labels_dict.keys(), key=lambda x: counts.get(x, 0), reverse=True)

    for key in sorted_categories:
        label = category_labels_dict.get(key, f"Clave Desconocida {key}")
        abs_freq = counts.get(key, 0)
        rel_freq = (abs_freq / total_pacientes) * 100 if total_pacientes > 0 else 0
        print(f"{label.title():<35} | {abs_freq:<15} | {rel_freq:<18.2f}%")
    print("----------------------------------------------------------\n")

    # 3. Calcular Moda
    if counts:
        max_freq = max(counts.values())
        modas = [category_labels_dict[key].title() for key, freq in counts.items() if freq == max_freq]
        print(f"Moda (Servicio(s) más frecuente(s)): {', '.join(modas)} (con {max_freq} pacientes cada uno)")
    else:
        print("No se pudo determinar la moda (no hay datos).")
    print("--- FIN ESTADÍSTICAS ---")
