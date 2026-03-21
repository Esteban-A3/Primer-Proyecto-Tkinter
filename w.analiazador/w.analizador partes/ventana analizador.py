import tkinter as tk

ventana_a = tk.Tk()
ventana_a.title("Analizador de Números")
ventana_a.geometry("600x400")
ventana_a.config(bg="tomato")
ventana_a.attributes(alpha=0.95)
ventana_a.resizable(False,False)

factorizar= tk.Frame(ventana_a)
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

ventana_a.mainloop()