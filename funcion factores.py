def factores(num):
    if num==0:
        return "No posee Factores"
    else:
        return factores_aux(abs(num),1)

def factores_aux(num, i):
    if i <= num and num % i == 0 and i <=num//i:
        return (((i, num//i),) + factores_aux(num, i+1))

    elif i>num:
        return ()

    else:
        return factores_aux(num,i+1)
