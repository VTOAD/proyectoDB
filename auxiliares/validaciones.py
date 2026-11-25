from datetime import date, time

def texto_obligatorio(valor, nombre):
    texto = valor.strip()
    if not texto:
        raise ValueError(f"Ingresa {nombre}.")
    return texto


def entero_no_negativo(valor, nombre):
    try:
        numero = int(valor)
    except ValueError:
        raise ValueError(f"{nombre} debe ser un número entero.") from None
    if numero < 0:
        raise ValueError(f"{nombre} debe ser mayor o igual a cero.")
    if numero > 2**63 - 1:
        raise ValueError(f"{nombre} supera el máximo permitido.")
    return numero


def convertir_fecha(valor, nombre):
    try:
        return date.fromisoformat(valor)
    except ValueError:
        raise ValueError(f"{nombre} debe tener el formato AAAA-MM-DD.") from None


def convertir_hora(valor, nombre):
    try:
        return time.fromisoformat(valor)
    except ValueError:
        raise ValueError(f"{nombre} debe tener el formato HH:MM.") from None
