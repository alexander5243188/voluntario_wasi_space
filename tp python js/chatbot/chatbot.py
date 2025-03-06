import tkinter as tk

# Diccionario de respuestas predefinidas.
respuestas = {
    "hola":"!Hola¡ ¿En qué puedo ayudarte?",
    "¿cómo estás?":"Estoy bie, gracias por preguntas",
    "¿qué puedes hacer?":"Puedo responder preguntas básicas. Intenta preguntasrme algo.",
    "adiós":"!Hasta luego¡ Que tengas un gran día.",
    "¿quién te creó?":"Fui creado con Python y Tkinter",
    "default":"Lo siento, no entiendo esa pregunta."
}

# Función para precesar la entrada del usuario
def responder():
    pregunta = entrada.get().strip().lower()
    # método get del objeto entrada es un widget de tipo entry, utilizado para recuperar texto
    # el método strip() elimina los espacios en blanco al principio y al final
    # el método lower() transforma todo el texto en minusculas
    respuesta = respuestas.get(pregunta, respuestas["default"]) # busca en el diccionario o usa respuesta por defecto

    chat.insert(tk.END, f"Tú: {pregunta}\n", "usuario") 
    # tk.END es el final de del contenido
    chat.insert(tk.END, f"Bot:{respuesta}\n\n", "bot")
    entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot Básico")
ventana.geometry("400x500")

# Área de chat
chat = tk.Text(ventana, wrap="word", height=20, width=50)
# tk.Text se crea un widget
# ventana define donde vivira el widget 
# wrap="word" no cortara palabras, sino que pasará a la siguiente linea
chat.pack(pady=10)
# pack, organiza los widgets en orden vertical u horizontal.
# pady=10, define espacio vertical (padding), alrededro del widget, se añade 10 pixeles
chat.tag_config("usuario", foreground="blue", font=("Arial", 10, "bold"))
# tag_config, configura un estilo especificopara el texto etiquetado en este caso "usuario"
# foreground, cambia el color de la fuente.
chat.tag_config("bot", foreground="green", font=("Arial",10))

# Campo de entrada
entrada = tk.Entry(ventana, width=40, font=("Arial",12))
# tk.Entry(), acepta datos simples, texto de una sola  linea
entrada.pack(pady=5)

# Boton para enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=responder,font=("Arial", 12) )
# tk.Button, crea botones interactivos
# text, texto que aparecesa sobre el botón
# command=, funcion que se ejecutara al hacer clic en el boton, en esta caso llamara a la funcion responder
boton_enviar.pack()

# Detectar "Enter" para enviar mensaje
ventana.bind("<Return>", lambda event: responder())
# bind(),este metodo asocia un evento del teclado o ratón a una accion
# en este caso <Returns> corresponde a enter, cada vez que se preciona la tecla, se ejecutara una accion
# lambda,   es una funcion anonima que permite definir una accion en una sola linea
# event, este argumento recibe informacion sobre el evento activado, en este caso la tecla enter 
# responder(), al precionar la tecla enter se ejecutar la funcion 


# Iniciar la interfaz
ventana.mainloop()
    