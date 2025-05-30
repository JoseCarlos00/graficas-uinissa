import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import statistics as stats # type: ignore
import pandas as pd # type: ignore

DICTIONARY_LEVEL_EDUCATION = {
  1: "ANALFABETA",
  2: "SABE LEER  Y ESCRIBIR ",
  3: "PREESCOLAR",
  4: "PRIMARIA",
  5: "EDUCACIÓN ESPECIAL ",
  6: "SECUNDARIA",
  7: "BACHILLERATO",
  8: "CARRERA TÉCNICA",
  9: "LICENCIATURA",
  10: "POSGRADO",
}

ESCOLARIDAD_LIST = [6,2,4,5,1,4,4,4,6,2,6,5,6,5,7,7,5,6,6,6,5,4,7,4,7,5,4,5,4,5,4,4,5,6,6,5,7,6,6,5,5,5,7,4,6,8,4,4,6,8,2,6,5,6,6,4,4,6,4,6,5,7,4,7,6,8,1,6,7,5,4,5,7,6,6,5,5,5,5,5,4,5,5,6,4,6,8,5,4,5,5,5,7,7,7,5,5,6,7,5,3,8,5,6,5,5,4,3,7,4]


# Crear una tabla de frecuencia
frecuencia_absoluta = pd.Series(ESCOLARIDAD_LIST).value_counts().sort_index()
print('=============================\n\n')

new_serie = pd.Series(ESCOLARIDAD_LIST)
min_calif = new_serie.min()
max_calif = new_serie.max()
media_calif = new_serie.mean()
mediana_calif = new_serie.median()
moda_calif = new_serie.mode().iloc[0]
rango_calif = max_calif - min_calif
varianza_calif = new_serie.var(ddof=1)
desviacion_estandar_calif = new_serie.std(ddof=1)

print('Min: ', min_calif)
print('Max: ', max_calif)
print('Media: ', round(media_calif, 2))
print('Mediana: ', round(mediana_calif, 2))
print('Moda: ', moda_calif)
print('Rango: ', rango_calif,)
print('Varianza: ', round(varianza_calif, 2))
print('Desviación estandar: ', round(desviacion_estandar_calif, 2))
print('=============================\n\n')
# print(new_serie)

tabla_frecuencia = {
  "Escolaridad":  [DICTIONARY_LEVEL_EDUCATION.get(i, f"Nivel {i}") for i in frecuencia_absoluta.index],
  "No. Personas": frecuencia_absoluta.values,
  "%": [round(frecuencia_absoluta.values[i] / new_serie.size, 2) for i in range(len(frecuencia_absoluta))],
}



tabla_frecuencia_frame = pd.DataFrame(tabla_frecuencia)
# print(tabla_frecuencia_frame)

# Guardar archivo en csv
tabla_frecuencia_frame.to_csv('tabla_frecuencia1.csv', index=False, sep=',', decimal='.', encoding='utf-8')

