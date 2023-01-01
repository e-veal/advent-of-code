#!/usr/bin/python3

#### Part 1

print("****** PART 1 ******")

# open file
with open("D2-input.txt") as file:
    commands = file.readlines()

horzion=0
depth=0
aim=0

for command in commands:
    if command[0:7] == "forward":
        horzion=horzion+int(command[8])
    elif command[0:4] == "down":
        depth=depth+int(command[5])
    elif command[0:2] == "up":
        depth=depth-int(command[3])

print("Horizontal Position:",horzion)
print("Depth:", depth)
print("Part 1 Answer:",horzion*depth)

#### Part 2

print("****** PART 2 ******")
p2_horzion=0
p2_depth=0
aim=0
for command in commands:
    if command[0:7] == "forward":
        p2_horzion=p2_horzion+int(command[8])
        print("Horizon:", p2_horzion)
        p2_depth=p2_depth+aim*int(command[8])
        print("Depth:", p2_depth)
    elif command[0:4] == "down":
        aim=aim+int(command[5])
        print("Aim:", aim)
    elif command[0:2] == "up":
        aim=aim-int(command[3])
        print("Aim: ", aim)

print("Horizontal Position:", p2_horzion)
print("Depth:", p2_depth)
print("Aim:", aim)
print("Part 2 Answer:",p2_horzion*p2_depth)