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

table = {

}

def add_team():  
    team = input("Ingrese el nombre del equipo: ")

    if team in table:
        print("El equipo ya existe en el torneo.")
    else:
        table[team] = {"Puntos":0}                                      # Generar equipo si no lo encuentra. Case sensitive


def add_result():
    while len(table) < 2:
        print("No hay suficientes equipos para agregar un resultado. Agregue algunos equipos: ")
        add_team()

    local = input("Ingrese al equipo local: ")

    while local not in table:
        print("Este equipo no forma parte del torneo. Intente otra vez. ")
        local = input("Ingrese al equipo local: ")
    
    visitor = input("Ingrese al equipo visitante: ")

    while visitor not in table:
        print("Este equipo no forma parte del torneo. Intente otra vez. ")
        visitor = input("Ingrese al equipo visitante: ")
    
    while True:
        score = input("Ingrese marcador del partido (Formato 4 - 2): ")

        if "-" not in score:
            print("Formato no válido.")
            continue

        goals = score.split()                                           # Crea una lista con los goles (y el guion)

        if goals[0].isdigit() and goals[2].isdigit():
            local_goals = int(goals[0])
            visitor_goals = int(goals[2])
            break
        else:
            print("Formato no válido.")

    if local_goals > visitor_goals:
        print(f"Gano {local}")
        table[local]["Puntos"] += 3
    elif visitor_goals > local_goals:
        print(f"Gano {visitor}")
        table[visitor]["Puntos"] += 3
    elif visitor_goals == local_goals:
        table[local]["Puntos"] += 1
        table[visitor]["Puntos"] += 1
                      

def show_table():
    if len(table) != 0:
        for team, score in sorted(table.items(), key=lambda x: x[1]["Puntos"], reverse=True):
            print(f"{team}: {score['Puntos']} puntos")
    else:
        print("La tabla esta vacia.")


def delete_team():
    if len(table) != 0:
        deleted_one = input("Ingrese el equipo a eliminar: ")
        if deleted_one not in table:
            print("El equipo no esta en la tabla.")
        else:
            del table[deleted_one]
            print(f"Se elimino al equipo {deleted_one}")
    else:
        print("La tabla esta vacia. No es posible eliminar equipos.")

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
            add_team()
        case 2:
            add_result()
        case 3: 
            show_table()
        case 4:
            delete_team()
        case 5:
            break