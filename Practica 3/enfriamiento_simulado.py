import numpy as np
import knn
import auxiliar

MU = 0.3
PHI = 0.3
K = 1

np.random.seed(123456789)

def enfriamiento(tk,beta):
    return tk/(1.0+beta*tk)

def EnfriamientoSimulado(data,k,MAX_EVALS=15000):
    #Se toman las tuplas y sus clases
    data_np = np.array([d[:-1] for d in data])
    labels_np = np.array([d[-1] for d in data])

    #Número de características
    ncar = len(data_np[0])

    #Solución inicial
    sol = np.random.uniform(0,1,ncar)
    mejor_sol = np.copy(sol)
    valoracion = knn.Valoracion(data_np, data_np,k,sol,labels_np, labels_np,True,True)
    valoracion_mejor_sol = valoracion

    #Temperatura inicial. Probablemente mal (reemplazar por 100-valoracion)
    T0 = (MU*valoracion)/np.log(PHI)

    #Temperatura final
    #Si la temperatura inicial es menor que la inicial entonces bajamos la temperatura final
    TF = 1e-03 if 1e-03>T0 else T0-1e-03

    #Número de enfriamientos y máximos vecinos
    max_vecinos = 10.0*ncar
    M = MAX_EVALS/max_vecinos

    #Beta
    beta = (T0-TF)/(M*T0*TF)

    #Inicializa la temperatura y evaluaciones
    t=T0
    evaluaciones = 1

    #Bucle principal
    while t<=TF and evaluaciones<MAX_EVALS:
        #Inicializo el número de vecinos considerados
        vecinos = 0
        #Booleano que indica si el vecino ha sido aceptado como solución
        aceptada = False
        #Mientras que no se acepte la solución y no se halla considerado el máximo número de vecinos
        while not aceptada and vecinos<max_vecinos:
            vecinos+=1
            evaluaciones+=1

            #Se obtiene el vecino y se ignora pos_nueva
            vecino,pos_nueva = auxiliar.mutacion(sol,np.random.randint(0,ncar-1))
            valoracion_vecino = knn.Valoracion(data_np,data_np,k,vecino,labels_np,labels_np,True,True)

            #Diferencia entre las valoraciones
            delta = valoracion_vecino - valoracion

            #Si la solución es mejor o un valor aleatorio cumple la condicion
            if delta<0 or np.random.uniform(0,1)<np.exp(-delta/(t*K)):
                #Aceptamos la solución
                sol = vecino
                valoracion = valoracion_vecino
                aceptada = True

                #Actualizamos la mejor solución si es necesario
                if valoracion_mejor_sol<valoracion:
                    mejor_sol = np.copy(sol)
                    valoracion_mejor_sol = valoracion
        #Disminuyo la temperatura
        t = enfriamiento(t,beta)

    return sol
