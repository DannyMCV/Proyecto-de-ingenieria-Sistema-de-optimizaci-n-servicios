# app/models/consumo.py
# Modelo que representa un registro de consumo mensual del usuario

class Consumo:
    def __init__(self, usuario_id: int, mes: str, cantidad: float, tipo: str):
        self.usuario_id = usuario_id
        self.mes = mes          # Ej: "2025-01"
        self.cantidad = cantidad # Ej: 350.5 (kWh, litros, etc.)
        self.tipo = tipo        # Ej: "electricidad", "agua", "gas"

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "mes": self.mes,
            "cantidad": self.cantidad,
            "tipo": self.tipo
        }