from paginas.clases import *
from paginas.views import *

def union (auto1, auto2, inicios, inicios2, letras1, letras2, finales1, finales2, num):
    nodo1 = auto1.nodos
    nodo2 = auto2.nodos
    cont = 0
    cont2 = 0
    for i in nodo1:
        for j in nodo2:
            for k in inicios:
                if(i == k):
                    auxnum = auxnum + 'cont' + ';'
                    cont =+1
            for l in inicios2:
                if(j == l):
                    auxnum2 = auxnum2 + 'cont2' + ';'
                    cont2 +=1
            aux1 = auxnum.split(';')
            aux2 = auxnum2.split(';')
            for m in aux1:
                for n in aux2:
                    auxm = int(m)
                    auxn = int(n)
                    if(letras1[auxm] == letras2[auxn]):
                        unioninicios = unioninicios + i + j + ';'
                        unionfinales = unionfinales + finales1[auxm] + finales2[auxn] + ';'
                        unionletras = unionletras + letras1[auxm] + ';'
    if(num == 0):
        return unioninicios
    if(num == 1):
        return unionfinales
    if(num == 3):
        return unionletras