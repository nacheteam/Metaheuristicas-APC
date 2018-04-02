#!/bin/usr/gnuplot

################################################################################
#                             GRAFICAS K=1                                     #
################################################################################

set title "Tasa agregada k=1"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K1/tasa_agr_bl.dat" using 2:xticlabels(1) title "Tasa agregada BL", "./K1/tasa_agr_knn.dat" using 2:xticlabels(1) title "Tasa agregada 1NN", "./K1/tasa_agr_relief.dat" using 2:xticlabels(1) title "Tasa agregada Relief"

set term png
set output "./Imagenes/K1/tasa_agr.png"
replot
set term x11

set title "Tasa simplicidad k=1"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K1/tasa_simp_bl.dat" using 2:xticlabels(1) title "Tasa simplicidad BL", "./K1/tasa_simp_knn.dat" using 2:xticlabels(1) title "Tasa simplicidad 1NN", "./K1/tasa_simp_relief.dat" using 2:xticlabels(1) title "Tasa simplicidad Relief"

set term png
set output "./Imagenes/K1/tasa_simpl.png"
replot
set term x11

set title "Tasa clasificación k=1"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K1/tasa_clas_bl.dat" using 2:xticlabels(1) title "Tasa clasificación BL", "./K1/tasa_clas_knn.dat" using 2:xticlabels(1) title "Tasa clasificación 1NN", "./K1/tasa_clas_relief.dat" using 2:xticlabels(1) title "Tasa clasificación Relief"

set term png
set output "./Imagenes/K1/tasa_clas.png"
replot
set term x11

set title "Tiempo k=1"
set auto x
set yrange [0:500]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K1/tiempo_bl.dat" using 2:xticlabels(1) title "Tiempo BL", "./K1/tiempo_knn.dat" using 2:xticlabels(1) title "Tiempo 1NN", "./K1/tiempo_relief.dat" using 2:xticlabels(1) title "Tiempo Relief"

set term png
set output "./Imagenes/K1/tiempo.png"
replot
set term x11

################################################################################
#                             GRAFICAS K=3                                     #
################################################################################

set title "Tasa agregada k=3"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K3/tasa_agr_bl.dat" using 2:xticlabels(1) title "Tasa agregada BL", "./K3/tasa_agr_knn.dat" using 2:xticlabels(1) title "Tasa agregada 3NN", "./K3/tasa_agr_relief.dat" using 2:xticlabels(1) title "Tasa agregada Relief"

set term png
set output "./Imagenes/K3/tasa_agr.png"
replot
set term x11

set title "Tasa simplicidad k=3"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K3/tasa_simp_bl.dat" using 2:xticlabels(1) title "Tasa simplicidad BL", "./K3/tasa_simp_knn.dat" using 2:xticlabels(1) title "Tasa simplicidad 3NN", "./K3/tasa_simp_relief.dat" using 2:xticlabels(1) title "Tasa simplicidad Relief"

set term png
set output "./Imagenes/K3/tasa_simpl.png"
replot
set term x11

set title "Tasa clasificación k=3"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K3/tasa_clas_bl.dat" using 2:xticlabels(1) title "Tasa clasificación BL", "./K3/tasa_clas_knn.dat" using 2:xticlabels(1) title "Tasa clasificación 3NN", "./K3/tasa_clas_relief.dat" using 2:xticlabels(1) title "Tasa clasificación Relief"

set term png
set output "./Imagenes/K3/tasa_clas.png"
replot
set term x11

set title "Tiempo k=3"
set auto x
set yrange [0:500]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K3/tiempo_bl.dat" using 2:xticlabels(1) title "Tiempo BL", "./K3/tiempo_knn.dat" using 2:xticlabels(1) title "Tiempo 3NN", "./K3/tiempo_relief.dat" using 2:xticlabels(1) title "Tiempo Relief"

set term png
set output "./Imagenes/K3/tiempo.png"
replot
set term x11


################################################################################
#                             GRAFICAS K=5                                     #
################################################################################

set title "Tasa agregada k=5"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K5/tasa_agr_bl.dat" using 2:xticlabels(1) title "Tasa agregada BL", "./K5/tasa_agr_knn.dat" using 2:xticlabels(1) title "Tasa agregada 5NN", "./K5/tasa_agr_relief.dat" using 2:xticlabels(1) title "Tasa agregada Relief"

set term png
set output "./Imagenes/K5/tasa_agr.png"
replot
set term x11

set title "Tasa simplicidad k=5"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K5/tasa_simp_bl.dat" using 2:xticlabels(1) title "Tasa simplicidad BL", "./K5/tasa_simp_knn.dat" using 2:xticlabels(1) title "Tasa simplicidad 5NN", "./K5/tasa_simp_relief.dat" using 2:xticlabels(1) title "Tasa simplicidad Relief"

set term png
set output "./Imagenes/K5/tasa_simpl.png"
replot
set term x11

set title "Tasa clasificación k=5"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K5/tasa_clas_bl.dat" using 2:xticlabels(1) title "Tasa clasificación BL", "./K5/tasa_clas_knn.dat" using 2:xticlabels(1) title "Tasa clasificación 5NN", "./K5/tasa_clas_relief.dat" using 2:xticlabels(1) title "Tasa clasificación Relief"

set term png
set output "./Imagenes/K5/tasa_clas.png"
replot
set term x11

set title "Tiempo k=5"
set auto x
set yrange [0:500]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./K5/tiempo_bl.dat" using 2:xticlabels(1) title "Tiempo BL", "./K5/tiempo_knn.dat" using 2:xticlabels(1) title "Tiempo 5NN", "./K5/tiempo_relief.dat" using 2:xticlabels(1) title "Tiempo Relief"

set term png
set output "./Imagenes/K5/tiempo.png"
replot
set term x11
