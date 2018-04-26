import random
import numpy as np
import knn
import auxiliar
import geneticos
import busqueda_local

TAM_POBLACION = 30
PROB_CRUCE_AGG = 0.7
PROB_MUTACION = 0.001
MAX_EVALUACIONES = 15000

random.seed(123456789)

def Memetico(data,k,operador_cruce,nGeneraciones,prob_bl,mejores=False):
    data_np = np.array(data)
    ncar = len(data[0][:-1])
    poblacion = geneticos.generaPoblacionInicial(ncar)
    num_parejas = 0
    mutaciones = int(PROB_MUTACION*TAM_POBLACION*ncar)
    if operador_cruce==geneticos.cruceAritmetico:
        num_parejas = int(TAM_POBLACION*PROB_CRUCE_AGG)
    elif operador_cruce==geneticos.cruceBLX:
        num_parejas = int(TAM_POBLACION*PROB_MUTACION)
    else:
        print("Has pasado un operador de cruce no válido.")
        return(-1)

    evaluaciones = TAM_POBLACION
    valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w) for w in poblacion])
    valoraciones = np.sum(valoraciones,axis=1)
    mejor_solucion_ind = np.argmax(valoraciones)
    mejor_solucion_valor = valoraciones[mejor_solucion_ind]
    mejor_solucion = poblacion[mejor_solucion_ind]
    contador_generaciones = 1
    while evaluaciones<MAX_EVALUACIONES:

        if contador_generaciones%nGeneraciones==0:
            n_elem_bl = int(prob_bl*TAM_POBLACION)
            individuos=[]
            if not mejores:
                individuos = random.sample(range(TAM_POBLACION),n_elem_bl)
            else:
                valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w) for w in poblacion])
                valoraciones = np.sum(valoraciones,axis=1)
                individuos = valoraciones.argsort()[-n_elem_bl:][::-1]
            for ind in individuos:
                poblacion[ind],ev = busqueda_local.busquedaLocal(data,k,300)
                evaluaciones+=ev

        contador_generaciones+=1
        for i in range(num_parejas):
            if operador_cruce==geneticos.cruceAritmetico:
                padres = [geneticos.torneoBinario(data,poblacion,k) for i in range(4)]
                hijos = []
                evaluaciones+=8
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[2]],poblacion[padres[3]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[2]]))
                hijos.append(operador_cruce(poblacion[padres[1]],poblacion[padres[2]]))
                for p,i in zip(padres,range(4)):
                    poblacion[p] = hijos[i]
            else:
                padres = [geneticos.torneoBinario(data,poblacion,k) for i in range(2)]
                hijos = []
                evaluaciones+=4
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                for p,i in zip(padres,range(2)):
                    poblacion[p] = hijos[i]
        for i in range(mutaciones):
            cr = random.randint(0,TAM_POBLACION-1)
            gen = random.randint(0,ncar-1)
            poblacion[cr],pos = auxiliar.mutacion(poblacion[cr],gen)

        valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w) for w in poblacion])
        valoraciones = np.sum(valoraciones,axis=1)
        evaluaciones+=TAM_POBLACION
        peor_solucion_ind = np.argmin(valoraciones)
        peor_solucion_valor = valoraciones[peor_solucion_ind]
        peor_solucion = poblacion[peor_solucion_ind]
        if peor_solucion_valor<mejor_solucion_valor:
            poblacion[peor_solucion_ind] = mejor_solucion
        mejor_solucion_ind = np.argmax(valoraciones)
        mejor_solucion_valor = valoraciones[mejor_solucion_ind]
        mejor_solucion = poblacion[mejor_solucion_ind]
    return np.array(mejor_solucion)
