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
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
    return data

#Calcula la distancia euclídea de e1 a e2
def distanciaEuclidea(e1,e2,w):
    """
    @brief Función que calcula la distancia euclídea.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos. Si w=-1 se toma como vector de pesos todo unos.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            distancia+=w[i]*(e1[i]-e2[i])**2 if w!=-1 else (e1[i]-e2[i])**2
    distancia = math.sqrt(distancia)
    return distancia

#Calcula la distancia Manhattan
def distanciaManhattan(e1,e2,w):
    """
    @brief Función que calcula la distancia de Manhattan.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos. Si w=-1 se toma como vector de pesos todo unos.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            distancia+=w[i]*abs(e1[i]-e2[i]) if w!=-1 else abs(e1[i]-e2[i])
    return distancia

#Calcula la distancia de Minkowski
def distanciaMinkowski(e1,e2,w,k):
    """
    @brief Función que calcula la distancia de Minkowski.
    @param e1 Elemento 1.
    @param e2 Elemento 2.
    @param w Vector de pesos. Si w=-1 se toma como vector de pesos todo unos.
    @param k Factor para la distancia.
    @return Devuelve la distancia entre e1 y e2.
    """
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            distancia+=w[i]*abs((e1[i]-e2[i])**k) if w!=-1 else abs((e1[i]-e2[i])**k)
    return math.pow(distancia,1/k)

#Función para obtener el elemento más común de una lista
def masComun(lista):
    """
    @brief Devuelve el elemento más común de una lista.
    @param lista Lista de la que se obtiene el elemento más común.
    @return Devuelve el elemento que más veces aparece en la lista.
    """
    return max(set(lista), key=lista.count)

def normaEuclidea(e):
    """
    @brief Función que devuelve la norma euclídea de un vector e.
    @param e Vector al que se le quiere calcular la norma.
    @return Devuelve un valor real que es la raíz cuadrada de la suma de cada componente del vector al cuadrado.
    """
    norma = 0
    for ei in e:
        norma+=ei**2
    return math.sqrt(norma)

def divideDatosFCV(data, num_folds):
    """
    @brief Función que divide los datos datos dados en particiones que mantienen el porcentaje de elementos de la misma clase que en el conjunto original.
    @param data Datos a particionar.
    @para num_folds Número de particiones a obtener.
    @return Devuelve una lista con num_folds listas de datos.
    """
    datos_divididos_clases = []
    clases = []
    num_clases_diferentes = 0
    for e in data:
        if e[-1] not in clases:
            clases.append(e[-1])
            num_clases_diferentes+=1
    for clase in clases:
        lista_clase = []
        for e in data:
            if e[-1]==clase:
                lista_clase.append(e)
        datos_divididos_clases.append(lista_clase)
    porcentajes_clases = []
    for i in range(datos_divididos_clases):
        porcentajes_clases.append(len(datos_divididos_clases[i])/len(data))
    folds = []
    for i in range(num_folds):
        fold = []
        tam_fold = len(data)/num_folds
        for j in range(tam_fold):
            for t in range(len(porcentajes_clases)):
                for k in range(int(tam_fold*porcentaje)):
                    fold.append(datos_divididos_clases[t][0])
                    del datos_divididos_clases[t][0]
        folds.append(fold)
    for e in datos_divididos_clases:
        for ei in e:
            folds[-1].append(ei)
    return folds
