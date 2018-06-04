#!/bin/usr/gnuplot

################################################################################
#                                 GRAFICAS TIEMPO                              #
################################################################################

set title "Tiempos ozone"
set auto x
set yrange [0:700]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Tiempos/ozone.dat" using 2:xticlabels(1) title "Tiempos"

set term png
set output "./Imagenes/Tiempos/tiempos_ozone.png"
replot
set term x11

set title "Tiempos parkinsons"
set auto x
set yrange [0:300]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Tiempos/parkinsons.dat" using 2:xticlabels(1) title "Tiempos"

set term png
set output "./Imagenes/Tiempos/tiempos_parkinsons.png"
replot
set term x11

set title "Tiempos spectf-heart"
set auto x
set yrange [0:700]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Tiempos/spectf-heart.dat" using 2:xticlabels(1) title "Tiempos"

set term png
set output "./Imagenes/Tiempos/tiempos_spectf-heart.png"
replot
set term x11


################################################################################
#                               GRAFICAS RESULTADOS                            #
################################################################################

set title "Resultados ozone"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/ozone.dat" using 2:xticlabels(1) title "Resultados"

set term png
set output "./Imagenes/Resultados/ozone.png"
replot
set term x11

set title "Resultados parkinsons"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/parkinsons.dat" using 2:xticlabels(1) title "Resultados"

set term png
set output "./Imagenes/Resultados/parkinsons.png"
replot
set term x11

set title "Resultados spectf-heart"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/spectf-heart.dat" using 2:xticlabels(1) title "Resultados"

set term png
set output "./Imagenes/Resultados/spectf-heart.png"
replot
set term x11

################################################################################
#                         GRAFICAS RESULTADOS COMPARATIVA                      #
################################################################################

set title "Resultados comparativa ozone"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/ozone_comparativa.dat" using 2:xticlabels(1) title "Resultados comparativa"

set term png
set output "./Imagenes/Resultados/ozone_comparativa.png"
replot
set term x11

set title "Resultados comparativa parkinsons"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/parkinsons_comparativa.dat" using 2:xticlabels(1) title "Resultados comparativa"

set term png
set output "./Imagenes/Resultados/parkinsons_comparativa.png"
replot
set term x11

set title "Resultados comparativa spectf-heart"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Resultados/spectf-heart_comparativa.dat" using 2:xticlabels(1) title "Resultados comparativa"

set term png
set output "./Imagenes/Resultados/spectf-heart_comparativa.png"
replot
set term x11
