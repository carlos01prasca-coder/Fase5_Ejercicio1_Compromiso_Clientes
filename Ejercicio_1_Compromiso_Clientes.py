# Programa para clasificar el nivel de compromiso de los clientes

# Matriz con los datos de cinco clientes
# Cada fila contiene: ID, duración de la sesión y número de clics

sesiones = [
    [101, 220, 12],
    [102, 40, 5],
    [103, 120, 6],
    [104, 250, 2],
    [105, 90, 10]
]

# Función para determinar el nivel de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Recorrer la matriz y clasificar cada cliente
print("RESULTADOS DE LOS CLIENTES")
print("---------------------------")

for cliente in sesiones:
    id_cliente = cliente[0]
    duracion = cliente[1]
    clics = cliente[2]

    nivel = clasificar_compromiso(duracion, clics)

    print("ID del cliente:", id_cliente)
    print("Duración:", duracion, "segundos")
    print("Número de clics:", clics)
    print("Nivel de compromiso:", nivel)
    print("---------------------------")
