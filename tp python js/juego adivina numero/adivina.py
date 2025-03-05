import random # importamos la libreria para generar números aleatorios

def adivina_el_numero():
    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    numero_secreto = random.randint(1,100) # Genera un número aleatorio entre 1 y 100
    intentos = 0 # Contador de intentos

    while True:
        try:
            # Pedimos al usuario que ingrese un número
            adivinanza = int(input("Introduce tu número: "))
            intentos += 1 # Aumentamos el número de intentos

            # Comprobamos si el usuario acertó, es mayor o menor
            if adivinanza < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break # Salimos del bucle si el usuario acierta
        except ValueError:
            print("Por favor. ingresa un nukmero válido.")

# Ejecutamos el juego
adivina_el_numero()