import random
import auxiliar
import knn
import time
import numpy as np

MU = 0
SIGMA = 0.3
MAX_EVALUACIONES = 15000
random.seed(123456789)

def primerVector(n):
    """
    @brief Función que te devuelve un vector inicial de pesos con valores aleatorios según una distribución uniforme entre 0 y 1.
    @param n Tamaño del vector.
    @return Devuelve un vector de pesos generado de forma aleatoria.
    """
    w = []
    for i in range(n):
        w.append(random.uniform(0,1))
    return w

def busquedaLocal(data,k):
    """
    @brief Función de busqueda local para hallar un vector de pesos.
    @param data Lista con el conjunto de datos.
    @param k Valor de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector de pesos.
    """
    data_np = np.array(data)
    MAX_VECINOS = 20*(len(data[0])-1)
    vecinos = 0
    evaluaciones = 0
    w = primerVector(len(data[0])-1)
    posicion_mutacion = 0
    tc,tr = knn.Valoracion(data_np,data_np,k,w,True)
    valoracion_actual = tc+tr
    while evaluaciones<MAX_EVALUACIONES and vecinos<MAX_VECINOS:
        evaluaciones+=1
        vecinos+=1
        vecino, posicion_mutacion = auxiliar.mutacion(w,posicion_mutacion)
        tc,tr = knn.Valoracion(data_np,data_np,k,vecino,True)
        valoracion_vecino = tc+tr
        if valoracion_vecino>valoracion_actual:
            vecinos=0
            w = vecino
            valoracion_actual=valoracion_vecino
            posicion_mutacion = 0
        elif posicion_mutacion==len(w):
            posicion_mutacion=0
    return w


def ValoracionBusquedaLocal(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método de búsqueda local.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()
        v = busquedaLocal(datos_train,k)
        fin = time.time()
        vectores.append(v)
        tc,tr = knn.Valoracion(particion,datos_train, k,v)
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
