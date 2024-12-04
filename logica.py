from Clases.carta import *
import random
import copy

mazo = (Carta(1, "espada"), Carta(1, "basto"), Carta(7, "espada"), Carta(3, "oro"), Carta(3, "copa"), Carta(3, "basto"), Carta(3, "espada"),
        Carta(2, "oro"), Carta(2, "copa"), Carta(2, "basto"), Carta(2,"espada"),
        Carta(1, "copa"), Carta(1, "oro"), Carta(12, "oro"), Carta(12, "copa"), Carta(12, "basto"), Carta(12, "espada"),
        Carta(11, "oro"), Carta(11, "copa"), Carta(11, "basto"), Carta(11, "espada"),
        Carta(10, "oro"), Carta(10, "copa"), Carta(10, "basto"), Carta(10, "espada"),
        Carta(7, "copa"),Carta(7, "basto"), Carta(6, "oro"), Carta(6, "copa"), Carta(6, "basto"), Carta(6, "espada"),
        Carta(5, "oro"), Carta(5, "copa"), Carta(5, "basto"), Carta(5, "espada"),
        Carta(4, "oro"), Carta(4, "copa"), Carta(4, "basto"), Carta(4, "espada"))
        
def valores_cartas(repartir_cartas):
    '''
    Recibe una tupla con las cartas
    Establece los valores de las cartas
    
    '''
    for i in range(len(mazo)):
        # if mazo[i].numero == 1 and mazo[i].palo == "Espada":
        #     mazo[i].valor = 15
        # elif mazo[i].numero == 1 and mazo[i].palo == "Basto":
        #     mazo[i].valor = 14
        match mazo[i].numero:
            case 1:
                if mazo[i].palo == "espada":
                    mazo[i].valor = 15
                elif mazo[i].palo == "basto":
                    mazo[i].valor = 14
                else:
                    mazo[i].valor = 9
            case 2:
                mazo[i].valor = 10
            case 3:
                mazo[i].valor = 11
            case 4:
                mazo[i].valor = 2
            case 5:
                mazo[i].valor = 3
            case 6:
                mazo[i].valor = 4
            case 7:
                if mazo[i].palo == "espada":
                    mazo[i].valor = 13
                elif mazo[i].palo == "oro":
                    mazo[i].valor = 12
                else:
                    mazo[i].valor = 5
            case 10:
                mazo[i].valor = 6
            case 11:
                mazo[i].valor = 7
            case 12:
                mazo[i].valor = 8
    return repartir_cartas()

def repartir_cartas() -> list:
    '''
    Copia el mazo original
    Reparte las cartas
    Remueve las cartas repartidas del mazo
    Devuelve dos listas una con las cartas repartidas del jugador y otra con las de la maquina
    '''
    mazo_copia = copy.deepcopy(mazo)
    mazo_copia = list(mazo_copia)

    cartas_jugador_1 = []
    cartas_maquina = []

    for i in range(3):
        #Proceso de eleccion random y eliminacion de cartas por parte del jugador

        carta_random_jugador = random.choice(mazo_copia)
        cartas_jugador_1.append(carta_random_jugador)
        mazo_copia.remove(carta_random_jugador)

        #Proceso de eleccion random y eliminacion de cartas por parte de la maquina

        carta_random_maquina = random.choice(mazo_copia)
        cartas_maquina.append(carta_random_maquina)
        mazo_copia.remove(carta_random_maquina)

        #print(f"Estas son tus cartas: {cartas_jugador_1[i].numero} de {cartas_jugador_1[i].palo}")
    
    #Mostrar cartas de la maquina
    for i in range(3):
        print(f"Estas son las cartas de la maquina: {cartas_maquina[i].numero} de {cartas_maquina[i].palo}")
    for i in range(3):
        print(f"Estas son las cartas tuyas: {cartas_jugador_1[i].numero} de {cartas_jugador_1[i].palo}")

    return cartas_jugador_1, cartas_maquina


def comparar_cartas(carta_jugador: any, carta_maquina: any) -> int:
    '''
    Recibe la carta del jugador y de la maquina
    Compara el valor de las cartas
    Retorna un entero
    '''


    if carta_jugador.valor > carta_maquina.valor:
        print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
        print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
        print(f"Felicidades ganaste la ronda!")
        return 1
    
    if carta_maquina.valor > carta_jugador.valor:
        print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
        print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
        print("Perdiste la ronda!")
        return -1

    if carta_maquina.valor == carta_jugador.valor:
        print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
        print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
        print(f"La ronda fue empate")
        return 0
    
def comparar_valores_cartas(carta_jugador: any, carta_maquina: any) -> int:
    '''
    Recibe la carta del jugador y de la maquina
    Compara el valor de las cartas
    Retorna un entero
    '''


    if carta_jugador != None and carta_maquina != 0 and carta_maquina != int:

        if carta_jugador.valor > carta_maquina.valor:
            print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
            print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
            print(f"Felicidades ganaste la ronda!")
            return True
        
        if carta_maquina.valor > carta_jugador.valor:
            print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
            print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
            print("Perdiste la ronda!")
            return False
        
        if carta_maquina.valor == carta_jugador.valor:
            print(f"Tiraste {carta_jugador.numero} de {carta_jugador.palo}")
            print(f"La maquina tiro: {carta_maquina.numero} de {carta_maquina.palo}")
            print(f"La ronda fue empate")
            #Hay que verificar si es mano o no y si es mano se pone adelante la carta del otro
            #Logica mas tarde
            return True


# def sumar_puntos(puntaje_jugador,puntaje_maquina,valor:int) -> int:
#     if valor == 1:
#         puntaje_jugador += 1
#     elif valor == -1:
#         puntaje_maquina += 1

#     return puntaje_jugador, puntaje_maquina
        
def estado_del_juego(puntaje_jugador:int, puntaje_maquina:int)-> bool:
    '''
    Recibe el puntaje del jugador y de la maquina
    Verifica quien gano, respecto a los puntos acumulados
    Retorna un booleano
    '''
    if puntaje_jugador < 3 and puntaje_maquina < 3:
        print(f"Estos son tus puntos: {puntaje_jugador}")
        print(f"Estos son los de la maquina: {puntaje_maquina}")
        return True
    
    if puntaje_jugador >= 3:
        #print("Felicidades ganasteEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!")
        return False
    elif puntaje_maquina >= 3:
        #print("Perdiste! Gano la maquinaEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        return False

def estado_de_la_ronda(puntaje_ronda_jugador: int, puntaje_ronda_maquina: int)-> int:
    '''
    Recibe el puntaje de la ronda del jugador y de la maquina
    Verifica quien gano, respecto a los puntos acumulados de la ronda
    Retorna un entero
    '''

    if puntaje_ronda_jugador > puntaje_ronda_maquina:
        return 1
    elif puntaje_ronda_maquina > puntaje_ronda_jugador:
        return -1
    
    #Si todas fueron empate, gana el que es mano
    elif puntaje_ronda_maquina == puntaje_ronda_jugador:
        return 0
    
def sumar_puntos_ronda(datos_ronda:dict,turno_jugador: bool) -> int:
    if turno_jugador:
        datos_ronda["puntaje_jugador_ronda"] += 1
    elif not turno_jugador:
        datos_ronda["puntaje_maquina_ronda"] += 1

    return datos_ronda


def verificar_estado_ronda(datos_ronda:dict) -> bool:
    if datos_ronda["puntaje_maquina_ronda"] >= 2:
        datos_ronda["ronda_terminada"] = True
    elif datos_ronda["puntaje_jugador_ronda"] >= 2:
        datos_ronda["ronda_terminada"] = True
    else:
        datos_ronda["ronda_terminada"] = False
    
    return datos_ronda["ronda_terminada"]

def reiniciar_ronda(datos_ronda:dict):
    datos_ronda["ronda_terminada"] = False
    datos_ronda["puntaje_jugador_ronda"] = 0
    datos_ronda["puntaje_maquina_ronda"] = 0
    datos_ronda["partida_iniciada"] = False
    datos_ronda["cartas_repartidas"] = False
    datos_ronda["turno_jugador"] = True
    datos_ronda["carta_ya_tirada_jugador"] = False
    datos_ronda["carta_ya_tirada_maquina"] = False
    datos_ronda["carta_segunda_ronda_maquina"] = None
    datos_ronda["toco_truco"] = False
    datos_ronda["puede_tocar_truco"] = True
    datos_ronda["truco"] = False
    datos_ronda["truco_rechazado"] = False

    for key, value in datos_ronda.items():
        print(f"Este es el valor {value} y esta la key {key}")

    return datos_ronda
    

def sumar_puntos(datos_ronda, puntaje_partida_jugador: int, puntaje_partida_maquina:int, truco):
    if datos_ronda["puntaje_jugador_ronda"] > datos_ronda["puntaje_maquina_ronda"]:
        if truco:
            print("Se suma el truquelson al jugador")
            puntaje_partida_jugador += 2
        else:
            puntaje_partida_jugador += 1
    if datos_ronda["puntaje_maquina_ronda"] > datos_ronda["puntaje_jugador_ronda"]:
        if truco:
            print("Se suma el truquelson a la maquina")
            puntaje_partida_maquina += 2
        else:
            puntaje_partida_maquina += 1

    return puntaje_partida_jugador, puntaje_partida_maquina

# def reiniciar_ronda():
#     global cartas_repartidas, partida_iniciada, cartas_jugador, cartas_maquina
#     global cartas_tablero, cartas_tablero_maquina, carta_guardada_jugador, carta_guardada_maquina
#     global carta_ya_tirada_jugador, carta_ya_tirada_maquina, lista_cartas_ronda, turno_jugador, ronda_terminada

#     cartas_repartidas = False
#     partida_iniciada = False
#     cartas_jugador = []
#     cartas_maquina = []
#     cartas_tablero = []
#     cartas_tablero_maquina = []
#     carta_guardada_jugador = None
#     carta_guardada_maquina = None
#     carta_ya_tirada_jugador = False
#     carta_ya_tirada_maquina = False
#     lista_cartas_ronda = []
#     turno_jugador = True
#     ronda_terminada = False

    
def guardar_cartas_ronda(carta_guardada_jugador, carta_guardada_maquina):
    if isinstance(carta_guardada_maquina, Carta) and isinstance(carta_guardada_jugador, Carta):
        return comparar_valores_cartas(carta_guardada_jugador, carta_guardada_maquina)
                

def cartas_guardadas_por_ronda(lista_cartas_ronda:list, carta_guardada_jugador, carta_guardada_maquina):
    lista_cartas_ronda.append(carta_guardada_jugador)
    lista_cartas_ronda.append(carta_guardada_maquina)
    return lista_cartas_ronda


# def truco(cantado:bool, decision_maquina) -> bool:
    
#     if not cantado:
#         accion = input("Quiere cantar Truco?: [si] [no]")
#         if accion.lower == "si":
#             if decision_maquina:
#                 return True
#             else:
#                 return False
#         elif accion.lower == "no":
#             return False

def truco(decision_jugador:bool, decision_maquina:bool)->bool:
    if decision_jugador:
        if decision_maquina:
            return True
        else:
            return False
        
def estado_de_ronda_modificado(turno_jugador: bool, puntaje_maquina, puntaje_jugador) -> int:
    if turno_jugador:
        puntaje_jugador += 1
    elif not turno_jugador:
        puntaje_maquina += 1

    return puntaje_maquina, puntaje_jugador
        

def tirar_carta(cartas: list,carta_tirada: int, rect_cartas:list, imagenes_cartas: list, cartas_tablero: list) -> list:
    if carta_tirada != None:
        i = None
        match carta_tirada:
                case 0:
                    #carta_tirada = cartas_jugador_1[0]
                    i = 0
                case 1:
                    #carta_tirada = cartas_jugador_1[1]
                    i = 1
                case 2:
                    #carta_tirada = cartas_jugador_1[2]
                    i = 2
        print(f"Se va a remover la carta {i}")
        print(carta_tirada)
        carta_tirada_tablero = cartas[i]

        cartas.remove(cartas[i])
        rect_cartas.remove(rect_cartas[i])
        cartas_tablero.append(imagenes_cartas[i])

        
        return rect_cartas,cartas,cartas_tablero, carta_tirada_tablero
    
#def verificacion(carta_jugador, carta_maquina):
#    if isinstance(carta_jugador, Carta) and isinstance(carta_maquina, Carta):
        

# def reiniciar_datos_del_juego(datos_del_juego):

def verificar_estado_partida(puntaje_jugador_partida: int, puntaje_maquina_partida: int, puntaje_para_ganar: int):
    if puntaje_jugador_partida >= puntaje_para_ganar:
        return "Jugador"
    if puntaje_maquina_partida >= puntaje_para_ganar:
        return "Maquina"

def jugar():
    '''
    Recibe el mazo con los valores establecidos
    Recibe las cartas repartidas
    Inicia la partida
    Verifica los puntajes de cada ronda 
    Verifica quien gano
    '''
    puntaje_maquina = 0
    puntaje_jugador = 0

    while estado_del_juego(puntaje_jugador, puntaje_maquina):
        
        #Establece los valores de la carta
        valores_cartas()
        #Reparte los valores
        cartas_jugador_1, cartas_maquina = repartir_cartas()

        puntaje_ronda_jugador = 0
        puntaje_ronda_maquina = 0
        truco_cantado = False
        
        while len(cartas_jugador_1) > 0 and len(cartas_maquina) > 0:

            for i in range(len(cartas_jugador_1)):
                print(f"Tenes estas cartas: {cartas_jugador_1[i].numero} de {cartas_jugador_1[i].palo}")

        #Todo este proceso analizarlo si hacerlo en el main:
        
            if len(cartas_jugador_1) == 3:
                carta_eleccion_jugador = int(input(f"Que carta quiere elegir?: [1], [2], [3]: " ))
                #cantar_truco = input("Quiere cantar truco? [si] [no]")
                #if cantar_truco.lower == "si":
                    #decision_maquina = random.choice(True, False)
                    #if truco(True, decision_maquina):
                    #    truco_cantado = True
                    
                #Envido
                #Truco
                # decision_maquina = [True, False]
                # truco_resultado = truco(truco_cantado, random.choice(decision_maquina))

            elif len(cartas_jugador_1) == 2:
                carta_eleccion_jugador = int(input(f"Que carta quiere elegir?: [1], [2]: " ))
            else:
                carta_eleccion_jugador = int(input(f"Que carta quiere elegir?: [1]: " ))
            match carta_eleccion_jugador:
                case 1:
                    carta_eleccion_jugador = cartas_jugador_1[0]
                case 2:
                    carta_eleccion_jugador = cartas_jugador_1[1]
                case 3:
                    carta_eleccion_jugador = cartas_jugador_1[2]
            
            carta_eleccion_maquina = random.choice(cartas_maquina)

            #Eliminar cartas tiradas
            
            cartas_jugador_1.remove(carta_eleccion_jugador)
            cartas_maquina.remove(carta_eleccion_maquina)

            resultado = comparar_cartas(carta_eleccion_jugador, carta_eleccion_maquina)
            
            #Sumar puntaje de la ronda
            if resultado == 1:
                puntaje_ronda_jugador += 1
            elif resultado == -1:
                puntaje_ronda_maquina += 1

            # if truco_resultado:
            #     truco_cantado = True
        
        #Obtener resultado de la ronda
        resultado_ronda = estado_de_la_ronda(puntaje_ronda_jugador, puntaje_ronda_maquina)
        #Sumar al puntaje del jugador
        if resultado_ronda == 1:
            puntaje_jugador += 1
        elif resultado_ronda == -1:
            puntaje_maquina += 1
        elif resultado_ronda == 0:
            puntaje_jugador += 1
    


#jugar()

def cantar_truco(decision_jugador: bool, decision_maquina: bool):
    truco_aceptado = False
    if decision_jugador and decision_maquina:
        truco_aceptado = True
        return truco_aceptado
    else:
        return truco_aceptado
