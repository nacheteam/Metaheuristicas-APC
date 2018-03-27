import knn
import auxiliar
import operator

def elementoMinimaDistancia(e,lista):
    """
    @brief Devuelve el elemento de la lista que está más cercano a e.
    @param e Elemento con el que comparamos la distancia.
    @param lista Lista de la que queremos obtener el objeto con menor distancia a e.
    @return Devuelve el elemento de la lista con menor distancia a e.
    """
    distancias = []
    for l in lista:
        if l!=e:
            distancias.append(auxiliar.distanciaEuclidea(e,l,-1))
        else:
            distancias.append(-1)

    maximo = max(distancias)
    for i in range(len(distancias)):
        if distancias[i]==-1:
            distancias[i] = maximo

    indice_menor_distancia = 0
    for i in range(len(distancias)):
        if distancias[i]<distancias[indice_menor_distancia]:
            indice_menor_distancia=i
    return lista[indice_menor_distancia]

def Relief(nombre_datos):
    """
    @brief Función que implementa el algoritmo greedy Relief.
    @param nombre_datos Nombre del fichero de datos a clasificar.
    @return Devuelve un vector de números entre 0 y 1 que nos dan la relevancia de cada característica.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    w = []
    for i in range(len(data[0])):
        w.append(0)

    for element in data:
        clase = element[-1]
        amigos = []
        enemigos = []
        for e in data:
            if e!=element:
                if e[-1]==clase:
                    amigos.append(e)
                else:
                    enemigos.append(e)
        amigo_cercano = elementoMinimaDistancia(element, amigos)
        enemigo_cercano = elementoMinimaDistancia(element, enemigos)

        resta_enemigo = list(map(operator.sub, element, enemigo_cercano))

        resta_amigo = list(map(operator.sub, element, amigo_cercano))

        w = list(map(operator.add, w, resta_enemigo))
        w = list(map(operator.sub, w, resta_amigo))
        w_max = max(w)
        for i in range(len(w)):
            if w[i]<0:
                w[i]=0
            else:
                w[i]=w[i]/w_max
    return w
