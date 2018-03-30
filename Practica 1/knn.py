import auxiliar
import time

ALPHA=0.5

def KNN(w,particion, data_train,k):
    """
    @brief Función que da una valoración del vector de pesos w para el conjunto de datos nombre_datos.
    @param w Vector de pesos.
    @param data Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato.
    @return Devuelve un número entre 0 y 1 indicando el ratio de aciertos con el vector de pesos dado.
    """
    clases = []

    if data_train==-1:
        #Para cada elemento de los datos calculo los k elementos más cercanos y luego clasifico en función de la clase más repetida entre los k escogidos.
        for i in range(len(particion)):
            distancias = []
            minimos = []
            for j in range(len(data_train)):
                if particion[i]!=data_train[j]:
                    distancias.append([j,auxiliar.distanciaEuclidea(data_train[j],particion[i],w)])
            distancias.sort(key=lambda x: x[1])
            minimos = [item[0] for item in distancias[:k]]
            clases_minimos = []
            for m in minimos:
                clases_minimos.append(data_train[m][-1])
            clases.append(auxiliar.masComun(clases_minimos))

    # Comprobamos cual ha sido el porcentaje de éxito en la clasificación.
    bien_clasificadas = 0
    for (c,d) in zip(clases,particion):
        if c==d[-1]:
            bien_clasificadas+=1

    return bien_clasificadas/len(particion)


def Valoracion(particion, data_train,k,w):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """
    aciertos = KNN(w,particion, data_train,k)
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
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método KNN con pesos a 1.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    w = []
    for i in range(len(data[0])):
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
