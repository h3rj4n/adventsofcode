#         [F] [Q]         [Q]        
# [B]     [Q] [V] [D]     [S]        
# [S] [P] [T] [R] [M]     [D]        
# [J] [V] [W] [M] [F]     [J]     [J]
# [Z] [G] [S] [W] [N] [D] [R]     [T]
# [V] [M] [B] [G] [S] [C] [T] [V] [S]
# [D] [S] [L] [J] [L] [G] [G] [F] [R]
# [G] [Z] [C] [H] [C] [R] [H] [P] [D]
#  1   2   3   4   5   6   7   8   9 

import re

list = [
    ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
    ['Z', 'S', 'M', 'G', 'V', 'P'],
    ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
    ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
    ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
    ['R', 'G', 'C', 'D'],
    ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
    ['P', 'F', 'V'],
    ['D', 'R', 'S', 'T', 'J'],
]

with open("5_data.txt") as f:
    for line in f:
        amount, fromStack, toStack = [int(x) for x in re.match(r'move (\d+) from (\d+) to (\d+)', line.strip()).groups()]

        # The part to append on the toStack
        toAppend = list[fromStack - 1][amount * -1:]
        list[toStack - 1] = list[toStack - 1] + toAppend

        # The new list.
        list[fromStack - 1] = list[fromStack - 1][:amount * -1]

answer = []

for item in list:
    answer += item[-1:]

print(''.join(answer))