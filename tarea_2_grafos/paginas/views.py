from django.shortcuts import render
from paginas.clases import *
from paginas.funciones import *
from paginas.union import *

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        auto1 = automata()
        auto2 = automata()
        autounion = automata()
        a1 = request.POST['nodos1']
        a2 = request.POST['nodos2']
        ab1 = request.POST['abcdario1']
        ab2 = request.POST['abcdario2']
        trans1 = request.POST['transicion1']
        trans2 = request.POST['transicion2']
        arraytrans1 = trans1.split(';')
        arraytrans2 = trans2.split(';')
        palabra1 = request.POST['parabra1']
        palabra2 = request.POST['parabra2']
        auto1.nodos = a1.split(';')
        auto2.nodos = a2.split(';')
        auto1.abcdario = ab1.split(';')
        auto2.abcdario = ab2.split(';')
        inicio1 = transiciones(arraytrans1,0)
        inicio2 = transiciones(arraytrans2,0)
        finales1 = transiciones(arraytrans1,1)
        finales2 = transiciones(arraytrans2,1)
        letras1 = transiciones(arraytrans1,2)
        letras2 = transiciones(arraytrans2,2)

        vali = validacion(palabra1,palabra2,auto1,auto2)
        if(vali == 0):
            print ("los abcdarios pertenecen a los automatas")
        if (vali == 1):
            print("el abcdario del automata1 no pertenece")
        if (vali == 2):
            print("el abcdario del automata2 no pertenece")
        else:
            print("problemas con la validacion")

        unioninicios = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 0)
        unionfinales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 1)
        unionletras = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 2)
         
    return render(request, 'index.html')

def aplicacion(request):
    return render(request, 'aplicacion.html')