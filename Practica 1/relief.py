import knn
import auxiliar

def elementoMinimaDistancia(e,lista):
    """
    @brief Devuelve el elemento de la lista que está más cercano a e.
    @param e Elemento con el que comparamos la distancia.
    @param lista Lista de la que queremos obtener el objeto con menor distancia a e.
    @return Devuelve el elemento de la lista con menor distancia a e.
    """
    distancias = []
    indice_elemento=-1
    for l in lista:
        if l!=e:
            distancias.append(auxiliar.distanciaEuclidea(e,l,-1))
        else:
            indice_elemento = lista.index(l)
            distancias.append(-1)

    if indice_elemento!=-1:
        distancias[indice_elemento] = max(distancias)
    return lista.index(min(distancias))

def Relief(nombre_datos):
    data = auxiliar.lecturaDatos(nombre_datos)
    w = []
    for i in range(len(data[0])-1):
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
        del resta_enemigo[-1]

        resta_amigo = list(map(operator.sub, element, amigo_cercano))
        del resta_amigo[-1]

        w = list(map(operador.add, w, resta_enemigo))
        w = list(map(operador.sub, w, resta_amigo))
        w_max = max(w)
        for wi in w:
            if wi<0:
                wi=0
            else:
                wi=wi/w_max
    return w
