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
    # Only execute the first instruction.
    break

output = []
for x in data:
    output.append(','.join(list(map(lambda t: str(t), x))))

print('answer: ', len(set(output)))
