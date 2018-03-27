import auxiliar

def KNN(w,nombre_datos,k):
    """
    @brief Función que da una valoración del vector de pesos w para el conjunto de datos nombre_datos.
    @param w Vector de pesos.
    @param nombre_datos Nombre del fichero (ruta) que contiene los datos.
    @param k Número de elementos con los que se compara cada dato.
    @return Devuelve un número entre 0 y 1 indicando el ratio de aciertos con el vector de pesos dado.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    clases = []

    #Para cada elemento de los datos calculo los k elementos más cercanos y luego clasifico en función de la clase más repetida entre los k escogidos.
    for i in range(len(data)):
        distancias = []
        minimos = []
        for e in data:
                distancias.append(aux.distanciaEuclidea(e,data[i],w))
        for j in k:
            minimo = j+1 if j<len(distancias)-1 else 0
            for l in range(distancias):
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

def Valoracion(nombre_datos,k,w):
    """
    @brief Ejecuta el algoritmo knn y da una media de 0 a 100 de lo bueno que es el vector de pesos dados considerando la simplicidad y la tasa de aciertos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de elementos con los que se compara cada dato en el knn.
    @param w Vector de pesos.
    @return Número del 0 al 100 que da una valoración del vector de pesos dado. 0 es el mínimo 100 el máximo.
    """
    aciertos = KNN(w,nombre_datos,k)
    simplicidad = 0

    pesos_bajos = 0
    for wi in w:
        if wi<0.2:
            pesos_bajos+=1
    simplicidad = pesos_bajos/len(w)
    return 100*(simplicidad+aciertos)
