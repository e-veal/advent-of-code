#!/usr/bin/env bash

#### Part 1
echo "****** PART 1 ******"

#set variables
INPUT_FILE="D1-input.txt"
SUM=0
EACH_ELF_TOTAL=[@]
ELF_NUMBER=1

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

#### Part 2
echo
echo "****** PART 2 ******"
echo "${EACH_ELF_TOTAL[*]}" | sort -nr | head -n3 | paste -sd+ | bc