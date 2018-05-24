import numpy as np
import knn
import auxiliar
import time

F = 0.5
CR = 0.1/0.9
TAM_POBLACION = 50

def poblacionInicial(ncar,TAM_POBLACION=TAM_POBLACION):
    poblacion = []
    #Genero TAM_POBLACION vectores con valores aleatorios entre 0 y 1
    for i in range(TAM_POBLACION):
        poblacion.append(np.random.uniform(0,1,ncar))

    return poblacion

def Rand1(individuo,poblacion,valoraciones):
    #Tomo una muestra aleatoria de 3 individuos
    sample = np.setdiff1d(np.arange(len(poblacion)),[individuo])
    np.random.shuffle(sample)
    sample = sample[:3]

    #Devuelvo el individuo generado
    return poblacion[sample[0]] + F*(poblacion[sample[1]]-poblacion[sample[2]])

def CTB1(individuo,poblacion,valoraciones):
    #Tomo una muestra de 2 individuos
    sample = np.setdiff1d(np.arange(len(poblacion)),[individuo])
    np.random.shuffle(sample)
    sample = sample[:2]

    #Encuentro al mejor individuo
    mejor = np.argmax(valoraciones)

    #Devuelvo el individuo generado
    return poblacion[individuo] + F*(poblacion[mejor] - poblacion[individuo]) + F*(poblacion[sample[0]] - poblacion[sample[1]])

def DE(data,k,operador_mutacion,MAX_EVALS=15000,TAM_POBLACION=TAM_POBLACION):
    #Se toman las tuplas y sus clases
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])

    #Número de características
    ncar = len(data_np[0])

    #Inicializa la población
    poblacion = poblacionInicial(ncar)
    valoraciones = [knn.Valoracion(data_np,data_np,k,poblacion[i],labels_np,labels_np,True,True) for i in range(TAM_POBLACION)]

    #Evaluaciones
    evaluaciones = TAM_POBLACION

    #Bucle principal
    while evaluaciones<MAX_EVALS:
        #Calculamos el vector de individuos mutados y sus valoraciones
        offspring = []
        for i in range(TAM_POBLACION):
            random = np.random.uniform(0,1)
            if random<CR:
                offspring.append(operador_mutacion(i,poblacion,valoraciones))
            else:
                offspring.append(poblacion[i])
        valoraciones_offspring = [knn.Valoracion(data_np,data_np,k,offspring[i],labels_np,labels_np,True,True) for i in range(TAM_POBLACION)]
        evaluaciones+=TAM_POBLACION

        #Calculamos la nueva población cogiendo los mejores individuos
        for i in range(TAM_POBLACION):
            if valoraciones[i]<valoraciones_offspring[i]:
                poblacion[i] = offspring[i]
                valoraciones[i] = valoraciones_offspring[i]

    return poblacion[np.argmax(valoraciones)]


def ValoracionDERand1(nombre_datos,k):
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
        v = DE(datos_train,k,Rand1)
        fin = time.time()
        vectores.append(v)

        #Hallamos la valoración de la solución
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones


def ValoracionDECTB1(nombre_datos,k):
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
        v = DE(datos_train,k,CTB1)
        fin = time.time()
        vectores.append(v)

        #Hallamos la valoración de la solución
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
