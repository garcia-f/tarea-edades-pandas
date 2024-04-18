import csv

# convierte el archivo csv en una lista
def obtener_csv_como_lista(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        next(archivo)
        edades = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            edades.append(int(linea))
        return edades
# obtener_csv_como_lista('edades_alumnos.csv')


# Obtengo la frecuencia absoluta ( fi ), ordenada por las claves (edades)
def obtener_fi():
    # lista
    edades = obtener_csv_como_lista('edades_alumnos.csv')
    fi = {}
    for i in edades:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    # Ordenar el diccionario por las claves (edades) de menor a mayor
    fi_ordenado = dict(sorted(fi.items()))
    return fi_ordenado

print(obtener_fi())


# Guardo el diccionario de frecuencia absolura ( fi ), en un nuevo archivo.csv
def guardar_csv(fi_ordenado, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Edad', 'fi'])
        for edad, frecuencia in fi_ordenado.items():
            writer.writerow([edad, frecuencia])

fi_ordenado = obtener_fi()
guardar_csv(fi_ordenado, 'frecuencia_absoluta.csv')

