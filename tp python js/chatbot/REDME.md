# Taller: "Chatbot Básico con Python y Tkinter"
# Objetivo:
    Crear un asistente virtual sencillo que pueda responder preguntas predefinidas mediante una interfaz gráfica
# Conceptos a Explicar:
    1. Interfaces Gráficas en Tkinter (`Label`, `Entry`, `Button`, `Text`).
    2. Eventos en Tkinter (`bind`, `command`).
    3. Diccionarios en Python para respuestas predefinidas.
    4. Manejo de cadenas (`lower()`, `strip()`)
# Explicación del Código:
    1. Interfaz Gráfica con Tkinter
        Se usa `tk.Text()` para mostrar la conversación.
        `tk.Entry()` permite escribir mensajes.
        `tk.Button()` ejecuta la función `responder()`.
    2. Diccionario de Respuestas
        Las respuestas están almacenadas en un diccionario.
        Se usa `.get()` con una respuesta por defecto si la pregunta no está en la lista.
    3. Interacción y Funcionalidad
        El usuario escribe y el bot responde en el chat.
        Se pueden agregar más preguntas y respuestas fácilmente.
        Se activa el envío con el botón o la tecla Enter

# Captura de chatbot
![Chatbot](/tp%20python%20js/chatbot/img/imagen.png)