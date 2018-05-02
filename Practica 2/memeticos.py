import random
import numpy as np
import knn
import auxiliar
import geneticos
import busqueda_local
import time

TAM_POBLACION = 10
PROB_CRUCE_AGG = 0.7
PROB_MUTACION = 0.001
MAX_EVALUACIONES = 15000

random.seed(123456789)

def Memetico(data,k,operador_cruce,nGeneraciones,prob_bl,mejores=False):
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])
    ncar = len(data[0][:-1])
    poblacion = geneticos.generaPoblacionInicial(ncar,TAM_POBLACION)
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
    valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
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
                individuos = valoraciones.argsort()[-n_elem_bl:][::-1]
            for ind in individuos:
                poblacion[ind],ev = busqueda_local.busquedaLocal(data,k,2*len(data_np[0]))
                evaluaciones+=ev
            valoraciones = np.array([knn.Valoracion(data_np,data_np,k,w,labels_np,labels_np,True) for w in poblacion])
            valoraciones = np.sum(valoraciones,axis=1)
            evaluaciones+=TAM_POBLACION

        contador_generaciones+=1
        hijos = []
        for i in range(num_parejas):
            if operador_cruce==geneticos.cruceAritmetico:
                padres = [geneticos.torneoBinario(data_np,poblacion,k,labels_np,valoraciones,TAM_POBLACION) for i in range(4)]
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[2]],poblacion[padres[3]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[2]]))
                hijos.append(operador_cruce(poblacion[padres[1]],poblacion[padres[2]]))
            else:
                padres = [geneticos.torneoBinario(data_np,poblacion,k,labels_np,valoraciones,TAM_POBLACION) for i in range(2)]
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
                hijos.append(operador_cruce(poblacion[padres[0]],poblacion[padres[1]]))
        for i in range(mutaciones):
            cr = random.randint(0,len(hijos)-1)
            gen = random.randint(0,ncar-1)
            hijos[cr],pos = auxiliar.mutacion(hijos[cr],gen)

        for i in range(len(hijos),TAM_POBLACION):
            hijos.append(poblacion[geneticos.torneoBinario(data_np,poblacion,k,labels_np,valoraciones,TAM_POBLACION)])

        poblacion = np.array(hijos)

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

def ValoracionMemetico(nombre_datos,k,operador_cruce,nGeneraciones,prob_bl,mejores):
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
        v = Memetico(datos_train,k,operador_cruce,nGeneraciones,prob_bl,mejores)
        fin = time.time()
        vectores.append(v)
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
