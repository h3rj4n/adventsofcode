with open('15_data.txt') as f:
    # Loop trough the lines and create multidimensional array.
    data = []
    for line in f:
        data.append(list(map(lambda x: int(x), list(line.strip()))))

# Our start position.
paths = [(0, 0, 0)]
# Keep track of all visited cords, when visited it's part of an existing
# and probably lower risk path.
visited = set()

maxYO = len(data)
maxXO = len(data[0])

# Let's calculate the value on the fly.
maxY = maxYO * 5
maxX = maxXO * 5


def getValue(x, y):
    value = data[y % maxYO][x % maxXO]
    value += (x // maxXO) + (y // maxYO)
    return (value - 1) % 9 + 1


output = []

while len(paths) > 0:
    x, y, value = paths.pop(0)

    if (x, y) in visited:
        # print('remove')
        continue
    visited.add((x, y))

    if x == maxX - 1 and y == maxY - 1:
        break

    # Let's walk to the next position.
    for moveX, moveY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newX = x + moveX
        newY = y + moveY

        if newX == maxX - 1 and newY == maxY - 1:
            print('added to output: ', value + getValue(newX, newY))
            output.append([(newX, newY), value + getValue(newX, newY)])
            break

        # Do not walk out of bound.
        if not (0 <= newX < maxX and 0 <= newY < maxY):
            continue

        paths.append(
            (newX, newY, value + getValue(newX, newY)))

    paths.sort(key=lambda x: x[2])
    if len(output) > 0:
        break


print(output)

# 2835, to high
