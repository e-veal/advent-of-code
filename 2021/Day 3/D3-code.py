#!/usr/bin/python3

#### Part 1

print("****** PART 1 ******")

# open file
with open("D3-input.txt") as file:
    lines = file.read().splitlines()

## For Test Example
# gamma=[0,0,0,0,0]
# epsilon=[0,0,0,0,0]
# counter_zeros=[0,0,0,0,0]
# counter_ones=[0,0,0,0,0]

gamma=[0,0,0,0,0,0,0,0,0,0,0,0]
epsilon=[0,0,0,0,0,0,0,0,0,0,0,0]
counter_zeros=[0,0,0,0,0,0,0,0,0,0,0,0]
counter_ones=[0,0,0,0,0,0,0,0,0,0,0,0]
power=0
count=0

for line in lines:
    count+=1
    for n, bit in enumerate(line):
        if bit == '0':
            counter_zeros[n]+=1
        else:
            counter_ones[n]+=1
# print(counter_zeros)
# print(counter_ones)

for n in range(len(counter_zeros)):
    if counter_zeros[n] > counter_ones[n]:
        # print('1:where n is:', n)
        gamma[n] = 1
        epsilon[n] = 0

    elif counter_zeros[n] < counter_ones[n]:
        # print('2:where n is:', n)
        gamma[n] = 0
        epsilon[n] = 1

def convertAnswer(arry):
    bi_num=''
    for elements in arry:
        bi_num=bi_num + str(elements)
    return int(bi_num,2)

print("Gamma: ", convertAnswer(gamma))
print("Epsilon: ", convertAnswer(epsilon))
power=convertAnswer(gamma)*convertAnswer(epsilon)

print("Power Consumption: ", power)


### Part 2

print("\n****** PART 2 ******")

oxygen = list(lines)      # Part 2
co2 = list(lines)         # Part 2
count_zeros=[0,0,0,0,0]
count_ones=[0,0,0,0,0]
items_to_pop=[]
life=0

def find_sum_zeros(enter_array):
    # print(count_zeros)
    # count_zeros=[0,0,0,0,0]       # Test Example
    count_zeros=[0,0,0,0,0,0,0,0,0,0,0,0]
    for line in enter_array:
        for n, bit in enumerate(line):
            if bit == '0':
                count_zeros[n]+=1
    # print("inside sum-zero", count_zeros)
    return count_zeros

def find_sum_ones(enter_array):
    # count_ones=[0,0,0,0,0]          # Test Example
    count_ones=[0,0,0,0,0,0,0,0,0,0,0,0]
    for line in enter_array:
        for n, bit in enumerate(line):
            if bit == '1':
                count_ones[n]+=1
    # print("inside sum-ones", count_ones)
    return count_ones

def find_co2_rating(enter_array):

    for n in range(len(enter_array)):
        count_zeros = find_sum_zeros(enter_array)
        count_ones = find_sum_ones(enter_array)
        # print("count", "\n", count_ones, "\n", count_zeros)
        count=len(enter_array)
        # print("COUNT", count)
        # print("enter_array", enter_array)
        # print("n", n)

        if count == 1:
            pass
        elif count > 1 and count_zeros[n] > count_ones[n]:
            # print(n, ': remove the 1')
            gamma[n] = 1
            epsilon[n] = 0
            for item in enter_array:  # Part 2
                if item[n] == '1':
                    items_to_pop.append(item)
            # print("items to pop:", items_to_pop)
            for element in items_to_pop:
                # print(element)
                # print("before:", enter_array)
                enter_array.remove(element)
                # print("after:", enter_array)
            # print(enter_array)     
        elif count > 1 and ((count_zeros[n] < count_ones[n] or count_zeros[n] == count_ones[n]) or (count_zeros[n] == count_ones[n])):
            # print(n, ': remove the 0')
            gamma[n] = 0
            epsilon[n] = 1
            for item in enter_array:  # Part 2
                if item[n] == '0':
                    items_to_pop.append(item)
            # print("items to pop:", items_to_pop)
            for element in items_to_pop:
                # print(element)
                # print("before:", enter_array)
                enter_array.remove(element)
                # print("after:", enter_array)
            # print(enter_array)     

        items_to_pop.clear()
    return convertAnswer(enter_array)

def find_oxygen_rating(enter_array):

    for n in range(len(enter_array)):
        count_zeros = find_sum_zeros(enter_array)
        count_ones = find_sum_ones(enter_array)
        # print("count", "\n", count_ones, "\n", count_zeros)
        count=len(enter_array)
        # print("COUNT", count)
        # print("enter_array", enter_array)
        # print("n", n)

        if count == 1:
            pass
        elif (count > 1 and count_zeros[n] < count_ones[n]) or (count_zeros[n] == count_ones[n]):
            # print(n, ': remove the 1')
            gamma[n] = 1
            epsilon[n] = 0
            for item in enter_array:  # Part 2
                if item[n] == '1':
                    items_to_pop.append(item)
            # print("items to pop:", items_to_pop)
            for element in items_to_pop:
                # print(element)
                # print("before:", enter_array)
                enter_array.remove(element)
            #     print("after:", enter_array)
            # print(enter_array)     
        elif count > 1 and (count_zeros[n] > count_ones[n] or count_zeros[n] == count_ones[n]):
            # print(n, ': remove the 0')
            gamma[n] = 0
            epsilon[n] = 1
            for item in enter_array:  # Part 2
                if item[n] == '0':
                    items_to_pop.append(item)
            # print("items to pop:", items_to_pop)
            for element in items_to_pop:
                # print(element)
                # print("before:", enter_array)
                enter_array.remove(element)
                # print("after:", enter_array)
            # print(enter_array)     

        items_to_pop.clear()
    return convertAnswer(enter_array)     

print("CO2 Rating:", find_co2_rating(co2))
print("Oxygen Rating:", find_oxygen_rating(oxygen))
life=find_co2_rating(co2)*find_oxygen_rating(oxygen)
print("Life Support Rating:", life)