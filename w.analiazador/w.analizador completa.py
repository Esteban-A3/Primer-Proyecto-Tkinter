import tkinter as tk
#Ventana Analizxador
def analisis_pares(num):
    if not isinstance(num,int):
        return "Error: Por favor introducir un número entero"
    if num<=0:
        return  "No posee factores positivos"
    else:
        return analisis_pares_aux(num,1)

def analisis_pares_aux(num, i):
    if i > int(num**0.5):
        return ()

    elif num%i == 0:
        return (((i, num//i),) + analisis_pares_aux(num, i+1))

    else:
        return analisis_pares_aux(num,i+1)

ventana_a = tk.Tk()
ventana_a.title("Analizador de Números")
ventana_a.geometry("600x400")
ventana_a.config(bg="tomato")
ventana_a.attributes(alpha=0.95)
ventana_a.resizable(False,False)

sideanalizar= tk.Frame(ventana_a)
sideanalizar.config(bg="indianred1", bd=10, width=450, height=200)

m_bienvenida= tk.Label(sideanalizar, text="Introdusca un número entero para analizar")
m_bienvenida.config(bg="indianred1",fg="gold", font=("Impact",15))

entrada_a= tk.Entry(sideanalizar)
entrada_a.config(bg="azure2", fg="gray25", font=("Impact",12))
entrada_a.insert(0, "Ejemplo: 10")

def pares():
    valor = entrada_a.get()
    if not valor or valor == "Ejemplo: 10":
        resultado.config(text="⚠️ Por favor ingrese un número")
        return
    if valor.isdigit():
        num = int(valor)
        if num > 100000:
            resultado.config(text="⚠️ Límite excedido: Intenta con un numero menor (Máx: 100,000)") #Limite para proteger interfaz. El verdadero limite de la funcion es 1 millon
            return
        else:
            res = analisis_pares(num)
            resultado.config(text=f"Factores de {num} = {res}")
    else:
        resultado.config(text="❌ Entrada inválida, debe ser un entero positivo")


analizar=tk.Button(sideanalizar, text="Analizar", command=pares)
analizar.config(bg="azure2", fg="gray23", font=("Impact", 12))

resultado=tk.Label(sideanalizar, text="")
resultado.config(bg="indianred1", fg="gold", font=("impact", 13, "italic"), wraplength=350, justify="center")

sideanalizar.place(relx=0.5,rely=0.5, anchor="center")
sideanalizar.pack_propagate(False)
m_bienvenida.pack()
entrada_a.pack()
resultado.pack()
analizar.pack()

ventana_a.mainloop()