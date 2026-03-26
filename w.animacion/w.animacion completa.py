import tkinter as tk
import math

ventana_a = tk.Tk()
ventana_a.title("Animación")
ventana_a.geometry("700x500")
ventana_a.config(bg="olivedrab1")
ventana_a.resizable(False,False)
ventana_a.attributes(alpha=0.95)

block_texto= tk.Frame(ventana_a, bg="olivedrab1")
block_velocidad = tk.Frame(ventana_a, bg="olivedrab1")

ATBienvenida=tk.Label(ventana_a,text="Bienvenido a animación",bg="olivedrab1", fg="grey60", font=("Impact", 18) )
ATvelocidad = tk.Label(block_texto, text="Ajusta la barra para configurar la velocidad",bg="olivedrab1", fg="grey60", font=("Impact", 15) )

def cerraranimacion():
    ventana_a.destroy()

BotonCA = tk.Button(ventana_a, text="Cerrar", command=cerraranimacion, bg="light cyan1",fg="grey60", font=("Impact", 12) )
barravelocidad = tk.Scale(block_velocidad, from_=0, to=85, orient=tk.HORIZONTAL, length=300,tickinterval=10, bg="olivedrab1", fg="grey60", font=("Impact", 12))
barravelocidad.set(50)

#Animacion de las pelotas
ANCHO_C, ALTO_C = 600, 300
r = 20
x1, y1, dx1, dy1 = 100, 100, 4, 3
x2, y2, dx2, dy2 = 500, 200, -3, -4

block_pelotas =tk.Canvas(ventana_a, bg="light cyan1", width=ANCHO_C, height=ALTO_C)
p1_id = block_pelotas.create_oval(x1-r, y1-r, x1+r, y1+r, fill="red", outline="black")
p2_id = block_pelotas.create_oval(x2-r, y2-r, x2+r, y2+r, fill="blue", outline="black")

def mover():
    global x1, y1, dx1, dy1, x2, y2, dx2, dy2

    x1 += dx1
    y1 += dy1
    if x1 - r <= 0 or x1 + r >= ANCHO_C: dx1 *= -1
    if y1 - r <= 0 or y1 + r >= ALTO_C: dy1 *= -1

    x2 += dx2
    y2 += dy2
    if x2 - r <= 0 or x2 + r >= ANCHO_C: dx2 *= -1
    if y2 - r <= 0 or y2 + r >= ALTO_C: dy2 *= -1

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distancia < (r * 2):
        dx1, dx2 = dx2, dx1
        dy1, dy2 = dy2, dy1

        x1 += dx1; y1 += dy1; x2 += dx2; y2 += dy2

    block_pelotas.coords(p1_id, x1-r, y1-r, x1+r, y1+r)
    block_pelotas.coords(p2_id, x2-r, y2-r, x2+r, y2+r)

    valor_barra = barravelocidad.get()
    if valor_barra == 0:
        espera = 100
    else:
        espera = int(100 - valor_barra + 1) 

    block_pelotas.after(espera, mover)

ATBienvenida.pack()
block_pelotas.pack()
block_pelotas.propagate(False)
block_texto.pack()
block_velocidad.pack()

ATvelocidad.pack()
barravelocidad.pack()
BotonCA.pack()
mover()
ventana_a.mainloop()