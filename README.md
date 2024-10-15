
# Aventura del Tesoro con Narración

Este es un juego interactivo de texto donde tomas decisiones para encontrar el tesoro escondido en una isla misteriosa. El juego incluye una narración en español que utiliza la librería `gTTS` para generar la voz y `pygame` para reproducirla. 

## Características
- Narración automática para todas las decisiones y eventos importantes del juego.
- Interacciones con enemigos y búsqueda de tesoros.
- Reproducción de audio en tiempo real mientras juegas.

## Requisitos
Este proyecto requiere Python 3.x y las siguientes librerías:

- `gTTS` (Google Text-to-Speech) para convertir texto a voz.
- `pygame` para la reproducción de los archivos de audio generados.
  
Puedes instalarlas con los siguientes comandos:

```bash
pip install gtts pygame
```

## Cómo jugar

1. Clona el repositorio o descarga el archivo del proyecto.
2. Ejecuta el archivo `main.py` en tu entorno local.
3. Sigue las instrucciones en pantalla para avanzar en la aventura.

```bash
python main.py
```

## Estructura del Proyecto

- **main.py**: Contiene el código principal del juego.
- **README.md**: Este archivo de documentación.
  
## Funcionalidades Clave

- **Narración dinámica**: Usa Google Text-to-Speech (gTTS) para generar archivos de audio con la narración de cada sección del juego.
- **Reproducción de audio**: Los archivos de voz se reproducen en tiempo real a medida que el jugador avanza en la historia.

## Autor
Este proyecto fue creado por **Ramiro Estigarribia**.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un _fork_ y abrir una solicitud de extracción.
