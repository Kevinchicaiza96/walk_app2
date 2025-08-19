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

            toggle.setAttribute("aria-expanded", "true");
            menu.setAttribute("aria-hidden", "false");
        });

        // Cerrar menú
        closeBtn.addEventListener("click", () => {
            menu.classList.remove("active");
            document.body.classList.remove("menu-open");

            toggle.setAttribute("aria-expanded", "false");
            menu.setAttribute("aria-hidden", "true");
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

                toggle.setAttribute("aria-expanded", "false");
                menu.setAttribute("aria-hidden", "true");
            }
        });

        // Cerrar con tecla ESC
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && menu.classList.contains("active")) {
                menu.classList.remove("active");
                document.body.classList.remove("menu-open");

                toggle.setAttribute("aria-expanded", "false");
                menu.setAttribute("aria-hidden", "true");
            }
        });
    }

    // ===== Overlay buscador =====
    const buscador = document.getElementById("buscador-overlay");

    if (buscador) {
        const form = buscador.querySelector(".buscador-form");

        // Funciones globales
        window.mostrarBuscador = () => {
            buscador.classList.add("active");
            buscador.setAttribute("aria-hidden", "false");
        };
        window.ocultarBuscador = () => {
            buscador.classList.remove("active");
            buscador.setAttribute("aria-hidden", "true");
        };

        // Cerrar con tecla ESC
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && buscador.classList.contains("active")) {
                ocultarBuscador();
            }
        });

        // Cerrar si se hace clic fuera del formulario
        buscador.addEventListener("click", (e) => {
            if (!form.contains(e.target)) {
                ocultarBuscador();
            }
        });
    }
});
