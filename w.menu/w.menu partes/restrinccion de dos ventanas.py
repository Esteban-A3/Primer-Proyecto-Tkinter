import tkinter as tk
from tkinter import Toplevel

ventana_actual = None

def abrir_ventana(nombre):
    global ventana_actual
    
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
    
    nueva_ventana = Toplevel(root)
    nueva_ventana.title(f"Ventana {nombre}")
    nueva_ventana.geometry("300x200")
    
    tk.Label(nueva_ventana, text=f"Contenido de la {nombre}", font=("Arial", 12)).pack(pady=40)
    
    ventana_actual = nueva_ventana

root = tk.Tk()
root.title("Menú Principal")
root.geometry("400x300")

tk.Label(root, text="Panel de Control", font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(root, text="Ir a Ventana A", width=20, command=lambda: abrir_ventana("A")).pack(pady=10)
tk.Button(root, text="Ir a Ventana B", width=20, command=lambda: abrir_ventana("B")).pack(pady=10)
tk.Button(root, text="Ir a Ventana C", width=20, command=lambda: abrir_ventana("C")).pack(pady=10)

root.mainloop()