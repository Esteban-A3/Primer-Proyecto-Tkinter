import tkinter as tk

ventana_f = tk.Tk()
ventana_f.title("Analizador de Números")
ventana_f.geometry("600x400")
ventana_f.config(bg="tomato")
ventana_f.attributes(alpha=0.95)
ventana_f.resizable(False,False)

factorizar= tk.Frame(ventana_f)
factorizar.config(bg="indianred1", bd=10)

m_bienvenida= tk.Label(factorizar, text="Introdusca un número entero para analizar")
m_bienvenida.config(bg="indianred1",fg="gold", font=("Impact",15))

entrada_f= tk.Entry(factorizar)
entrada_f.config(bg="azure2", fg="gray25", font=("Impact",12))
entrada_f.insert(0, "Ejemplo: 10")

analizar=tk.Button(factorizar, text="Analizar")
analizar.config(bg="azure2", fg="gray23", font=("Impact", 12))

resultado=tk.Label(factorizar, text="")
resultado.config(bg="indianred1", fg="gold", font=("impact", 13, "italic"))


factorizar.place(relx=0.19,rely=0.30)
m_bienvenida.pack()
entrada_f.pack()
resultado.pack()
analizar.pack()

ventana_f.mainloop()