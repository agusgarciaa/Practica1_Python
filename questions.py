import random

# Modificá el juego para que las palabras estén agrupadas por categoría.
# Al inicio de cada partida, mostrar las categorías disponibles y permitir
# que el usuario elija una. 
dictionary = {
    "Lenguajes": ["python", "pascal", "java"], #Agrego algunos lenguajes extras.
    "Conceptos": ["programa", "variable", "funcion", "bucle"],
    "Tipos de datos": ["cadena", "entero", "lista",]
    }

print("¡Bienvenido al Ahorcado!")
print()

matches = 0
while True:
    score = 0

    print("Categorias disponibles: ")
    i = 1
    for category in dictionary:
        print(f"-{category}")
        i += 1

    while True:
        choice = input("Elija una categoria: ")
        if len(dictionary[choice]) == 0:
            print(f"No quedan palabras en la categoría {choice}. Elegí otra.")
            continue
        if choice in dictionary: 
            break
        else:
         print("Opción no válida. Por favor, intente otra vez.")

    # Modificá el juego para que, al jugar varias rondas seguidas, no se
    # repita la misma palabra.   
    word = random.sample(dictionary[choice],1)[0]
    dictionary[choice].remove(word)
    guessed = []
    attempts = 6
    print(f"Has elegido la categoria: {choice}")


    while attempts > 0:
     # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            score += 6 
            print("¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = str(input("Ingresá una letra: "))

        #El juego tiene un bug. Si el usuario ingresa más de una letra, un número o cualquier otro carácter inválido,
        #el programa se comporta de manera inesperada. Modificalo para que en ese caso
        #muestre el mensaje
        #"Entrada no válida" y continúe el juego en la siguiente iteración.
        if len(letter) != 1 or not ('a' <= letter <= 'z' or 'A' <= letter <= 'Z'):
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0

    # Modificá el juego para que al final de la partida se muestre el puntaje
    # del jugador. El puntaje se calcula de la siguiente forma: cada letra
    # incorrecta resta 1 punto, adivinar la palabra completa suma 6 puntos,
    # y perder deja el puntaje en 0.
    print(f"Tu puntaje fue de: {score}")
    matches += 1
    if matches == 10:
        print("Ya no quedan mas palabras, ¡Gracias por jugar!")
        break
    play_again = input("¿Desea seguir jugando? (s/n): ")
    if play_again != "s":
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        break
