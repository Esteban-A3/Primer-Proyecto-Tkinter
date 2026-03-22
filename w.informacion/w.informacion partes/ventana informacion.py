def cerrarVentana():
    ventana_i.destroy()

import tkinter as tk

ventana_i = tk.Tk()
ventana_i.title("Ventana de información")
ventana_i.geometry("700x500")
ventana_i.config(bg="sky blue")
ventana_i.resizable(False,False)
ventana_i.attributes(alpha=0.95)

block_nce =tk.Frame(ventana_i)
block_nce.config(bg="light cyan1",bd=5, width="400", height="100")

block_bio =tk.Frame(ventana_i)
block_bio.config(bg="light cyan2",bd=5, width="400", height="200")

block_music =tk.Frame(ventana_i)
block_music.config(bg="light cyan3", bd=5, width="400", height="100")

block_foto=tk.Frame(ventana_i)
block_foto.config(bg="pale green1", bd=8, width="200", height="200")

block_l =tk.Frame(ventana_i)
block_l.config(bg="pale green2", bd=8,width="250", height="200")

botonCi = tk.Button(ventana_i,text="X",command= cerrarVentana)


block_nce.place(relx=0.3, rely=0.16, anchor="center")
block_nce.propagate(False)
block_bio.place(relx=0.3, rely=0.5, anchor="center")
block_bio.propagate(False)
block_music.place(relx=0.3, rely=0.84 ,anchor="center")
block_music.propagate(False)
block_foto.place(relx=0.80, rely=0.25 ,anchor="center")
block_foto.propagate(False)
block_l.place(relx=0.80, rely=0.70 ,anchor="center")
block_l.propagate(False)
botonCi.place(x=670, y=8)
ventana_i.mainloop()