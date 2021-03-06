import auxiliar
import time
import numpy as np
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import DistanceMetric

ALPHA=0.5

def KNNumpy(w_np,particion_np, data_train_np,labels_train, labels_particion,k,mismos_conjuntos):
    '''
    @brief Función que implementa el KNN devolviendo el porcentaje de aciertos conseguido con el vector de pesos dado.
    @param w_np Vector de pesos con valores entre 0 y 1 y de tipo numpy.
    @param particion_np Conjunto de test.
    @param data_train_np Conjunto de entrenamiento.
    @param labels_train Clases del conjunto de entrenamiento.
    @param labels_particion Clases del conjunto de test.
    @param k Número de vecinos para el KNN.
    @param mismos_conjuntos Valor booleano que nos indica si los conjuntos data_train_np y particion_np son iguales.
    @return Devuelve un float entre 0 y 1 donde 0 significa ningún acierto y 1 la mayor tasa de aciertos.
    '''
    tam_data_train_np = len(data_train_np)

    clases = []

    for i in range(len(particion_np)):
        dist = np.sum(np.tile(w_np,(tam_data_train_np,1))*(np.tile(particion_np[i],(tam_data_train_np,1))-data_train_np)**2,axis=1)
        if mismos_conjuntos:
            dist[i]=float('inf')
        clases.append(auxiliar.masComun(labels_train[np.argpartition(dist, k)[:k]]))

    return np.sum(clases == labels_particion)/len(labels_particion)

def Valoracion(particion, data_train,k,w,labels_train, labels_particion,mismos_conjuntos=False,suma=False):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param particion Datos a clasificar.
    @param data_train Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @param labels_train Clases del conjunto de entrenamiento.
    @param labels_particion Clases del conjunto de test.
    @param mismos_conjuntos Booleano que indica si los conjuntos de test y entrenamiento son iguales. Por defecto está a false.
    @param suma Booleano que nos indica si queremos que de devuelva la suma de las tasas. Por defecto está a false.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """

    ##########################################################################################################################################
    #nbr = KNeighborsClassifier(n_neighbors=1,algorithm='auto',metric='wminkowski', metric_params={'w':w},n_jobs=1)
    #nbr.fit([data_train[i][:-1] for i in range(len(data_train))],[data_train[i][-1] for i in range(len(data_train))])
    #particion_formateada = [particion[i][:-1] for i in range(len(particion))]
    #etiquetas = [particion[i][-1] for i in range(len(particion))]
    #aciertos = nbr.score(particion_formateada,etiquetas)
    ##########################################################################################################################################


    #Los pesos que son menores que 0.2 se truncan a 0
    for i in range(len(w)):
        if w[i]<0.2:
            w[i]=0

    #Se calcula la tasa de aciertos con KNN
    aciertos = KNNumpy(w,np.array(particion), np.array(data_train),labels_train,labels_particion,k,mismos_conjuntos)
    simplicidad = 0

    #Se calcula la simplicidad contando el número de ceros
    pesos_bajos = (np.where(w<0.2))[0].size
    simplicidad = pesos_bajos/len(w)
    tasa_clas = 100*ALPHA*aciertos
    tasa_red = 100*(1-ALPHA)*simplicidad

    #Se devuelve la suma o por separado
    if not suma:
        return tasa_clas, tasa_red
    else:
        return tasa_clas+tasa_red

def ValoracionKNN(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos a calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método KNN con pesos a 1.
    """
    #Inicializa los datos con los del fichero y las particiones
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0

    #Se toma como vector solución el que tiene todas las posiciones a 1
    w = []
    for i in range(len(data[0])-1):
        w.append(1)
    w=np.array(w)

    #Para cada partición
    for particion in particiones:
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()

        #Se calcula la valoración del vector de pesos a 1
        tc,tr = Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,w,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        fin = time.time()
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
