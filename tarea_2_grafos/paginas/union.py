from paginas.clases import *
from paginas.views import *

def union (auto1, auto2, inicios, inicios2, letras1, letras2, finales1, finales2, num):
    nodo1 = auto1.nodos
    nodo2 = auto2.nodos
    cont = 0
    cont2 = 0
    unioninicios = ""
    unionfinales = ""
    unionletras = ""
    auxnum = []
    auxnum2 = []
    for i in nodo1:
        for j in nodo2:
            for k in inicios:
                ma = " " + i 
                me = i + " "
                mi = " " + i + " "
                if(k == i or k == ma or k == me or k == mi):
                    auxnum=[i for i,a in enumerate(inicios) if a==i]
                    auxnumma=[i for i,a in enumerate(inicios) if a==ma]
                    auxnumme=[i for i,a in enumerate(inicios) if a==me]
                    auxnummi=[i for i,a in enumerate(inicios) if a==mi]
                    auxnum.extend(auxnumma)
                    auxnum.extend(auxnumme)
                    auxnum.extend(auxnummi)
                    auxnum.sort()
            for l in inicios2:
                na = " "+ j
                ne = j + " "
                ni = " " + j + " "
                if(j == l or l == na or l == ne or l == ni):
                    auxnum2=[i for i,a in enumerate(inicios2) if a==j]
                    auxnumna=[i for i,a in enumerate(inicios2) if a==na]
                    auxnumne=[i for i,a in enumerate(inicios2) if a==ne]
                    auxnumni=[i for i,a in enumerate(inicios2) if a==ni]
                    auxnum2.extend(auxnumna)
                    auxnum2.extend(auxnumne)
                    auxnum2.extend(auxnumni)
                    auxnum2.sort()
            aux1 = auxnum
            aux2 = auxnum2
            for m in aux1:
                for n in aux2:
                    eme=m
                    ene=n
                    auxm = int(eme)
                    auxn = int(ene)
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