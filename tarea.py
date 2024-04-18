import pandas as pd

# leer un csv
data_frame = pd.read_csv("frecuencia_absoluta.csv", delimiter=",")

# mostrar por consola la informacion de la data frame, en forma de tabla

# para acceder a una columna especifica
# print(data_frame["fi"])

# crear y agregar el Fi en una nueva columna
data_frame["Fi"] = data_frame["fi"].cumsum()

# crear y agregar ri en una nueva columna
data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()

# crear y agregar Ri en una nueva columna
data_frame["Ri"] = data_frame["ri"].cumsum()

# crear y agregar pi% en una nueva columna
data_frame['pi%'] = data_frame["ri"] * 100

# crear y agregar Pi% en una nueva columna
data_frame["Pi%"] = data_frame["Ri"] * 100

print(data_frame)

data_frame.to_clipboard(index=False, decimal=',')
