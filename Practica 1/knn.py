import auxiliar


def UnoNN(w,nombre_datos):
    """
    @brief Función que da una valoración del vector de pesos w para el conjunto de datos nombre_datos.
    @param w Vector de pesos.
    @param nombre_datos Nombre del fichero (ruta) que contiene los datos.
    @return Devuelve un número entre 0 y 1 indicando el ratio de aciertos con el vector de pesos dado.
    """

    data = auxiliar.lecturaDatos(nombre_datos)
    clases = []

    # Para cada elemento tomamos la distancia mínima y lo clasificamos.
    for i in range(len(data)):
        c_min = data[i+1][-1] if i<len(data)-1 else 0
        d_min = auxiliar.distanciaEuclidea(data[i],data[i+1],w) if i<len(data)-1 else auxiliar.distanciaEuclidea(data[i],data[0],w)
        for e in data:
            if e!=data[i]:
                d = auxiliar.distanciaEuclidea(data[i],e,w)
                if d_min>d:
                    c_min = e[-1]
                    d_min = d
        clases.append(c_min)

    # Comprobamos cual ha sido el porcentaje de éxito en la clasificación.
    bien_clasificadas = 0
    for (c,d) in zip(clases,data):
        if c==d[-1]:
            bien_clasificadas+=1

    return bien_clasificadas/len(data)
