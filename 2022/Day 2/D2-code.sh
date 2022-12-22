#!/bin/bash

#### Part 1
echo "****** PART 1 ******"

# variables
INPUT_FILE="D2-input.txt"
TOTAL=0

while IFS=" " read -r opp_choice my_choice; do

    case $opp_choice in
        A)
            case $my_choice in
                X)
                    TOTAL=$(( TOTAL + 3 + 1 ))
                    ;;
                Y)
                    TOTAL=$(( TOTAL + 6 + 2 ))
                    ;;
                Z)
                    TOTAL=$(( TOTAL + 0  + 3 ))
                    ;;
            esac
            ;;
        B)
            case $my_choice in
                X)
                    TOTAL=$(( TOTAL + 0 + 1 ))
                    ;;
                Y)
                    TOTAL=$(( TOTAL + 3 + 2 ))
                    ;;
                Z)
                    TOTAL=$(( TOTAL + 6  + 3 ))
                    ;;
            esac
            ;;
        C)
            case $my_choice in
                X)
                    TOTAL=$(( TOTAL + 6 + 1 ))
                    ;;
                Y)
                    TOTAL=$(( TOTAL + 0 + 2 ))
                    ;;
                Z)
                    TOTAL=$(( TOTAL + 3  + 3 ))
                    ;;
            esac
            ;;
        *)
        ;;
    esac

done < $INPUT_FILE

echo $TOTAL

#### Part 2
NEW_TOTAL=0
echo "****** PART 2 ******"
while IFS=" " read -r opp_choice outcome; do
    case $outcome in
        X)
            NEW_TOTAL=$(( NEW_TOTAL + 0 ))
            ;;
        Y)
            NEW_TOTAL=$(( NEW_TOTAL + 3 ))
            ;;
        Z)
            NEW_TOTAL=$(( NEW_TOTAL + 6 ))
            ;;
    esac

    case $opp_choice in
        A)
            case $outcome in
                X)
                    NEW_TOTAL=$(( NEW_TOTAL + 3 ))
                    ;;
                Y)
                    NEW_TOTAL=$(( NEW_TOTAL + 1 ))
                    ;;
                Z)
                    NEW_TOTAL=$(( NEW_TOTAL + 2 ))
                    ;;
            esac
            ;;
        B)
            case $outcome in
                X)
                    NEW_TOTAL=$(( NEW_TOTAL + 1 ))
                    ;;
                Y)
                    NEW_TOTAL=$(( NEW_TOTAL + 2 ))
                    ;;
                Z)
                    NEW_TOTAL=$(( NEW_TOTAL + 3 ))
                    ;;
            esac
            ;;
        C)
            case $outcome in
                X)
                    NEW_TOTAL=$(( NEW_TOTAL + 2 ))
                    ;;
                Y)
                    NEW_TOTAL=$(( NEW_TOTAL + 3 ))
                    ;;
                Z)
                    NEW_TOTAL=$(( NEW_TOTAL + 1 ))
                    ;;
            esac
            ;;
    esac 

done < $INPUT_FILE

echo $NEW_TOTAL
