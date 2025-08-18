// navbar.js

document.addEventListener("DOMContentLoaded", function () {

    // ===== Menú móvil =====
    const menu = document.getElementById("mobileMenu");
    const toggle = document.getElementById("openMenu");
    const closeBtn = document.getElementById("closeMenu");

    if (menu && toggle && closeBtn) {
        // Abrir menú
        toggle.addEventListener("click", () => {
            menu.classList.add("active");
            document.body.classList.add("menu-open");
        });

        // Cerrar menú
        closeBtn.addEventListener("click", () => {
            menu.classList.remove("active");
            document.body.classList.remove("menu-open");
        });

        // Cerrar al hacer clic fuera del menú
        window.addEventListener("click", (e) => {
            if (
                menu.classList.contains("active") &&
                !menu.contains(e.target) &&
                !toggle.contains(e.target)
            ) {
                menu.classList.remove("active");
                document.body.classList.remove("menu-open");
            }
        });
    }

    // ===== Overlay buscador =====
    const buscador = document.getElementById("buscador-overlay");

    if (buscador) {
        // Funciones globales para usar en el HTML
        window.mostrarBuscador = () => buscador.classList.add("active");
        window.ocultarBuscador = () => buscador.classList.remove("active");

        // Cerrar con tecla ESC
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") {
                buscador.classList.remove("active");
            }
        });

        // Cerrar si se hace clic fuera del formulario
        buscador.addEventListener("click", (e) => {
            if (e.target === buscador) {
                buscador.classList.remove("active");
            }
        });
    }

});
