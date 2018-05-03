#!/bin/usr/gnuplot

################################################################################
#                         GRAFICAS CONVERGENCIA                                #
################################################################################

set title "Convergencia AGE CA"
set auto x
set yrange [0:100]
plot "./Convergencia/convergencia_estacionario_aritmetico.dat" title "Media poblaciones" with lines

set term png
set output "./Imagenes/Convergencia/convergencia_estacionario_aritmetico.png"
replot
set term x11

set title "Convergencia AGE BLX"
set auto x
set yrange [0:100]
plot "./Convergencia/convergencia_estacionario_blx.dat" title "Media poblaciones" with lines

set term png
set output "./Imagenes/Convergencia/convergencia_estacionario_blx.png"
replot
set term x11

set title "Convergencia AGG CA"
set auto x
set yrange [0:100]
plot "./Convergencia/convergencia_generacional_aritmetico.dat" title "Media poblaciones" with lines

set term png
set output "./Imagenes/Convergencia/convergencia_generacional_aritmetico.png"
replot
set term x11

set title "Convergencia AGG BLX"
set auto x
set yrange [0:100]
plot "./Convergencia/convergencia_generacional_blx.dat" title "Media poblaciones" with lines

set term png
set output "./Imagenes/Convergencia/convergencia_generacional_blx.png"
replot
set term x11


################################################################################
#                                GRAFICAS MUTACION                             #
################################################################################

set title "Mutacion=0.001 vs Mutacion=0.2"
set auto x
set yrange [0:100]
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
plot "./Mutacion/mutacion.dat" using 2:xticlabels(1) title "Mutacion=0.2", "./Mutacion/sin_mutacion.dat" using 2:xticlabels(1) title "Mutacion=0.001"

set term png
set output "./Imagenes/Mutacion/mutacion.png"
replot
set term x11

################################################################################
#                                 GRAFICAS TIEMPO                              #
################################################################################

set title "Tiempos ozone"
set auto x
set yrange [0:1500]
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
set yrange [0:600]
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
set yrange [0:1000]
set style data histogram
set style fill solid border -1
set boxwidth 0.2
set xtic rotate by -45 scale 0
plot "./Tiempos/spectf-heart.dat" using 2:xticlabels(1) title "Tiempos"

set term png
set output "./Imagenes/Tiempos/tiempos_spectf-heart.png"
replot
set term x11
