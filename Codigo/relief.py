import knn
import auxiliar
import operator
import time
import numpy as np

def elementoMinimaDistancia(e,lista):
    """
    @brief Devuelve el elemento de la lista que está más cercano a e.
    @param e Elemento con el que comparamos la distancia.
    @param lista Lista de la que queremos obtener el objeto con menor distancia a e.
    @return Devuelve el elemento de la lista con menor distancia a e.
    """

    #Calcula el vector de distancias con pesos a 1
    distancias = []
    w = []
    for i in range(len(lista)):
        w.append(1)
    for l in lista:
        if l!=e:
            distancias.append(auxiliar.distanciaEuclideaSimple(e,l,w))
        else:
            distancias.append(-1)

    #Coloca en la posición i-esima el máximo
    maximo = max(distancias)
    for i in range(len(distancias)):
        if distancias[i]==-1:
            distancias[i] = maximo

    #Obtiene el índice del elemento con menor distancia
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
    #Inicializa la solución a cero
    w = []
    for i in range(len(data[0])):
        w.append(0)

    #Bucle principal
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
        #Se hallan el amigo y enemigo más cercanos
        amigo_cercano = elementoMinimaDistancia(element, amigos)
        enemigo_cercano = elementoMinimaDistancia(element, enemigos)

        #Se resta al enemigo y se suma al amigo
        resta_enemigo = list(map(operator.sub, element, enemigo_cercano))

        resta_amigo = list(map(operator.sub, element, amigo_cercano))

        w = list(map(operator.add, w, resta_enemigo))
        w = list(map(operator.sub, w, resta_amigo))

    #Normalizamos la solución
    w_max = max(w)
    for i in range(len(w)):
        if w[i]<0:
            w[i]=0
        else:
            w[i]=w[i]/w_max
    return np.array(w[:len(w)-1])

def ValoracionRelief(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método relief.
    """
    #Inicializa los datos con los del fichero y las particiones
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0

    #Para cada partición
    for particion in particiones:
        #print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()

        #Hallamos el vector de pesos con el algoritmo relief
        v = Relief(datos_train)
        fin = time.time()
        vectores.append(v)

        #Hallamos la valoración del vector de pesos obtenido
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        tr=0
        val = [[tc,tr], fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
