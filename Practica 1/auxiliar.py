import math

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
    return data

#Calcula la distancia euclídea de e1 a e2
def distanciaEuclidea(e1,e2,w):
    """
    @brief Función que calcula la distancia euclídea.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            if w[i]>=0.2:
                distancia+=w[i]*(e1[i]-e2[i])**2 if w!=-1 else (e1[i]-e2[i])**2
    distancia = math.sqrt(distancia)
    return distancia

#Calcula la distancia Manhattan
def distanciaManhattan(e1,e2,w):
    """
    @brief Función que calcula la distancia de Manhattan.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            if w[i]>=0.2:
                distancia+=w[i]*abs(e1[i]-e2[i]) if w!=-1 else abs(e1[i]-e2[i])
    return distancia

#Calcula la distancia de Minkowski
def distanciaMinkowski(e1,e2,w,k):
    """
    @brief Función que calcula la distancia de Minkowski.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos.
    @param k Factor para la distancia.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            if w[i]>=0.2:
                distancia+=w[i]*abs((e1[i]-e2[i])**k) if w!=-1 else abs((e1[i]-e2[i])**k)
    return math.pow(distancia,1/k)

#Función para obtener el elemento más común de una lista
def masComun(lista):
    return max(set(lista), key=lista.count)
