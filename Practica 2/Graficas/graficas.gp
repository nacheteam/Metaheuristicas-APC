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
