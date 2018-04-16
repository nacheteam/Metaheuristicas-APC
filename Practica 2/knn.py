import auxiliar
import time
import numpy as np

ALPHA=0.5

def devuelveKminimos(distancias, k):
    minimos = []
    for i in range(k):
        minimo = i
        for j in range(len(distancias)):
            if distancias[j][1]<distancias[minimo][1]:
                minimo = j
        minimos.append(distancias[minimo])
    return minimos

def KNN(w,particion, data_train,k,mismos_conjuntos):
    """
    @brief Función que da una valoración del vector de pesos w para el conjunto de datos nombre_datos.
    @param w Vector de pesos.
    @param particion Datos a clasificar.
    @param data_train Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato.
    @return Devuelve un número entre 0 y 1 indicando el ratio de aciertos con el vector de pesos dado.
    """
    particion_np = np.array(particion)
    data_train_np = np.array(data_train)
    w_np = np.array(w)
    for i in range(len(w_np)):
        if w_np[i]<0.2:
            w_np[i]=0
    clases = []
    if not mismos_conjuntos:
        #Para cada elemento de los datos calculo los k elementos más cercanos y luego clasifico en función de la clase más repetida entre los k escogidos.
        for i in range(len(particion_np)):
            distancias = []
            minimos = []
            for j in range(len(data_train_np)):
                if particion_np[i]!=data_train_np[j]
                    distancias.append([j,auxiliar.distanciaEuclidea(data_train_np[j][:len(data_train_np[j])-1],particion_np[i][:len(particion_np[i])-1],w_np)])
            min_distancias = devuelveKminimos(distancias,k)
            minimos = [item[0] for item in min_distancias]
            clases_minimos = []
            for m in minimos:
                clases_minimos.append(data_train_np[m][-1])
            clases.append(auxiliar.masComun(clases_minimos))
    else:
        distancias = []
        for i in range(len(particion_np)):
            dis = []
            for j in range(len(particion_np)):
                dis.append([j,float('inf')])
            distancias.append(dis)

        for i in range(len(particion_np)):
            for j in range(i,len(particion_np)):
                if particion_np[i]!=particion_np[j]:
                    distancias[i][j] = [distancias[i][j][0], auxiliar.distanciaEuclidea(particion_np[i][:len(particion_np[i])-1],particion_np[j][:len(particion_np[j])-1],w_np)]
                    distancias[j][i] = [distancias[j][i][0], distancias[i][j][1]]

        for i in range(len(particion_np)):
            min_distancias = devuelveKminimos(distancias[i],k)
            minimos = [item[0] for item in min_distancias]
            clases_minimos = []
            for m in minimos:
                clases_minimos.append(particion_np[m][-1])
            clases.append(auxiliar.masComun(clases_minimos))

    # Comprobamos cual ha sido el porcentaje de éxito en la clasificación.
    bien_clasificadas = 0
    for (c,d) in zip(clases,particion_np):
        if c==d[-1]:
            bien_clasificadas+=1

    return bien_clasificadas/len(particion_np)


def Valoracion(particion, data_train,k,w,mismos_conjuntos=False):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param particion Datos a clasificar.
    @param data_train Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """
    aciertos = KNN(w,particion, data_train,k,mismos_conjuntos)
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
    for particion in particiones:
        #print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()
        tc,tr = Valoracion(particion, datos_train,k,w)
        fin = time.time()
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
