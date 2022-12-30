#!/usr/bin/python3

#### Part 1

print("****** PART 1 ******")

# open file
with open("D1-input.txt") as file:
    lines = file.read().splitlines()

count=0
slide_count=0
length=len(lines)

for n, line in enumerate(lines):
    if n<length-1:
        if lines[n]<lines[n+1]:
            count+=1
        else:
            pass

print("Measurements:", count)

#### Part 2

print("\n****** PART 2 ******")

for n, line in enumerate(lines):
    if n<length-3:
        first_window=int(lines[n])+int(lines[n+1])+int(lines[n+2])
        second_window=int(lines[n+1])+int(lines[n+2])+int(lines[n+3])
        if (first_window)<(second_window):
            slide_count+=1
        else:
            pass

print("Three-measurement window:", slide_count)