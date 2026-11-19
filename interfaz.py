def mostrar_bienvenida():
    print("========================================")
    print("   ¡BIENVENIDO AL JUEGO DEL BLACKJACK!  ")
    print("========================================")

def mostrar_estado_partida(jugador_manos, puntos_jugador, banca_manos):
    print("\n--- ESTADO DE LA PARTIDA ---")
    print(f"Tus cartas: {jugador_manos} (Puntuación: {puntos_jugador})")
    print(f"Carta visible de la banca: {banca_manos}")

def preguntar_accion():
    while True:
        accion = input("\n¿Qué deseas hacer? (1: Pedir otra carta, 2: Plantarse): ").strip()
        if accion in ["1", "2"]:
            return int(accion)
        print("Opción no válida. Por favor, introduce 1 o 2.")

def mostrar_resultado_final(resultado, puntos_jugador, puntos_banca):
    print("\n========================================")
    print("          RESULTADO FINAL               ")
    print("========================================")
    print(f"Tus puntos: {puntos_jugador} | Puntos de la banca: {puntos_banca}")
    print(f">> {resultado}")
    print("========================================")