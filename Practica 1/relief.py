import knn
import auxiliar

def elementoMinimaDistancia(e,lista):
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
        
