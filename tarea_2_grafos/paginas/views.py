from django.shortcuts import render
from paginas.clases import *
from paginas.funciones import *
from paginas.union import *
from django.template import RequestContext

# Create your views here.
def index(request):      
    return render(request, 'index.html')

def aplicacion(request):
    if (request.method == 'POST'):
        auto1 = automata()                      #automatas entregados
        auto2 = automata()
        autounion = automata()                  #automata union
        autoInter = automata()                  #automata interseccion
        auto1Com = automata()                   #complementos de los automatas anteriores
        auto2Com = automata()
        autoUnionCom = automata()
        autoInterCom = automata()
        a1 = request.POST['nodos1']
        a2 = request.POST['nodos2']
        ab1 = request.POST['abcdario1']
        ab2 = request.POST['abcdario2']
        trans1 = request.POST['transicion1']
        trans2 = request.POST['transicion2']
        ai1 = request.POST['nodo_inicial1']         #inicial AFD
        ai2 = request.POST['nodo_inicial2']         #inicial AFD
        af1 = request.POST['nodo_final1']
        af2 = request.POST['nodo_final2']
        uninicios1 = []
        NodosLista1 = []
        NodosLista2 = []
        str(trans1)
        str(trans2)
        str(a1)
        str(a2)
        str(ab1)
        str(ab2)
        arraytrans1 = trans1.split(';')
        arraytrans1 = "".join(arraytrans1)
        arraytrans2 = trans2.split(';')
        arraytrans2 = "".join(arraytrans2)
        palabra1 = request.POST['palabra1']
        palabra2 = request.POST['palabra2']
        auto1.nodos = a1.split(';')
        auto2.nodos = a2.split(';')
        auto1.abcdario = ab1.split(';')
        auto2.abcdario = ab2.split(';')
        auto1.inicial = ai1
        auto2.inicial = ai2
        auto1.finales = af1.split(';')
        auto2.finales = af2.split(';')
        inicio1 = transiciones(arraytrans1,0)
        inicio2 = transiciones(arraytrans2,0)
        finales1 = transiciones(arraytrans1,1)
        finales2 = transiciones(arraytrans2,1)
        letras1 = transiciones(arraytrans1,2)
        letras2 = transiciones(arraytrans2,2)

        unioninicios = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 0)               #Entrega los datos de la union
        unionfinales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 1)
        unionletras = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 2)
        autounion.inicial = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 3)
        autounion.finales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 4)
        interInicios = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 0)               #entrega datos de la interseccion
        interFinales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 1)
        interLetras = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 2)
        autoInter.iniciales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 3)
        autoInter.finales = union(auto1, auto2, inicio1, inicio2, letras1, letras2, finales1, finales2, 5)

        auto1Com = auto1                                                                                            #complemento
        auto1Com.finales = complemento (auto1)
        NodosLista1 = crearNodos(finales1, letras1, auto1)
        NodosLista2 = crearNodos(finales2, letras2, auto2)
        unioniniciosOrdenada=ordenar(unioninicios)
        unionfinalesOrdenada=ordenar(unionfinales)
        autounion.nodos = unioniniciosOrdenada
        variable1=autoInter.iniciales
        variable2=autoInter.finales
        variable3=auto1Com.finales
        contexto={'inicios':unioniniciosOrdenada,
                  'finales':unionfinalesOrdenada,
                  'letras':unionletras,
                  'automataunionI':autounion.inicial,
                  'automataunionF':autounion.finales,
                  'interinicios':interInicios,
                  'interfinales':interFinales,
                  'interletras':interLetras,
                  'autointerI':variable1,
                  'autointerF':variable2,
                  'automatacom':variable3
                }
        return render(request,'aplicacion.html',contexto)
    return render(request, 'aplicacion.html')