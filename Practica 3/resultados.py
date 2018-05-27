import knn
import relief
import auxiliar
import busqueda_local
import geneticos
import memeticos
import ils
import enfriamiento_simulado
import evolucion_diferencial

FICHEROS_DATOS = ["../Data/ozone-320.arff","../Data/parkinsons.arff","../Data/spectf-heart.arff"]
#ALGORITMOS = ["KNN", "RELIEF", "BL", "GeneticoEstacionarioBLX", "GeneticoEstacionarioAritmetico", "GeneticoGeneracionalBLX", "GeneticoGeneracionalAritmetico", "Memetico prob=1 BLX", "Memetico prob=0.1 BLX", "Memetico prob=0.1 a los mejores BLX", "Memetico prob=1 Aritmetico", "Memetico prob=0.1 Aritmetico", "Memetico prob=0.1 a los mejores Aritmetico", "ES","ILS","DE Rand1","DE CTB1"]
ALGORITMOS = ["ES","ILS","DE Rand1","DE CTB1"]
NUM_PARTICIONES = 5

for k in [1]:

    print("############################################")
    print("El valor utilizado es K = " + str(k) + "\n")
    print("############################################")
    print("\n\n\n")

    for fichero in FICHEROS_DATOS:
        '''
        res_1nn = knn.ValoracionKNN(fichero,k)
        print("Acabado KNN")
        res_relief = relief.ValoracionRelief(fichero,k)
        print("Acabado Relief")
        res_bl = busqueda_local.ValoracionBusquedaLocal(fichero,k)
        print("Acabado BL")
        res_genetico_estacionario_blx = geneticos.ValoracionGeneticoEstacionario(fichero,k,geneticos.cruceBLX)
        print("Acabado Genetico Estacionario BLX")
        res_genetico_estacionario_aritmetico = geneticos.ValoracionGeneticoEstacionario(fichero,k,geneticos.cruceAritmetico)
        print("Acabado Genetico Estacionario Aritmetico")
        res_genetico_generacional_blx = geneticos.ValoracionGeneticoGeneracional(fichero,k,geneticos.cruceBLX)
        print("Acabado Genetico Generacional BLX")
        res_genetico_generacional_aritmetico = geneticos.ValoracionGeneticoGeneracional(fichero,k,geneticos.cruceAritmetico)
        print("Acabado Genetico Generacional Aritmetico")
        res_memetico_1_blx = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,1,False)
        print("Acabado Memetico BLX prob=1 sin mejores")
        res_memetico_01_blx = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,0.1,False)
        print("Acabado Memetico BLX prob=0.1 sin mejores")
        res_memetico_01_mejores_blx = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,0.1,True)
        print("Acabado Memetico BLX prob=0.1 con mejores")
        res_memetico_1_aritmetico = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,1,False)
        print("Acabado Memetico Aritmetico prob=1 sin mejores")
        res_memetico_01_aritmetico = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,0.1,False)
        print("Acabado Memetico Aritmetico prob=0.1 sin mejores")
        res_memetico_01_mejores_aritmetico = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,0.1,True)
        print("Acabado Memetico Aritmetico prob=0.1 con mejores")
        '''
        res_es = enfriamiento_simulado.ValoracionEnfriamientoSimulado(fichero,k)
        print("Acabado Enfriamiento Simulado")
        res_ils = ils.ValoracionILS(fichero,k)
        print("Acabado ILS")
        res_DE_rand1 = evolucion_diferencial.ValoracionDERand1(fichero,k)
        print("Acabado DE Rand1")
        res_DE_CTB1 = evolucion_diferencial.ValoracionDECTB1(fichero,k)
        print("Acabado DE CTB1")
        #resultados = [res_1nn, res_relief, res_bl, res_genetico_estacionario_blx, res_genetico_estacionario_aritmetico, res_genetico_generacional_blx, res_genetico_generacional_aritmetico, res_memetico_1_blx, res_memetico_01_blx, res_memetico_01_mejores_blx, res_memetico_1_aritmetico, res_memetico_01_aritmetico, res_memetico_01_mejores_aritmetico, res_es, res_ils, res_DE_rand1, res_DE_CTB1]
        resultados = [res_es, res_ils, res_DE_rand1, res_DE_CTB1]
        print("\n\n\n")
        print("############################################")
        print("Fichero de datos: " + fichero)
        print("############################################")
        print("Tasa clasificación --- Tasa simplicidad --- Tasa total --- Tiempo\n")
        for i in range(len(ALGORITMOS)):
            print(ALGORITMOS[i] + ":\n")
            for res in resultados[i]:
                print(str(res[0][0]*2) + "-----" + str(res[0][1]*2) + "-----" + str(res[0][0]+res[0][1]) + "-----" + str(res[1]) + "\n")

        '''
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

        media_tiempo_genetico_estacionario_blx = 0
        media_tc_genetico_estacionario_blx = 0
        media_tr_genetico_estacionario_blx = 0
        for res in res_genetico_estacionario_blx:
            media_tc_genetico_estacionario_blx+=2*res[0][0]/NUM_PARTICIONES
            media_tr_genetico_estacionario_blx+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_genetico_estacionario_blx+=res[1]/NUM_PARTICIONES

        media_tiempo_genetico_estacionario_aritmetico = 0
        media_tc_genetico_estacionario_aritmetico = 0
        media_tr_genetico_estacionario_aritmetico = 0
        for res in res_genetico_estacionario_aritmetico:
            media_tc_genetico_estacionario_aritmetico+=2*res[0][0]/NUM_PARTICIONES
            media_tr_genetico_estacionario_aritmetico+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_genetico_estacionario_aritmetico+=res[1]/NUM_PARTICIONES

        media_tiempo_genetico_generacional_blx = 0
        media_tc_genetico_generacional_blx = 0
        media_tr_genetico_generacional_blx = 0
        for res in res_genetico_generacional_blx:
            media_tc_genetico_generacional_blx+=2*res[0][0]/NUM_PARTICIONES
            media_tr_genetico_generacional_blx+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_genetico_generacional_blx+=res[1]/NUM_PARTICIONES

        media_tiempo_genetico_generacional_aritmetico = 0
        media_tc_genetico_generacional_aritmetico = 0
        media_tr_genetico_generacional_aritmetico = 0
        for res in res_genetico_generacional_aritmetico:
            media_tc_genetico_generacional_aritmetico+=2*res[0][0]/NUM_PARTICIONES
            media_tr_genetico_generacional_aritmetico+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_genetico_generacional_aritmetico+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_1_blx = 0
        media_tc_memetico_1_blx = 0
        media_tr_memetico_1_blx = 0
        for res in res_memetico_1_blx:
            media_tc_memetico_1_blx+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_1_blx+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_1_blx+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_01_blx = 0
        media_tc_memetico_01_blx = 0
        media_tr_memetico_01_blx = 0
        for res in res_memetico_01_blx:
            media_tc_memetico_01_blx+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_01_blx+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_01_blx+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_01_mejores_blx = 0
        media_tc_memetico_01_mejores_blx = 0
        media_tr_memetico_01_mejores_blx = 0
        for res in res_memetico_01_mejores_blx:
            media_tc_memetico_01_mejores_blx+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_01_mejores_blx+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_01_mejores_blx+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_1_aritmetico = 0
        media_tc_memetico_1_aritmetico = 0
        media_tr_memetico_1_aritmetico = 0
        for res in res_memetico_1_aritmetico:
            media_tc_memetico_1_aritmetico+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_1_aritmetico+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_1_aritmetico+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_01_aritmetico = 0
        media_tc_memetico_01_aritmetico = 0
        media_tr_memetico_01_aritmetico = 0
        for res in res_memetico_01_aritmetico:
            media_tc_memetico_01_aritmetico+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_01_aritmetico+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_01_aritmetico+=res[1]/NUM_PARTICIONES

        media_tiempo_memetico_01_mejores_aritmetico = 0
        media_tc_memetico_01_mejores_aritmetico = 0
        media_tr_memetico_01_mejores_aritmetico = 0
        for res in res_memetico_01_mejores_aritmetico:
            media_tc_memetico_01_mejores_aritmetico+=2*res[0][0]/NUM_PARTICIONES
            media_tr_memetico_01_mejores_aritmetico+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_memetico_01_mejores_aritmetico+=res[1]/NUM_PARTICIONES

        '''
        media_tiempo_es = 0
        media_tc_es = 0
        media_tr_es = 0
        for res in res_es:
            media_tc_es+=2*res[0][0]/NUM_PARTICIONES
            media_tr_es+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_es+=res[1]/NUM_PARTICIONES

        media_tiempo_ils = 0
        media_tc_ils = 0
        media_tr_ils = 0
        for res in res_ils:
            media_tc_ils+=2*res[0][0]/NUM_PARTICIONES
            media_tr_ils+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_ils+=res[1]/NUM_PARTICIONES

        media_tiempo_DE_rand1 = 0
        media_tc_DE_rand1 = 0
        media_tr_DE_rand1 = 0
        for res in res_DE_rand1:
            media_tc_DE_rand1+=2*res[0][0]/NUM_PARTICIONES
            media_tr_DE_rand1+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_DE_rand1+=res[1]/NUM_PARTICIONES

        media_tiempo_DE_CTB1 = 0
        media_tc_DE_CTB1 = 0
        media_tr_DE_CTB1 = 0
        for res in res_DE_CTB1:
            media_tc_DE_CTB1+=2*res[0][0]/NUM_PARTICIONES
            media_tr_DE_CTB1+=2*res[0][1]/NUM_PARTICIONES
            media_tiempo_DE_CTB1+=res[1]/NUM_PARTICIONES

        print("\n\n")
        print("################################################################")
        print("MEDIAS: \n")
        '''
        print("1NN: " + str(media_tc_1nn) + " --- " + str(media_tr_1nn) + " --- " + str(0.5*media_tc_1nn+0.5*media_tr_1nn) + " --- " + str(media_tiempo_1nn) + "\n")
        print("RELIEF: " + str(media_tc_relief) + " --- " + str(media_tr_relief) + " --- " + str(0.5*media_tc_relief+0.5*media_tr_relief) + " --- " + str(media_tiempo_relief) + "\n")
        print("BL: " + str(media_tc_bl) + " --- " + str(media_tr_bl) + " --- " + str(0.5*media_tc_bl+0.5*media_tr_bl) + " --- " + str(media_tiempo_bl) + "\n")
        print("GeneticoEstacionarioBLX: " + str(media_tc_genetico_estacionario_blx) + " --- " + str(media_tr_genetico_estacionario_blx) + " --- " + str(0.5*media_tc_genetico_estacionario_blx+0.5*media_tr_genetico_estacionario_blx) + " --- " + str(media_tiempo_genetico_estacionario_blx) + "\n")
        print("GeneticoEstacionarioAritmetico: " + str(media_tc_genetico_estacionario_aritmetico) + " --- " + str(media_tr_genetico_estacionario_aritmetico) + " --- " + str(0.5*media_tc_genetico_estacionario_aritmetico+0.5*media_tr_genetico_estacionario_aritmetico) + " --- " + str(media_tiempo_genetico_estacionario_aritmetico) + "\n")
        print("GeneticoGeneracionalBLX: " + str(media_tc_genetico_generacional_blx) + " --- " + str(media_tr_genetico_generacional_blx) + " --- " + str(0.5*media_tc_genetico_generacional_blx+0.5*media_tr_genetico_generacional_blx) + " --- " + str(media_tiempo_genetico_generacional_blx) + "\n")
        print("GeneticoGeneracionalAritmetico: " + str(media_tc_genetico_generacional_aritmetico) + " --- " + str(media_tr_genetico_generacional_aritmetico) + " --- " + str(0.5*media_tc_genetico_generacional_aritmetico+0.5*media_tr_genetico_generacional_aritmetico) + " --- " + str(media_tiempo_genetico_generacional_aritmetico) + "\n")
        print("Memetico prob=1 BLX: " + str(media_tc_memetico_1_blx) + " --- " + str(media_tr_memetico_1_blx) + " --- " + str(0.5*media_tc_memetico_1_blx+0.5*media_tr_memetico_1_blx) + " --- " + str(media_tiempo_memetico_1_blx) + "\n")
        print("Memetico prob=0.1 BLX: " + str(media_tc_memetico_01_blx) + " --- " + str(media_tr_memetico_01_blx) + " --- " + str(0.5*media_tc_memetico_01_blx+0.5*media_tr_memetico_01_blx) + " --- " + str(media_tiempo_memetico_01_blx) + "\n")
        print("Memetico prob=0.1 a los mejores BLX: " + str(media_tc_memetico_01_mejores_blx) + " --- " + str(media_tr_memetico_01_mejores_blx) + " --- " + str(0.5*media_tc_memetico_01_mejores_blx+0.5*media_tr_memetico_01_mejores_blx) + " --- " + str(media_tiempo_memetico_01_mejores_blx) + "\n")
        print("Memetico prob=1 Aritmetico: " + str(media_tc_memetico_1_aritmetico) + " --- " + str(media_tr_memetico_1_aritmetico) + " --- " + str(0.5*media_tc_memetico_1_aritmetico+0.5*media_tr_memetico_1_aritmetico) + " --- " + str(media_tiempo_memetico_1_aritmetico) + "\n")
        print("Memetico prob=0.1 Aritmetico: " + str(media_tc_memetico_01_aritmetico) + " --- " + str(media_tr_memetico_01_aritmetico) + " --- " + str(0.5*media_tc_memetico_01_aritmetico+0.5*media_tr_memetico_01_aritmetico) + " --- " + str(media_tiempo_memetico_01_aritmetico) + "\n")
        print("Memetico prob=0.1 a los mejores Aritmetico: " + str(media_tc_memetico_01_mejores_aritmetico) + " --- " + str(media_tr_memetico_01_mejores_aritmetico) + " --- " + str(0.5*media_tc_memetico_01_mejores_aritmetico+0.5*media_tr_memetico_01_mejores_aritmetico) + " --- " + str(media_tiempo_memetico_01_mejores_aritmetico) + "\n")
        '''
        print("ES: " + str(media_tc_es) + " --- " + str(media_tr_es) + " --- " + str(0.5*media_tc_es+0.5*media_tr_es) + " --- " + str(media_tiempo_es) + "\n")
        print("ILS: " + str(media_tc_ils) + " --- " + str(media_tr_ils) + " --- " + str(0.5*media_tc_ils+0.5*media_tr_ils) + " --- " + str(media_tiempo_ils) + "\n")
        print("DE Rand1: " + str(media_tc_DE_rand1) + " --- " + str(media_tr_DE_rand1) + " --- " + str(0.5*media_tc_DE_rand1+0.5*media_tr_DE_rand1) + " --- " + str(media_tiempo_DE_rand1) + "\n")
        print("DE CTB1: " + str(media_tc_DE_CTB1) + " --- " + str(media_tr_DE_CTB1) + " --- " + str(0.5*media_tc_DE_CTB1+0.5*media_tr_DE_CTB1) + " --- " + str(media_tiempo_DE_CTB1) + "\n")
        print("################################################################")
