import random
import numpy as np

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
        poblacion.append(cromosoma)
    return poblacion

def cruceAritmetico(cromosoma1, cromosoma2):
    return (cromosoma1+cromosoma2)/2

def cruceBLX(cromosoma1,cromosoma2):
    hijo = []
    for g1,g2 in zip(cromosoma1,cromosoma2):
        if g1<g2:
            hijo.append(random.uniform(g1,g2))
        else:
            hijo.append(random.uniform(g2,g1))
    return np.array(hijo)
