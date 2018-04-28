import math
import numpy as np
import random

MU = 0
SIGMA = 0.3

def lecturaDatos(nombre_fich):
    """
    @brief Función que lee un fichero con formato arff y devuelve una lista con los datos.
    @param nombre_fich Nombre del fichero arff para leer.
    @return Lista con los datos formateados.
    """
    data = []
    f = open(nombre_fich, "r")
    #El siguiente booleano indica cuando empiezan los datos en el fichero.
    son_datos = False
    linea_data = False
    for linea in f:
        #Tenemos en cuenta la aparición de @data y cogemos la línea de después.
        if son_datos:
            linea_data=True
        if "@data" in linea:
            son_datos=True
        if linea_data:
            data.append((linea.rstrip()).split(","))
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])

    min_max = []
    for i in range(len(data)):
        if min_max==[]:
            for j in range(len(data[i])):
                min_max.append([data[i][j],data[i][j]])
        else:
            for j in range(len(data[i])):
                if min_max[j][0]>data[i][j]:
                    min_max[j][0]=data[i][j]
                if min_max[j][1]<data[i][j]:
                    min_max[j][1]=data[i][j]

    for i in range(len(data)):
        for j in range(len(data[i])-1):
            data[i][j] = (data[i][j]-min_max[j][0])/(min_max[j][1]-min_max[j][0])

    data_sin_repeticiones = []
    for i in range(len(data)):
        unico = True
        for j in range(i,len(data)):
            if data[i]==data[j]:
                unico = False
        data_sin_repeticiones.append(data[i])

    return data_sin_repeticiones

def distanciaEuclideaSimple(e1,e2,w):
    """
    @brief Función que calcula la distancia euclídea.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos. Si w=-1 se toma como vector de pesos todo unos.
    @return Devuelve la distancia entre e1 y e2.
    """

    distancia = 0
    for i in range(len(e1)-1):
        if w[i]>0.2:
            distancia+=w[i]*(e1[i]-e2[i])**2
    return distancia

#Calcula la distancia euclídea de e1 a e2
def distanciaEuclidea(e1,e2,w):
    """
    @brief Función que calcula la distancia euclídea.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos. Si w=-1 se toma como vector de pesos todo unos.
    @return Devuelve la distancia entre e1 y e2.
    """

    return np.sum(w*(e1-e2)**2)

#Función para obtener el elemento más común de una lista
def masComun(lista):
    """
    @brief Devuelve el elemento más común de una lista.
    @param lista Lista de la que se obtiene el elemento más común.
    @return Devuelve el elemento que más veces aparece en la lista.
    """
    (values,counts) = np.unique(lista,return_counts=True)
    ind=np.argmax(counts)
    return values[ind]

def divideDatosFCV(data, num_folds):
    """
    @brief Función que divide los datos datos dados en particiones que mantienen el porcentaje de elementos de la misma clase que en el conjunto original.
    @param data Datos a particionar.
    @param num_folds Número de particiones a obtener.
    @return Devuelve una lista con num_folds listas de datos.
    """
    clases = []
    data_aux = data
    proporciones_clases = []
    folds = []
    usados = []
    tam_fold = int(len(data_aux)/num_folds)
    for d in data_aux:
        if d[-1] not in clases:
            clases.append(d[-1])
    for clase in clases:
        num = 0
        for d in data_aux:
            if d[-1]==clase:
                num+=1
        proporciones_clases.append(num/len(data_aux))

    for i in range(num_folds):
        fold = []
        for j in range(len(clases)):
            num_elementos_clase = int(proporciones_clases[j]*tam_fold)
            for k in range(len(data_aux)):
                if data_aux[k][-1]==clases[j] and num_elementos_clase>0 and k not in usados:
                    fold.append(data_aux[k])
                    usados.append(k)
                    num_elementos_clase-=1
        folds.append(fold)

    for i in range(len(data_aux)):
        if i not in usados:
            folds[-1].append(data_aux[i])

    return folds


def mutacion(w, pos):
    """
    @brief Dado un vector de pesos w se altera una de las posiciones que estén en vector_posiciones sumándole
    un valor generado por una distribución normal de media 0 y desviación 0.3.
    @param w Vector de pesos al que se le hace la mutación.
    @param vector_posiciones Vector que contiene las posiciones que aún no han sido mutadas.
    @return Se devuelve el vector de pesos mutados y el vector de posiciones con la posición usada elminada.
    """
    incremento = random.gauss(MU,SIGMA)
    pos_nueva =pos+1
    w[pos]+=incremento
    if w[pos]<0:
        w[pos] = 0
    elif w[pos]>1:
        w[pos] = 1
    return w,pos_nueva
