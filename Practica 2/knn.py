import auxiliar
import time
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import DistanceMetric

ALPHA=0.5

def KNNumpy(w_np,particion_np, data_train_np,k,mismos_conjuntos):
    particion_np_sin_etiquetas = [particion_np[i][:-1] for i in range(len(particion_np))]
    data_train_np_sin_etiquetas = [data_train_np[i][:-1] for i in range(len(data_train_np))]
    labels_train = np.array([data_train_np[i][-1] for i in range(len(data_train_np))])
    labels_particion = np.array([particion_np[i][-1] for i in range(len(particion_np))])
    clases = []
    w_np_m = np.tile(w_np,(len(data_train_np_sin_etiquetas),1))
    for p in particion_np_sin_etiquetas:
        p_m = np.tile(p,(len(data_train_np_sin_etiquetas),1))
        dist = np.sum(w_np_m*(p_m-data_train_np_sin_etiquetas)**2,axis=1)
        mins = np.argpartition(dist, k)[:k]
        clases.append(auxiliar.masComun(list(labels_train[mins])))

    return np.sum(clases == labels_particion)/len(labels_particion)

def Valoracion(particion, data_train,k,w,mismos_conjuntos=False):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param particion Datos a clasificar.
    @param data_train Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """
    #nbr = KNeighborsClassifier(n_neighbors=1,metric='wminkowski', metric_params={'w':w},n_jobs=1)
    #nbr.fit([data_train[i][:-1] for i in range(len(data_train))],[data_train[i][-1] for i in range(len(data_train))])
    #particion_formateada = [particion[i][:-1] for i in range(len(particion))]
    #etiquetas = [particion[i][-1] for i in range(len(particion))]
    #aciertos = nbr.score(particion_formateada,etiquetas)
    aciertos = KNNumpy(w,np.array(particion), np.array(data_train),k,mismos_conjuntos)
    simplicidad = 0

    pesos_bajos = 0
    for wi in w:
        if wi<0.2:
            pesos_bajos+=1
    simplicidad = pesos_bajos/len(w)
    tasa_clas = 100*ALPHA*aciertos
    tasa_red = 100*(1-ALPHA)*simplicidad
    return tasa_clas, tasa_red

def ValoracionKNN(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos a calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método KNN con pesos a 1.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    w = []
    for i in range(len(data[0])-1):
        w.append(1)
    w=np.array(w)
    for particion in particiones:
        #print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()
        tc,tr = Valoracion(np.array(particion), np.array(datos_train),k,w)
        fin = time.time()
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
