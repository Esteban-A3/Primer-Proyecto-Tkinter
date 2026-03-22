import tkinter  as tk
import pygame

pygame.mixer.init()

paused = False
music = False

def playmusic():
    global paused
    global music
    if music== False:
        if paused==True:
            pygame.mixer.music.unpause()
            paused=False
            music=True
        else:
            pygame.mixer.music.load("w.informacion partes/Me and Michael.mp3")
            pygame.mixer.music.play()
    else:
        ()

def pausemusic():
    global paused
    global music
    pygame.mixer.music.pause()
    paused=True
    music=False

def stopmusic():
    global paused
    global music
    pygame.mixer.music.stop()
    paused=False
    music=False

def restardmusic():
    global paused
    global music
    pygame.mixer.music.stop()
    pygame.mixer.music.load("w.informacion partes/Me and Michael.mp3")
    pygame.mixer.music.play()
    paused = False
    music = True


pruebamusica= tk.Tk()
pruebamusica.title("Reproductor prueba")
pruebamusica.geometry("300x200")

botonplay = tk.Button(pruebamusica, text="▶️ Reproducir", command=playmusic)
botonplay.pack(pady=10)

botonpause = tk.Button(pruebamusica, text="⏸️ Pausar", command=pausemusic)
botonpause.pack(pady=10)

botonstop = tk.Button(pruebamusica, text="⏹️ Detener", command=stopmusic)
botonstop.pack(pady=10)

botonrestard = tk.Button(pruebamusica, text="⏮️ Retroceso", command=restardmusic)
botonrestard.pack(pady=10)

pruebamusica.mainloop()