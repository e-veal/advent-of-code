#!/usr/bin/env bash

#set variables
INPUT_FILE="day-one-input.txt"
SUM=0
EACH_ELF_TOTAL=[@]
ELF_NUMBER=1

mapfile -t TOTAL_CALORIES < $INPUT_FILE

while read -r CALORIE; do
        if [ ! -z $CALORIE ]; then
            SUM=$(( $SUM + $CALORIE ))
        else
            EACH_ELF_TOTAL[ELF_NUMBER]=$SUM
            (( ELF_NUMBER++ ))
            SUM=0
        fi
done < $INPUT_FILE

# find max
IFS=$'\n'
echo "${EACH_ELF_TOTAL[*]}" | sort -nr | head -n1