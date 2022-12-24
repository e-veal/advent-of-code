#!/usr/bin/python3

# Second Guess: VWLCWGSD (Wrong)
# Correct Answer: VWLCWGSDQ (Use redditer.py to check)

#### Part 1

print("****** PART 1 ******")
print("****** PART 1 ******", file=open('output.log','w'))

####### MOVES ######## 
with open("D5-input.txt") as file:
# with open("D5-test.txt") as file:
    lines = file.read().splitlines()

moves=[]

for line in lines:
    for part in line.split():
        if part.isdigit():
            moves.append(int(part))

mLength=len(moves)
# print(moves, file=open('output.log','a'))
#######################

# variables
# crate=[['Z','N'],['M','C','D'],['P']] #manually created
crate=['Q','F','M','R','L','W','C','V'],['D','Q','L'],['P','S','R','G','W','C','N','B'],['L','C','D','H','B','Q','G'],['V','G','L','F','Z','S'],['D','G','N','P'],['D','Z','P','V','F','C','W'],['C','P','D','M','S'],['Z','N','W','T','V','M','P','C']
# print(crate, file=open('output.log','a'))

for n in range(0,mLength,3):
    x=0
    print("\n\nLINE", file=open('output.log','a'))
    while x < moves[n]:                     #move
        mFrom=moves[n+1]-1
        mTo=moves[n+2]-1
        rLength=len(crate[mFrom])
        # print(rLength)
        mCrate=crate[mFrom][rLength-1] 

        print("moving: ", mCrate, file=open('output.log','a'))
        print("mFrom: ",mFrom, file=open('output.log','a'))    
        print("mTo: ",mTo, file=open('output.log','a'))  

        # print(crate)
        crate[mFrom].pop()
        # print(crate, file=open('output.log','a'))  
        crate[mTo].append(mCrate)
        # for item in enumerate(crate):
        #     print("{}".format(item), file=open('output.log','a'))
        x+=1
        print("TOTAL TIMES SHOULD MOVE:", moves[n], file=open('output.log','a'))
        print("LOOP #:", x, file=open('output.log','a'))

for i in range(9):
    rLength=len(crate[i])
    print(crate[i][rLength-1])