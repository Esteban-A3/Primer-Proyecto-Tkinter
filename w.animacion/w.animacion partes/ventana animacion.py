import tkinter as tk

ventana_a = tk.Tk()
ventana_a.geometry("700x500")
ventana_a.config(bg="olivedrab1")
ventana_a.resizable(False,False)
ventana_a.attributes(alpha=0.95)

block_pelotas =tk.Frame(ventana_a, bg="light cyan1",bd=5, width="600", height="300")
block_texto= tk.Frame(ventana_a, bg="olivedrab1")
block_velocidad = tk.Frame(ventana_a, bg="olivedrab1")

ATBienvenida=tk.Label(ventana_a,text="Bienvenido a animación",bg="olivedrab1", fg="grey60", font=("Impact", 18) )
ATvelocidad = tk.Label(block_texto, text="Ajusta la barra para configurar la velocidad",bg="olivedrab1", fg="grey60", font=("Impact", 15) )

def cerraranimacion():
    ventana_a.destroy()

BotonCA = tk.Button(ventana_a, text="Cerrar", command=cerraranimacion, bg="light cyan1",fg="grey60", font=("Impact", 12) )
barravelocidad = tk.Scale(block_velocidad, from_=0, to=100, orient=tk.HORIZONTAL, length=300,tickinterval=10, bg="olivedrab1", fg="grey60", font=("Impact", 12))
barravelocidad.set(50)


ATBienvenida.pack()
block_pelotas.pack()
block_pelotas.propagate(False)
block_texto.pack()
block_velocidad.pack()

ATvelocidad.pack()
barravelocidad.pack()
BotonCA.pack()
ventana_a.mainloop()