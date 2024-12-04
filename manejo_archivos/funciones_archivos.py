import os

def leer_puntaje(puntajes_partida: dict, ganador: str):
    ruta_absoluta = os.path.join(os.path.dirname(__file__), 'partidas.txt')
    
    with open(ruta_absoluta, "r") as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split(": ")
            puntajes_partida[clave] = int(valor)

    if ganador in puntajes_partida:
        puntajes_partida[ganador] += 1
    else:
        print(f"Error: '{ganador}' no es una clave válida.")

    with open(ruta_absoluta, "w") as archivo:
        for clave, valor in puntajes_partida.items():
            archivo.write(f"{clave}: {valor}\n")

    print("Puntajes actualizados:")
    for clave, valor in puntajes_partida.items():
        print(f"{clave}: {valor}")


def leer_partidas():
    ruta_absoluta = os.path.join(os.path.dirname(__file__), 'partidas.txt')
    puntajes_partida = {}
    
    with open(ruta_absoluta, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            clave, valor = linea.strip().split(": ")
            puntajes_partida[clave] = int(valor)
    
    return puntajes_partida