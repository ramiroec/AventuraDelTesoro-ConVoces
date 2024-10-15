import os
import time
import random
from gtts import gTTS
import pygame

def reproducir_audio(texto, nombre_archivo="temp.mp3"):
    """Convierte el texto a audio, lo guarda temporalmente y lo reproduce usando pygame."""
    try:
        # Convertir el texto a audio usando gTTS y guardar en un archivo temporal
        tts = gTTS(text=texto, lang='es')
        tts.save(nombre_archivo)

        # Inicializar el mixer de pygame
        pygame.mixer.init()

        # Cargar y reproducir el archivo de audio
        pygame.mixer.music.load(nombre_archivo)
        pygame.mixer.music.play()

        # Esperar hasta que termine la reproducción
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Detener el mixer y limpiar
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error al reproducir el audio: {e}")
    finally:
        # Eliminar el archivo temporal
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def bienvenida():
    mensaje = "🏝️ ¡Bienvenido a la Aventura del Tesoro! 🏝️\nTienes que tomar decisiones inteligentes para encontrar el tesoro.\n¿Estás listo para comenzar? ¡Vamos!\n"
    print(mensaje)
    reproducir_audio(mensaje)

def camino():
    mensaje = "Te encuentras en una encrucijada.\n1. Tomar el camino de la derecha 🌳\n2. Tomar el camino de la izquierda 🏞️\n"
    print(mensaje)
    reproducir_audio(mensaje)
    eleccion = input("¿Qué camino eliges? (1 o 2): ")
    return eleccion

def enfrentar_enemigo():
    enemigos = ["dragón 🐉", "pirata 🏴‍☠️", "serpiente 🐍"]
    enemigo = random.choice(enemigos)
    mensaje = f"¡Oh no! Te has encontrado con un {enemigo} en tu camino.\n1. Luchar 🗡️\n2. Huir 🏃‍♂️\n"
    print(mensaje)
    reproducir_audio(mensaje)
    accion = input("¿Qué decides hacer? (1 o 2): ")
    
    if accion == "1":
        if random.randint(1, 2) == 1:
            mensaje_ganar = f"¡Ganaste la batalla contra el {enemigo}! 🎉\n"
            print(mensaje_ganar)
            reproducir_audio(mensaje_ganar)
            return True
        else:
            mensaje_perder = f"Has sido derrotado por el {enemigo}... 😢\n"
            print(mensaje_perder)
            reproducir_audio(mensaje_perder)
            return False
    else:
        mensaje_huir = "¡Escapaste con éxito! Pero has perdido tiempo... ⏳\n"
        print(mensaje_huir)
        reproducir_audio(mensaje_huir)
        return True

def buscar_tesoro():
    mensaje = "Has llegado a una cueva misteriosa.\n1. Entrar en la cueva 🕯️\n2. Seguir explorando afuera 🚶‍♂️\n"
    print(mensaje)
    reproducir_audio(mensaje)
    eleccion = input("¿Qué decides hacer? (1 o 2): ")
    
    if eleccion == "1":
        if random.randint(1, 3) == 3:
            mensaje_tesoro = "🎉 ¡Has encontrado el tesoro mágico! ¡Felicidades! 🏆💰\n"
            print(mensaje_tesoro)
            reproducir_audio(mensaje_tesoro)
            return True
        else:
            mensaje_no_tesoro = "La cueva está vacía... Sigue buscando. 🔍\n"
            print(mensaje_no_tesoro)
            reproducir_audio(mensaje_no_tesoro)
            return False
    else:
        mensaje_no_entrar = "Decidiste no entrar. Sigues explorando...\n"
        print(mensaje_no_entrar)
        reproducir_audio(mensaje_no_entrar)
        return False

def aventura():
    bienvenida()
    
    # Primera decisión de caminos
    eleccion_camino = camino()
    
    if eleccion_camino == "1":
        mensaje_camino = "Tomaste el camino de la derecha y avanzas por el bosque.\n"
    elif eleccion_camino == "2":
        mensaje_camino = "Tomaste el camino de la izquierda y sigues por una playa solitaria.\n"
    else:
        mensaje_invalido = "Elección no válida. Estás perdido en la isla. 🏝️\n"
        print(mensaje_invalido)
        reproducir_audio(mensaje_invalido)
        return
    
    print(mensaje_camino)
    reproducir_audio(mensaje_camino)
    
    # Enfrentando un enemigo
    si_superaste_enemigo = enfrentar_enemigo()
    if not si_superaste_enemigo:
        mensaje_fin = "Fin de la aventura. ¡Inténtalo de nuevo!\n"
        print(mensaje_fin)
        reproducir_audio(mensaje_fin)
        return
    
    # Buscar el tesoro
    si_encontraste_tesoro = buscar_tesoro()
    if si_encontraste_tesoro:
        mensaje_final_exito = "¡Eres el gran aventurero de la isla del tesoro! 🎉\n"
        print(mensaje_final_exito)
        reproducir_audio(mensaje_final_exito)
    else:
        mensaje_final_fallo = "El tesoro sigue perdido. ¡Sigue buscando en otra aventura!\n"
        print(mensaje_final_fallo)
        reproducir_audio(mensaje_final_fallo)

    # Mensaje de despedida
    mensaje_despedida = "¡Gracias por jugar! 🏝️ Hasta la próxima aventura.\n"
    print(mensaje_despedida)
    reproducir_audio(mensaje_despedida)

if __name__ == "__main__":
    aventura()
