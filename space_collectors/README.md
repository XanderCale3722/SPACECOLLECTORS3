# Space Collectors — NASA Space Apps Challenge 2026

Una plataforma web para visualizar señales cósmicas, espectros electromagnéticos
y cambios temporales en la radiación de cuerpos celestes.

---

## ¿Cómo ejecutar el proyecto?

### 1. Instala los requisitos
Abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
pip install flask
```

### 2. Ejecuta la aplicación
```bash
python app.py
```

### 3. Abre el navegador
Ve a: **http://localhost:5000**

---

## Estructura del proyecto

```
space_collectors/
│
├── app.py                  ← Aplicación principal (rutas/páginas)
├── requirements.txt        ← Dependencias de Python
│
├── templates/              ← Diseño HTML de cada página
│   ├── base.html           ← Plantilla base (navbar, footer)
│   ├── index.html          ← Página principal (hero + tarjetas)
│   ├── sky.html            ← Sky Explorer
│   ├── spectral.html       ← Spectral Explorer
│   ├── time.html           ← Time Explorer
│   ├── library.html        ← Space Library
│   └── about.html          ← About Us (equipo)
│
└── static/
    ├── css/
    │   └── style.css       ← Todos los estilos visuales
    ├── js/
    │   └── main.js         ← Interactividad (estrellas, animaciones)
    └── img/                ← (Crear esta carpeta) Imágenes del proyecto
```

---

## Colaboración grupal — GitHub (Recomendado)

GitHub es la mejor opción para trabajar en equipo porque:
- Todos pueden editar al mismo tiempo sin pisar el trabajo del otro
- Guarda un historial de todos los cambios
- Los jueces de NASA Space Apps pueden ver el repositorio

### Pasos para configurar GitHub:

**Una persona del equipo (admin):**
1. Crea una cuenta en [github.com](https://github.com)
2. Crea un repositorio nuevo (New repository) → nombre: `space-collectors`
3. Sube el proyecto:
   ```bash
   git init
   git add .
   git commit -m "Primer commit - maqueta inicial"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/space-collectors.git
   git push -u origin main
   ```

**Los otros 5 integrantes:**
1. Crean su cuenta en GitHub
2. El admin los invita en: Settings → Collaborators → Add people
3. Cada uno clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/space-collectors.git
   ```

**Para subir cambios:**
```bash
git add .
git commit -m "Descripción de lo que cambiaste"
git push
```

**Para bajar cambios de los demás:**
```bash
git pull
```

---

## Páginas del proyecto

| Ruta URL              | Archivo            | Sección               |
|-----------------------|--------------------|-----------------------|
| `/`                   | `index.html`       | Hero + Navegación     |
| `/sky-explorer`       | `sky.html`         | Imágenes y coordenadas|
| `/spectral-explorer`  | `spectral.html`    | Espectros             |
| `/time-explorer`      | `time.html`        | Cambios temporales    |
| `/space-library`      | `library.html`     | Biblioteca            |
| `/about`              | `about.html`       | Nuestro equipo        |

---

## ¿Cómo añadir los datos cuando lleguen?

Busca los comentarios en el HTML que dicen `<!-- AQUÍ VAN... -->` o `<!-- AÑADIR ... AQUÍ -->`.
Cada placeholder tiene instrucciones sobre qué tipo de contenido va ahí.

Para imágenes, guárdalas en `static/img/` y úsalas así en el HTML:
```html
<img src="{{ url_for('static', filename='img/tu_imagen.jpg') }}" alt="Descripción">
```

---

*Space Collectors Team — NASA Space Apps Challenge 2026*
