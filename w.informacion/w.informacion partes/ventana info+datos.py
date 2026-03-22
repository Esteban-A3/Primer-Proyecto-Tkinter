import tkinter as tk

ventana_i = tk.Tk()
ventana_i.title("Ventana de información")
ventana_i.geometry("700x500")
ventana_i.config(bg="sky blue")
ventana_i.resizable(False, False)
ventana_i.attributes(alpha=0.95)

block_nce = tk.Frame(ventana_i, bg="light cyan1", bd=5, width=400, height=100)
block_bio = tk.Frame(ventana_i, bg="light cyan2", bd=5, width=400, height=200)
block_music = tk.Frame(ventana_i, bg="light cyan3", bd=5, width=400, height=100)
block_foto = tk.Frame(ventana_i, bg="pale green1", bd=8, width=150, height=200)
block_l = tk.Frame(ventana_i, bg="pale green2", bd=8, width=250, height=150)

nombre = tk.Label(block_nce, text="Esteban Sánchez Ledezma", bg="light cyan1", fg="grey60", font=("Impact", 15))
carnet = tk.Label(block_nce, text="2026108570", bg="light cyan1", fg="grey60", font=("Impact", 15))
edad = tk.Label(block_nce, text="19 años", bg="light cyan1", fg="grey60", font=("Impact", 15))

programadorM = tk.PhotoImage(file="w.informacion partes/Programador.png")
sideP= tk.Label(block_foto, image=programadorM)
lugar= tk.PhotoImage(file="w.informacion partes/lugar.png")
sideL= tk.Label(block_l, image=lugar)
textoL = tk.Label(block_l, text="Lugar donde vive:", bg="pale green2", fg="grey60", font=("Impact", 15) )

texto = """Soy técnico electromecánico graduado y actualmente estudiante de Ingeniería en Computadores en el Tecnológico de Costa Rica. 
Además, he complementado mi formación en el área de redes, alcanzando el nivel de CCNA 3 con certificación académica. 

Me caracterizo por ser una persona proactiva, con gran interés en la tecnología, la programación y las redes. 
Busco constantemente fortalecer mis conocimientos y adquirir nuevas habilidades que me permitan crecer profesionalmente.
Mi objetivo es desarrollarme como ingeniero en computación y aportar soluciones innovadoras en el ámbito tecnológico."""

biografia = tk.Label(block_bio, text=texto,font=("Time new Roman", 9), wraplength=380,fg="grey40", justify="left", bg="light cyan2")
biografia.pack(padx=5, pady=5)

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

nombre.pack()
carnet.pack()
edad.pack()
sideP.pack()
textoL.pack()
sideL.pack()

ventana_i.mainloop()