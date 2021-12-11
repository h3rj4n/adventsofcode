with open('11_data.txt') as f:
    # Loop trough the lines and create multidimensional array.
    data = []
    for line in f:
        data.append(list(map(lambda x: int(x), list(line.strip()))))

#print(print('\n'.join(''.join(str(x) for x in row) for row in data)))

positions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# The amount of steps to take
steps = 0

maxAmountFlashes = len(data) * len(data[0])
flashes = 0

notSynced = True

while notSynced:
    steps += 1
    flashed = []
    added = []
    processFlashed = True
    while processFlashed:
        processFlashed = False
        # Loop trough the rows
        for ri, row in enumerate(data):
            # Loop trough the numbers
            for ni, number in enumerate(row):
                # Increase the value.
                if (ri, ni) not in added:
                    data[ri][ni] += 1
                    added.append((ri, ni))

                if data[ri][ni] > 9:
                    data[ri][ni] = 0
                    flashes += 1
                    flashed.append((ri, ni))
                    # Force to start all over again
                    processFlashed = True

                    # Increase the value of all the fields around it.
                    for x, y in positions:
                        try:
                            if (ri - x, ni - y) not in flashed and ri - x >= 0 and ni - y >= 0:
                                data[ri - x][ni - y] += 1
                        except IndexError:
                            pass
    if len(flashed) == maxAmountFlashes:
        notSynced = False

    # print('----')
    # print(print('\n'.join(''.join(str(x) for x in row) for row in data)))
print(steps)
