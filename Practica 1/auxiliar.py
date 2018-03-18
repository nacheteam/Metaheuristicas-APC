data = []

def lecturaDatos(nombre_fich):
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
