from astropy.io import fits
from astropy.visualization import simple_norm
from astropy.time import Time
from astropy.wcs import WCS
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Archivo FITS
ruta_fits = Path(
    "level2_2025W18_1B_0002_3D3_spx_l2b-v27-2026-196.fits"
)

# 2. Abrir archivo
with fits.open(ruta_fits) as archivo:

    archivo.info()

    # Extraer imagen cientifica
    imagen = archivo["IMAGE"].data.copy()

    # Obtener los metadatos
    header = archivo["IMAGE"].header
    primary = archivo[0].header

    # Leer coordenadas astronomicas de la imagen
    wcs = WCS(archivo["IMAGE"].header)

    # Calcular el centro de la imagen en pixeles
    alto, ancho = imagen.shape
    x = (ancho - 1) / 2
    y = (alto - 1) / 2

    # Convertir el centro a coordenadas RA y Dec
    ra, dec = wcs.pixel_to_world_values(x, y)

    print(f"RA: {ra:.6f} grados")
    print(f"Dec: {dec:.6f} grados")

    # Buscar fecha real de observacion
    fecha = (
        header.get("DATE-AVG")
        or header.get("DATE-OBS")
        or primary.get("DATE-AVG")
        or primary.get("DATE-OBS")
    )

    if fecha:
        tiempo = Time(fecha, format="isot", scale="utc")
    else:
        mjd = (
            header.get("MJD-AVG")
            or header.get("MJD-OBS")
            or primary.get("MJD-AVG")
            or primary.get("MJD-OBS")
        )
        if mjd is None:
            raise ValueError("No se encontró la fecha de observacion")

        tiempo = Time(mjd, format="mjd", scale="utc")

# 3. Crear timestamp para el nombre
timestamp = tiempo.strftime("%Y%m%d_%H%M%S")

# Nombre unico con fecha y nombre FITS original
nombre_png = f"{timestamp}_{ruta_fits.stem}.png"

print("Fecha de observacion:", tiempo.isot)
print("Archivo generado:", nombre_png)

# 4. Ajustar contraste
norm = simple_norm(
    imagen,
    stretch="asinh",
    percent=99.5
)

# 5. Crear figura sin margenes
fig = plt.figure(figsize=(8, 8), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])

ax.imshow(
    imagen,
    cmap="gray",
    origin="lower",
    norm=norm,
    aspect="auto"
)

# 6. Ocultar elementos
ax.set_axis_off()

# 7. Guardar con timestamp
plt.savefig(
    nombre_png,
    dpi=150,
    pad_inches=0
)

plt.close(fig)

print("Imagen guardada correctamente")