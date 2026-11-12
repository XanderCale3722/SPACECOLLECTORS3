// ============================================================
//  SPACE COLLECTORS — JavaScript principal
//  NASA Space Apps Challenge 2026
// ============================================================
//
//  Este archivo controla:
//   1. Las estrellas animadas del fondo
//   2. La animación de las tarjetas al hacer scroll
//   3. El scroll suave al botón "Explorar secciones"
//   4. El menú hamburguesa en móvil
//   5. El efecto de la navbar al hacer scroll
//


// ===========================================================
//  1. ESTRELLAS ANIMADAS
//  Creamos puntos blancos aleatorios en el fondo para simular
//  el cielo estrellado.
// ===========================================================

function crearEstrellas() {
    const fondo = document.getElementById('estrellas');
    if (!fondo) return; // Si el elemento no existe, salimos

    const CANTIDAD = 200; // Número total de estrellas

    for (let i = 0; i < CANTIDAD; i++) {
        const estrella = document.createElement('div');
        estrella.classList.add('estrella');

        // Posición aleatoria en la pantalla (en porcentaje)
        estrella.style.left = Math.random() * 100 + '%';
        estrella.style.top  = Math.random() * 100 + '%';

        // Tamaño aleatorio: entre 0.5px y 3px
        const tamanio = (Math.random() * 2.5 + 0.5).toFixed(1) + 'px';
        estrella.style.width  = tamanio;
        estrella.style.height = tamanio;

        // Duración y retraso aleatorio para que no titilen todas juntas
        estrella.style.setProperty('--dur',   (Math.random() * 3 + 2).toFixed(1) + 's');
        estrella.style.setProperty('--delay', (Math.random() * 5).toFixed(1) + 's');

        // Algunas estrellas son más brillantes que otras
        estrella.style.opacity = (Math.random() * 0.5 + 0.3).toFixed(2);

        fondo.appendChild(estrella);
    }
}

// Llamamos la función inmediatamente
crearEstrellas();


// ===========================================================
//  2. ANIMACIONES AL HACER SCROLL (Intersection Observer)
//
//  El Intersection Observer es una API del navegador que
//  detecta cuando un elemento HTML entra en la pantalla.
//  Cuando entra, le añadimos la clase 'visible' para que
//  aparezca con animación.
// ===========================================================

function activarAnimacionesScroll() {
    // Configuración del observador
    const opciones = {
        threshold: 0.12,        // El elemento debe ser 12% visible para activarse
        rootMargin: '0px 0px -20px 0px'  // Un poco antes de que llegue al borde
    };

    const observador = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // El elemento es visible → hacerlo aparecer
                entry.target.classList.add('visible');
                // Dejamos de observarlo (ya no necesita la animación de entrada)
                observador.unobserve(entry.target);
            }
        });
    }, opciones);

    // Observar las TARJETAS con animación escalonada
    // (cada tarjeta aparece un poco después de la anterior)
    const tarjetas = document.querySelectorAll('.tarjeta');
    tarjetas.forEach((tarjeta, indice) => {
        tarjeta.style.transitionDelay = (indice * 0.08) + 's'; // 80ms entre cada tarjeta
        observador.observe(tarjeta);
    });

    // Observar elementos con la clase .animar (textos, cajas, etc.)
    const elementosAnimados = document.querySelectorAll('.animar');
    elementosAnimados.forEach((elemento, indice) => {
        elemento.style.transitionDelay = (indice * 0.06) + 's';
        observador.observe(elemento);
    });
}

// Iniciamos las animaciones cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    activarAnimacionesScroll();
});


// ===========================================================
//  3. SCROLL SUAVE AL BOTÓN "EXPLORAR SECCIONES"
//  El botón del hero baja suavemente a la sección de tarjetas
// ===========================================================

const btnExplorar = document.getElementById('btnExplorar');

if (btnExplorar) {
    btnExplorar.addEventListener('click', (evento) => {
        evento.preventDefault(); // Evitamos el salto brusco de un link normal

        const seccionDestino = document.getElementById('secciones');
        if (seccionDestino) {
            seccionDestino.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
}


// ===========================================================
//  4. MENÚ HAMBURGUESA (MÓVIL)
//  En pantallas pequeñas, el botón ☰ abre/cierra el menú
// ===========================================================

const botonMenu  = document.getElementById('navToggle');
const linksMenu  = document.getElementById('navLinks');

if (botonMenu && linksMenu) {

    // Al hacer clic en el botón hamburguesa
    botonMenu.addEventListener('click', () => {
        const estaAbierto = linksMenu.classList.toggle('abierto');

        // Cambiamos el ícono: ☰ (bars) ↔ ✕ (xmark)
        const icono = botonMenu.querySelector('i');
        if (estaAbierto) {
            icono.classList.replace('fa-bars', 'fa-xmark');
        } else {
            icono.classList.replace('fa-xmark', 'fa-bars');
        }
    });

    // Cerrar el menú al hacer clic en cualquier enlace
    linksMenu.querySelectorAll('.nav-link').forEach(enlace => {
        enlace.addEventListener('click', () => {
            linksMenu.classList.remove('abierto');
            const icono = botonMenu.querySelector('i');
            icono.classList.replace('fa-xmark', 'fa-bars');
        });
    });

    // Cerrar el menú si el usuario hace clic fuera de él
    document.addEventListener('click', (evento) => {
        const dentroDeNavbar = evento.target.closest('.navbar');
        if (!dentroDeNavbar && linksMenu.classList.contains('abierto')) {
            linksMenu.classList.remove('abierto');
            const icono = botonMenu.querySelector('i');
            icono.classList.replace('fa-xmark', 'fa-bars');
        }
    });
}


// ===========================================================
//  5. EFECTO DE LA NAVBAR AL HACER SCROLL
//  La barra de navegación se vuelve más sólida al bajar
// ===========================================================

window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    if (window.scrollY > 60) {
        // Usuario bajó: navbar más sólida y con sombra
        navbar.style.background  = 'rgba(6, 11, 24, 0.98)';
        navbar.style.boxShadow   = '0 4px 24px rgba(0, 0, 0, 0.5)';
    } else {
        // Usuario arriba: navbar más transparente
        navbar.style.background  = 'rgba(6, 11, 24, 0.85)';
        navbar.style.boxShadow   = 'none';
    }
}, { passive: true }); // passive: true mejora el rendimiento del scroll
