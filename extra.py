# Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol.
# El programa debe tener un menú interactivo con las siguientes opciones:
# Agregar un equipo al torneo.
# Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 - 2. 
# El programa debe actualizar los puntos automáticamente (3 puntos por victoria, 1 por empate, 0 por derrota).
# Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.
# Eliminar un equipo del torneo.
# Salir del programa.
# Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un resultado con un equipo
# desconocido, o ingresar un marcador con formato inválido.

tabla = {

}

def agregar_equipo():
    equipo = input("Ingrese el nombre del equipo: ")
    if equipo in tabla:
        print("El equipo ya existe en el torneo.")
    else:
        tabla[equipo] = {"Puntuacion:" : 0}

print ("Bienvenido a la tabla de posiciones del Torneo")
while True:
    print(""" ¿Qué desea hacer?: 
          (1) Agregar un equipo al torneo.
          (2) Registrar un resultado.
          (3) Mostrar la tabla de posiciones.
          (4) Eliminar un Equipo del torneo.
          (5) Salir del programa.
          """)
    
    option = int(input())
    match option:
        case 1:
            agregar_equipo()

        case 5:
            break