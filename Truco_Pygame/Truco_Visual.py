import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logica import *
from Clases.carta import *
from time import sleep
from funciones_pygame import *
import datos
from manejo_archivos.funciones_archivos import *

datos_boton_salir = datos.boton_salir

datos_boton_truco = datos.boton_truco

datos_boton_salir_terminado = datos.boton_salir_terminado

datos_boton_envido = datos.boton_envido

pygame.init()

ANCHO = 1920
LARGO = 1080
screen = pygame.display.set_mode((ANCHO, LARGO))
ejecutar_juego = True
puntaje_jugador = 0
puntaje_maquina = 0
cartas_repartidas = False
texto_mostrado = False

fuente_personalizada = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
fuente_personalizada_escalada = pygame.font.Font("Fuentes/fuente_und.ttf", 70)
menu_mostrado = False
def mostrar_background():
    imagen_background = pygame.image.load("ImagenesMenu/fondo_menu4.jpg")
    imagen_background = pygame.transform.scale(imagen_background, (screen.get_width(), screen.get_height()))
    screen.blit(imagen_background, (0, 0))


estado = "Menu"
partida_iniciada = False
cartas_repartidas = False
cartas_mostradas = False
cartas_tablero = []
cartas_tablero_maquina = []
scale_cartas = (150, 200)
reloj = pygame.time.Clock()
cantidad_cartas_tiradas = 0

x = 30
y = screen.get_height() // 2 - 200

carta_tirada_maquina = 0
turno_jugador = True
turno_maquina = False
carta_tirada = None
primera_ronda = True
carta_guardada_jugador = None
carta_guardada_maquina = None
primera_ronda = True
ronda = 0
comparar_segunda_ronda = False
segunda_ronda_comparada = False
ronda_terminada = False

puntaje_jugador_partida = 0
puntaje_maquina_partida = 0
guardada = False
ganador = ""
lista_cartas_ronda = []

posicion_boton = (200, 100)
escala_boton = (400, 160)

#escala_boton_agrandado = (500, 200)

ruta_imagen_boton_salir = "ImagenesMenu/botonSalir.png"

datos_ronda = {
    "ronda_terminada": False,
    "puntaje_jugador_ronda": 0,
    "puntaje_maquina_ronda": 0,
    "partida_iniciada": False,
    "cartas_repartidas": False,
    "turno_jugador": True,
    "carta_ya_tirada_jugador": False,
    "carta_ya_tirada_maquina": False,
    "carta_segunda_ronda_maquina": None,
    "truco": False,
    "puede_tocar_truco": True,
    "toco_truco": False,
    "truco_rechazado": False,
    "sonido_ambiente": False
}

jugador_tocando_salir = False
jugador_tocando_truco = False
decisiones_maquina = [True, False]

jugador_tocando_envido = False

posicion_burbja_texto = [1000, 50]

truco_tocado = False

cancion_reproducida = False
terminado = False

jugador_toco_salir = False

seguimiento_partidas = {"Jugador": 0, "Maquina": 0}

while ejecutar_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar_juego = False
    carta_clickeada = False
    
    mouse_x, mouse_y = pygame.mouse.get_pos() #Obtener posicion del mouse

    

    if estado == "Menu":
        if not cancion_reproducida:
            son = reproducir_sonido_ambiente(datos.sonido_musica_menu, True, 0.3)
            cancion_reproducida = True
        titulo_menu(screen)
        match animacion_menu(screen,evento,mouse_x, mouse_y, datos.sonido_opciones, datos.sonido_click_opciones, mostrar_background):
            case "Jugar":
                estado = "Jugar"
            case "Opciones":
                print("Abriendo opciones...")
            case "Salir":
                ejecutar_juego = False

    elif estado == "Jugar":
        son.stop()
        if not datos_ronda["partida_iniciada"] and not terminado:
            datos_ronda["partida_iniciada"] = True
            if not datos_ronda["cartas_repartidas"]:
                cartas_jugador, cartas_maquina = valores_cartas(repartir_cartas) #Establecer valores de las cartas y repartirlas
                datos_ronda["cartas_repartidas"] = True
            #sleep(1)
            print("Partida iniciada")
            #datos_ronda["cartas_repartidas"] = True
            #sleep(1)
        if terminado:
            mostrar_pantalla_final(screen, datos_terminados, leer_partidas)
            nuevo_boton_salir = crear_boton(screen, datos_boton_salir_terminado, True)
            nuevo_boton_salir, jugador_toco_salir = animacion_tocar_boton(nuevo_boton_salir, mouse_x, mouse_y, fuente_personalizada_escalada, 
                                                                        jugador_toco_salir, datos_boton_salir_terminado["color_escalado"])
            if jugador_toco_salir:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    ejecutar_juego = False

        #if puede_envido(cartas_jugador) and primera_ronda:
            #print("Se entro ap uede envido")
            #datos_boton_creado_envido = crear_boton(screen, datos_boton_envido, True)
            #datos_boton_creado_envido, jugador_tocando_envido = animacion_tocar_boton(datos_boton_creado_envido, mouse_x, mouse_y, 
                                                                                    #fuente_personalizada_escalada, jugador_tocando_envido, datos_boton_envido["color_escalado"])


            #print(f"Boton Envido: {datos_boton_creado_envido}")
            #dibujar_boton(screen, datos_boton_creado_envido)
            #ganador_envido = cantar_envido(cartas_jugador, cartas_maquina)
        

        if datos_ronda["partida_iniciada"]:
            if len(cartas_jugador) >= 1 and not datos_ronda["ronda_terminada"]:
                if not datos_ronda["sonido_ambiente"]:
                    reproducir_sonido_ambiente(datos.sonido_ambiente_juego, True, 0.2)
                    datos_ronda["sonido_ambiente"] = True
                    
                rect_cartas, imagenes_cartas = mostrar_cartas(cartas_jugador, screen)#Mostrar cartas del jugador en la pantalla
                rect_cartas_maquina, imagenes_cartas_maquina = dibujar_cartas_maquina(cartas_maquina, scale_cartas) #Dibujar cartas de la maquina
                rect_cartas = animaciones_cartas_optimizado(screen,rect_cartas, imagenes_cartas, mouse_x, mouse_y, evento)
                carta_tirada = verificar_tocar_carta(rect_cartas, evento, mouse_x, mouse_y, datos.sonido_carta, datos.sonido_tirar_carta)
                datos_boton_creado_salir = crear_boton(screen, datos_boton_salir ,True)
                datos_boton_creado_salir, jugador_tocando_salir = animacion_tocar_boton(datos_boton_creado_salir, mouse_x, mouse_y, 
                                                                                        fuente_personalizada_escalada, jugador_tocando_salir, datos_boton_salir["color_escalado"])

                #Boton truco
                if not datos_ronda["toco_truco"] and not truco_tocado:
                    datos_boton_creado_truco = crear_boton(screen, datos_boton_truco, True)
                    datos_boton_creado_truco, jugador_tocando_truco = animacion_tocar_boton(datos_boton_creado_truco, mouse_x, mouse_y, 
                                                                                            fuente_personalizada_escalada, jugador_tocando_truco, datos_boton_truco["color_escalado"])

                    dibujar_boton(screen, datos_boton_creado_truco)
                dibujar_boton(screen,datos_boton_creado_salir)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        ejecutar_juego = False
                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        if jugador_tocando_salir:
                            ejecutar_juego = False
                        elif jugador_tocando_truco and datos_ronda["puede_tocar_truco"]:
                            jugador_tocando_truco = False
                            datos_ronda["puede_tocar_truco"] = False
                            datos_ronda["toco_truco"] = True
                    
                if datos_ronda["toco_truco"]:
                    print("Se canto truquelson")
                    datos_ronda["truco"] = cantar_truco(datos_ronda["toco_truco"], random.choice(decisiones_maquina))

                    if datos_ronda["truco"]:

                        truco_cantado_texto(screen, "QUIERO", posicion_burbja_texto, datos.sonido_notificacion_truco)
                        sleep(2.5)
                        print("Se acepto el truquelson")
                    else:
                        print("Se rechazo el truquelson")
                        truco_cantado_texto(screen, "NO QUIERO", posicion_burbja_texto, datos.sonido_notificacion_truco)
                        sleep(2.5)
                        datos_ronda["truco_rechazado"] = True
                        

                    datos_ronda["toco_truco"] = False
                    truco_tocado = True


                if datos_ronda["turno_jugador"] and carta_tirada != None:
                    rect_cartas, cartas_jugador, cartas_tablero, carta_tirada = tirar_carta(cartas_jugador, carta_tirada, rect_cartas, imagenes_cartas, cartas_tablero)
                    carta_guardada_jugador = carta_tirada
                    if primera_ronda:
                        primera_ronda = False
                        datos_ronda["turno_jugador"] = False
                    datos_ronda["carta_ya_tirada_jugador"] = True
                    
                    sleep(0.5)
                
                #for carta in cartas_maquina:
                #    print(f"Esta es la carta de la maquina tiene: {carta.numero} de {carta.palo}")

                if not datos_ronda["turno_jugador"] and len(cartas_maquina) >= 1 or isinstance(carta_guardada_jugador, Carta) and not isinstance(carta_guardada_maquina, Carta):
                        rect_cartas_maquina, cartas_maquina, cartas_tablero_maquina, carta_tirada_maquina = tirar_carta(cartas_maquina, eleccion_carta_maquina(cartas_maquina), 
                                                                                        rect_cartas_maquina, imagenes_cartas_maquina, cartas_tablero_maquina)
                        datos_ronda["turno_jugador"] = True
                        carta_guardada_maquina = carta_tirada_maquina
                        datos_ronda["carta_ya_tirada_maquina"] = True
                        print("TIRANDO CARTA DE LA MQAUSAIANANANANANNANA")
                        print("TIRANDO CARTA MAQUINOLA")

                if isinstance(carta_guardada_maquina, Carta) and isinstance(carta_guardada_jugador, Carta):
                    lista_cartas_ronda.append(carta_guardada_jugador)
                    if isinstance(datos_ronda["carta_segunda_ronda_maquina"], Carta):
                        lista_cartas_ronda.append(datos_ronda["carta_segunda_ronda_maquina"])
                        datos_ronda["carta_segunda_ronda_maquina"] = None
                    else:
                        lista_cartas_ronda.append(carta_guardada_maquina)

                if isinstance(carta_guardada_maquina, Carta) and not isinstance(carta_guardada_jugador, Carta):
                    datos_ronda["carta_segunda_ronda_maquina"] = carta_guardada_maquina

                if datos_ronda["carta_ya_tirada_jugador"] and datos_ronda["carta_ya_tirada_maquina"] and len(lista_cartas_ronda) >= 2:
                    
                    datos_ronda["carta_ya_tirada_maquina"] = False
                    datos_ronda["carta_ya_tirada_jugador"] = False
                
                    datos_ronda["turno_jugador"] = comparar_valores_cartas(lista_cartas_ronda[0], lista_cartas_ronda[1])
                    datos_ronda = sumar_puntos_ronda(datos_ronda, datos_ronda["turno_jugador"])
                    print(f"Turno del jugador: {datos_ronda["turno_jugador"]}")
                    carta_guardada_maquina = None
                    carta_guardada_jugador = None
                    lista_cartas_ronda = []
                    ##print(evento)

                    print(f"Puntaje del jugador {datos_ronda["puntaje_jugador_ronda"]}")
                    print(f"Puntaje de la maquina {datos_ronda["puntaje_maquina_ronda"]}")

                if not datos_ronda["truco_rechazado"]:
                    datos_ronda["ronda_terminada"] = verificar_estado_ronda(datos_ronda)
                
                if datos_ronda["truco_rechazado"]:
                    datos_ronda["ronda_terminada"] = True

                if len(cartas_maquina) < 1 and len(cartas_jugador) >= 1:
                    datos_ronda["turno_jugador"] = True
            
                mostrar_carta_tirada(screen, cartas_tablero, y)#Mostrar carta tirada del jugador
                mostrar_carta_tirada(screen, cartas_tablero_maquina, y - 100)#Mostrar carta tirada de la maquina
                mostrar_puntaje_partida(screen, puntaje_jugador_partida, puntaje_maquina_partida)

            else:
                background_game(screen)
                mostrar_carta_tirada(screen, cartas_tablero, y) #Mostrar cartas tiradas del jugador
                mostrar_carta_tirada(screen, cartas_tablero_maquina, y - 100) #Mostrar cartas tiradas de la maquina
                sleep(1.5)
                if not datos_ronda["truco_rechazado"]:
                    puntaje_jugador_partida, puntaje_maquina_partida = sumar_puntos(datos_ronda, puntaje_jugador_partida, puntaje_maquina_partida, datos_ronda["truco"])
                elif datos_ronda["truco_rechazado"]:
                    puntaje_jugador_partida += 1

                print(f"PUNTAJE DEL JUGADOR DE LA PARTIDA: {puntaje_jugador_partida}")
                print(f"PUNTAJE DE LA MAQUINA DE LA PARTIDA: {puntaje_maquina_partida}")
                primera_ronda = True
                carta_guardada_jugador = None
                carta_guardada_maquina = None
                cartas_tablero = []
                cartas_tablero_maquina = []
                posicion_burbja_texto = [1000, 50]
                truco_tocado = False
                datos_ronda = reiniciar_ronda(datos_ronda)
                print("Se entro al elseEEEEEEEEEEE")
    
                ganador = verificar_estado_partida(puntaje_jugador_partida, puntaje_maquina_partida, 1)

                if ganador == "Jugador" or ganador == "Maquina":
                    datos_terminados = {
                        "puntaje_jugador_partida": puntaje_jugador_partida,
                        "puntaje_maquina_partida":puntaje_maquina_partida,
                        "ganador": ganador
                    }
                    leer_puntaje(seguimiento_partidas, ganador)
                    terminado = True
                    puntaje_jugador_partida = 0
                    puntaje_maquina_partida = 0
                    background_game(screen)
                    sleep(0.5)
                    #mostrar_texto_ganador(ganador)
                    sleep(2.5)
                    ganador = ""
                    #ejecutar_juego = False

    reloj.tick(60)
    pygame.display.update()

pygame.quit()