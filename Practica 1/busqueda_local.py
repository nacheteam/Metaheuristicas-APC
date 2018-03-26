import random
import auxiliar
import knn

MU = 0
SIGMA = 0.3
MAX_EVALUACIONES = 15000
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
    i = random.randint(0,len(vector_posiciones))
    pos = vector_posiciones[i]
    w[pos]+=incremento
    for wi in w:
        if wi<0:
            wi=0
        else:
            wi=wi/w_max
    delete vector_posiciones[pos]
    return w,vector_posiciones

def busquedaLocal(nombre_datos):
    data = auxiliar.lecturaDatos(nombre_datos)
    MAX_VECINOS = 20*(len(data[0]))
    vecinos = 0
    evaluaciones = 0
    while evaluaciones<MAX_EVALUACIONES and vecinos<MAX_VECINOS:
        
