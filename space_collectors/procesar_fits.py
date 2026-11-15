
from pathlib import Path
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS

def obtener_observacion(ruta):
    ruta = Path(ruta)

    with fits.open(ruta) as archivo:
        imagen_hdu = archivo["IMAGE"]
        imagen = imagen_hdu.data

        if imagen is None or imagen.ndim != 2:
            raise ValueError("Se requiere una imagen FITS 2D")

        header = imagen_hdu.header
        primary = archivo[0].header

        alto, ancho = imagen.shape
        wcs = WCS(header).celestial

        ra, dec = wcs.pixel_to_world_values(
            (ancho - 1) / 2,
            (alto - 1) / 2
        )

        fecha = (
            header.get("DATE-AVG")
            or header.get("DATE-OBS")
            or primary.get("DATE-AVG")
            or primary.get("DATE-OBS")
        )

        if fecha:
            tiempo = Time(fecha, scale="utc")
        else:
            mjd = (
                header.get("MJD-AVG")
                or header.get("MJD-OBS")
                or primary.get("MJD-AVG")
                or primary.get("MJD-OBS")
            )
            if mjd is None:
                raise ValueError("Falta la fecha de observación")
            tiempo = Time(mjd, format="mjd", scale="utc")

        return {
            "archivo": ruta.name,
            "fecha": tiempo.isot,
            "ra": float(ra),
            "dec": float(dec),
            "ancho": ancho,
            "alto": alto
        }
