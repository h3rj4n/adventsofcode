with open('15_data.txt') as f:
    # Loop trough the lines and create multidimensional array.
    data = []
    for line in f:
        data.append(list(map(lambda x: int(x), list(line.strip()))))

# Our start position.
paths = [
    [(0, 0), 0]
]
# Keep track of all visited cords, when visited it's part of an existing
# and probably lower risk path.
visited = set()

maxY = len(data)
maxX = len(data[0])

ans = None

# for _ in range(18):
while len(paths) > 0:
    newPaths = []
    for pos, value in paths:
        # Let's walk to the next position.
        for moveX, moveY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            newX = pos[0] + moveX
            newY = pos[1] + moveY

            if (newX, newY) in visited:
                continue
            visited.add((newX, newY))

            # Do not walk out of bound.
            if not (0 <= newX < maxX and 0 <= newY < maxY):
                continue

            newPaths.append(
                [(newX, newY), value + data[newY][newX]])

    # Sort the paths and keep only the 1000 most promising
    newPaths.sort(key=lambda x: x[1])
    newPaths = newPaths[:1000]

    # Overwrite the paths.
    paths = newPaths
    ans = ans if len(paths) == 0 else paths[0]

print('answer: ', ans[1])

# 571, to high
