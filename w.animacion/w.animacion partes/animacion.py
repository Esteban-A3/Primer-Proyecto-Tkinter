import tkinter as tk
import math

root = tk.Tk()
root.title("Pelotas con Control")

ANCHO_C, ALTO_C = 400, 400
canvas = tk.Canvas(root, width=ANCHO_C, height=ALTO_C, bg="green", bd=0, highlightthickness=0)
canvas.pack(pady=10)

r = 20
x1, y1, dx1, dy1 = 100, 100, 4, 3
x2, y2, dx2, dy2 = 300, 300, -3, -4

p1_id = canvas.create_oval(x1-r, y1-r, x1+r, y1+r, fill="red", outline="black")
p2_id = canvas.create_oval(x2-r, y2-r, x2+r, y2+r, fill="blue", outline="black")


barra = tk.Scale(root, from_=0, to=85, orient=tk.HORIZONTAL, length=300, label="Velocidad (FPS)")
barra.set(50) 
barra.pack(pady=10)

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

    canvas.coords(p1_id, x1-r, y1-r, x1+r, y1+r)
    canvas.coords(p2_id, x2-r, y2-r, x2+r, y2+r)

    valor_barra = barra.get()
    if valor_barra == 0:
        espera = 100
    else:
        espera = int(100 - valor_barra + 1) 

    root.after(espera, mover)

mover()
root.mainloop()