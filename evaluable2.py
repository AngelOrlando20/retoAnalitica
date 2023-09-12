# Actividad Evaluable: Obtención de estadisticas descriptivas. 
# Nombre: Angel Orlando Vazquez Morales
# Matrícula: A01659000.

import pandas as pd
import numpy as np

df1 = pd.read_csv('avocado.csv')

# Imprimir resumen de datos (primeras filas de datos)

print("= DATOS: =")
print(df1.head())
print()

# Número de columnas y datos.

print("Columnas: ", len(df1.axes[0]))
print("Filas: ", len(df1.axes[1]))
print("")

# Rango de datos de precio promedio.

print("= Rango de precio promedio: =")
print("Minimo:", df1['AveragePrice'].min())
print("Maximo:", df1['AveragePrice'].max())
print()

# Media, mediana y desv. estándar de cada precio promedio de los datos.
print("= Promedio de precios promedios: =")
print("Promedio: ", df1['AveragePrice'].mean())
print("Mediana: ", df1["AveragePrice"].median())
print("Desviación estándar: ", np.std(df1["AveragePrice"].std()))
print()
