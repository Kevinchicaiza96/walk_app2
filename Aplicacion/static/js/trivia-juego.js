const preguntas = [
  {
    id: 1, 
    categoria: "rutas", 
    titulo: "¿Cuál es una de las rutas de senderismo más populares en Popayán?", 
    opcionA: "Cerro de las Tres Cruces", 
    opcionB: "Cañón del Chicamocha", 
    opcionC: "Parque Nacional El Cocuy", 
    opcionD: "Nevado del Ruiz", 
    correcta: "a",
  },
  { 
    id: 2, 
    categoria: "rutas", 
    titulo: "¿Qué reserva natural cercana a Popayán es ideal para senderismo y observación de fauna?", 
    opcionA: "Reserva Natural La Planada", 
    opcionB: "Reserva Natural El Danubio", 
    opcionC: "Parque Nacional Puracé", 
    opcionD: "Santuario de Fauna y Flora Otún Quimbaya", 
    correcta: "c" 
  },
  { 
    id: 3, 
    categoria: "rutas", 
    titulo: "¿Cuál de estos lugares en Popayán es ideal para una caminata con vistas panorámicas de la ciudad?", 
    opcionA: "Pueblito Patojo", 
    opcionB: "Morro de Tulcán", 
    opcionC: "Parque Caldas", 
    opcionD: "Puente del Humilladero", 
    correcta: "b" 
  },
  { 
    id: 4, 
    categoria: "rutas", 
    titulo: "¿Qué atractivo natural en las afueras de Popayán cuenta con senderos y cascadas?", 
    opcionA: "Cascada de Fin del Mundo", 
    opcionB: "Salto de Bordones", 
    opcionC: "Cascadas de Julumito", 
    opcionD: "Laguna de La Cocha", 
    correcta: "c" 
  },
  { 
    id: 5, 
    categoria: "rutas", 
    titulo: "¿Cómo se llama el sendero que lleva a las aguas termales de Coconuco, cerca de Popayán?", 
    opcionA: "Sendero del Azufral", 
    opcionB: "Ruta del Volcán", 
    opcionC: "Camino Real", 
    opcionD: "Sendero a Termales de Coconuco", 
    correcta: "d" 
  },
  { 
    id: 6, 
    categoria: "equipo", 
    titulo: "¿Qué tipo de calzado es el más recomendado para hacer senderismo en terrenos irregulares?", 
    opcionA: "Sandalias", 
    opcionB: "Zapatillas deportivas", 
    opcionC: "Botas de senderismo", 
    opcionD: "Zapatos casuales", 
    correcta: "c" 
  },
  { 
    id: 7, 
    categoria: "equipo", 
    titulo: "¿Cuál es un elemento esencial para mantenerse hidratado durante una caminata larga?", 
    opcionA: "Bebidas gaseosas", 
    opcionB: "Cantimplora o botella de agua", 
    opcionC: "Refrescos azucarados", 
    opcionD: "Café caliente", 
    correcta: "b" 
  },
  { 
    id: 8, 
    categoria: "equipo", 
    titulo: "¿Qué objeto es fundamental para la orientación en rutas de senderismo desconocidas?", 
    opcionA: "Brújula y mapa", 
    opcionB: "Reloj de pulsera", 
    opcionC: "Gafas de sol", 
    opcionD: "Linterna", 
    correcta: "a" 
  },
  { 
    id: 9, 
    categoria: "equipo", 
    titulo: "¿Por qué es importante llevar una linterna en una ruta de senderismo?", 
    opcionA: "Para tomar mejores fotos", 
    opcionB: "Para iluminar en caso de que se haga de noche", 
    opcionC: "Para espantar animales salvajes", 
    opcionD: "Para hacer señales de luz a otros senderistas", 
    correcta: "b" 
  },
  { 
    id: 10, 
    categoria: "equipo", 
    titulo: "¿Qué prenda de vestir es ideal para protegerse del frío en caminatas de altura?", 
    opcionA: "Chaqueta impermeable y térmica", 
    opcionB: "Camiseta de algodón", 
    opcionC: "Pantalón corto y ligero", 
    opcionD: "Bufanda de lana", 
    correcta: "a" 
  },
  { 
    id: 11, 
    categoria: "seguridad", 
    titulo: "¿Qué medida de seguridad es recomendable al visitar el centro histórico de Popayán?", 
    opcionA: "Evitar llevar objetos de valor a la vista", 
    opcionB: "No visitar en horarios nocturnos", 
    opcionC: "Permanecer en grupos y zonas concurridas", 
    opcionD: "Todas las anteriores", 
    correcta: "d" 
  },
  { 
    id: 12, 
    categoria: "seguridad", 
    titulo: "¿Qué parque nacional se encuentra cerca de Popayán?", 
    opcionA: "Parque Nacional Natural Puracé", 
    opcionB: "Parque Nacional Tayrona", 
    opcionC: "Parque Nacional Natural Los Nevados", 
    opcionD: "Parque Nacional Natural Gorgona", 
    correcta: "a" 
  },
  { 
    id: 13, 
    categoria: "seguridad", 
    titulo: "¿Cuál es uno de los sitios turísticos más emblemáticos de Popayán?", 
    opcionA: "El Morro de Tulcán", 
    opcionB: "El Parque Arqueológico de San Agustín", 
    opcionC: "El Desierto de la Tatacoa", 
    opcionD: "El Santuario de Las Lajas", 
    correcta: "a" 
  },
  { 
    id: 14, 
    categoria: "seguridad", 
    titulo: "¿Qué es el Pueblito Patojo en Popayán?", 
    opcionA: "Un Restaurante Típico", 
    opcionB: "Una Réplica a Escala del Centro Histórico", 
    opcionC: "Un Centro Comercial", 
    opcionD: "Una Feria Artesanal", 
    correcta: "b" 
  },
  { 
    id: 15, 
    categoria: "seguridad", 
    titulo: "¿Cuál es el nombre del parque donde se puede observar el nacimiento del río Magdalena?", 
    opcionA: "Parque Puracé", 
    opcionB: "Parque Los Farallones", 
    opcionC: "Parque Los Nevados", 
    opcionD: "Parque La Cocha", 
    correcta: "a" 
  },
  { 
    id: 16, 
    categoria: "flora-fauna", 
    titulo: "¿Cuál de estos árboles es característico de la región de Popayán?", 
    opcionA: "Ceiba", 
    opcionB: "Guayacán", 
    opcionC: "Nogal", 
    opcionD: "Pino", 
    correcta: "b" 
  },
  { 
    id: 17, 
    categoria: "flora-fauna", 
    titulo: "¿Qué animal emblemático se puede encontrar en el Parque Nacional Natural Puracé?", 
    opcionA: "El Cóndor de los Andes", 
    opcionB: "El Oso de Anteojos", 
    opcionC: "El Jaguar", 
    opcionD: "El Tapir", 
    correcta: "a" 
  },
  { 
    id: 18, 
    categoria: "flora-fauna", 
    titulo: "¿Cuál de estas especies de orquídeas es representativa de la flora de la región?", 
    opcionA: "Cattleya trianae", 
    opcionB: "Vanilla planifolia", 
    opcionC: "Oncidium", 
    opcionD: "Dendrobium", 
    correcta: "a" 
  },
  { 
    id: 19, 
    categoria: "flora-fauna", 
    titulo: "¿Qué mamífero se encuentra comúnmente en las montañas del Cauca?", 
    opcionA: "Armadillo", 
    opcionB: "Venado de cola blanca", 
    opcionC: "Perezoso", 
    opcionD: "Zorro gris", 
    correcta: "b" 
  },
  { 
    id: 20, 
    categoria: "flora-fauna", 
    titulo: "¿Cuál de estos cuerpos de agua es el hábitat de diversas especies de anfibios en la región de Popayán?", 
    opcionA: "Laguna de la Magdalena", 
    opcionB: "Laguna de Sonso", 
    opcionC: "Laguna de Guatavita", 
    opcionD: "Ciénaga Grande", 
    correcta: "a" 
  },
  { 
    id: 21, 
    categoria: "tecnicas", 
    titulo: "¿Cuál es el tipo de calzado más adecuado para practicar senderismo?", 
    opcionA: "Zapatillas deportivas", 
    opcionB: "Botas de senderismo", 
    opcionC: "Sandalias de montaña", 
    opcionD: "Zapatos casuales", 
    correcta: "b" 
  },
  { 
    id: 22, 
    categoria: "tecnicas", 
    titulo: "¿Cuál es la mejor manera de distribuir el peso en una mochila de senderismo?", 
    opcionA: "Objetos pesados arriba y alejados de la espalda", 
    opcionB: "Objetos pesados cerca de la espalda y en el centro", 
    opcionC: "Objetos ligeros abajo y pesados arriba", 
    opcionD: "Distribuir el peso sin orden específico", 
    correcta: "b" 
  },
  { 
    id: 23, 
    categoria: "tecnicas", 
    titulo: "¿Qué debe incluir un botiquín básico de primeros auxilios para senderismo?", 
    opcionA: "Solo vendas y alcohol", 
    opcionB: "Gasas, vendas, desinfectante, analgésicos y curitas", 
    opcionC: "Un silbato y una manta térmica", 
    opcionD: "Solo agua oxigenada y algodón", 
    correcta: "b" 
  },
  {
    id: 24,
    categoria: "tecnicas",
    titulo: "¿Mejor forma de cruzar un río en caminata?",
    opcionA: "Cruzar rápido para no mojarse",
    opcionB: "Buscar el tramo angosto y cruzar con calma",
    opcionC: "Descalzo y correr para evitar resbalar",
    opcionD: "Usar un bastón y cruzar despacio",
    correcta: "d"
  },
  {
    id: 25,
    categoria: "tecnicas",
    titulo: "¿Qué hacer si te pierdes en un sendero?",
    opcionA: "Caminar sin rumbo hasta salir",
    opcionB: "Gritar fuerte pidiendo ayuda",
    opcionC: "Quedarse en un lugar seguro y pedir auxilio",
    opcionD: "Regresar aunque no recuerdes la ruta",
    correcta: "c"
  },
  { 
    id: 26, 
    categoria: "lugares", 
    titulo: "¿Cuál es uno de los destinos más populares para hacer senderismo cerca de Popayán?", 
    opcionA: "Parque Nacional Natural Puracé", 
    opcionB: "Cañón del Chicamocha", 
    opcionC: "Serranía de la Macarena", 
    opcionD: "Desierto de la Tatacoa", 
    correcta: "a" 
  },
  { 
    id: 27, 
    categoria: "lugares", 
    titulo: "¿Qué volcán cercano a Popayán es un destino popular para senderistas?", 
    opcionA: "Volcán Machín", 
    opcionB: "Volcán Nevado del Tolima", 
    opcionC: "Volcán Puracé", 
    opcionD: "Volcán Galeras", 
    correcta: "c" 
  },
  { 
    id: 28, 
    categoria: "lugares", 
    titulo: "¿Qué atractivo natural en el Parque Puracé es ideal para una caminata?", 
    opcionA: "Cascada de Juanambú", 
    opcionB: "Laguna de Buey", 
    opcionC: "Cueva de los Guácharos", 
    opcionD: "Salto de Bordones", 
    correcta: "b" 
  },
  { 
    id: 29, 
    categoria: "lugares", 
    titulo: "¿Qué reserva natural cerca de Popayán es un buen lugar para caminatas ecológicas?", 
    opcionA: "Reserva Natural El Danubio", 
    opcionB: "Cañón del Güejar", 
    opcionC: "Parque Nacional Tayrona", 
    opcionD: "Santuario de Iguaque", 
    correcta: "a" 
  },
  { 
    id: 30, 
    categoria: "lugares", 
    titulo: "¿Qué sitio natural ofrece senderos y aguas termales en el Cauca?", 
    opcionA: "Cueva del Esplendor", 
    opcionB: "Termales de San Juan", 
    opcionC: "Cascadas del Fin del Mundo", 
    opcionD: "Santuario de Las Lajas", 
    correcta: "b" 
  }
];

const txtPuntaje = document.querySelector("#puntos");
const nombre = document.querySelector("#nombre");

nombre.innerHTML = localStorage.getItem("nombre") || "Invitado";

let numPreguntaActual = 0;
let puntajeTotal = parseInt(localStorage.getItem("puntaje-total")) || 0;
txtPuntaje.innerHTML = puntajeTotal;

const categoriaActual = localStorage.getItem("categoria-actual");
const preguntasCategoria = preguntas.filter(p => p.categoria === categoriaActual);

// Validación por si no hay preguntas en la categoría
if (!categoriaActual || preguntasCategoria.length === 0) {
    alert("Categoría inválida o sin preguntas disponibles.");
    location.href = "/trivia/menu/";
}

function cargarSiguientePregunta(num) {
    if (!preguntasCategoria[num]) return;

    const numPregunta = document.querySelector("#num-pregunta");
    const txtPregunta = document.querySelector("#txt-pregunta");
    const opcionA = document.querySelector("#a");
    const opcionB = document.querySelector("#b");
    const opcionC = document.querySelector("#c");
    const opcionD = document.querySelector("#d");

    numPregunta.innerHTML = num + 1;
    txtPregunta.innerHTML = preguntasCategoria[num].titulo;
    opcionA.innerHTML = preguntasCategoria[num].opcionA;
    opcionB.innerHTML = preguntasCategoria[num].opcionB;
    opcionC.innerHTML = preguntasCategoria[num].opcionC;
    opcionD.innerHTML = preguntasCategoria[num].opcionD;

    const botonesRespuesta = document.querySelectorAll(".opcion");
    botonesRespuesta.forEach(opcion => {
        opcion.onclick = null;
        opcion.classList.remove("correcta", "incorrecta", "no-events");
        opcion.addEventListener("click", agregarEventListenerBoton);
    });

    txtPuntaje.classList.remove("efecto");
}

function agregarEventListenerBoton(e) {
    const respuestaUsuario = e.currentTarget.id;
    const correcta = preguntasCategoria[numPreguntaActual].correcta;

    if (respuestaUsuario === correcta) {
        e.currentTarget.classList.add("correcta");
        puntajeTotal += 100;
        txtPuntaje.innerHTML = puntajeTotal;
        localStorage.setItem("puntaje-total", puntajeTotal);
        txtPuntaje.classList.add("efecto");
    } else {
        e.currentTarget.classList.add("incorrecta");
        const correctaBtn = document.querySelector("#" + correcta);
        correctaBtn.classList.add("correcta");
    }

    document.querySelectorAll(".opcion").forEach(opcion => {
        opcion.classList.add("no-events");
    });
}

cargarSiguientePregunta(numPreguntaActual);

const btnSiguiente = document.querySelector("#siguiente");
btnSiguiente.addEventListener("click", () => {
    numPreguntaActual++;
    if (numPreguntaActual < preguntasCategoria.length) {
        cargarSiguientePregunta(numPreguntaActual);
    } else {
        const categoriasJugadasLS = JSON.parse(localStorage.getItem("categorias-jugadas") || "[]");
        if (categoriasJugadasLS.length < 6) {
            location.href = "/trivia/menu/";  // volver a elegir categoría
        } else {
            location.href = "/trivia/final/";  // juego terminado
        }
    }
});
