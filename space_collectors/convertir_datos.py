"""
Convierte los archivos *headers.txt (uno por imagen) en static/data/sky_data.json

Uso:
    python convertir_datos.py RUTA_A_TUS_CARPETAS

Busca dentro de todas las subcarpetas, toma hasta MAX_IMAGENES archivos,
copia cada PNG a static/img/sky y guarda el JSON que lee sky.html.
"""
import json
import re
import shutil
import sys
from pathlib import Path

MAX_IMAGENES = 50
SALIDA = Path("static/data/sky_data.json")
CARPETA_IMG = Path("static/img/sky")      # aquí se copian las fotos PNG solas


def bloque_imagen(texto):
    """Devuelve solo el bloque 'HDU 1: IMAGE' (las claves se repiten en otros HDU)."""
    partes = re.split(r"===== HDU \d+:", texto)
    for p in partes:
        if p.lstrip().startswith("IMAGE"):
            return p
    return ""


def valor(bloque, clave):
    patron = rf"^(?:HIERARCH\s+)?{re.escape(clave)}\s*=\s*('[^']*'|[^/\n]+)"
    m = re.search(patron, bloque, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip("'").strip()


def numero(bloque, clave):
    v = valor(bloque, clave)
    return float(v) if v is not None else None


def terna(bloque, sufijos):
    return [numero(bloque, s) for s in sufijos]


def procesar(ruta):
    b = bloque_imagen(ruta.read_text(encoding="utf-8", errors="ignore"))
    if not b:
        return None
    base = re.sub(r"[_\-.]*headers?\.txt$", "", ruta.name, flags=re.I)
    # la foto PNG vive en la misma carpeta que el headers.txt
    pngs = sorted(ruta.parent.glob("*.png"))
    imagen = pngs[0].name if pngs else base + "_01_IMAGE.png"
    if pngs:
        CARPETA_IMG.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pngs[0], CARPETA_IMG / imagen)
    return {
        "id": base,
        "nombre": valor(b, "SPS_TARGET") or base,
        "imagen": imagen,
        "obsid": valor(b, "OBSID"),
        "detector": valor(b, "DETECTOR"),
        "fecha_obs": valor(b, "DATE-OBS"),
        "unidad": valor(b, "BUNIT"),
        "ra": numero(b, "CRVAL1"),
        "dec": numero(b, "CRVAL2"),
        "inicio": {
            "fecha": valor(b, "DATE-BEG"),
            "xyz": terna(b, ["X_SC_START", "Y_SC_START", "Z_SC_START"]),
            "vel": terna(b, ["VX_SC_START", "VY_SC_START", "VZ_SC_START"]),
        },
        "mitad": {
            "fecha": valor(b, "DATE-AVG"),
            "xyz": terna(b, ["X_SC", "Y_SC", "Z_SC"]),
            "vel": terna(b, ["VX_SC", "VY_SC", "VZ_SC"]),
        },
        "final": {
            "fecha": valor(b, "DATE-END"),
            "xyz": terna(b, ["X_SC_END", "Y_SC_END", "Z_SC_END"]),
            "vel": terna(b, ["VX_SC_END", "VY_SC_END", "VZ_SC_END"]),
        },
    }


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    archivos = sorted(carpeta.rglob("*headers*.txt"))[:MAX_IMAGENES]
    datos = [d for d in (procesar(a) for a in archivos) if d]
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Listo: {len(datos)} observaciones guardadas en {SALIDA}")


if __name__ == "__main__":
    main()
