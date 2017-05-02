#!/bin/bash

awk 'NR%9==1 {print $1, $2, $3, $4}' solar.dat >> mercury.dat
awk 'NR%9==2 {print $1, $2, $3, $4}' solar.dat >> venus.dat
awk 'NR%9==3 {print $1, $2, $3, $4}' solar.dat >> earth.dat
awk 'NR%9==4 {print $1, $2, $3, $4}' solar.dat >> mars.dat
awk 'NR%9==5 {print $1, $2, $3, $4}' solar.dat >> jupiter.dat
awk 'NR%9==6 {print $1, $2, $3, $4}' solar.dat >> saturn.dat
awk 'NR%9==7 {print $1, $2, $3, $4}' solar.dat >> uranus.dat
awk 'NR%9==8 {print $1, $2, $3, $4}' solar.dat >> neptune.dat
awk 'NR%9==0 {print $1, $2, $3, $4}' solar.dat >> pluto.dat
