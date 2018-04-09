import random
import auxiliar
import knn
import time

MU = 0
SIGMA = 0.3
MAX_EVALUACIONES = 15000
random.seed(123456789)

def mutacion(w, vector_posiciones):
    """
    @brief Dado un vector de pesos w se altera una de las posiciones que estén en vector_posiciones sumándole
    un valor generado por una distribución normal de media 0 y desviación 0.3.
    @param w Vector de pesos al que se le hace la mutación.
    @param vector_posiciones Vector que contiene las posiciones que aún no han sido mutadas.
    @return Se devuelve el vector de pesos mutados y el vector de posiciones con la posición usada elminada.
    """
    incremento = random.gauss(MU,SIGMA)
    i = random.randint(0,len(vector_posiciones)-1)
    vector_posiciones_aux = []
    pos = vector_posiciones[i]
    w[pos]+=incremento
    w_max = max(w)
    if w[pos]<0:
        w[pos] = 0
    elif w[pos]>1:
        w[pos] = 1
    for v in vector_posiciones:
        if v!=pos:
            vector_posiciones_aux.append(v)
    return w,vector_posiciones_aux

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
    MAX_VECINOS = 20*(len(data[0]))
    vecinos = 0
    evaluaciones = 0
    w = primerVector(len(data[0]))
    vector_posiciones = list(range(len(w)))
    tc,tr = knn.Valoracion(data,data,k,w,True)
    valoracion_actual = tc+tr
    while evaluaciones<MAX_EVALUACIONES and vecinos<MAX_VECINOS:
        evaluaciones+=1
        vecinos+=1
        vecino, vector_posiciones = mutacion(w,vector_posiciones)
        tc,tr = knn.Valoracion(data,data,k,vecino,True)
        valoracion_vecino = tc+tr
        if valoracion_vecino>valoracion_actual:
            w = vecino
            valoracion_actual=valoracion_vecino
            vector_posiciones = list(range(len(w)))
        elif vector_posiciones==[]:
            return w
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
        #print("Completado " + str((contador/len(particiones))*100) + "%\n")
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
