import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## Cargar el DataFrame desde el archivo Excel
df = pd.read_excel('C:/Users/fabri/Documents/workspace/Analisis_de_outliers/data/data.xlsx')

## Eliminar la última fila que contiene el promedio logarítmico
promedios_por_columna = df.iloc[-1, 1:].astype(float)

## Reemplazar los valores '--' por NaN
df = df.replace('--', np.nan)

## Reemplazar las comas por puntos en las columnas numéricas
columnas_numericas = df.columns[1:]
df[columnas_numericas] = df[columnas_numericas].replace({',': '.'}, regex=True)

## Graficar un diagrama de caja con seaborn
# Esta línea crea una nueva figura de matplotlib con un tamaño de 10 pulgadas de ancho y 6 pulgadas de alto.
# La función plt.figure() crea una nueva figura vacía, y el argumento figsize especifica las dimensiones de la figura.
plt.figure(figsize=(20, 10))
# Esta línea genera un diagrama de caja utilizando la biblioteca Seaborn.
# Toma los datos del DataFrame df utilizando la función iloc para seleccionar todas las filas (:) y todas las columnas a partir de la segunda (1:),
#  luego los convierte a tipo de dato float utilizando astype(float). Se crea un diagrama de caja para cada columna numérica en el DataFrame.
sns.boxplot(data=df.iloc[:, 1:].astype(float))
# Este bucle itera sobre los índices y los valores de la serie promedios_por_columna, que contiene los promedios por columna calculados previamente.
for i, promedio in enumerate(promedios_por_columna):
# Esta línea agrega un texto a la figura en las coordenadas (i, promedio). El texto es el valor del promedio formateado con dos decimales (f'{promedio:.2f}').
# ha='center' y va='bottom' especifican la alineación horizontal y vertical del texto.
    plt.text(i, promedio, f'{promedio:.2f}', ha='center', va='bottom')
# Esta línea establece el título del gráfico como "Diagrama de Caja de Mediciones de Ruido por Estación - Horario".
plt.title('Diagrama de Caja de Mediciones de Ruido por Estación - Horario')
# Esta línea establece el título del eje X como "Estaciones de Ruido - Horario".
plt.xlabel('Estaciones de Ruido - Horario')
# Esta línea establece el título del eje Y como "Nivel de Ruido".
plt.ylabel('Nivel de Ruido')
# Esta línea rota las etiquetas del eje X 45 grados para mejorar la legibilidad si hay muchas estaciones de ruido.
plt.xticks(rotation=45)
# Guardar la figura como una imagen en la carpeta "output"
plt.savefig('C:/Users/fabri/Documents/workspace/Analisis_de_outliers/output/diagrama_caja_ruido.png')
# Esta línea muestra la figura completa con todas las características especificadas anteriormente.
plt.show()
