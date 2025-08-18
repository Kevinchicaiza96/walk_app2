const nombre = document.querySelector("#nombre");
const btnComenzar = document.querySelector("#comenzar");

btnComenzar.addEventListener("click", () => {
    localStorage.setItem("nombre", nombre.value);
    localStorage.setItem("puntaje-total", 0);
    localStorage.removeItem("categorias-jugadas");

    location.href = "/trivia/menu/";  // ← ruta definida en urls.py
});