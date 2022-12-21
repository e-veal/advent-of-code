#!/usr/bin/env bash

#set variables
INPUT_FILE="day-one-test.txt"
SUM=0

#read lines
mapfile -t ELVES_CALORIES < $INPUT_FILE

# for CALORIE in $ELVES_CALORIES; do
#     $SUM+=$CALORIE
# done

echo ${ELVES_CALORIES[@]}