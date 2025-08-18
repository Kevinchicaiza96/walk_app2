// animacion de texto

const elementsToFadeIn = document.querySelectorAll('.fade-in-element');

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target); // Opcional: dejar de observar una vez que aparece
        }
    });
}, {
    threshold: 0.1 // Define qué porcentaje del elemento debe ser visible para activar la animación
});

elementsToFadeIn.forEach(element => {
    observer.observe(element);
});

//boton verde 
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".card__button.secondary");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const heart = document.createElement("span");
            heart.classList.add("heart-icon");
            heart.innerHTML = "&#x1F49A;"; // Green heart emoji
            heart.style.cursor = "pointer";
            heart.style.marginLeft = "10px";

            button.parentNode.appendChild(heart);

            heart.addEventListener("click", () => {
                heart.remove();
            });
        });
    });
});

// validacion de contrasena

    document.addEventListener('DOMContentLoaded', function () {
        const passwordInput = document.querySelector('input[name="contraseña"]');

        if (!passwordInput) return;

        const form = passwordInput.closest('form');

        // Crear texto de ayuda
        const ayuda = document.createElement('small');
        ayuda.style.color = 'gray';
        ayuda.textContent = "Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.";
        passwordInput.parentNode.appendChild(ayuda);

        // Crear contenedor para error
        const errorMsg = document.createElement('span');
        errorMsg.id = "passwordError";
        errorMsg.style.color = "red";
        passwordInput.parentNode.appendChild(errorMsg);

        // Validación en tiempo real
        passwordInput.addEventListener('input', function () {
            const password = passwordInput.value;
            const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;

            if (regex.test(password)) {
                errorMsg.textContent = "";
                passwordInput.style.borderColor = "green";
            } else {
                errorMsg.textContent = "La contraseña no cumple con los requisitos.";
                passwordInput.style.borderColor = "red";
            }
        });

        // Validación al enviar
        form.addEventListener('submit', function (e) {
            const password = passwordInput.value;
            const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;

            if (!regex.test(password)) {
                e.preventDefault();
                errorMsg.textContent = "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.";
                passwordInput.focus();
            }
        });
    });

/* overlay */

function mostrarBuscador() {
  document.getElementById("buscador-overlay").classList.add("active");
}

function ocultarBuscador() {
  document.getElementById("buscador-overlay").classList.remove("active");
}

// BONUS: cerrar con tecla ESC
document.addEventListener('keydown', function (e) {
  if (e.key === "Escape") {
    ocultarBuscador();
  }
});

/* responsit */
 document.addEventListener("DOMContentLoaded", function () {
    const menu = document.getElementById("mobileMenu");
    const toggle = document.querySelector(".hamburger");
    const closeBtn = document.getElementById("closeMenu");

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

    // Cerrar al hacer clic fuera
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
  });