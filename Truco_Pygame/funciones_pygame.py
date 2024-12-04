import pygame
from random import choice
from time import sleep

def background_game(screen):
    background_table = pygame.image.load("ImagenesMenu/background_table_dark.webp")
    background_table = pygame.transform.scale(background_table, (screen.get_width(), screen.get_height()))
    screen.blit(background_table, (0, 0))


def mostrar_cartas(cartas_jugador:list, screen) -> list:
    '''
    Recibe las cartas del jugador y la pantalla
    Dibuja las cartas
    Devuelve dos listas con los rects e imagenes creadas de las cartas
    '''
    POSICION_JUGADOR_Y = 600
    imagenes_cartas = []
    rect_cartas = []
    # POSICION_MAQUINA_Y = 300
    x = 700
    for carta_jugador in cartas_jugador:
        imagen_carta_jugador = pygame.image.load(carta_jugador.imagen_carta())
        imagen_scaled_jugador = pygame.transform.scale(imagen_carta_jugador, (150, 200))
        imagen_escalada_jugador_rect = imagen_scaled_jugador.get_rect()

        imagen_escalada_jugador_rect.topleft = (x, POSICION_JUGADOR_Y)

        rect_cartas.append(imagen_escalada_jugador_rect)
        imagenes_cartas.append(imagen_carta_jugador)
        #if imagen_carta_jugador.get_rect.collide
        screen.blit(imagen_scaled_jugador, (x, POSICION_JUGADOR_Y))
        x += 200
    return rect_cartas,imagenes_cartas


def dibujar_cartas_maquina(cartas_maquina:list, scale: tuple) -> list:
    '''
    Recibe las cartas del jugador y la pantalla
    Dibuja las cartas
    Devuelve dos listas con los rects e imagenes creadas de las cartas
    '''
    rect_cartas_maquina = []
    imagenes_cartas_maquina = []

    for carta in cartas_maquina:
        imagen_carta = pygame.image.load(carta.imagen_carta())
        imagen_carta_escalada = pygame.transform.scale(imagen_carta, scale)
        imagen_carta_rect = imagen_carta_escalada.get_rect() 

        rect_cartas_maquina.append(imagen_carta_rect)
        imagenes_cartas_maquina.append(imagen_carta_escalada)

    return rect_cartas_maquina, imagenes_cartas_maquina
#carta_tocada = False

def eleccion_carta_maquina(cartas_maquina: list) -> int:
    '''
    Recibe la lista de cartas
    Elije una entre esas cartas
    Devuelve el indice de la carta elegida
    '''
    if len(cartas_maquina) >= 1:
        carta_elegida = choice(cartas_maquina)

        indice = cartas_maquina.index(carta_elegida)

        return indice

# def mostrar_carta_maquina(screen ,cartas_tiradas):
#     x = 30
#     posicion_tablero = (x, screen.get_height() // 2)
#     if len(cartas_tiradas) >= 1:
#         for i in range(len(cartas_tiradas)):
#             screen.blit(cartas_tiradas[i], posicion_tablero)
#             x += 270
#             posicion_tablero = (x)

def mostrar_carta_tirada(screen ,cartas_tiradas: list, y:int):
    '''
    Recibe la pantalla, recibe las cartas tiradas y la posicion para posicicionarlas en el tablero
    Dibuja las cartas en el tablero
    '''
    x = 500
    posicion_tablero = (x, y)
    if len(cartas_tiradas) >= 1:
        for i in range(len(cartas_tiradas)):
            screen.blit(cartas_tiradas[i], posicion_tablero)
            x += 270
            posicion_tablero = (x , y)

# def mostrar_cartas_tiradas_modificada(screen ,cartas_tiradas: list, y:int, imagenes_cartas: list):

#     cartas_pares = []
#     #[[carta_tirada_jugador: object, carta_tirada_maquina: object], [carta_tirada_jugador2: object, carta_tirada_maquina2: object]]
#     x = 30
#     posicion_tablero = (x, y)
#     if len(cartas_tiradas) >= 1:
#         for i in range(len(cartas_tiradas)):
#             cartas_ordenadas = sorted(cartas_tiradas[i], key=lambda carta: carta.valor)
#             cartas_pares.append(cartas_ordenadas)
#             #[2, 1]
#             for j in range(cartas_pares):
#                 imagen_carta = pygame.image.load(cartas_pares[j].imagen_carta())
#                 imagen_carta_escalada = pygame.transform.scale(imagen_carta, posicion_tablero)
#                 imagen_carta_rect = imagen_carta_escalada.get_rect() 
#                 screen.blit(imagenes_cartas[j], posicion_tablero)
#                 x += 270
#                 posicion_tablero = (x , y)




def animaciones_cartas_optimizado(screen, rect_cartas: list, imagenes_cartas: list, mouse_x: int, mouse_y: int, evento) -> int:

    '''
    Recibe la pantalla y los datos para dibujar la carta
    Verifica si la carta esta siendo tocada
    Devuelve un rect de cartas
    '''

    tamaño_original = (150, 200)
    tamaño_resaltado = (200, 250)
    carta_clickeada = False

    for i in range(len(rect_cartas)):
        posicion_carta = rect_cartas[i]
        if rect_cartas[i].collidepoint(mouse_x, mouse_y):
            #Agrandar la carta
            imagenes_cartas[i] = pygame.transform.scale(imagenes_cartas[i], tamaño_resaltado)
            rect_cartas[i] = imagenes_cartas[i].get_rect()
            rect_cartas[i].center = posicion_carta.center

            #mostrar cartas
            for j in range(len(rect_cartas)):
                screen.blit(imagenes_cartas[j], rect_cartas[j])
            # if evento.type == pygame.MOUSEBUTTONUP and not carta_clickeada:
            #     carta_clickeada = True
            #     return i
        else:
            #Volver las cartas a su tamaño original
            imagenes_cartas[i] = pygame.transform.scale(imagenes_cartas[i], tamaño_original)
            rect_cartas[i] = imagenes_cartas[i].get_rect()
            rect_cartas[i].center = posicion_carta.center

            #mostrar cartas
            background_game(screen)
            for j in range(len(rect_cartas)):
                screen.blit(imagenes_cartas[j], rect_cartas[j])

    return rect_cartas



    # #if not carta_tocada:
    # for j in range(len(rect_cartas)):
    #     posicion_carta = rect_cartas[j]
    #     imagenes_cartas[j] = pygame.transform.scale(imagenes_cartas[j], (200, 150))
    #     rect_cartas[j] = imagenes_cartas[j].get_rect()
    #     rect_cartas[j].center = posicion_carta.center
    #     screen.blit(imagenes_cartas[j], rect_cartas[j])
    


def verificar_tirar_carta(rect_cartas: list, evento, mouse_x, mouse_y):
    '''
    Recibe la colision de las cartas
    Verifica si fueron tocadas
    Retorna un Entero si fueron tocadas, sino un None
    '''
    for i in range(len(rect_cartas)):
        if rect_cartas[i].collidepoint(mouse_x, mouse_y):
            if evento.type == pygame.MOUSEBUTTONUP:
                return i
            else:
                return None

def reproducir_sonido_ambiente(sonido:pygame.mixer.Sound, volumen:bool, cantidad_volumen:int = 0):
    '''
    Recibe el sonido a reproducir
    Recibe un booleano volumen para decidir si modificarlo a tu gusto, con la cantidad de volumen que desee
    Retorna el sonido reproducido
    '''
    if volumen:
        sonido.set_volume(cantidad_volumen)
        sonido.play()
        return sonido
    else:
        sonido.play()
        return sonido


def animaciones_cartas(screen,rect_cartas: list,imagenes_cartas: list, mouse_x: int, mouse_y:int, evento, cartas_jugador):

    

        #print(type(carta_1))
    posicion_carta = rect_cartas[0]
    imagen_carta = imagenes_cartas[0]

    #Logica carta 1
    if rect_cartas[0].collidepoint(mouse_x, mouse_y):
        #print("Se toco la carta")
        imagenes_cartas[0] = pygame.transform.scale(imagenes_cartas[0], (200, 250))
        rect_cartas[0] = imagenes_cartas[0].get_rect()
        rect_cartas[0].center = posicion_carta.center
        screen.blit(imagenes_cartas[0], rect_cartas[0])
        if evento.type == pygame.MOUSEBUTTONUP:
            imagenes_cartas.remove(imagenes_cartas[0])
            return 1
            
    else:
        background_game(screen)
        imagenes_cartas[0] = pygame.transform.scale(imagenes_cartas[0], (150, 200))
        rect_cartas[0] = imagenes_cartas[0].get_rect()
        rect_cartas[0].center = posicion_carta.center
        screen.blit(imagenes_cartas[0], rect_cartas[0])

    #Logica carta 2
    posicion_carta = rect_cartas[1]
    imagen_carta = imagenes_cartas[1]


    if rect_cartas[1].collidepoint(mouse_x, mouse_y):
        print("Se toco la carta")
        imagenes_cartas[1] = pygame.transform.scale(imagenes_cartas[1], (200, 250))
        rect_cartas[1] = imagenes_cartas[1].get_rect()
        rect_cartas[1].center = posicion_carta.center
        screen.blit(imagenes_cartas[1], rect_cartas[1])
        if evento.type == pygame.MOUSEBUTTONUP:
            imagenes_cartas.remove(imagenes_cartas[1])
            return 2
    else:
        #background_game(screen)
        imagenes_cartas[1] = pygame.transform.scale(imagenes_cartas[1], (150, 200))
        rect_cartas[1] = imagenes_cartas[1].get_rect()
        rect_cartas[1].center = posicion_carta.center
        screen.blit(imagenes_cartas[1], rect_cartas[1])

    #Logica carta 3
    posicion_carta = rect_cartas[2]
    imagen_carta = imagenes_cartas[2]
    if rect_cartas[2].collidepoint(mouse_x, mouse_y):
        print("Se toco la carta")
        imagenes_cartas[2] = pygame.transform.scale(imagenes_cartas[2], (200, 250))
        rect_cartas[2] = imagenes_cartas[2].get_rect()
        rect_cartas[2].center = posicion_carta.center
        screen.blit(imagenes_cartas[2], rect_cartas[2])
        if evento.type == pygame.MOUSEBUTTONUP:
            imagenes_cartas.remove(imagenes_cartas[0])
            return 3
    else:
        #background_game(screen)
        imagenes_cartas[2] = pygame.transform.scale(imagenes_cartas[2], (150, 200))
        rect_cartas[2] = imagenes_cartas[2].get_rect()
        rect_cartas[2].center = posicion_carta.center
        screen.blit(imagenes_cartas[2], rect_cartas[2])

        #carta_1_escalada = pygame.transform.scale(carta_1, (400, 400))
        #carta_1_escalada_rect = carta_1_escalada.get_rect()
        #carta_1_escalada_rect.center = carta_1_escalada.center





#PRUEBA PARA INTENTAR SUPERPONER LAS CARTAS
def animaciones_cartas_prueba(screen,rect_cartas: list,imagenes_cartas: list, mouse_x: int, mouse_y:int):

    global carta_1_tocada, carta_2_tocada, carta_3_tocada
    

        #print(type(carta_1))
    posicion_carta = rect_cartas[0]
    imagen_carta = imagenes_cartas[0]

    #Logica carta 1
    if rect_cartas[0].collidepoint(mouse_x, mouse_y):
        print("Se toco la carta")
        imagenes_cartas[0] = pygame.transform.scale(imagenes_cartas[0], (200, 250))
        rect_cartas[0] = imagenes_cartas[0].get_rect()
        rect_cartas[0].center = posicion_carta.center
        carta_1_tocada = True
        carta_2_tocada = False
        carta_3_tocada = False
        #screen.blit(imagenes_cartas[0], rect_cartas[0])
    else:
        background_game(screen)
        imagenes_cartas[0] = pygame.transform.scale(imagenes_cartas[0], (100, 150))
        rect_cartas[0] = imagenes_cartas[0].get_rect()
        rect_cartas[0].center = posicion_carta.center
        screen.blit(imagenes_cartas[0], rect_cartas[0])
        carta_1_tocada = False
        carta_2_tocada = False
        carta_3_tocada = False

    #Logica carta 2
    posicion_carta = rect_cartas[1]
    imagen_carta = imagenes_cartas[1]

    if rect_cartas[1].collidepoint(mouse_x, mouse_y):
        print("Se toco la carta")
        imagenes_cartas[1] = pygame.transform.scale(imagenes_cartas[1], (200, 250))
        rect_cartas[1] = imagenes_cartas[1].get_rect()
        rect_cartas[1].center = posicion_carta.center
        #screen.blit(imagenes_cartas[1], rect_cartas[1])
        carta_1_tocada = False
        carta_2_tocada = True
        carta_3_tocada = False
    else:
        #background_game(screen)
        imagenes_cartas[1] = pygame.transform.scale(imagenes_cartas[1], (100, 150))
        rect_cartas[1] = imagenes_cartas[1].get_rect()
        rect_cartas[1].center = posicion_carta.center
        screen.blit(imagenes_cartas[1], rect_cartas[1])

    #Logica carta 3
    posicion_carta = rect_cartas[2]
    imagen_carta = imagenes_cartas[2]
    if rect_cartas[2].collidepoint(mouse_x, mouse_y):
        print("Se toco la carta")
        imagenes_cartas[2] = pygame.transform.scale(imagenes_cartas[2], (200, 250))
        rect_cartas[2] = imagenes_cartas[2].get_rect()
        rect_cartas[2].center = posicion_carta.center
        screen.blit(imagenes_cartas[2], rect_cartas[2])
        carta_1_tocada = False
        carta_2_tocada = False
        carta_3_tocada = True
    else:
        #background_game(screen)
        imagenes_cartas[2] = pygame.transform.scale(imagenes_cartas[2], (100, 150))
        rect_cartas[2] = imagenes_cartas[2].get_rect()
        rect_cartas[2].center = posicion_carta.center
        screen.blit(imagenes_cartas[2], rect_cartas[2])

    if carta_1_tocada:
        screen.blit(imagenes_cartas[1], rect_cartas[1])
        screen.blit(imagenes_cartas[2], rect_cartas[2])
        screen.blit(imagenes_cartas[0], rect_cartas[0])
        carta_2_tocada = False
    if carta_2_tocada:
        screen.blit(imagenes_cartas[1], rect_cartas[0])
        screen.blit(imagenes_cartas[2], rect_cartas[2])
        screen.blit(imagenes_cartas[0], rect_cartas[1])
        carta_1_tocada = False


        #carta_1_escalada = pygame.transform.scale(carta_1, (400, 400))
        #carta_1_escalada_rect = carta_1_escalada.get_rect()
        #carta_1_escalada_rect.center = carta_1_escalada.center


def crear_boton(screen: pygame.surface ,datos_boton: dict, texto: bool) -> dict:
    '''
    Recibe un diccionario con los datos del boton a crear
    Devuelve el boton creado con las caracteristicas del diccionario
    '''

    boton = pygame.image.load(datos_boton["ruta_imagen"])
    boton = pygame.transform.scale(boton, datos_boton["escala_boton"])
    boton_rect = boton.get_rect()
    boton_rect.center = datos_boton["posicion"]

    if texto:
        texto_creado, texto_rect = crear_texto(screen,boton_rect, datos_boton["fuente"], datos_boton["texto"], datos_boton["color_texto"])
        datos_boton_creado = {
            "boton": boton,
            "boton_rect": boton_rect,
            "texto_creado": texto_creado,
            "texto_rect": texto_rect,
            "posicion_boton": datos_boton["posicion"],
            "fuente_texto": datos_boton["fuente"],
            "texto_escrito": datos_boton["texto"],
            "boton_tocado": False,
            "escala_boton_animacion": datos_boton["escala_boton_agrandado"],
            "color_texto": datos_boton["color_texto"]
        }
        #print(datos_boton_creado["boton"])
        return datos_boton_creado

def dibujar_boton(screen,datos_boton_creado: dict):
    '''
    Recibe los datos del boton creado anteriormente
    Dibuja en pantalla el boton
    '''
    ##print(type(datos_boton_creado["boton"]))
    screen.blit(datos_boton_creado["boton"], datos_boton_creado["boton_rect"])
    screen.blit(datos_boton_creado["texto_creado"], datos_boton_creado["texto_rect"])
    #print(f"Boton {datos_boton_creado["texto_creado"]} se creo correctamente")


def crear_texto(screen: pygame.surface ,boton,fuente, texto, color):
    '''
    Recibe los datos del texto a crear
    Recibe la colision del boton, para centrarlo a su posicion
    Devuelve los datos del texto creado
    '''
    fuente_cargada = fuente
    texto = fuente_cargada.render(texto, True, color)
    texto_rect = texto.get_rect()
    texto_rect.center = boton.center
    texto_rect.y = texto_rect.y + 6
    screen.blit(texto, texto_rect)
    #print("sE DIBUJO LA FUENTE")
    return texto ,texto_rect

def animacion_tocar_boton(datos_boton_creado: dict, mouse_x:int, mouse_y: int, fuente_escalada: pygame.font.Font, jugador_tocando, color_escalado):
    '''
    Recibe los datos del boton creado
    Verifica si el boton fue colisionado, haciendo una animacion
    '''
    if datos_boton_creado["boton_rect"].collidepoint(mouse_x, mouse_y):
        datos_boton_creado["boton"] = pygame.transform.scale(datos_boton_creado["boton"], datos_boton_creado["escala_boton_animacion"])
        datos_boton_creado["boton_rect"] = datos_boton_creado["boton"].get_rect()
        datos_boton_creado["boton_rect"].center = datos_boton_creado["posicion_boton"]

        datos_boton_creado["fuente_texto"] = fuente_escalada
        texto_escalado = datos_boton_creado["fuente_texto"].render(datos_boton_creado["texto_escrito"], True, color_escalado)
        texto_rect_escalado = texto_escalado.get_rect()
        texto_rect_escalado.center = datos_boton_creado["boton_rect"].center

        # Actualizar los valores en el diccionario
        datos_boton_creado["texto_creado"] = texto_escalado
        datos_boton_creado["texto_rect"] = texto_rect_escalado
        jugador_tocando = True
        
        return datos_boton_creado, jugador_tocando
    else:
        jugador_tocando = False
        return datos_boton_creado, jugador_tocando
    
def truco_cantado_texto(screen,texto: str, posicion: tuple, sonido: pygame.mixer.Sound):
    '''
    Recibe un texto, posicion y sonido
    Crea la burbuja de texto
    La posiciona con los datos dados anteriormente
    '''
    posicion_final = (1000, 400)
    texto_escrito = texto
    sonido_ya_reproducido = False
    while posicion_final[1] > posicion[1]:

        burbuja_texto_imagen = pygame.image.load("ImagenesMenu/burbuja_texto.png")
        burbuja_texto_imagen_rect = burbuja_texto_imagen.get_rect()
        burbuja_texto_imagen_rect.center = posicion

        fuente = pygame.font.Font("Fuentes/Minecraft.ttf", 30)
        
        texto = fuente.render(texto_escrito, True, (0,0,0))
        texto_rect = texto.get_rect()
        texto_rect.center = burbuja_texto_imagen_rect.center
        texto_rect.y = texto_rect.y -10
        screen.fill((0,0,0))
        screen.blit(burbuja_texto_imagen, burbuja_texto_imagen_rect)
        screen.blit(texto, texto_rect)
        if not sonido_ya_reproducido:
            sonido.play()
            sonido_ya_reproducido = True
        posicion[1] += 2

        pygame.display.flip()
    # sleep(duracion)





# def animacion_menu(screen,mouse_x: int, mouse_y: int, evento, mostrar_background):

    
#     # Lista de textos para los botones

#     boton_menu = pygame.image.load("ImagenesMenu/flat.png")
#     boton_menu = pygame.transform.scale(boton_menu, (300, 100))
#     boton_menu_rect = boton_menu.get_rect()
#     boton_menu_rect.center = (screen.get_width() // 2, 300)
#     #Boton menu 2
#     boton_menu_rect_2 = boton_menu.get_rect()
#     boton_menu_rect_2.center = boton_menu_rect.center
#     boton_menu_rect_2.y = boton_menu_rect_2.y + 250

#     #Boton menu 3
#     boton_menu_rect_3 = boton_menu.get_rect()
#     boton_menu_rect_3.center = boton_menu_rect_2.center
#     boton_menu_rect_3.y = boton_menu_rect_3.y + 250
#     textos = ["Jugar", "Opciones", "Salir"]

#     #Texto menu
#     fuente = pygame.font.Font("Fuentes/fuente.ttf", 52)
#     texto = fuente.render("Jugar", True, (0, 255, 0))
#     texto_rect = texto.get_rect()
#     texto_rect.center = boton_menu_rect.center
#     texto_rect.y = texto_rect.y + 6
    
#     # Primer botón (Jugar)
#     boton_menu_escalado = pygame.transform.scale(boton_menu, (400, 150))
#     boton_menu_escalado_rect = boton_menu_escalado.get_rect()

#     if boton_menu_rect.collidepoint(mouse_x, mouse_y):
#         # Agrandar el primer botón
#         boton_menu_escalado_rect.center = boton_menu_rect.center
#         screen.blit(boton_menu_escalado, boton_menu_escalado_rect)
#         # Agrandar el texto del primer botón
#         fuente_escalada = pygame.font.Font("Fuentes/fuente.ttf", 70)
#         texto_escalado = fuente_escalada.render(textos[0], True, (0, 0, 0))
#         texto_escalado_rect = texto_escalado.get_rect()
#         texto_escalado_rect.center = boton_menu_escalado_rect.center
#         texto_escalado_rect.y = texto_escalado_rect.y + 8
#         screen.blit(texto_escalado, texto_escalado_rect)
#         if evento.type == pygame.MOUSEBUTTONUP:
#             print("Tocaste JUGAR gordo")
#             return "Jugar"
#     else:
#         mostrar_background(screen)
#         screen.blit(boton_menu, boton_menu_rect)
#         fuente = pygame.font.Font("Fuentes/fuente.ttf", 52)
#         texto = fuente.render(textos[0], True, (0, 0, 0))
#         texto_rect = texto.get_rect()
#         texto_rect.center = boton_menu_rect.center
#         texto_rect.y = texto_rect.y + 6
#         screen.blit(texto, texto_rect)

#     # Segundo botón (Opciones)
#     if boton_menu_rect_2.collidepoint(mouse_x, mouse_y):
#         # Agrandar el segundo botón
#         boton_menu_escalado_2 = pygame.transform.scale(boton_menu, (400, 150))
#         boton_menu_escalado_rect_2 = boton_menu_escalado_2.get_rect()
#         boton_menu_escalado_rect_2.center = boton_menu_rect_2.center
#         screen.blit(boton_menu_escalado_2, boton_menu_escalado_rect_2)
#         # Agrandar el texto del segundo botón
#         fuente_escalada = pygame.font.Font("Fuentes/fuente.ttf", 70)
#         texto_escalado = fuente_escalada.render(textos[1], True, (0, 0, 0))
#         texto_escalado_rect = texto_escalado.get_rect()
#         texto_escalado_rect.center = boton_menu_escalado_rect_2.center
#         texto_escalado_rect.y = texto_escalado_rect.y + 8
#         screen.blit(texto_escalado, texto_escalado_rect)
#         if evento.type == pygame.MOUSEBUTTONUP:
#             print("Tocaste OPCIONES GORDO")
#             return "Opciones"
            
#     else:

#         screen.blit(boton_menu, boton_menu_rect_2)
#         fuente = pygame.font.Font("Fuentes/fuente.ttf", 52)
#         texto = fuente.render(textos[1], True, (0, 0, 0))
#         texto_rect = texto.get_rect()
#         texto_rect.center = boton_menu_rect_2.center
#         texto_rect.y = texto_rect.y + 6
#         screen.blit(texto, texto_rect)

#     # Tercer botón (Salir)
#     if boton_menu_rect_3.collidepoint(mouse_x, mouse_y):
#         # Agrandar el tercer botón
#         boton_menu_escalado_3 = pygame.transform.scale(boton_menu, (400, 150))
#         boton_menu_escalado_rect_3 = boton_menu_escalado_3.get_rect()
#         boton_menu_escalado_rect_3.center = boton_menu_rect_3.center
#         screen.blit(boton_menu_escalado_3, boton_menu_escalado_rect_3)
#         # Agrandar el texto del tercer botón
#         fuente_escalada = pygame.font.Font("Fuentes/fuente.ttf", 70)
#         texto_escalado = fuente_escalada.render(textos[2], True, (0, 0, 0))
#         texto_escalado_rect = texto_escalado.get_rect()
#         texto_escalado_rect.center = boton_menu_escalado_rect_3.center
#         texto_escalado_rect.y = texto_escalado_rect.y + 8
#         screen.blit(texto_escalado, texto_escalado_rect)
#         if evento.type == pygame.MOUSEBUTTONUP:
#             print("Tocaste SALIR GORDO")
#             return "Salir"
#     else:
#         screen.blit(boton_menu, boton_menu_rect_3)
#         fuente = pygame.font.Font("Fuentes/fuente.ttf", 52)
#         texto = fuente.render(textos[2], True, (0, 0, 0))
#         texto_rect = texto.get_rect()
#         texto_rect.center = boton_menu_rect_3.center
#         texto_rect.y = texto_rect.y + 6
#         screen.blit(texto, texto_rect)


carta_tocada = {}

def verificar_tocar_carta(rect_cartas, evento, mouse_x, mouse_y, sonido_carta, sonido_tirar_carta):
    for i in range(len(rect_cartas)):
        if rect_cartas[i].collidepoint(mouse_x, mouse_y):
            if i not in carta_tocada or not carta_tocada[i]:  # Verifica si la carta no ha sido tocada o si el sonido ya se reprodujo
                sonido_carta.play()  # Reproduce el sonido
                carta_tocada[i] = True  # Marca la carta como tocada para que el sonido no se reproduzca de nuevo
            if evento.type == pygame.MOUSEBUTTONDOWN:
                sonido_tirar_carta.play()
                return i
        else:
            # Si el mouse no está sobre la carta, resetea la variable para esa carta
            if i in carta_tocada:
                carta_tocada[i] = False
sonido_reproducido = {"Jugar": False, "Opciones": False, "Salir": False}


def titulo_menu(screen):
    '''
    Recibe la pantalla
    Crea el titulo del menu
    '''
    boton = pygame.image.load("ImagenesMenu/banner.png")
    boton = pygame.transform.scale(boton, (1000, 300))
    boton_rect = boton.get_rect()
    boton_rect.center = (screen.get_width() // 2, 100)
    fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 90)
    texto1 = fuente.render("TRUQUELSON", True, (255, 255, 255))
    texto1_rect = texto1.get_rect()
    texto1_rect.center = boton_rect.center
    texto1_rect.y = texto1_rect.y + 6
    screen.blit(boton, boton_rect)
    screen.blit(texto1, texto1_rect)

def animacion_menu(screen,evento,mouse_x: int, mouse_y: int, sonido_opcion, sonido_click, mostrar_background):
    
    boton_menu = pygame.image.load("ImagenesMenu/banner.png")
    boton_menu = pygame.transform.scale(boton_menu, (300, 100))
    boton_menu_rect = boton_menu.get_rect()
    boton_menu_rect.center = (screen.get_width() // 2, 300)
    #Boton menu 2
    boton_menu_rect_2 = boton_menu.get_rect()
    boton_menu_rect_2.center = boton_menu_rect.center
    boton_menu_rect_2.y = boton_menu_rect_2.y + 250

    #Boton menu 3
    boton_menu_rect_3 = boton_menu.get_rect()
    boton_menu_rect_3.center = boton_menu_rect_2.center
    boton_menu_rect_3.y = boton_menu_rect_3.y + 250

    #Texto menu
    fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
    texto = fuente.render("Jugar", True, (255, 255, 255))
    texto_rect = texto.get_rect()
    texto_rect.center = boton_menu_rect.center
    texto_rect.y = texto_rect.y + 6
    global sonido_reproducido  # Para modificar la variable global
    textos = ["Jugar", "Opciones", "Salir"]

    # Botón Jugar
    if boton_menu_rect.collidepoint(mouse_x, mouse_y):
        if not sonido_reproducido["Jugar"]:  # Reproducir sonido solo si no se ha reproducido
            sonido_opcion.play()
            sonido_reproducido["Jugar"] = True  # Marcar el sonido como reproducido
        boton_menu_escalado = pygame.transform.scale(boton_menu, (400, 150))
        boton_menu_escalado_rect = boton_menu_escalado.get_rect()
        boton_menu_escalado_rect.center = boton_menu_rect.center
        screen.blit(boton_menu_escalado, boton_menu_escalado_rect)
        fuente_escalada = pygame.font.Font("Fuentes/fuente_und.ttf", 70)
        texto_escalado = fuente_escalada.render(textos[0], True, (255, 255, 255))
        texto_escalado_rect = texto_escalado.get_rect()
        texto_escalado_rect.center = boton_menu_escalado_rect.center
        texto_escalado_rect.y += 8
        screen.blit(texto_escalado, texto_escalado_rect)
        titulo_menu(screen)
        if evento.type == pygame.MOUSEBUTTONUP:
            sonido_click.play()
            print("Tocaste JUGAR gordo")
            return "Jugar"
    else:
        mostrar_background()
        titulo_menu(screen)
        sonido_reproducido["Jugar"] = False  # Resetear el estado cuando el cursor salga del botón
        screen.blit(boton_menu, boton_menu_rect)
        fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
        texto = fuente.render(textos[0], True, (150, 150, 150))
        texto_rect = texto.get_rect()
        texto_rect.center = boton_menu_rect.center
        texto_rect.y += 6
        screen.blit(texto, texto_rect)

    # Botón Opciones
    if boton_menu_rect_2.collidepoint(mouse_x, mouse_y):
        if not sonido_reproducido["Opciones"]:
            sonido_opcion.play()
            sonido_reproducido["Opciones"] = True
        boton_menu_escalado_2 = pygame.transform.scale(boton_menu, (400, 150))
        boton_menu_escalado_rect_2 = boton_menu_escalado_2.get_rect()
        boton_menu_escalado_rect_2.center = boton_menu_rect_2.center
        screen.blit(boton_menu_escalado_2, boton_menu_escalado_rect_2)
        fuente_escalada = pygame.font.Font("Fuentes/fuente_und.ttf", 70)
        texto_escalado = fuente_escalada.render(textos[1], True, (255, 255, 255))
        texto_escalado_rect = texto_escalado.get_rect()
        texto_escalado_rect.center = boton_menu_escalado_rect_2.center
        texto_escalado_rect.y += 8
        screen.blit(texto_escalado, texto_escalado_rect)
        titulo_menu(screen)
        if evento.type == pygame.MOUSEBUTTONUP:
            print("Tocaste OPCIONES GORDO")
            return "Opciones"
    else:
        sonido_reproducido["Opciones"] = False
        screen.blit(boton_menu, boton_menu_rect_2)
        fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
        texto = fuente.render(textos[1], True, (150, 150, 150))
        texto_rect = texto.get_rect()
        texto_rect.center = boton_menu_rect_2.center
        texto_rect.y += 6
        screen.blit(texto, texto_rect)

    # Botón Salir
    if boton_menu_rect_3.collidepoint(mouse_x, mouse_y):
        if not sonido_reproducido["Salir"]:
            sonido_opcion.play()
            sonido_reproducido["Salir"] = True
        boton_menu_escalado_3 = pygame.transform.scale(boton_menu, (400, 150))
        boton_menu_escalado_rect_3 = boton_menu_escalado_3.get_rect()
        boton_menu_escalado_rect_3.center = boton_menu_rect_3.center
        screen.blit(boton_menu_escalado_3, boton_menu_escalado_rect_3)
        fuente_escalada = pygame.font.Font("Fuentes/fuente_und.ttf", 70)
        texto_escalado = fuente_escalada.render(textos[2], True, (255, 255, 255))
        texto_escalado_rect = texto_escalado.get_rect()
        texto_escalado_rect.center = boton_menu_escalado_rect_3.center
        texto_escalado_rect.y += 8
        screen.blit(texto_escalado, texto_escalado_rect)
        titulo_menu(screen)
        if evento.type == pygame.MOUSEBUTTONUP:
            print("Tocaste SALIR GORDO")
            return "Salir"
    else:
        sonido_reproducido["Salir"] = False
        screen.blit(boton_menu, boton_menu_rect_3)
        fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
        texto = fuente.render(textos[2], True, (150, 150, 150))
        texto_rect = texto.get_rect()
        texto_rect.center = boton_menu_rect_3.center
        texto_rect.y += 6
        screen.blit(texto, texto_rect)


def mostrar_pantalla_final(screen,datos_final:dict, leer_partidas):
    boton = pygame.image.load("ImagenesMenu/banner.png")
    boton = pygame.transform.scale(boton, (1000, 300))
    boton_rect = boton.get_rect()
    boton_rect.center = (screen.get_width() // 2, 100)
    fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 90)
    fuente_puntajes = pygame.font.Font("Fuentes/fuente_und.ttf", 60)

    #Boton texto jugador
    boton_texto_jugador = pygame.image.load("ImagenesMenu/banner.png")
    boton_texto_jugador = pygame.transform.scale(boton_texto_jugador, (1000, 300))
    boton_rect_texto_jugador = boton_texto_jugador.get_rect()
    boton_rect_texto_jugador.center = (350, 300)

    #Boton texto maquina:
    boton_texto_maquina = pygame.image.load("ImagenesMenu/banner.png")
    boton_texto_maquina = pygame.transform.scale(boton_texto_maquina, (1000, 300))
    boton_rect_texto_maquina = boton_texto_maquina.get_rect()
    boton_rect_texto_maquina.center = (screen.get_width() // 2 + 600, 300)

    #Total de partidas ganadas jugador
    boton_total_partidas_jugador = pygame.image.load("ImagenesMenu/banner.png")
    boton_total_partidas_jugador = pygame.transform.scale(boton_total_partidas_jugador, (1000, 300))
    boton_rect_texto_total_partidas_jugador = boton_total_partidas_jugador.get_rect()
    boton_rect_texto_total_partidas_jugador.center = (350, 900)

    #Total de partidas ganadas maquina
    boton_total_partidas_maquina = pygame.image.load("ImagenesMenu/banner.png")
    boton_total_partidas_maquina = pygame.transform.scale(boton_total_partidas_maquina, (1000, 300))
    boton_rect_texto_total_partidas_maquina = boton_total_partidas_maquina.get_rect()
    boton_rect_texto_total_partidas_maquina.center = (1750, 1020)

    datos_partidas = leer_partidas()


    if datos_final["ganador"] == "Jugador":
        texto1 = fuente.render("Ganaste!", True, (255, 255, 255))
        texto1_rect = texto1.get_rect()
        texto1_rect.center = boton_rect.center
        texto1_rect.y = texto1_rect.y + 6

        #Texto puntaje jugador
        
        texto_puntaje_jugador = fuente.render(f"Jugador: {datos_final['puntaje_jugador_partida']}", True, (255, 255, 255))
        texto_puntaje_jugador_rect = texto_puntaje_jugador.get_rect()
        texto_puntaje_jugador_rect.center = boton_rect_texto_jugador.center
        texto_puntaje_jugador_rect.y = texto_puntaje_jugador_rect.y + 6

        #Dibuajr puntaje jugador
        screen.blit(boton_texto_jugador, boton_rect_texto_jugador)
        screen.blit(texto_puntaje_jugador, texto_puntaje_jugador_rect)
        
        #Texto puntaje maquina
        texto_puntaje_maquina = fuente.render(f"Maquina: {datos_final['puntaje_maquina_partida']}", True, (255, 255, 255))
        texto_puntaje_maquina_rect = texto_puntaje_maquina.get_rect()
        texto_puntaje_maquina_rect.center = boton_rect_texto_maquina.center
        texto_puntaje_maquina_rect.y = texto_puntaje_maquina_rect.y + 6

        #Dibujar puntaje maquina:
        screen.blit(boton_texto_maquina, boton_rect_texto_maquina)
        screen.blit(texto_puntaje_maquina, texto_puntaje_maquina_rect)

        #Texto puntaje total partidas jugador
        texto_puntaje_total_jugador = fuente_puntajes.render(f"Partidas ganadas J: {datos_partidas["Jugador"]}", True, (255, 255, 255))
        texto_puntaje_total_jugador_rect = texto_puntaje_total_jugador.get_rect()
        texto_puntaje_total_jugador_rect.center = boton_rect_texto_total_partidas_jugador.center
        texto_puntaje_total_jugador_rect.y = texto_puntaje_total_jugador_rect.y + 6

        #Texto puntaje total partidas maquina
        texto_puntaje_total_maquina = fuente_puntajes.render(f"Partidas ganadas M: {datos_partidas["Maquina"]}", True, (255, 255, 255))
        texto_puntaje_total_maquina_rect = texto_puntaje_total_maquina.get_rect()
        texto_puntaje_total_maquina_rect.center = boton_rect_texto_total_partidas_maquina.center
        texto_puntaje_total_maquina_rect.y = texto_puntaje_total_maquina_rect.y + 6


        #Dibujar puntaje total jugador:
        screen.blit(boton_total_partidas_jugador, boton_rect_texto_total_partidas_jugador)
        screen.blit(texto_puntaje_total_jugador, texto_puntaje_total_jugador_rect)

        #Dibujar puntaje total maquina:
        screen.blit(boton_total_partidas_maquina, boton_rect_texto_total_partidas_maquina)
        screen.blit(texto_puntaje_total_maquina, boton_rect_texto_total_partidas_maquina)

        #Dibujar texto de ganar
        screen.blit(boton, boton_rect)
        screen.blit(texto1, texto1_rect)
    
    elif datos_final["ganador"] == "Maquina":
        texto1 = fuente.render("Perdiste!", True, (255, 255, 255))
        texto1_rect = texto1.get_rect()
        texto1_rect.center = boton_rect.center
        texto1_rect.y = texto1_rect.y + 6

        #Texto puntaje jugador
        
        texto_puntaje_jugador = fuente.render(f"Jugador: {datos_final['puntaje_jugador_partida']}", True, (255, 255, 255))
        texto_puntaje_jugador_rect = texto_puntaje_jugador.get_rect()
        texto_puntaje_jugador_rect.center = boton_rect_texto_jugador.center
        texto_puntaje_jugador_rect.y = texto_puntaje_jugador_rect.y + 6

        #Dibuajr puntaje jugador
        screen.blit(boton_texto_jugador, boton_rect_texto_jugador)
        screen.blit(texto_puntaje_jugador, texto_puntaje_jugador_rect)
        
        #Texto puntaje maquina
        texto_puntaje_maquina = fuente.render(f"Maquina: {datos_final['puntaje_maquina_partida']}", True, (255, 255, 255))
        texto_puntaje_maquina_rect = texto_puntaje_maquina.get_rect()
        texto_puntaje_maquina_rect.center = boton_rect_texto_maquina.center
        texto_puntaje_maquina_rect.y = texto_puntaje_maquina_rect.y + 6

        #Dibujar puntaje maquina:
        screen.blit(boton_texto_maquina, boton_rect_texto_maquina)
        screen.blit(texto_puntaje_maquina, texto_puntaje_maquina_rect)


        #Texto puntaje total partidas jugador
        texto_puntaje_total_jugador = fuente_puntajes.render(f"Partidas ganadas J: {datos_partidas["Jugador"]}", True, (255, 255, 255))
        texto_puntaje_total_jugador_rect = texto_puntaje_total_jugador.get_rect()
        texto_puntaje_total_jugador_rect.center = boton_rect_texto_total_partidas_jugador.center
        texto_puntaje_total_jugador_rect.y = texto_puntaje_total_jugador_rect.y + 6

        #Texto puntaje total partidas maquina
        texto_puntaje_total_maquina = fuente_puntajes.render(f"Partidas ganadas M: {datos_partidas["Maquina"]}", True, (255, 255, 255))
        texto_puntaje_total_maquina_rect = texto_puntaje_total_maquina.get_rect()
        texto_puntaje_total_maquina_rect.center = boton_rect_texto_total_partidas_maquina.center
        texto_puntaje_total_maquina_rect.y = texto_puntaje_total_maquina_rect.y + 6

        #Dibujar texto puntaje total jugador
        screen.blit(boton_total_partidas_jugador, boton_rect_texto_total_partidas_jugador)
        screen.blit(texto_puntaje_total_jugador, texto_puntaje_total_jugador_rect)

        #Dibujar puntaje total maquina:
        screen.blit(boton_total_partidas_maquina, boton_rect_texto_total_partidas_maquina)
        screen.blit(texto_puntaje_total_maquina, boton_rect_texto_total_partidas_maquina)

        #Dibujar texto de perder
        screen.blit(boton, boton_rect)
        screen.blit(texto1, texto1_rect)


def mostrar_puntaje_partida(screen,puntaje_partida_jugador:int, puntaje_partida_maquina:int):
    '''
    Recibe la pantalla y los puntajes del jugador y de la maquina
    Dibuja los puntajes en la pantalla
    
    '''
    #Boton texto jugador:
    boton_texto_jugador = pygame.image.load("ImagenesMenu/banner.png")
    boton_texto_jugador = pygame.transform.scale(boton_texto_jugador, (1000, 300))
    boton_rect_texto_jugador = boton_texto_jugador.get_rect()
    boton_rect_texto_jugador.center = (350, 1000)

    #Boton texto maquina:
    boton_texto_maquina = pygame.image.load("ImagenesMenu/banner.png")
    boton_texto_maquina = pygame.transform.scale(boton_texto_maquina, (1000, 300))
    boton_rect_texto_maquina = boton_texto_maquina.get_rect()
    boton_rect_texto_maquina.center = (screen.get_width() // 2 + 600, 1000)

    #Texto puntaje jugador:
    fuente = pygame.font.Font("Fuentes/fuente_und.ttf", 90)
    texto_puntaje_jugador = fuente.render(f"Jugador: {puntaje_partida_jugador}", True, (255, 255, 255))
    texto_puntaje_jugador_rect = texto_puntaje_jugador.get_rect()
    texto_puntaje_jugador_rect.center = boton_rect_texto_jugador.center
    texto_puntaje_jugador_rect.y = texto_puntaje_jugador_rect.y + 6

    #Texto puntaje maquina:
    texto_puntaje_maquina = fuente.render(f"Maquina: {puntaje_partida_maquina}", True, (255, 255, 255))
    texto_puntaje_maquina_rect = texto_puntaje_maquina.get_rect()
    texto_puntaje_maquina_rect.center = boton_rect_texto_maquina.center
    texto_puntaje_maquina_rect.y = texto_puntaje_maquina_rect.y + 6

    #Dibujar datos jugador:
    screen.blit(boton_texto_jugador, boton_rect_texto_jugador)
    screen.blit(texto_puntaje_jugador, texto_puntaje_jugador_rect)

    #Dibujar datos maquina:
    screen.blit(boton_texto_maquina, boton_rect_texto_maquina)
    screen.blit(texto_puntaje_maquina, texto_puntaje_maquina_rect)


def puede_envido(cartas_jugador: list) -> bool:

    '''
    Recibe una lista con las cartas del jugador
    Verifica si el jugador tiene 2 o mas cartas del mismo palo
    Devuelve un booleano
    '''

    cartas_mismo_palo = 0

    for carta in cartas_jugador:
        for carta_2 in cartas_jugador:
            if carta.palo == carta_2.palo and carta.numero != carta_2.numero:
                cartas_mismo_palo += 1
    
    if cartas_mismo_palo >= 2:
        #print(f"Las cartas del mismo palo son {cartas_mismo_palo}")
        return True
    else:
        return False
    
def cantar_envido(cartas_jugador: list, cartas_maquina:list, puntaje_jugador_partida:int, puntaje_maquina_partida:int) -> str:
    '''
    Recibe dos listas, una con las cartas del jugador y otra con las de la maquina
    Suma el envido total de cada uno
    Devuelve el retorno de la funcion "verificar_ganador_envido"
    '''
    
    total_envido_jugador = 0
    total_envido_maquina = 0
    for carta in cartas_jugador:
        for carta_2 in cartas_jugador:
            if carta.palo == carta_2.palo and carta.numero != carta_2.numero:
                total_envido_jugador += carta.valor_envido
    
    for carta in cartas_maquina:
        for carta_2 in cartas_maquina:
            if carta.palo == carta_2.palo and carta.numero != carta_2.numero:
                total_envido_maquina += carta.valor_envido

    return verificar_ganador_envido(total_envido_jugador, total_envido_maquina, puntaje_jugador_partida, puntaje_maquina_partida)

def verificar_ganador_envido(total_envido_jugador:int, total_envido_maquina:int, puntaje_jugador_partida:int, puntaje_maquina_partida:int) -> str:
    '''
    Recibe dos enteros
    Evalua cual es mayor
    Devuelve los puntajes sumados de cada jugador
    '''

    if total_envido_jugador >= total_envido_maquina:
        puntaje_jugador_partida += 2
        return puntaje_jugador_partida, puntaje_maquina_partida
    elif total_envido_maquina >= total_envido_jugador:
        puntaje_maquina_partida += 2
        return puntaje_jugador_partida, puntaje_maquina_partida


