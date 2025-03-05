# Taller: "Juego de Adivina el Número" en JavaScript
## Objetivo
    Crear un juego interactivo donde la computadora genera un número aleatorio y el usuario debe adivinarlo con
    pistas en una página web.

## Conceptos a Explicar
    1. Manipulación del DOM (`document.getElementById()`, `innerHTML`).
    2. Generación de números aleatorios (`Math.random()`).
    3. Eventos en JavaScript (`addEventListener`).
    4. Condicionales (`if-else`) y bucles (`while`).
    5. Conversión de tipos (`parseInt()`).

## Explicación del Código:
    1. HTML crea la estructura del juego, incluyendo una caja de entrada (`<input>`) y un botón (`<button>`).
    2. CSS estiliza la página para que se vea atractiva.
    3. JavaScript:
        Se genera un número aleatorio entre 1 y 100 con `Math.random()`.
        La función `adivinar()` obtiene el número del usuario y lo compara con el número secreto.
        Se muestra un mensaje con pistas (`"El número es mayor"` o `"El número es menor"`).
        Se cuenta el número de intentos y, si el usuario acierta, se muestra un mensaje de victoria.

## Captura de imagen
![adivina](/tp%20python%20js/juego%20adivina%20numero%20js/img/adivina.png)