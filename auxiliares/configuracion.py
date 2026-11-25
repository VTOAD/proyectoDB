from pathlib import Path
from dotenv import dotenv_values

RAIZ = Path(__file__).resolve().parents[1]
configuracion = dotenv_values(RAIZ / ".env")
RUTA_BASE_DATOS = RAIZ / (configuracion.get("RUTA_BASE_DATOS") or "taller.sqlite3")
