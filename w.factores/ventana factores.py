import tkinter as tk

ventana_f = tk.Tk()
ventana_f.title("Factores")
ventana_f.geometry("500x300")
ventana_f.minsize(400,250)
ventana_f.maxsize(600,400)
ventana_f.config(bg="tomato")
ventana_f.attributes(alpha=0.9)

factorizar= tk.Frame(ventana_f)
factorizar.config(width=300 ,height=200 , bg="blue", bd=5)
factorizar.pack()

ventana_f.mainloop()