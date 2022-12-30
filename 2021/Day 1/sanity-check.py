#!/usr/bin/python3

#Checked with ret0h (https://www.reddit.com/r/adventofcode/comments/r66vow/comment/hopzd48/)

def get_increases(measurements):
    prev_depth = measurements[0]
    increases = 0

    for depth in measurements[1:]:
        if depth > prev_depth:
            increases += 1
        prev_depth = depth

    return increases


with open("D1-input.txt", "r") as f:
    lines = f.readlines()
    measurements = [int(depth.strip()) for depth in lines]

    ### A
    increases = get_increases(measurements)
    print(increases)