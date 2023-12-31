# Actividad Evaluable: Obtención de estadisticas descriptivas. 
# Nombre: Angel Orlando Vazquez Morales
# Matrícula: A01659000.
# Para correr: Con la terminal cambiar de directorio al repositorio (cd retoAnalitica) 
# y ejecutar (python evaluable2.py)

import pandas as pd
import numpy as np

# CARGA DE DATOS CON PANDAS.
df1 = pd.read_csv('./avocado.csv')

# Imprimir resumen de datos (primeras filas de datos)
print("= DATOS: =")
print(df1.head())
print()

# Número de columnas y datos.

print("= Cantidad de DATOS =")
print("Columnas: ", len(df1.axes[0]))
print("Filas: ", len(df1.axes[1]))
print("Total de datos: ", len(df1.axes[0]) * len(df1.axes[1]))
print("= Tipos de datos =")
print(list(df1.columns))
print("")

for col in df1.columns:
    print(f'Rango de "{col}": [{df1[col].min()}, {df1[col].max()}]')
print()

print("= Rangos =")
print(df1.axes[0])
print(df1.axes[1])
print()

# Rango de datos de precio promedio.
print("= Max/Min de precio promedio: =")
print("Minimo:", df1['AveragePrice'].min())
print("Maximo:", df1['AveragePrice'].max())
print()

# Media, mediana y desv. estándar de cada precio promedio de los datos.
print("= Promedio de precios promedios: =")
print("Promedio: ", df1['AveragePrice'].mean())
print("Mediana: ", df1["AveragePrice"].median())
print("Desviación estándar: ", df1["AveragePrice"].std())
print()

# Media, mediana y desv. estándar sobre el volumen total.
print("= Datos sobre los precios promedio: =")
print("Promedio: ", df1["Total Volume"].mean())
print("Mediana: ", df1["Total Volume"].median())
print("Desviación estándar: ", df1["Total Volume"].std())
print()

# Se imprimen todas las regiones presentes en los datos.
regions = df1['region'].unique()
print("= Todas las regiones =")
print(regions)

max: int = df1.loc[df1['region'] == regions[0]]['Total Volume'].sum()
region: str = ""
for i in range(1, len(regions)):
  a = df1.loc[df1['region'] == regions[i]]['Total Volume'].sum()
  if (a > max):
    max = a
    region = regions[i]

# Se imprime la región con el mayor volumen total de aguacates.
print()
print('Volumen mayor: ', max, ', región: ', region)
