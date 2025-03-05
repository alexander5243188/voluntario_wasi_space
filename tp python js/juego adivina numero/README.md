## Descripción del Proyecto.
  Este proyecto consiste enel desarrollo de un juego en Python en el que el usuario intenta adivinar un número aleatorio generado por el sistema. A través de pistas sobre si el número secreto es mayor o menor, el jugador ajusta conjeturas hasta encontrar la respuesta correcta.

## Objetivos.
    1. Desarrollar un programa en Python que permita la interacción del usuario con el sistema.
    2. Aplicar estructuras de control como bucles y condicionales en Python.
    3. Fomentar el pensamiento lógico y algorítmico mediante la programación de un juego.

## Conceptos a explicar
1. Entrada y salida de datos:
   1.  El código utiliza input() para recibir la entrada del usuario (adivinanza = int(input("Introduce tu número: "))). Esto permite que el jugador ingrese un número.

   2. Además, usa print() para mostrar mensajes al usuario, como las pistas ("El número es mayor") o el mensaje de victoria (print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")).

2. Números aleatorios:
   1. Se emplea random.randint(1, 100) para generar el número secreto de manera aleatoria entre 1 y 100, representando el concepto de generación de números aleatorios.

3. Estructuras de control:
   1. El if se utiliza para verificar si el número ingresado es menor, mayor o igual al número secreto, y actúa en consecuencia.
   2. El while True mantiene el juego en ejecución hasta que el usuario adivine el número correctamente (break detiene el bucle al acertar).

4. Manejo de errores:
   1. El bloque try-except asegura que el programa no se bloquee si el usuario ingresa un dato no válido (como texto en vez de un número). En este caso, se captura el error de tipo (ValueError) y se muestra un mensaje de ayuda (print("Por favor, ingresa un número válido.")).

5. Bucles y condicionales:
   1. El bucle while repite el juego mientras el número no sea adivinado, permitiendo múltiples intentos.
   2. Las condiciones dentro del if verifican si el usuario debe continuar jugando o si ha ganado, proporcionando retroalimentación específica en cada caso.

## Explicación del Código:
1. Se importa la librería `random` para generar un número aleatorio.
2. Se define la función `adivina_el_numero()`, que contiene la lógica del juego.
3. Se genera un número aleatorio entre 1 y 100 con `random.randint(1, 100)`.
4. Se usa un `while True` para repetir intentos hasta que el usuario acierte.
5. Se captura la entrada del usuario con `input()` y se convierte a `int()`.
6. Se comparan los valores para dar pistas sobre si el número es mayor o menor.
7. Se maneja el error de entrada con `try-except` en caso de que el usuario ingrese texto en lugar de un número.
8. El juego termina cuando el usuario acierta, mostrando el número de intentos usados.

## Captura adivina numero
![Adivina](/tp%20python%20js/juego%20adivina%20numero/img/adivina.png)

## Captura adivina numero, mejoras
![Adivina v2](/tp%20python%20js/juego%20adivina%20numero/img/adivina_mejoras.png)