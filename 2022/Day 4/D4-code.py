#!/usr/bin/python3
# import re

#### Part 1
print("****** PART 1 ******")

# open file
with open("D4-input.txt") as file:
    lines = file.read().splitlines()

# variables
numbers=[]
total_duplicates=0
total_overlap=0

# add numbers to an array
for line in lines:
    for nocomma in line.split(","):
        for char in nocomma.split("-"):
            if char.isdigit():
                numbers.append(int(char))

numbers_length=len(numbers)
# print(numbers)

for n in range(0,numbers_length-2,4):
    if numbers[n] >= numbers[n+2] and numbers[n+1]<=numbers[n+3]:
        # print("In range: ", numbers[n+2]," | ", numbers[n] ,"-", numbers[n+1], "| ", numbers[n+3])
        total_duplicates+=1
    elif numbers[n+2] >= numbers[n] and numbers[n+3]<=numbers[n+1]:
        # print("In range: ", numbers[n+2]," | ", numbers[n] ,"-", numbers[n+1], "| ", numbers[n+3])
        total_duplicates+=1
    else:
        # print("Not in range: ", numbers[n+2]," | ", numbers[n], "-", numbers[n+1], "| ", numbers[n+3])
        pass
print("Total Duplicates: ", total_duplicates)


#### Part 2
print("****** PART 2 ******")

for n in range(0,numbers_length-2,4):
    if (numbers[n] >= numbers[n+2] and numbers[n] <= numbers[n+3]) or (numbers[n+1]<=numbers[n+3] and numbers[n+1]>=numbers[n+2]):
        # print("1st Overlap ", numbers[n+2]," | ", numbers[n] ,"-", numbers[n+1], "| ", numbers[n+3])
        total_overlap+=1
    elif numbers[n+2] >= numbers[n] and numbers[n+3]<=numbers[n+1]:
        # print("2nd Overlap: ", numbers[n+2]," | ", numbers[n] ,"-", numbers[n+1], "| ", numbers[n+3])
        total_overlap+=1
    else:
        # print("No overlap: ", numbers[n+2]," | ", numbers[n], "-", numbers[n+1], "| ", numbers[n+3])
        pass
print("Total Overlaps: ", total_overlap)