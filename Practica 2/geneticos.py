import random
import numpy as np
import knn
import auxiliar

TAM_POBLACION = 30
PROB_CRUCE_AGG = 0.7
PROB_MUTACION = 0.001
MAX_EVALUACIONES = 15000

random.seed(123456789)

def generaPoblacionInicial(longitud):
    poblacion = []
    for i in range(TAM_POBLACION):
        cromosoma = []
        for j in range(longitud):
            cromosoma.append(random.uniform(0,1))
        poblacion.append(np.array(cromosoma))
    return np.array(poblacion)

def cruceAritmetico(cromosoma1, cromosoma2):
    return np.divide((cromosoma1+cromosoma2),2)

def cruceBLX(cromosoma1,cromosoma2):
    hijo = []
    for g1,g2 in zip(cromosoma1,cromosoma2):
        if g1<g2:
            hijo.append(random.uniform(g1,g2))
        else:
            hijo.append(random.uniform(g2,g1))
    return np.array(hijo)

def torneoBinario(data,poblacion,k):
    individuos = random.sample(range(TAM_POBLACION),2)
    valoracion_ind1 = knn.Valoracion(data,data,k,poblacion[individuos[0]])
    valoracion_ind2 = knn.Valoracion(data,data,k,poblacion[individuos[1]])
    if valoracion_ind1>valoracion_ind2:
        return individuos[0]
    return individuos[1]


def GeneticoEstacionario(data,k,operador_cruce):
    num_padres = 0
    if operador_cruce==cruceAritmetico:
        num_padres=4
    elif operador_cruce==cruceBLX:
        num_padres=2
    else:
        print("Has pasado un operador de cruce no válido.")
        return(-1)
    data_np = np.array(data)
    poblacion = generaPoblacionInicial(len(data[0][:-1]))
    evaluaciones = 0
    while evaluaciones < MAX_EVALUACIONES:
        if num_padres==4:
            padres = [torneoBinario(data,poblacion,k) for i in range(4)]
            hijo1 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
            hijo2 = operador_cruce(poblacion[padres[2]],poblacion[padres[3]])
            evaluaciones+=8
        else:
            padres = [torneoBinario(data,poblacion,k) for i in range(2)]
            hijo1 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
            hijo2 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
            evaluaciones+=4
        for i in range(len(hijo1)):
            if random.randint(1,1000)==1:
                hijo1,pos=auxiliar.mutacion(hijo1,i)
        for i in range(len(hijo2)):
            if random.randint(1,1000)==1:
                hijo2,pos=auxiliar.mutacion(hijo2,i)
        poblacion = np.append(poblacion,[hijo1],axis=0)
        poblacion = np.append(poblacion,[hijo2],axis=0)
        valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w) for w in poblacion])
        valoraciones = np.sum(valoraciones,axis=1)
        indices_nueva_poblacion = np.argpartition(valoraciones, 2)[::-1][:TAM_POBLACION]
        poblacion = poblacion[indices_nueva_poblacion]
        evaluaciones+=TAM_POBLACION+2
    valoraciones_final = np.array([knn.Valoracion(data,data,k,w) for w in poblacion])
    valoraciones_final = np.sum(valoraciones_final,axis=1)
    return np.array(poblacion[np.argpartition(valoraciones_final,1)[0]])

def GeneticoGeneracional(data,k,operador_cruce):
    data_np = np.array(data)
    ncar = len(data[0][:-1])
    poblacion = generaPoblacionInicial(ncar)
    num_parejas = 0
    mutaciones = int(PROB_MUTACION*TAM_POBLACION*ncar)
    if operador_cruce==cruceAritmetico:
        num_parejas = int(TAM_POBLACION*PROB_CRUCE_AGG)
    elif operador_cruce==cruceBLX:
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
    while evaluaciones<MAX_EVALUACIONES:
        for i in range(num_parejas):
            if operador_cruce==cruceAritmetico:
                padres = [torneoBinario(data,poblacion,k) for i in range(4)]
                hijos = []
                evaluaciones+=8
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[2]],poblacion[padres[3]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[2]]))
                hijos.append(operador_cruce(poblacion[padres[1]],poblacion[padres[2]]))
                for p,i in zip(padres,range(4)):
                    poblacion[p] = hijos[i]
            else:
                padres = [torneoBinario(data,poblacion,k) for i in range(2)]
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
