#Boton Salir
import pygame

pygame.init()

#Sonidos menu
sonido_musica_menu = pygame.mixer.Sound("Sonidos/ost.mp3")
sonido_opciones =  pygame.mixer.Sound("Sonidos/sonido_opciones.wav")
sonido_click_opciones = pygame.mixer.Sound("Sonidos/menu_click.wav")

#Sonidos juego
sonido_carta = pygame.mixer.Sound("Sonidos/sonido_carta.mp3")
sonido_tirar_carta = pygame.mixer.Sound("Sonidos/tirar_carta_sonido.wav")
sonido_ambiente_juego = pygame.mixer.Sound("Sonidos/ruins_slowed.mp3")
sonido_notificacion_truco = pygame.mixer.Sound("Sonidos/notificacion.mp3")


#Fuente de los botones
fuente_boton = pygame.font.Font("Fuentes/fuente_und.ttf", 52)
fuente_boton_escalada = pygame.font.Font("Fuentes/fuente_und.ttf", 70)


#Variables boton_salir
posicion_boton_salir = (200, 100)
escala_boton_salir = (300, 150)
ruta_imagen_boton_salir = "ImagenesMenu/banner.png"
escala_boton_agrandado = (350, 170)
texto_boton_salir = "Salir"
color_texto_salir = (150, 150, 150)

color_texto_escalado = (255, 255, 255)

posicion = ()

boton_salir = {
    "posicion": posicion_boton_salir,
    "escala_boton": escala_boton_salir,
    "escala_boton_agrandado": escala_boton_agrandado,
    "ruta_imagen": ruta_imagen_boton_salir,
    "fuente": fuente_boton,
    "fuente_escalado": fuente_boton_escalada,
    "texto": texto_boton_salir,
    "color_texto": color_texto_salir,
    "color_escalado": color_texto_escalado
}

posicion_boton_salir_terminado = (960, 700)

boton_salir_terminado = {
    "posicion": posicion_boton_salir_terminado,
    "escala_boton": escala_boton_salir,
    "escala_boton_agrandado": escala_boton_agrandado,
    "ruta_imagen": ruta_imagen_boton_salir,
    "fuente": fuente_boton,
    "fuente_escalado": fuente_boton_escalada,
    "texto": texto_boton_salir,
    "color_texto": color_texto_salir,
    "color_escalado": color_texto_escalado
}

#Variables boton_truco

posicion_boton_truco = (400, 800)
escala_boton_truco = (300, 150)
ruta_imagen_boton_truco = "ImagenesMenu/banner.png"
texto_boton_truco = "Truco"
color_texto_truco = (150, 150, 150)

boton_truco = {
    "posicion":  posicion_boton_truco,
    "escala_boton": escala_boton_truco,
    "escala_boton_agrandado": escala_boton_agrandado,
    "ruta_imagen": ruta_imagen_boton_truco,
    "fuente": fuente_boton,
    "fuente_escalado": fuente_boton_escalada,
    "texto": texto_boton_truco,
    "color_texto": color_texto_truco,
    "color_escalado": color_texto_escalado

}
posicion_boton_envido = (700, 600)
texto_boton_envido = "Envido"

boton_envido = {
    "posicion":  posicion_boton_envido,
    "escala_boton": escala_boton_truco,
    "escala_boton_agrandado": escala_boton_agrandado,
    "ruta_imagen": ruta_imagen_boton_truco,
    "fuente": fuente_boton,
    "fuente_escalado": fuente_boton_escalada,
    "texto": texto_boton_envido,
    "color_texto": color_texto_truco,
    "color_escalado": color_texto_escalado

}