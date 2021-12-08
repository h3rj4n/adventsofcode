# Get the data
f = open("2_data.txt")

horizontal = 0
depth = 0
aim = 0

for command in f:
    changes = command.split(" ")
    
    match changes[0]:
        case 'forward':
            horizontal += int(changes[1])
            depth += aim * int(changes[1])
        case 'down':
            aim += int(changes[1])
        case 'up':
            aim -= int(changes[1])
            
print('horizontal: ', horizontal)
print('depth: ', depth)
print('awnser: ', depth * horizontal)
# 1947824
