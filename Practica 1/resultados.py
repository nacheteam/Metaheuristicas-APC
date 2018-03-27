import knn
import relief
import auxiliar
import busqueda_local

FICHEROS_DATOS = ["../Data/ozone-320.arff","../Data/parkinsons.arff","../Data/spectf-heart.arff"]
ALGORITMOS = ["1NN", "RELIEF", "BL"]

for fichero in FICHEROS_DATOS:
    res_1nn = knn.ValoracionKNN(fichero)
    res_relief = relief.ValoracionRelief(fichero)
    res_bl = busqueda_local.ValoracionBusquedaLocal(fichero)
    resultados = [res_1nn, res_relief, res_bl]
    print("Fichero de datos: " + fichero)
    print("Tasa clasificación --- Tasa simplicidad --- Tasa total --- Tiempo\n")
    for i in range(len(ALGORITMOS)):
        print(ALGORITMOS[i] + ":\n")
        for res in resultados[i]:
            print(str(res[0][0]) + " --- " + str(res[0][1]) + " --- " + str(res[0][0]+res[0][1]) + " --- " + str(res[1]) + "\n")
