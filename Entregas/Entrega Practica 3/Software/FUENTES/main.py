import knn
import relief
import auxiliar
import busqueda_local
import geneticos
import memeticos
import enfriamiento_simulado
import ils
import evolucion_diferencial

#Todos los algoritmos implementados
ALGORITMOS = ["KNN", "RELIEF", "BL", "GeneticoEstacionarioBLX", "GeneticoEstacionarioAritmetico", "GeneticoGeneracionalBLX", "GeneticoGeneracionalAritmetico", "Memetico prob=1 BLX", "Memetico prob=0.1 BLX", "Memetico prob=0.1 a los mejores BLX", "Memetico prob=1 Aritmetico", "Memetico prob=0.1 Aritmetico", "Memetico prob=0.1 a los mejores Aritmetico","ES","ILS","DE Rand1","DE CTB1"]
fichero = input("Introduzca el fichero de datos: ")
for i in range(len(ALGORITMOS)):
    print(str(i) + ": " + ALGORITMOS[i])
algoritmo = int(input("Introduzca el número del algoritmo que quiere ejecutar: "))
NUM_PARTICIONES = int(input("Introduzca el número de particiones de datos a realizar: "))
k = int(input("Introduzca el valor de k: "))

print("\nEl valor utilizado es K = " + str(k) + "\n")

resultados = []

if algoritmo==0:
    res_1nn = knn.ValoracionKNN(fichero,k)
    resultados=res_1nn
elif algoritmo==1:
    res_relief = relief.ValoracionRelief(fichero,k)
    resultados=res_relief
elif algoritmo==2:
    res_bl = busqueda_local.ValoracionBusquedaLocal(fichero,k)
    resultados=res_bl
elif algoritmo==3:
    res_genetico_estacionario_blx = geneticos.ValoracionGeneticoEstacionario(fichero,k,geneticos.cruceBLX)
    resultados=res_genetico_estacionario_blx
elif algoritmo==4:
    res_genetico_estacionario_aritmetico = geneticos.ValoracionGeneticoEstacionario(fichero,k,geneticos.cruceAritmetico)
    resultados=res_genetico_estacionario_aritmetico
elif algoritmo==5:
    res_genetico_generacional_blx = geneticos.ValoracionGeneticoGeneracional(fichero,k,geneticos.cruceBLX)
    resultados=res_genetico_generacional_blx
elif algoritmo==6:
    res_genetico_generacional_aritmetico = geneticos.ValoracionGeneticoGeneracional(fichero,k,geneticos.cruceAritmetico)
    resultados=res_genetico_generacional_aritmetico
elif algoritmo==7:
    res_memetico_1_blx = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,1,False)
    resultados=res_memetico_1_blx
elif algoritmo==8:
    res_memetico_01_blx = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,0.1,False)
    resultados=res_memetico_01_blx
elif algoritmo==9:
    res_memetico_01_blx_mejores = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceBLX,10,0.1,True)
    resultados=res_memetico_01_blx_mejores
elif algoritmo==10:
    res_memetico_1_aritmetico = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,1,False)
    resultados=res_memetico_1_aritmetico
elif algoritmo==11:
    res_memetico_01_aritmetico = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,0.1,False)
    resultados=res_memetico_01_aritmetico
elif algoritmo==12:
    res_memetico_01_aritmetico_mejores = memeticos.ValoracionMemetico(fichero,k,geneticos.cruceAritmetico,10,0.1,True)
    resultados=res_memetico_01_aritmetico_mejores
elif algoritmo==13:
    res_es = enfriamiento_simulado.ValoracionEnfriamientoSimulado(fichero,k)
    resultados=res_es
elif algoritmo==14:
    res_ils = ils.ValoracionILS(fichero,k)
    resultados = res_ils
elif algoritmo==15:
    res_DE_rand1 = evolucion_diferencial.ValoracionDERand1(fichero,k)
    resultados = res_DE_rand1
elif algoritmo==16:
    res_DE_CTB1 = evolucion_diferencial.ValoracionDECTB1(fichero,k)
    resultados = res_DE_CTB1
else:
    print("El número no es válido")
    exit()
print("Fichero de datos: " + fichero)
print("Tasa clasificación --- Tasa simplicidad --- Tasa total --- Tiempo\n")
for res in resultados:
    print(str(res[0][0]*2) + "-----" + str(res[0][1]*2) + "-----" + str(res[0][0]+res[0][1]) + "-----" + str(res[1]) + "\n")


media_tiempo = 0
media_tc = 0
media_tr = 0
for res in resultados:
    media_tc+=2*res[0][0]/NUM_PARTICIONES
    media_tr+=2*res[0][1]/NUM_PARTICIONES
    media_tiempo+=res[1]/NUM_PARTICIONES

print("MEDIAS: \n")
print(ALGORITMOS[algoritmo] + ": " + str(media_tc) + " --- " + str(media_tr) + " --- " + str(0.5*media_tc+0.5*media_tr) + " --- " + str(media_tiempo) + "\n")
