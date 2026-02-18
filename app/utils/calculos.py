# app/utils/calculos.py

def calcular_promedio_consumo(datos: list) -> float:
    """Calcula el promedio de una lista de consumos mensuales."""
    if not datos:
        return 0.0
    return round(sum(datos) / len(datos), 2)


def generar_alerta(consumo_actual: float, promedio: float) -> dict:
    """
    Compara el consumo actual contra el promedio histórico
    y retorna una alerta con nivel y mensaje.
    """
    if promedio == 0:
        return {"nivel": "SIN_DATOS", "mensaje": "No hay datos históricos suficientes."}

    porcentaje = ((consumo_actual - promedio) / promedio) * 100

    if porcentaje > 20:
        return {
            "nivel": "ALTO",
            "mensaje": f"Tu consumo está un {round(porcentaje, 1)}% por encima de tu promedio.",
            "porcentaje": round(porcentaje, 1)
        }
    elif porcentaje > 0:
        return {
            "nivel": "MEDIO",
            "mensaje": f"Tu consumo está un {round(porcentaje, 1)}% sobre tu promedio.",
            "porcentaje": round(porcentaje, 1)
        }
    else:
        return {
            "nivel": "NORMAL",
            "mensaje": f"Tu consumo está un {round(abs(porcentaje), 1)}% por debajo de tu promedio.",
            "porcentaje": round(porcentaje, 1)
        }


def calcular_tendencia(datos: list) -> str:
    """
    Determina si el consumo va en aumento, bajada o es estable
    comparando la primera y segunda mitad del historial.
    """
    if len(datos) < 2:
        return "SIN_DATOS"

    mitad = len(datos) // 2
    primera_mitad = sum(datos[:mitad]) / mitad
    segunda_mitad = sum(datos[mitad:]) / (len(datos) - mitad)

    diferencia = ((segunda_mitad - primera_mitad) / primera_mitad) * 100

    if diferencia > 10:
        return "SUBIENDO"
    elif diferencia < -10:
        return "BAJANDO"
    return "ESTABLE"