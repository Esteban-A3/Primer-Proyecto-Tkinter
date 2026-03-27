import tkinter as tk
import pygame as pg
from tkinter import Toplevel

#Proyecto de Esteban Alejandro Sanchez Ledezma
#Consejo: Si esta en visual code use los corchetes para cerrar las funciones, asi se puede analizar mejor el codigo


#Funcion de analisis de pares
def analisis_pares(num):
    if not isinstance(num,int): #Se podria quitar estas restrincciones ya que la ventana ya las aplica pero las dejo para no danar la funcion
        return "Error: Por favor introducir un número entero"
    if num<=0:
        return  "No posee factores positivos"
    else:
        return analisis_pares_aux(num,1)
def analisis_pares_aux(num, i):
    if i > int(num**0.5):
        return ()

    elif num%i == 0:
        return (((i, num//i),) + analisis_pares_aux(num, i+1))

    else:
        return analisis_pares_aux(num,i+1)


pg.mixer.init()
paused = False 
music = False

def playmusic():
    global paused
    global music
    if music== False:
        if paused==True:
            pg.mixer.music.unpause()
            paused=False
            music=True
        else:
            pg.mixer.music.load("Proyecto Multimedia/Me and Michael.mp3")
            pg.mixer.music.play()
    else:
        ()
def pausemusic():
    global paused
    global music
    pg.mixer.music.pause()
    paused=True
    music=False
def stopmusic():
    global paused
    global music
    pg.mixer.music.stop()
    paused=False
    music=False
def restardmusic():
    global paused
    global music
    pg.mixer.music.stop()
    pg.mixer.music.load("Proyecto Multimedia/Me and Michael.mp3")
    pg.mixer.music.play()
    paused = False
    music = True


ventana_actual = None   #variable para saber si hay una ventana activa

#Ventana de Analisis
def abrir_ventana_a():
    global ventana_actual
    
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
        stopmusic()     #Por si se dejo la musica activa en la ventana informacion
    
    ventana_a = Toplevel(ventana_m)
    ventana_a.title("Analizador de Números")
    ventana_a.geometry("600x400")
    ventana_a.config(bg="tomato")
    ventana_a.attributes(alpha=0.95)
    ventana_a.resizable(False,False)

    sideanalizar= tk.Frame(ventana_a)
    sideanalizar.config(bg="indianred1", bd=10, width=450, height=200)

    ATBienvenida=tk.Label(ventana_a,text="Bienvenido al Analizador",bg="Tomato", fg="White", font=("Impact", 24) )
    m_bienvenida= tk.Label(sideanalizar, text="Introdusca un número entero para analizar")
    m_bienvenida.config(bg="indianred1",fg="gold", font=("Impact",15))

    entrada_a= tk.Entry(sideanalizar)
    entrada_a.config(bg="azure2", fg="gray25", font=("Impact",12))
    entrada_a.insert(0, "Ejemplo: 10")
    def pares():
        valor = entrada_a.get()
        if not valor or valor == "Ejemplo: 10":
            resultado.config(text="⚠️ Por favor ingrese un número")
            return
        elif valor.isdigit():
            num = int(valor)
            if num > 100000:
                resultado.config(text="⚠️ Límite excedido: Intenta con un numero menor (Máx: 100,000)") #Limite para proteger interfaz. El verdadero limite de la funcion es 1 millon
                return
            else:
                res = analisis_pares(num)
                resultado.config(text=f"Factores de {num} = {res}")
        else:
            resultado.config(text="❌ Entrada inválida, debe ser un entero positivo")
    analizar=tk.Button(sideanalizar, text="Analizar", command=pares)
    analizar.config(bg="azure2", fg="gray23", font=("Impact", 12))

    resultado=tk.Label(sideanalizar, text="")
    resultado.config(bg="indianred1", fg="gold", font=("impact", 13, "italic"), wraplength=350, justify="center")
    def cerraranalizador():
        ventana_a.destroy()

    BotonCA = tk.Button(ventana_a, text="Cerrar", command=cerraranalizador, bg="white", fg="grey60", font=("Impact", 12), relief=tk.RAISED)

    ATBienvenida.pack()
    sideanalizar.place(relx=0.5,rely=0.5, anchor="center")
    sideanalizar.pack_propagate(False)
    m_bienvenida.pack()
    entrada_a.pack()
    resultado.pack()
    analizar.pack()
    BotonCA.place(relx=0.50,rely=0.90, anchor="center")

    ventana_actual = ventana_a
#Ventana de Informacion
def abrir_ventana_i():
    global ventana_actual
    
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
    
    ventana_i = Toplevel(ventana_m)
    ventana_i.title("Ventana de información")
    ventana_i.geometry("700x500")
    ventana_i.config(bg="sky blue")
    ventana_i.resizable(False, False)
    ventana_i.attributes(alpha=0.95)

    block_nce = tk.Canvas(ventana_i, bg="light cyan1", bd=5, width=400, height=100)
    block_bio = tk.Canvas(ventana_i, bg="light cyan2", bd=5, width=400, height=200)
    block_music = tk.Canvas(ventana_i, bg="light cyan3", bd=5, width=400, height=100)
    block_foto = tk.Frame(ventana_i, bg="pale green1", bd=8, width=150, height=200)
    block_l = tk.Canvas(ventana_i, bg="pale green2", bd=8, width=250, height=130)
    musiccentertext = tk.Frame(block_music,bg="light cyan3")

    def cerrarVentanaInformacion():
        ventana_i.destroy()

    botonCi = tk.Button(ventana_i,text="Cerrar",command= cerrarVentanaInformacion, bg="white", fg="grey60", font=("Impact", 12), relief=tk.RAISED)

    nombre = tk.Label(block_nce, text="Esteban Sánchez Ledezma", bg="light cyan1", fg="grey60", font=("Impact", 15))
    carnet = tk.Label(block_nce, text="2026108570", bg="light cyan1", fg="grey60", font=("Impact", 15))
    edad = tk.Label(block_nce, text="19 años", bg="light cyan1", fg="grey60", font=("Impact", 15))

    programadorM = tk.PhotoImage(file="Proyecto Multimedia/Programador.png")
    sideP= tk.Label(block_foto, image=programadorM)
    sideP.image = programadorM

    lugar= tk.PhotoImage(file="Proyecto Multimedia/lugar.png")
    sideL= tk.Label(block_l, image=lugar)
    sideL.image = lugar 
    textoL = tk.Label(block_l, text="Lugar donde vive:", bg="pale green2", fg="grey60", font=("Impact", 15) )

    textobiografia = """Soy técnico electromecánico graduado y actualmente estudiante de Ingeniería en Computadores en el Tecnológico de Costa Rica. 
    Además, he complementado mi formación en el área de redes, alcanzando el nivel de CCNA 3 con certificación académica. 

    Me caracterizo por ser una persona proactiva, con gran interés en la tecnología, la programación y las redes. 
    Busco constantemente fortalecer mis conocimientos y adquirir nuevas habilidades que me permitan crecer profesionalmente.
    Mi objetivo es desarrollarme como ingeniero en computación y aportar soluciones innovadoras en el ámbito tecnológico."""

    biografia = tk.Label(block_bio, text=textobiografia,font=("Time new Roman", 9), wraplength=380,fg="grey40", justify="left", bg="light cyan2")
    biografia.pack(padx=5, pady=5)

    bandaygenero = """Nombre de la banda: MGMT 
    Genero: Indi Rock
    Canción: Me and Michael"""

    textoM = tk.Label(block_music, text=bandaygenero, bg="light cyan3", fg="grey60", font=("Impact", 12))

    Ibanda = tk.PhotoImage(file="Proyecto Multimedia/banda.png")
    sideIb = tk.Label(musiccentertext, image=Ibanda)
    sideIb.image = Ibanda 

    botonBack = tk.Button(musiccentertext, text="⏮",command=restardmusic)
    botonPlay = tk.Button(musiccentertext, text="▶", command=playmusic)
    botonPause = tk.Button(musiccentertext, text="⏸", command=pausemusic)
    botonstop = tk.Button(musiccentertext, text="⏹", command=stopmusic)

    block_nce.place(relx=0.3, rely=0.16, anchor="center")
    block_nce.propagate(False)

    block_bio.place(relx=0.3, rely=0.5, anchor="center")
    block_bio.propagate(False)

    block_music.place(relx=0.3, rely=0.84, anchor="center")
    block_music.propagate(False)

    block_foto.place(relx=0.80, rely=0.25, anchor="center")
    block_foto.propagate(False)

    block_l.place(relx=0.80, rely=0.70, anchor="center")
    block_l.propagate(False)

    botonCi.place(x=530, y=440)
    nombre.pack()
    carnet.pack()
    edad.pack()
    sideP.pack()
    textoL.pack()
    sideL.pack()
    textoM.pack()

    musiccentertext.pack(expand=True)
    sideIb.pack(side="left", anchor="center",padx=10)
    botonBack.pack(side="left", padx=5)
    botonPlay.pack(side="left", padx=5)
    botonPause.pack(side="left",padx=5)
    botonstop.pack(side="left", padx=5)
    ventana_actual = ventana_i
#Ventana de Animcacion
def abrir_ventana_an():
    global ventana_actual    
    
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
        stopmusic()     #Por si se dejo la musica activa en la ventana informacion

    ventana_an = Toplevel(ventana_m)
    ventana_an.title("Animación")
    ventana_an.geometry("700x500")
    ventana_an.config(bg="olivedrab1")
    ventana_an.resizable(False,False)
    ventana_an.attributes(alpha=0.95)

    block_texto= tk.Frame(ventana_an, bg="olivedrab1")
    block_velocidad = tk.Frame(ventana_an, bg="olivedrab1")

    ATNBienvenida=tk.Label(ventana_an,text="Bienvenido a animación",bg="olivedrab1", fg="grey60", font=("Impact", 18) )
    ATNvelocidad = tk.Label(block_texto, text="Ajusta la barra para configurar la velocidad",bg="olivedrab1", fg="grey60", font=("Impact", 15) )

    def cerraranimacion():
        ventana_an.destroy()

    BotonCAN = tk.Button(ventana_an, text="Cerrar", command=cerraranimacion, bg="light cyan1",fg="grey60", font=("Impact", 12), relief=tk.RAISED)
    barravelocidad = tk.Scale(block_velocidad, from_=0, to=85, orient=tk.HORIZONTAL, length=300,tickinterval=10, bg="olivedrab1", fg="grey60", font=("Impact", 12))
    barravelocidad.set(50)
    ANCHO_C, ALTO_C = 600, 300
    r = 20
    x1, y1, dx1, dy1 = 100, 100, 4, 3
    x2, y2, dx2, dy2 = 500, 200, -3, -4

    block_pelotas =tk.Canvas(ventana_an, bg="light cyan1", width=ANCHO_C, height=ALTO_C)
    p1_id = block_pelotas.create_oval(x1-r, y1-r, x1+r, y1+r, fill="red", outline="black")
    p2_id = block_pelotas.create_oval(x2-r, y2-r, x2+r, y2+r, fill="blue", outline="black")

    def mover():
        nonlocal x1, y1, dx1, dy1, x2, y2, dx2, dy2 

        x1 += dx1
        y1 += dy1
        if x1 - r <= 0 or x1 + r >= ANCHO_C: 
            dx1 *= -1
        if y1 - r <= 0 or y1 + r >= ALTO_C: 
            dy1 *= -1

        x2 += dx2
        y2 += dy2
        if x2 - r <= 0 or x2 + r >= ANCHO_C: 
            dx2 *= -1
        if y2 - r <= 0 or y2 + r >= ALTO_C: 
            dy2 *= -1
        
        if (x2 - x1)**2 + (y2 - y1)**2 <= (2*r)**2:
            dx1, dx2 = dx2, dx1
            dy1, dy2 = dy2, dy1

            x1 += dx1 * 2
            y1 += dy1 * 2
            x2 += dx2 * 2
            y2 += dy2 * 2

        block_pelotas.coords(p1_id, x1-r, y1-r, x1+r, y1+r)
        block_pelotas.coords(p2_id, x2-r, y2-r, x2+r, y2+r)

        valor_barra = barravelocidad.get()
        if valor_barra == 0:
            espera = 100
        else:
            espera = int(100 - valor_barra + 1) 

        block_pelotas.after(espera, mover)


    ATNBienvenida.pack()
    block_pelotas.pack()
    block_pelotas.propagate(False)
    block_texto.pack()
    block_velocidad.pack()

    ATNvelocidad.pack()
    barravelocidad.pack()
    BotonCAN.pack()
    mover()
    ventana_actual = ventana_an



def cerrarmenu():
    ventana_m.destroy()

#Ventana de Menu
ventana_m = tk.Tk()
ventana_m.title("Menu")
ventana_m.geometry("900x500")
ventana_m.config(bg="aquamarine")
ventana_m.resizable(False, False)
ventana_m.attributes("-alpha", 0.95)

Bienvenida = tk.Label(ventana_m, text="Bienvenido", bg="aquamarine", fg="White", font=("Impact", 50))
Bienvenida.pack()

Mensaje = tk.Label(ventana_m, text="Selecciona un botón para abrir una pestaña", bg="aquamarine", fg="White", font=("Impact", 25))
Mensaje.pack()

BlockVentanas = tk.Frame(ventana_m, bg="aquamarine")
BlockVentanas.pack(pady=20)

botonwA = tk.Button(BlockVentanas, width=25, height=10, text="Analizador de Números", bg="tomato", fg="White", font=("Impact"), command=lambda: abrir_ventana_a())
botonwI = tk.Button(BlockVentanas, width=25, height=10, text="Información del programador", bg="sky blue", fg="White", font=("Impact"), command=lambda: abrir_ventana_i())
BotonwP = tk.Button(BlockVentanas, width=25, height=10, text="Animación", bg="olivedrab1", fg="White", font=("Impact"), command=lambda: abrir_ventana_an())


botonwA.grid(row=0, column=0, padx=10)
botonwI.grid(row=0, column=1, padx=10)
BotonwP.grid(row=0, column=2, padx=10)

BotonCM = tk.Button(ventana_m, text="Cerrar", command=cerrarmenu, bg="white", fg="grey60", font=("Impact", 12), relief=tk.RAISED)
BotonCM.pack(pady=5)

ventana_m.mainloop()