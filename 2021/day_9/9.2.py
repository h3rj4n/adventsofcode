# Let's bruteforce the solution. Build a multidimensional array.
with open('9_data.txt') as f:
    # Loop trough the lines.
    data = []
    for line in f:
        data.append(list(map(lambda x: int(x), list(line.strip()))))

maxX = len(data[0])
maxY = len(data)

lowpoints = []

for index, row in enumerate(data):
    for col, number in enumerate(row):
        # By default, asome this pos is low. Prove otherwise.
        low = True

        # Check any pos around is lower.
        for ax, ay in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = col - ax
            ny = index - ay

            # Check out of bound.
            if not (0 <= nx < maxX and 0 <= ny < maxY):
                continue

            # Add the new XY cords to the positions array.
            if data[ny][nx] <= data[index][col]:
                low = False
        if low:
            lowpoints.append((col, index))

# Keep track of the sizes.
sizes = []

# Loop trough all the low points and see how big they are.
for px, py in lowpoints:
    amount = 0
    start = [(px, py)]
    visited = set()

    while len(start) > 0:
        x, y = start.pop(0)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        amount += 1

        for ax, ay in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x - ax
            ny = y - ay

            # Check out of bound.
            if not (0 <= nx < maxX and 0 <= ny < maxY):
                continue

            if data[y][x] <= data[ny][nx] and data[ny][nx] < 9:
                start.append((nx, ny))
    sizes.append(amount)

sizes.sort()

print('answer: ', sizes[-1] * sizes[-2] * sizes[-3])
