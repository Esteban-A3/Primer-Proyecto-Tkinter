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
