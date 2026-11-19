import random

def crear_baraja():
    """Crea una baraja estándar de 52 cartas y la mezcla."""
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    baraja = [(valor, palo) for palo in palos for valor in valores]
    random.shuffle(baraja)
    return baraja

def repartir_carta(baraja):
    """Saca y devuelve la última carta de la baraja."""
    if len(baraja) == 0:
        baraja.extend(crear_baraja())
    return baraja.pop()

def formatear_carta(carta):
    """Devuelve una representación legible de la carta, ej: 'A de Picas'."""
    return f"{carta[0]} de {carta[1]}"