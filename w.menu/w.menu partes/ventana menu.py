import tkinter as tk

ventana_m = tk.Tk()
ventana_m.title("Menu")
ventana_m.geometry("900x500")
ventana_m.config(bg="aquamarine")
ventana_m.resizable(False,False)
ventana_m.attributes(alpha=0.95)

Bienvenida = tk.Label(text="Bienvenido", bg="aquamarine",fg="White", font=("Impact", 50))
Mensaje = tk.Label(text="Selecciona una boton para abrir una pestalla", bg="aquamarine",fg="White", font=("Impact", 25))
BlockVentanas = tk.Frame(ventana_m)


botonwA = tk.Button(BlockVentanas, width=25, height=10, text="Analizador de Números", bg="tomato",fg="White", font=("Impact"))
botonwI = tk.Button(BlockVentanas, width=25, height=10, text="Información del programador", bg="sky blue",fg="White", font=("Impact"))
BotonwP = tk.Button(BlockVentanas, width=25, height=10, text="Animación", bg="olivedrab1",fg="White", font=("Impact"))

Bienvenida.pack()
Mensaje.pack()
BlockVentanas.pack()

botonwA.grid(row=2, column=2)
botonwI.grid(row=2,column=3)
BotonwP.grid(row=2,column=4)
ventana_m.mainloop()