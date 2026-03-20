import tkinter as tk

def factores(num):
    if num==0:
        return "No posee Factores"
    else:
        return factores_aux(abs(num),1)

def factores_aux(num, i):
    if i>num:
        return ()

    elif i <= num and num % i == 0 and i <=num//i:
        return (((i, num//i),) + factores_aux(num, i+1))

    else:
        return factores_aux(num,i+1)

ventana_f = tk.Tk()
ventana_f.title("Factores")
ventana_f.geometry("500x500")

entrada_f = tk.Entry(ventana_f)
entrada_f.place(x=50 , y=10)
entrada_f.pack()

resultado = tk.Label(ventana_f, text="")
resultado.pack()

def calcular():
    num = int(entrada_f.get())
    res = factores(num)
    
    resultado.config(text=f"Factores de {num} = {res}")

boton_f = tk.Button(ventana_f, text="Calcular", command=calcular)
boton_f.place(x=50 , y=50)



ventana_f.mainloop()