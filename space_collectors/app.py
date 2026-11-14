# ==============================================
#  DESKTOOOOOP SPACE COLLECTORS weeeb prueba de editado — NASA Space Apps 2026
#  Archivo principal de la aplicación web
# ==============================================
#
#  Para ejecutar el proyecto:
#    1. Abre tu terminal en esta carpeta
#    2. Instala Flask:   pip install flask
#    3. Ejecuta:         python app.py
#    4. Abre el navegador en: http://localhost:5000
#

from flask import Flask, render_template

 #esto es las librerias necesarias solo para iniciar la pagina y que no tarde tanto por el render   

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Creamos la aplicación Flask
# Flask es el motor que hace funcionar nuestra página web
app = Flask(__name__)


# ---- RUTAS (PÁGINAS) ------------------------------------------------
# Cada función de abajo corresponde a una página de la web.
# El @app.route('/ruta') le dice a Flask qué URL muestra esa página.
# render_template('archivo.html') carga el diseño HTML de la página.
# ---------------------------------------------------------------------

@app.route('/')
def inicio():
    """Página principal: hero + tarjetas de navegación."""
    return render_template('index.html')


@app.route('/sky-explorer')
def sky_explorer():
    """Sky Explorer — Imágenes y coordenadas de objetos espaciales."""
    return render_template('sky.html')


@app.route('/spectral-explorer')
def spectral_explorer():
    """Spectral Explorer — Datos de espectros y ondas electromagnéticas."""
    return render_template('spectral.html')


@app.route('/time-explorer')
def time_explorer():
    """Time Explorer — Cambios temporales en las señales espaciales."""
    return render_template('time.html')


@app.route('/space-library')
def space_library():
    """Space Library — Biblioteca de recursos y documentación."""
    return render_template('library.html')


@app.route('/about')
def about():
    """About Us — Información sobre el equipo."""
    return render_template('about.html')


# ---- INICIO DEL SERVIDOR -------------------------------------------
if __name__ == '__main__':
    # debug=True: recarga automática al guardar cambios + muestra errores
    # Cambia a debug=False cuando subas el proyecto a producción
    app.run(debug=True)
