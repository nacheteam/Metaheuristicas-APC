import auxiliar
import time

ALPHA=0.5

def KNN(w,data,k):
    """
    @brief Función que da una valoración del vector de pesos w para el conjunto de datos nombre_datos.
    @param w Vector de pesos.
    @param data Datos usados para clasificar.
    @param k Número de elementos con los que se compara cada dato.
    @return Devuelve un número entre 0 y 1 indicando el ratio de aciertos con el vector de pesos dado.
    """
    clases = []

    #Para cada elemento de los datos calculo los k elementos más cercanos y luego clasifico en función de la clase más repetida entre los k escogidos.
    for i in range(len(data)):
        distancias = []
        minimos = []
        for e in data:
                distancias.append(auxiliar.distanciaEuclidea(e,data[i],w))
        for j in range(k):
            minimo = j+1 if j<len(distancias)-1 else 0
            for l in range(len(distancias)):
                if l not in minimos and distancias[minimo]>distancias[l] and l!=i:
                    minimo=l
            minimos.append(minimo)
        clases_minimos = []
        for m in minimos:
            clases_minimos.append(data[m][-1])
        clases.append(auxiliar.masComun(clases_minimos))

    # Comprobamos cual ha sido el porcentaje de éxito en la clasificación.
    bien_clasificadas = 0
    for (c,d) in zip(clases,data):
        if c==d[-1]:
            bien_clasificadas+=1

    return bien_clasificadas/len(data)

def Valoracion(data,k,w):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """
    aciertos = KNN(w,data,k)
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
        comienzo = time.time()
        tc,tr = Valoracion(particion,k,w)
        fin = time.time()
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
