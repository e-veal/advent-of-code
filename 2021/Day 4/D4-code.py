#!/usr/bin/python3
# Answer from MaximVT (https://www.reddit.com/r/adventofcode/comments/r8i1lq/comment/hpiqrih/)

#### Part 1
print("****** PART 1 ******")
# print("****** PART 1 ******", file=open('output.log','w'))

# open file
with open("D4-input.txt") as file:
    numbers, *boards = file.read().split('\n\n')
    numbers = [int(num) for num in numbers.split(',')]
    allBoards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]

# for board in allBoards:
#     for row in board:
#         print(row)
#     print('\n')

def mark_board(number, board):
     for row in board:
        for col in range (0, len(row)):
            if row[col] == number:
                row[col] = 'x'

mark_board(18, allBoards[0])

# for row in allBoards[0]:
#     print(row)

def sum_board(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum


def check_for_winner(board):
    winner = False

    # Check each row for a winner
    for row in board:
        winner = all(item in ['x'] for item in row)     #checks if all the item in the row is an 'x'

        if winner:
            return winner

    # Check each column for winner
    for col in range(0,5):
        winner = all(item in ['x'] for item in [row[col] for row in board])  #checks if all the item in the column is an 'x'

        if winner:
            return winner

    return winner

# Part 1
def part1():
    boards = allBoards

    for number in numbers:
        # print(number, file=open('output.log','a'))
        for board in boards:
            mark_board(number, board)
            # for row in board:
            #     print(row, file=open('output.log','a'))
            # print('\n', file=open('output.log','a'))

            if check_for_winner(board):
                # print("Final number: ", number, file=open('output.log','a'))
                return sum_board(board) * number

def part2():
    boards = allBoards
    copyNumbers = numbers
            
    winner = False

    while not winner:
        number = copyNumbers[0]
        copyNumbers = copyNumbers[1:]
        
        for board in boards:
            mark_board(number, board)

        index = 0

        while index < len(boards):
            if check_for_winner(boards[index]):
                if len(boards) > 1:
                    boards.pop(index)

                else:
                    winner = True
                    return sum_board(boards[index]) * number

            else:
                index+=1
            
print("Winner's Score:", part2())