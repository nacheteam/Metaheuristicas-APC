import numpy as np
import knn
import auxiliar
import time
import busqueda_local

MU = 0
SIGMA = 0.4

def mutacionILS(solucion,MU=MU,SIGMA=SIGMA):
    #Calculamos el número de posiciciones a mutar (10%)
    num_mutaciones = int(0.1*len(solucion))

    #Tomamos una lista de indices de tamaño num_mutaciones
    sample = numpy.arange(len(solucion))
    numpy.random.shuffle(sample)
    sample = sample[:num_mutaciones]

    #Mutamos la solución usando el algoritmo de mutacion ya conocido
    for i in sample:
        solucion[i] = auxiliar.mutacion(w,i,MU,SIGMA)

    return solucion

def ILS(data,k,MAX_EVALS=15000):
    #Se toman las tuplas y sus clases
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])

    #Número de características
    ncar = len(data_np[0])

    #Mejor solución hasta el momento
    mejor_solucion = np.zeros(ncar)
    valoracion_mejor_solucion = 0

    #Número de evaluaciones
    evaluaciones = 1

    #Bucle principal
    while evaluaciones < MAX_EVALS:

        #Generamos una solución inicial
        solucion = np.uniform(0,1,ncar)
        valoracion = knn.Valoracion(data_np, data_np,k,solucion,labels_np, labels_np,True,True)

        #Comprobamos la mejor solución
        if valoracion>valoracion_mejor_solucion:
            mejor_solucion = np.copy(solucion)
            valoracion_mejor_solucion = valoracion

        #Genero la solución mejorada con BL
        mejorada,ev = busqueda_local.busquedaLocal(data,k,1000,solucion):
        evaluaciones+=ev
        valoracion_mejorada = knn.Valoracion(data_np, data_np,k,mejorada,labels_np, labels_np,True,True)

        #Comprobamos la mejor solución
        if valoracion_mejorada>valoracion_mejor_solucion:
            mejor_solucion = np.copy(mejorada)
            valoracion_mejor_solucion = valoracion_mejorada

        #Comprobamos la solución mejor entre las dos obtenidas
        mejor_local =  np.copy(solucion) if valoracion>valoracion_mejorada else np.copy(mejorada)
        valoracion_mejor_local = valoracion if valoracion>valoracion_mejorada else valoracion_mejorada
        evaluaciones+=1

        #Comprobamos la mejor solución
        if valoracion_mejor_local>valoracion_mejor_solucion:
            mejor_solucion = np.copy(mejor_local)
            valoracion_mejor_solucion = valoracion_mejor_local

        for i in range(14):
            #Genero la solución mutada y le aplico la búsqueda local
            mutada = mutacionILS(mejor_local)
            valoracion_mutada = knn.Valoracion(data_np, data_np,k,mutada,labels_np, labels_np,True,True)
            mutada_mejorada = busqueda_local.busquedaLocal(data,k,1000,mutada)
            valoracion_mutada_mejorada = knn.Valoracion(data_np, data_np,k,mutada_mejorada,labels_np, labels_np,True,True)
            evaluaciones+=2

            #Actualizamos el mejor local
            mejor_local =  np.copy(mutada) if valoracion_mutada>valoracion_mutada_mejorada else np.copy(mutada_mejorada)
            valoracion_mejor_local = valoracion_mutada if valoracion_mutada>valoracion_mutada_mejorada else valoracion_mutada_mejorada

            #Comprobamos la mejor solución
            if valoracion_mejor_local>valoracion_mejor_solucion:
                mejor_solucion = np.copy(mejor_local)
                valoracion_mejor_solucion = valoracion_mejor_local

    return mejor_solucion

def ValoracionILS(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el algoritmo genético estacionario.
    """
    #Inicializa los datos con los del fichero y las particiones
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0

    #Para cada partición
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()

        #Aplicamos el algoritmo ILS con el conjunto de entrenamiento data-particion
        v = ILS(datos_train,k)
        fin = time.time()
        vectores.append(v)

        #Hallamos la valoración de la solución
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
