

def multiplo(num):
    resultado=""
    if(num % 3==0) and (num % 5 == 0):
        resultado="Hola Clase P33"
    elif (num % 3==0):
        resultado ="Hola"
    elif(num %5 ==0):
        resultado="clase p 33"
    else:
        resultado=num
    return resultado

def calculo(ListaNum):
    resultado=""
    for numero in ListaNum:
        if numero%10==0:
            resultado +="\n"
        resultado += "" + str(multiplo(numero)) +"-"
    return resultado
#Mete los valores del 1 al 100 en una lista.
lista_num= list(range(1,101))
print(calculo(lista_num))

import calendar,locale
locale.setlocale(locale.LC_ALL, 'es-ES')
meses=list()
for m in range (1,13):
    mes=calendar.month_name[m] 
    meses.append(mes)

print(meses)