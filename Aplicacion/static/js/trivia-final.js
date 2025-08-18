const txtPuntaje = document.querySelector("#puntos");
const nombre = document.querySelector("#nombre");
const nombreJugador = document.querySelector("#nombre-jugador");
const puntajeFinal = document.querySelector("#puntaje-final");
const totalAcertadas = document.querySelector("#total-acertadas");
const totalNoAcertadas = document.querySelector("#total-no-acertadas");
const btnComenar = document.querySelector("#btn-comenzar")

nombre.innerHTML = localStorage.getItem("nombre");
nombreJugador.innerHTML = localStorage.getItem("nombre");
txtPuntaje.innerHTML = parseInt(localStorage.getItem("puntaje-total"));
puntajeFinal.innerHTML = parseInt(localStorage.getItem("puntaje-total")) + " Puntos";

const correctas = parseInt(localStorage.getItem("puntaje-total"))/100;
const incorrectas = 30 - correctas;
totalAcertadas.innerHTML = correctas;
totalNoAcertadas.innerHTML = incorrectas;

btnComenar.addEventListener("click", () => {
    // Limpiar datos del juego
    localStorage.removeItem("nombre");
    localStorage.removeItem("puntaje-total");
    localStorage.removeItem("categoria-actual");
    localStorage.removeItem("categorias-jugadas");

    // Redirigir a la página de inicio de la trivia
    const urlInicio = btnComenar.dataset.url;
    location.href = urlInicio;
});