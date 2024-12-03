# Import the data
f = open("5_data.txt")

data = []

# Process the data to a valid input array
for index, line in enumerate(f):
    # Split on the arrow part, the first part is from, second to.
    processed = line.rstrip('\n').split(' -> ')
    data.append(processed)

    # For debug purposes, limit the for loop.
    # if index > 1:
    #     break

grid = {}

for item in data:
    # Process the from.
    xyFrom = list(map(lambda x: int(x), item[0].split(',')))
    xyTo = list(map(lambda x: int(x), item[1].split(',')))

    # The X to start
    startX = xyFrom[0]
    endX = xyTo[0]
    originalX = [startX, endX]

    # The Y to start
    startY = xyFrom[1]
    endY = xyTo[1]
    originalY = [startY, endY]

    executeOnce = False

    while startX != endX or startY != endY:
        if executeOnce is False:
            # Add the endpoint to the grid.
            e = ','.join([str(endX), str(endY)])
            if originalX[0] != originalX[1] and originalY[0] != originalY[1]:
                print(e)
            if e not in grid:
                grid[e] = 0
            grid[e] += 1
            executeOnce = True

        # Add current point to the dict.
        i = ','.join([str(startX), str(startY)])
        if originalX[0] != originalX[1] and originalY[0] != originalY[1]:
            print(i)
        if i not in grid:
            grid[i] = 0
        grid[i] += 1

        if originalX[0] != originalX[1]:
            startX = startX + 1 if startX < endX else startX - 1
        if originalY[0] != originalY[1]:
            startY = startY + 1 if startY < endY else startY - 1

# Filter out where the count is 1
test = dict(filter(lambda x: x[1] > 1, grid.items()))

print('answer: ', len(test))

# 21577
