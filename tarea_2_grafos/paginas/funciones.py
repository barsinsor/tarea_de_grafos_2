from paginas.clases import *
from paginas.views import *

def validacion(palabra1,palabra2,auto1, auto2):
    arrayabc1 = auto1.abcdario
    arrayabc2 = auto2.abcdario
    arraypal1 = palabra1.split(',')
    arraypal2 = palabra2.split(',')
    pertabc = 0
    pertabc2 = 0
    coincidencia = 0
    coincidencia2 = 0
    for i in arraypal1:                             #automata1
        for j in arrayabc1:
            palabraaux = i
            abcaux = j
            if(palabraaux.equals(abcaux)):
                pertabc=+1
        if (pertabc > 0):
            pertabc = 0
            coincidencia =+1
    for i in arraypal2:                             #automata2
        for j in arrayabc2:
            palabraaux2 = i
            abcaux2 = j
            if(palabraaux2.equals(abcaux2)):
                pertabc2=+1
        if (pertabc2 > 0):
            pertabc2 = 0
            coincidencia2 =+1
    if (coincidencia == arraypal1.length & coincidencia2 == arraypal2.length): #0 todo ok, 1 error en auto1, 2 error en auto2
        return 0
    if (coincidencia != arraypal1.length):
        return 1
    else:
        return 2


def transiciones (tran,num):
    tra = " ".join(tran)
    trans = tra.split(',')
    cont = 0
    conta = 0
    contb = 0
    contc = 0
    inicio = []
    final = []
    letra = []
    for i in trans:
        if (cont == 0):
            inicio.append(i)
            conta +=1
        if (cont == 1):
            final.append(i)
            contb +=1
        if (cont == 2):
            letra.append(i)
            cont = -1
            contc +=1
        cont +=1
    if(num == 0):
        return inicio
    if(num == 1):
        return final 
    if(num ==2):
        return letra

def complemento (auto):
    nodos = auto.nodos
    finales = auto.finales
    finales1 = []
    aux = 0
    for i in nodos:
        if (finales.count(i) == 0):
            finales1.append(i)
    return finales1

def crearNodos(finales, letras, auto):
    cantidadNodos = len(auto.nodos)
    automata = []
    cont = 0
    x = len(auto.nodos)
    aux = 0
    aux1 = 0
    while(cantidadNodos > 0):
        nodito = PropNodo()
        nodito.nodo = auto.nodos[aux]
        print ('a')
        while(x >  0):
            a = finales[aux1]
            nodito.nodoFin = nodito.nodoFin + a + ';'
            y = letras [aux1]
            nodito.condicion = nodito.condicion + y + ';'
            x = x - 1
            aux1 = aux1 + 1
        automata.append(nodito)
        cantidadNodos = cantidadNodos - 1
        cont = cont + 1
        aux = aux + 1
        x = len(auto.nodos)

    return automata

def ordenar(lista):
    listaOrdenada=[]
    for i in lista.split(';'):
        if i not in listaOrdenada:
            listaOrdenada.append(i)
    return listaOrdenada 

def pertenece(abc, palabra):
    cont = 0
    palabraaux = []
    abcaux = []
    for j in palabra:
        palabraaux.append(j)
    abcaux = abc.split(';')
    for i in abcaux:
        for k in palabraaux:
            if (i == k):
                cont = cont + 1 
    if (cont > len(abcaux)):
        return 1
    else: 
        return 0