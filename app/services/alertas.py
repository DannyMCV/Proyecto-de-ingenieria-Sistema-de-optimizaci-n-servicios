# app/services/alertas.py

# Límites fijos de consumo eléctrico mensual (kWh) definidos por el sistema
LIMITES_ELECTRICIDAD = {
    "NORMAL": 150,   # Hasta 150 kWh → consumo eficiente
    "MEDIO": 300,    # Entre 150 y 300 kWh → consumo moderado
    "ALTO": 500,     # Entre 300 y 500 kWh → consumo elevado
                     # Más de 500 kWh → consumo crítico
}

def generar_alerta_electricidad(consumo_kwh: float) -> dict:
    """
    Evalúa el consumo eléctrico mensual en kWh y retorna
    una alerta con nivel, mensaje y sugerencia.
    """
    if consumo_kwh < 0:
        return {
            "nivel": "ERROR",
            "mensaje": "El consumo no puede ser negativo.",
            "sugerencia": "Verifica los datos ingresados."
        }

    if consumo_kwh <= LIMITES_ELECTRICIDAD["NORMAL"]:
        return {
            "nivel": "NORMAL",
            "mensaje": f"Tu consumo de {consumo_kwh} kWh es eficiente.",
            "sugerencia": "¡Sigue así! Estás dentro del rango óptimo."
        }

    elif consumo_kwh <= LIMITES_ELECTRICIDAD["MEDIO"]:
        return {
            "nivel": "MEDIO",
            "mensaje": f"Tu consumo de {consumo_kwh} kWh es moderado.",
            "sugerencia": "Revisa el uso de electrodomésticos en horas pico."
        }

    elif consumo_kwh <= LIMITES_ELECTRICIDAD["ALTO"]:
        return {
            "nivel": "ALTO",
            "mensaje": f"Tu consumo de {consumo_kwh} kWh es elevado.",
            "sugerencia": "Considera revisar aires acondicionados y calefacción."
        }

    else:
        return {
            "nivel": "CRITICO",
            "mensaje": f"Tu consumo de {consumo_kwh} kWh es crítico.",
            "sugerencia": "Se recomienda una auditoría energética urgente."
        }
