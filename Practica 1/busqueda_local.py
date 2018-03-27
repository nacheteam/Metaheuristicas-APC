import random
import auxiliar
import knn

MU = 0
SIGMA = 0.3
MAX_EVALUACIONES = 15000
K=1
random.seed(1010101010)

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
    for i in range(len(w)):
        if w[i]<0:
            w[i]=0
        else:
            w[i]=w[i]/w_max
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

def busquedaLocal(nombre_datos):
    """
    @brief Función de busqueda local para hallar un vector de pesos.
    @param nombre_datos Fichero con el que se quiere ajustar el vector de pesos.
    @return Devuelve un vector de pesos.
    """
    data = auxiliar.lecturaDatos(nombre_datos)
    MAX_VECINOS = 20*(len(data[0]))
    vecinos = 0
    evaluaciones = 0
    w = primerVector(len(data[0]))
    vector_posiciones = list(range(len(w)))
    valoracion_actual = knn.Valoracion(nombre_datos,K,w)
    while evaluaciones<MAX_EVALUACIONES and vecinos<MAX_VECINOS:
        evaluaciones+=1
        vecinos+=1
        vecino, vector_posiciones = mutacion(w,vector_posiciones)
        valoracion_vecino = knn.Valoracion(nombre_datos,K,vecino)
        if valoracion_vecino>valoracion_actual:
            print("Se ha mejorado")
            w = vecino
            valoracion_actual=valoracion_vecino
            print(valoracion_actual)
            vector_posiciones = list(range(len(w)))
        elif vector_posiciones==[]:
            return w
    return w
