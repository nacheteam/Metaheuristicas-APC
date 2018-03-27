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

def Relief(data):
    """
    @brief Función que implementa el algoritmo greedy Relief.
    @param data Datos de los que se obtiene el vector de pesos.
    @return Devuelve un vector de números entre 0 y 1 que nos dan la relevancia de cada característica.
    """
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

def ValoracionRelief(nombre_datos):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método relief.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        v = Relief(particion)
        vectores.append(v)
        datos_test = []
        for d in data:
            if d not in particion:
                datos_test.append(d)
        tc,tr = knn.Valoracion(datos_test,1,v)
        valoraciones.append(tc+tr)
        contador+=1
    return valoraciones
