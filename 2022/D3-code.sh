#!/bin/bash

#### Part 1
# echo "****** PART 1 ******"

# # variables
# INPUT_FILE="D3-test.txt"

# while read -r rucksack; do
#     first_part=${rucksack:0:${#rucksack}/2}
#     second_part=${rucksack:${#rucksack}/2}
#     i=0

#     while [ $i -ne ${#first_part} ]; do
#         item=${first_part:$i:1}
#         if [[ $result != *$item* && $second_part == *$item* ]]; then
#             case $item in
#                 ([[:lower:]]) 
#                     value=$((`LC_CTYPE=C printf '%d' "'$item"` - 96))
#                     ;;
#                 ([[:upper:]])
#                     value=$((`LC_CTYPE=C printf '%d' "'$item"` - 38))
#                     ;;
#             esac
#             # echo $value " ($item)"
#             PRIORITY_TOTAL=$(( PRIORITY_TOTAL + $value ))
#             break
#         fi
#         ((i++))
#     done

# done < $INPUT_FILE

# echo $PRIORITY_TOTAL

#### Part 2

echo "****** PART 2 ******"

# variables
INPUT_FILE="D3-test.txt"

