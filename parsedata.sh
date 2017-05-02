#!/bin/bash

step=43200
FILE='solar_'$step'.dat'

awk 'NR%9==1 {print $1"," $2"," $3"," $4"," $5}' $FILE >> mercury_$step.csv
awk 'NR%9==2 {print $1"," $2"," $3"," $4"," $5}' $FILE >> venus_$step.csv
awk 'NR%9==3 {print $1"," $2"," $3"," $4"," $5}' $FILE >> earth_$step.csv
awk 'NR%9==4 {print $1"," $2"," $3"," $4"," $5}' $FILE >> mars_$step.csv
awk 'NR%9==5 {print $1"," $2"," $3"," $4"," $5}' $FILE >> jupiter_$step.csv
awk 'NR%9==6 {print $1"," $2"," $3"," $4"," $5}' $FILE >> saturn_$step.csv
awk 'NR%9==7 {print $1"," $2"," $3"," $4"," $5}' $FILE >> uranus_$step.csv
awk 'NR%9==8 {print $1"," $2"," $3"," $4"," $5}' $FILE >> neptune_$step.csv
awk 'NR%9==0 {print $1"," $2"," $3"," $4"," $5}' $FILE >> pluto_$step.csv