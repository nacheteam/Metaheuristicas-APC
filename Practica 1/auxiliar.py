import math

def lecturaDatos(nombre_fich):
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
def distanciaEuclidea(e1,e2):
    distancia = 0
    if len(e1)!=len(e2):
        print("No se puede hallar la distancia euclídea porque hay diferente número de atributos.")
    else:
        for i in range(len(e1)):
            distancia+=(e1[i]-e2[i])**2
    distancia = math.sqrt(distancia)
    return distancia
