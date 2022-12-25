#!/usr/bin/python3

#Code from aasthas97 (https://www.reddit.com/r/adventofcode/comments/zdw0u6/comment/izif05u/?utm_source=share&utm_medium=web2x&context=3)

#### Part 1
print("****** PART 1 ******")
# print("****** PART 1 ******", file=open('output.log','w'))

#### Open File
with open("D6-input.txt") as file:
# with open("D6-test.txt") as file:
    lines = file.read()#.splitlines()

i = 0

def findMarker(signal, marker_length):
   for i in range(len(signal)-(marker_length-1)):   # for each item (all items in file)
    marker =  signal[i:i+marker_length]             # marker is the array of 1-4
    if len(set(marker)) == marker_length:           # if set, then the length = marker length
        return i+marker_length                      # return position

print("Marker:", findMarker(lines, 14)) 