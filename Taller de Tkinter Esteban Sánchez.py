import tkinter as tk
import pygame as pg
from tkinter import Toplevel


ventana_actual = None

def abrir_ventana(nombre):
    global ventana_actual
    
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
    
    nueva_ventana = Toplevel(ventana_m)
    nueva_ventana.title(f"Ventana: {nombre}")
    nueva_ventana.geometry("400x300")
    nueva_ventana.config(bg="white")
    
    tk.Label(nueva_ventana, text=f"Ventana {nombre}", bg="white", font=("Impact", 20)).pack(pady=50)
    
    ventana_actual = nueva_ventana



def cerrarmenu():
    ventana_m.destroy()

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

botonwA = tk.Button(BlockVentanas, width=25, height=10, text="Analizador de Números", bg="tomato", fg="White", font=("Impact"), command=lambda: abrir_ventana("Analizador"))
botonwI = tk.Button(BlockVentanas, width=25, height=10, text="Información del programador", bg="sky blue", fg="White", font=("Impact"), command=lambda: abrir_ventana("Información"))
BotonwP = tk.Button(BlockVentanas, width=25, height=10, text="Animación", bg="olivedrab1", fg="White", font=("Impact"), command=lambda: abrir_ventana("Animación"))


botonwA.grid(row=0, column=0, padx=10)
botonwI.grid(row=0, column=1, padx=10)
BotonwP.grid(row=0, column=2, padx=10)

BotonCM = tk.Button(ventana_m, text="Cerrar", command=cerrarmenu, bg="white", fg="grey60", font=("Impact", 12), relief=tk.RAISED)
BotonCM.pack(pady=20)

ventana_m.mainloop()