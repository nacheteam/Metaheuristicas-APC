import random
import auxiliar
import knn
import time
import numpy as np

MU = 0
SIGMA = 0.3
MAX_EVALUACIONES_GL = 15000
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

def busquedaLocal(data,k,MAX_EVALUACIONES=MAX_EVALUACIONES_GL,w_param=-1):
    """
    @brief Función de busqueda local para hallar un vector de pesos.
    @param data Lista con el conjunto de datos.
    @param k Valor de vecinos que se quieren calcular en KNN.
    @param MAX_EVALUACIONES Número máximo de evaluaciones, por defecto es MAX_EVALUACIONES_GL=15000
    @param w_param Vector de pesos del que se quiere arrancar la búsqueda local. Por defecto el valor es -1, con lo que se toma una solución inicial aleatoria.
    @return Devuelve un vector de pesos.
    """
    #Obtengo las clases de las tuplas
    labels_np = np.array([d[-1] for d in data])
    #Convierto todas las tuplas menos la clase a un numpy array
    data_np = np.array([d[:-1] for d in data])

    #El máximo número de vecinos a explorar es 20 por la dimension
    MAX_VECINOS = 20*(len(data[0])-1)
    vecinos = 0
    evaluaciones = 0

    #Inicializo la solución
    w = primerVector(len(data[0])-1) if w_param==-1 else w_param
    posicion_mutacion = 0

    #Inicializo la valoración de la solución
    tc,tr = knn.Valoracion(data_np,data_np,k,np.array(w),labels_np,labels_np,True)
    valoracion_actual = tc+tr

    #Bucle principal
    while evaluaciones<MAX_EVALUACIONES and vecinos<MAX_VECINOS:
        evaluaciones+=1
        vecinos+=1

        #Tomo un vecino con el operador de mutación
        vecino, posicion_mutacion = auxiliar.mutacion(w,posicion_mutacion)
        #Calculo su valoración
        tc,tr = knn.Valoracion(data_np,data_np,k,np.array(vecino),labels_np,labels_np,True)
        valoracion_vecino = tc+tr

        #Si ha mejorado a la solución w entonces la reemplazamos
        if valoracion_vecino>valoracion_actual:
            vecinos=0
            w = vecino
            valoracion_actual=valoracion_vecino
            posicion_mutacion = 0
        elif posicion_mutacion==len(w):
            posicion_mutacion=0

    #Devuelve la solución como un numpy array y el número de evaluaciones
    return np.array(w),evaluaciones


def ValoracionBusquedaLocal(nombre_datos,k):
    """
    @brief Función que obtiene la valoración para 5 particiones del conjunto de datos.
    @param nombre_datos Nombre del fichero de datos.
    @param k Número de vecinos que se quieren calcular en KNN.
    @return Devuelve un vector con las valoraciones de los vectores de pesos obtenidos por el método de búsqueda local.
    """
    #Inicializa los datos con los del fichero y las particiones
    data = auxiliar.lecturaDatos(nombre_datos)
    particiones = auxiliar.divideDatosFCV(data,5)
    vectores = []
    valoraciones = []
    contador = 0

    #Para cada partición
    for particion in particiones:
        print("Completado " + str((contador/len(particiones))*100) + "%\n")
        datos_train = []
        for d in data:
            if d not in particion:
                datos_train.append(d)
        comienzo = time.time()

        #Aplicamos la búsqueda local con el conjunto de entrenamiento data-particion
        v,ev = busquedaLocal(datos_train,k)
        fin = time.time()
        vectores.append(v)

        #Hallamos la valoración de la solución
        tc,tr = knn.Valoracion(np.array([p[:-1] for p in particion]), np.array([t[:-1] for t in datos_train]),k,v,np.array([p[-1] for p in datos_train]), np.array([t[-1] for t in particion]))
        val = [[tc,tr],fin-comienzo]
        valoraciones.append(val)
        contador+=1
    return valoraciones
