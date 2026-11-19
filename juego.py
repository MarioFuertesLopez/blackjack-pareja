def calcular_puntuacion(mano):
    """Calcula los puntos totales de una mano ajustando el valor de los Ases (11 o 1)."""
    puntos = 0
    ases = 0
    
    for valor, _ in mano:
        if valor in ["J", "Q", "K"]:
            puntos += 10
        elif valor == "A":
            puntos += 11
            ases += 1
        else:
            puntos += int(valor)
            
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
        
    return puntos

def es_blackjack(mano):
    """Devuelve True si la mano tiene 21 puntos con exactamente 2 cartas."""
    return len(mano) == 2 and calcular_puntuacion(mano) == 21

def se_ha_pasado(mano):
    """Devuelve True si la puntuación supera 21."""
    return calcular_puntuacion(mano) > 21

def determinar_ganador(mano_jugador, mano_banca):
    """Compara las manos finales y devuelve el resultado de la partida."""
    pts_jugador = calcular_puntuacion(mano_jugador)
    pts_banca = calcular_puntuacion(mano_banca)
    
    if pts_jugador > 21:
        return "Has perdido: te has pasado de 21."
    elif pts_banca > 21:
        return "¡Has ganado! La banca se ha pasado de 21."
    elif es_blackjack(mano_jugador) and not es_blackjack(mano_banca):
        return "¡Blackjack! Has ganado."
    elif pts_jugador > pts_banca:
        return "¡Has ganado por puntuación!"
    elif pts_jugador < pts_banca:
        return "Has perdido: la banca tiene mayor puntuación."
    else:
        return "Empate."