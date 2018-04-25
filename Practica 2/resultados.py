import knn
import relief
import auxiliar
import busqueda_local

FICHEROS_DATOS = ["../Data/ozone-320.arff","../Data/parkinsons.arff","../Data/spectf-heart.arff"]
ALGORITMOS = ["KNN", "RELIEF", "BL"]
NUM_PARTICIONES = 5

for k in [1,3,5]:

    print("############################################")
    print("El valor utilizado es K = " + str(k) + "\n")
    print("############################################")
    print("\n\n\n")

    for fichero in FICHEROS_DATOS:
        res_1nn = knn.ValoracionKNN(fichero,k)
        print("Acabado KNN")
        res_relief = relief.ValoracionRelief(fichero,k)
        print("Acabado Relief")
        res_bl = busqueda_local.ValoracionBusquedaLocal(fichero,k)
        print("Acabado BL")
        resultados = [res_1nn, res_relief, res_bl]
        print("\n\n\n")
        print("############################################")
        print("Fichero de datos: " + fichero)
        print("############################################")
        print("Tasa clasificación --- Tasa simplicidad --- Tasa total --- Tiempo\n")
        for i in range(len(ALGORITMOS)):
            print(ALGORITMOS[i] + ":\n")
            for res in resultados[i]:
                print(str(res[0][0]*2) + "-----" + str(res[0][1]*2) + "-----" + str(res[0][0]+res[0][1]) + "-----" + str(res[1]) + "\n")

        media_tiempo_1nn = 0
        media_tc_1nn = 0
        media_tr_1nn = 0
        for res in res_1nn:
            media_tc_1nn+=2*res[0][0]/NUM_PARTICIONES
            media_tr_1nn+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_1nn+=res[1]/NUM_PARTICIONES

        media_tiempo_relief = 0
        media_tc_relief = 0
        media_tr_relief = 0
        for res in res_relief:
            media_tc_relief+=2*res[0][0]/NUM_PARTICIONES
            media_tr_relief+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_relief+=res[1]/NUM_PARTICIONES

        media_tiempo_bl = 0
        media_tc_bl = 0
        media_tr_bl = 0
        for res in res_bl:
            media_tc_bl+=2*res[0][0]/NUM_PARTICIONES
            media_tr_bl+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_bl+=res[1]/NUM_PARTICIONES

        print("\n\n")
        print("################################################################")
        print("MEDIAS: \n")
        print("1NN: " + str(media_tc_1nn) + " --- " + str(media_tr_1nn) + " --- " + str(0.5*media_tc_1nn+0.5*media_tr_1nn) + " --- " + str(media_tiempo_1nn) + "\n")
        print("RELIEF: " + str(media_tc_relief) + " --- " + str(media_tr_relief) + " --- " + str(0.5*media_tc_relief+0.5*media_tr_relief) + " --- " + str(media_tiempo_relief) + "\n")
        print("BL: " + str(media_tc_bl) + " --- " + str(media_tr_bl) + " --- " + str(0.5*media_tc_bl+0.5*media_tr_bl) + " --- " + str(media_tiempo_bl) + "\n")
        print("################################################################")
