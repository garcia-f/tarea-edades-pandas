import pandas as pd

def analisis_estadistico(nombre_archivo):
    # Leer el archivo CSV
    data_frame = pd.read_csv(nombre_archivo, delimiter=",")

    # Calcular la frecuencia acumulada (Fi)
    data_frame["Fi"] = data_frame["fi"].cumsum()

    # Calcular la frecuencia relativa (ri)
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()

    # Calcular la frecuencia relativa acumulada (Ri)
    data_frame["Ri"] = data_frame["ri"].cumsum()

    # Calcular la probabilidad (pi%)
    data_frame['pi%'] = data_frame["ri"] * 100

    # Calcular la probabilidad acumulada (Pi%)
    data_frame["Pi%"] = data_frame["Ri"] * 100

    # Retornar el DataFrame resultante
    return data_frame


resultado_analisis = analisis_estadistico("frecuencia_absoluta.csv")
print(resultado_analisis)

# Copiar el DataFrame al portapapeles
resultado_analisis.to_clipboard(index=False, decimal=',')

