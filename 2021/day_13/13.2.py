from collections import defaultdict

with open('13_data.txt') as f:
    data = []
    instructions = []
    emptyLine = False
    for line in f:
        emptyLine = emptyLine if emptyLine or len(line.strip()) > 0 else True
        # Process all the x,y cords until an empty line is found.
        if emptyLine is False:
            data.append(list(map(lambda x: int(x), line.strip().split(','))))
        elif len(line.strip()) > 0:
            # Process the instructions.
            instructions.append(line.strip()[11:].split('='))

# Loop trough the instructions and execute them.
for ins in instructions:
    pos = 0 if ins[0] == 'x' else 1
    # Loop trough the x,y cords and fold to the new position.
    for index, value in enumerate(data):
        if value[pos] > int(ins[1]):
            # Calculate new pos.
            data[index][pos] = int(ins[1]) - (value[pos] - int(ins[1]))

output = defaultdict(list)
for x, y in data:
    output[y].append(x)

r = max(output[0]) + 10
keys = list(output.keys())
keys.sort()
for i in keys:
    p = '' + str(max(output[i])) + ' '
    for _ in range(r):
        p += '#' if _ in output[i] else ' '
    print(p)


# print(output)
