import random
import numpy as np
import knn
import auxiliar
import time

TAM_POBLACION = 30
PROB_CRUCE_AGG = 0.7
PROB_MUTACION = 0.001
MAX_EVALUACIONES = 15000
ALPHA = 0.3

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
    max_c1 = np.amax(cromosoma1)
    max_c2 = np.amax(cromosoma2)
    min_c1 = np.amin(cromosoma1)
    min_c2 = np.amin(cromosoma2)
    max_intervalo = max_c1 if max_c1>max_c2 else max_c2
    min_intervalo = min_c1 if min_c1<min_c2 else min_c2
    delta = (max_intervalo-min_intervalo)*ALPHA
    for i in range(len(cromosoma1)):
        hijo.append(random.uniform(min_intervalo-delta,max_intervalo+delta))
    hijo = np.array(hijo)
    hijo[hijo<0]=0
    hijo[hijo>1]=1
    return hijo

def torneoBinario(data,poblacion,k,labels_np,valoraciones):
    individuos = random.sample(range(TAM_POBLACION),2)
    valoracion_ind1 = valoraciones[individuos[0]]
    valoracion_ind2 = valoraciones[individuos[1]]
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
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])
    poblacion = generaPoblacionInicial(len(data[0][:-1]))
    valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
    valoraciones = np.sum(valoraciones,axis=1)
    evaluaciones = TAM_POBLACION
    while evaluaciones < MAX_EVALUACIONES:
        if num_padres==4:
            padres = [torneoBinario(data_np,poblacion,k,labels_np,valoraciones) for i in range(4)]
            hijo1 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
            hijo2 = operador_cruce(poblacion[padres[2]],poblacion[padres[3]])
        else:
            padres = [torneoBinario(data_np,poblacion,k,labels_np,valoraciones) for i in range(2)]
            hijo1 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
            hijo2 = operador_cruce(poblacion[padres[0]],poblacion[padres[1]])
        for i in range(len(hijo1)):
            if random.randint(1,1000)==1:
                hijo1,pos=auxiliar.mutacion(hijo1,i)
        for i in range(len(hijo2)):
            if random.randint(1,1000)==1:
                hijo2,pos=auxiliar.mutacion(hijo2,i)
        poblacion = np.append(poblacion,[hijo1],axis=0)
        tc,tr = knn.Valoracion(data_np,data_np,k,poblacion[-1],labels_np,labels_np,True)
        valoraciones = np.append(valoraciones,tc+tr)
        poblacion = np.append(poblacion,[hijo2],axis=0)
        tc,tr = knn.Valoracion(data_np,data_np,k,poblacion[-1],labels_np,labels_np,True)
        valoraciones = np.append(valoraciones,tc+tr)

        indices_nueva_poblacion = np.argpartition(valoraciones, 2)[::-1][:TAM_POBLACION]
        poblacion = poblacion[indices_nueva_poblacion]
        valoraciones = valoraciones[indices_nueva_poblacion]
        evaluaciones+=2
    valoraciones_final = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
    valoraciones_final = np.sum(valoraciones_final,axis=1)
    return np.array(poblacion[np.argmax(valoraciones_final)])

def GeneticoGeneracional(data,k,operador_cruce):
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])
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
    valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
    valoraciones = np.sum(valoraciones,axis=1)
    mejor_solucion_ind = np.argmax(valoraciones)
    mejor_solucion_valor = valoraciones[mejor_solucion_ind]
    mejor_solucion = poblacion[mejor_solucion_ind]
    while evaluaciones<MAX_EVALUACIONES:
        for i in range(num_parejas):
            if operador_cruce==cruceAritmetico:
                padres = [torneoBinario(data_np,poblacion,k,labels_np,valoraciones) for i in range(4)]
                hijos = []
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[2]],poblacion[padres[3]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[2]]))
                hijos.append(operador_cruce(poblacion[padres[1]],poblacion[padres[2]]))
                for p,i in zip(padres,range(4)):
                    poblacion[p] = hijos[i]
            else:
                padres = [torneoBinario(data_np,poblacion,k,labels_np,valoraciones) for i in range(2)]
                hijos = []
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                for p,i in zip(padres,range(2)):
                    poblacion[p] = hijos[i]
        for i in range(mutaciones):
            cr = random.randint(0,TAM_POBLACION-1)
            gen = random.randint(0,ncar-1)
            poblacion[cr],pos = auxiliar.mutacion(poblacion[cr],gen)

        valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
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

def ValoracionGeneticoGeneracional(nombre_datos,k,operador_cruce):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método de búsqueda local.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()
        v = GeneticoGeneracional(datos_train,k,operador_cruce)
        fin = time.time()
        vectores.append(v)
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones

def ValoracionGeneticoEstacionario(nombre_datos,k,operador_cruce):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método de búsqueda local.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()
        v = GeneticoEstacionario(datos_train,k,operador_cruce)
        fin = time.time()
        vectores.append(v)
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
