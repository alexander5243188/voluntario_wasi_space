import random

def guardar_record(intentos):
    # Guarda el récord de menos intentos en un archivo
    try:
        with open("record.txt", "r") as archivo:
            record_anterior = int(archivo.read())
    except (FileNotFoundError, ValueError):
        record_anterior = float("inf")  # Si no existe el archivo, ponemos un valor muy alto

    if intentos < record_anterior:
        with open("record.txt", "w") as archivo:
            archivo.write(str(intentos))
        print(f"¡Nuevo récord! {intentos} intentos.")
    else:
        print(f"Récord actual: {record_anterior} intentos.")

def seleccionar_modo():
    # Permite al usuario elegir un modo de dificultad
    print("Selecciona un modo de juego:")
    print("1. Fácil (1-50)")
    print("2. Medio (1-100)")
    print("3. Difícil (1-500)")
    while True:
        try:
            opcion = int(input("Ingresa el número del modo deseado: "))
            if opcion == 1:
                return 1, 50
            elif opcion == 2:
                return 1, 100
            elif opcion == 3:
                return 1, 500
            else:
                print("Por favor, selecciona una opción válida (1, 2 o 3).")
        except ValueError:
            print("Entrada inválida. Ingresa un número (1, 2 o 3).")

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    rango_min, rango_max = seleccionar_modo()
    print(f"Estoy pensando en un número entre {rango_min} y {rango_max}. ¡Tienes 10 intentos para adivinarlo!")
    numero_secreto = random.randint(rango_min, rango_max)
    intentos = 0
    limite_intentos = 10

    while intentos < limite_intentos:
        try:
            adivinanza = int(input("Introduce tu número: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                guardar_record(intentos)
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

        if intentos == limite_intentos:
            print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}. Mejor suerte la próxima vez.")
            break

# Ejecutamos el juego
adivina_el_numero()
