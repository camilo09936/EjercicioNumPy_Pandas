import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("datos/estudiantes.csv") #df= DataFrame
print("=== DATOS ===")
print(df)

print("=== INFORMACION ===")
print(df.info())

print("=== ESTADISTICAS ===")
print(df.describe())

print("=== PROMEDIO ===")
promedio= np.mean(df["Nota"])
print("Promedio:", promedio)

print("=== NOTA MÁXIMA ===")
notaMaxima= np.max(df["Nota"])
print("Nota máxima:", notaMaxima)

print("=== NOTA MINIMA ===")
notaMinima= np.min(df["Nota"])
print("Nota minima:", notaMinima)

print("=== ESTUDIANTES APROBADOS ===")
estudianteAprobado= df[df["Nota"]>=3.0]
print(estudianteAprobado)

print("=== ESTUDIANTES REPROBADOS ===")
estudianteReprobados= df[df["Nota"]<3.0]
print(estudianteReprobados)

print("=== RESULTADO FINAL ===")
df["Estado"]= np.where(df["Nota"]>=3.0, "Aprobó", "Reprobó")
print(df)

#plt.bar(df["Nombre"], df["Nota"])
#plt.title("Notas de Estudiantes")
#plt.xlabel("Estudiantes")
#plt.ylabel("Nota")
#plt.show()

#Actividad#

print("=== DETECTAR VALORES NULOS ===")
if df.isnull().values.any():
    print("Hay valores nulos en el los datos. La siguiente tabla indica la cantidad de datos nulos por columna:")
print(df.isnull().sum())

print("=== REEMPLAZO DE NULOS POR 0 ===")
df_reemplazo= df.fillna(0)
print(df_reemplazo)
print()

print("=== ELIMINAR FILAS CON NULOS ===")
df_eliminandonulos= df.dropna().copy()
print(df_eliminandonulos)
print()

print("=== ORDENAR POR NOTA ===")
print("=== ASCENDENTE ===")
df_ascendente= df_eliminandonulos.sort_values("Nota")
print(df_ascendente)
print("=== DESCENDENTE ===")
df_descendente= df_eliminandonulos.sort_values("Nota", ascending=False)
print(df_descendente)
print()

print("=== TOP 3 ESTUDIANTES ===")
print(df_descendente.head(3))
print()

print("=== ESTUDIANTES MAYORES A 20 AÑOS ===")
print(df_eliminandonulos[df_eliminandonulos["Edad"]>20])
print()

print("=== ESTUDIANTES EXCELENTES ===")
print(df_eliminandonulos[df_eliminandonulos["Nota"]>=4.5])
print()

print("=== PORCENTAJE DE APROBADOS ===")
aprobados= df_eliminandonulos[df_eliminandonulos["Nota"]>=3.0]
porcentajeAprobados= (len(aprobados)/len(df_eliminandonulos)) * 100
print(f"Porcentaje de aprobados: {porcentajeAprobados:.2f}%\n")

print("=== INTEGRACION CURSOS DE ESTUDIANTES ===")
listaCursos= ["Matematicas", "Programacion", "Matematicas", "Ingles", "Programacion", "Matematicas", "Ingles", "Programacion"]
df_eliminandonulos["Curso"]= pd.Series(listaCursos, index=df_eliminandonulos.index)
print(df_eliminandonulos)
print()

print("=== PROMEDIO POR CURSO ===")
print(df_eliminandonulos.groupby("Curso")["Nota"].mean())
print()

print("=== RESULTADOS EN CSV ===")
df_eliminandonulos.to_csv("datos/Resultados.csv", index=False)
print("Archivo 'Resultados.csv' guardado exitosamente.")