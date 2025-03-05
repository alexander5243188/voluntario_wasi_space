// Generar un número aleatorio entre 1 y 100
let numeroSecreto = Math.floor(Math.random() * 100) + 1;
let intentos = 0;

// Funcion para procesar la adivinanza del usuario
function adivinar() {
    let input = document.getElementById("userInput");
    let mensaje = document.getElementById("mensaje");
    let numeroUsuario = parseInt(input.value);
    
    //Verificar si el usuario ingresó un número válido
    if(isNaN(numeroUsuario) || numeroUsuario < 1 || numeroUsuario > 100){
        mensaje.innerHTML="⚠ Ingresaun número valido entre 1 y 100";
        return;
    }
    intentos++;

    //Comprobar si el usurio acertó es mayor o menor
    if (numeroUsuario < numeroSecreto) {
        mensaje.innerHTML = "🔼 El número es mayor. Inténtalo de nuevo.";    
    } else if (numeroUsuario > numeroSecreto){
        mensaje.innerHTML = "🔽 El número es menor. Inténtalo de nuevo.";
    } else[
        mensaje.innerHTML  = `🎉 ¡Felicidades! Adivinaste el número en ${intentos} intentos.`
    ]
    input.value = ""; // Limpiar el campo de entrada
}