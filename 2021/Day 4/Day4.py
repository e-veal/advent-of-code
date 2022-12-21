with open("test") as f:
    lines = f.readlines()
    
randomNumber=lines[0].split(",")
x=0

# for x in randomNumber:
#     print(x)
i=3
for i in range(len(lines)):
    print(lines[i])
    i+=1
