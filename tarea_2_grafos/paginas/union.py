from paginas.clases import *
from paginas.views import *

def union (auto1, auto2, inicios, inicios2, letras1, letras2, finales1, finales2, num):
    nodo1 = auto1.nodos
    nodo2 = auto2.nodos
    ini1 = auto1.inicial
    ini2 = auto2.inicial
    fin1 = auto1.finales
    fin2 = auto2.finales
    cont = 0
    cont2 = 0
    unioninicios = ""
    unionfinales = ""
    unionletras = ""
    unionodoinicial = ""
    unionodofinales = ""
    auxnum = []
    auxnum2 = []
    intersec = []
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
    
    for i in nodo1:                                                                 #crea str nodos iniciales de la union
            for j in nodo2:
                for k in ini1:
                    for l in ini2:
                        if(i == k and j == l):
                            unionodoinicial = i + j

    for i in nodo1:                                                                    #crea str nodos finales de la union
        for j in nodo2:
            for k in fin1:
                for l in fin2:
                    ma = " " + i 
                    me = i + " "
                    mi = " " + i + " "
                    na = " "+ j
                    ne = j + " "
                    ni = " " + j + " "
                    if (j == l or l == na or l == ne or l == ni or k == i or k == ma or k == me or k == mi):
                        unionodofinales = unionodofinales + i + j + ";"

    
    if (num == 5):                              #crea lista de los nodos finales de la interseccion
        for i in nodo1:
            for j in nodo2:
                for k in fin1:
                    for l in fin2:
                        if(i == k and j == l):
                            intersec.append(i+j)
        return intersec
    
    
    
    
    if(num == 0):
        return unioninicios
    if(num == 1):
        return unionfinales
    if(num == 2):
        return unionletras
    if (num == 3):
        return unionodoinicial
    if (num == 4):
        return unionodofinales