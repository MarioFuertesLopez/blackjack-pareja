from interfaz import mostrar_bienvenida, mostrar_estado_partida, preguntar_accion, mostrar_resultado_final
# Nota: Importarás las funciones de lógica cuando el Alumno A las tenga listas en juego.py y cartas.py
# from juego import iniciar_partida, calcular_puntos, turno_banca

def main():
    mostrar_bienvenida()
    
    # Simulación del flujo de la partida (se conectará con la lógica de juego.py)
    print("\n[INFO] Esperando a la integración con la lógica de cartas y juego...")
    
    # Ejemplo de estructura de bucle que utilizará la interfaz:
    # juego_activo = True
    # while juego_activo:
    #     accion = preguntar_accion()
    #     if accion == 1:
    #         # Lógica de pedir carta
    #         pass
    #     else:
    #         # Lógica de plantarse y turno de la banca
    #         break

if __name__ == "__main__":
    main()