# Actividad Evaluable: Obtención de estadisticas descriptivas. 
# Nombre: Angel Orlando Vazquez Morales
# Matrícula: A01659000.

import pandas as pd
import numpy as np

# CARGA DE DATOS CON PANDAS.
df1 = pd.read_csv('avocado.csv')

# Imprimir resumen de datos (primeras filas de datos)

print("= DATOS: =")
print(df1.head())
print()

# Número de columnas y datos.

print("= Cantidad de DATOS =")
print("Columnas: ", len(df1.axes[0]))
print("Filas: ", len(df1.axes[1]))
print("= Tipos de datos =")
print(list(df1.columns))
print("")
# ? Tipo de variable?

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
print("Desviación estándar: ", np.std(df1["AveragePrice"].std()))
print()
