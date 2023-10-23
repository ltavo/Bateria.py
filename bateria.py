import pygame
import keyboard

#Inicializamos pygame
pygame.init()

#Variable para rastrear el estado de la tecla
tecla_presionada = False

#Reproducir sonido
while True:
    event = keyboard.read_event()

    print(f"Tecla: {event.name}, Tipo: {event.event_type}")

    if event.event_type == keyboard.KEY_DOWN and event.name == 's':
        sonido = pygame.mixer.Sound('song/5592.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        sonido = pygame.mixer.Sound('song/7741.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
        sonido = pygame.mixer.Sound('song/7739.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        sonido = pygame.mixer.Sound('song/6595.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        sonido = pygame.mixer.Sound('song/6586.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'e':
        sonido = pygame.mixer.Sound('song/7483.mp3')
        sonido.play()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'r':
        sonido = pygame.mixer.Sound('song/7756.mp3')
        sonido.play()

#Mantener el programa en espera miestars el sonido se reproduzca completamente
pygame.time.delay(int(sonido.get_length() * 1000)) #convertir a milisegundos