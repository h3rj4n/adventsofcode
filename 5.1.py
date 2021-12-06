# Import the data
f = open("5_data.txt")

data = []

# Process the data to a valid input array
for index, line in  enumerate(f):
    # Split on the arrow part, the first part is from, second to.
    processed = line.rstrip('\n').split(' -> ')
    data.append(processed)

    # For debug purposes, limit the for loop.
    if index > 10:
        break

grid = {}

for item in data:
    # Process the from.
    # @todo Changes map() the order?
    xyFrom = list(map(lambda x: int(x), item[0].split(',')))
    xyTo = list(map(lambda x: int(x), item[1].split(',')))

    # Only process the items where x/y from and to are equal.
    if (xyFrom[0] == xyTo[0] or xyFrom[1] == xyTo[1]):
        # Do something with the data.
        if xyFrom[0] == xyTo[0]:
            startY = xyFrom[1] if xyFrom[1] < xyTo[1] else xyTo[1]
            endY = xyFrom[1] if xyFrom[1] > xyTo[1] else xyTo[1]

            # The y changes, while loop until values matches.
            while startY < endY:
                i = ','.join([str(xyFrom[0]), str(startY)])
                if i not in grid:
                    grid[i] = 0
                grid[i] += 1
                startY += 1

        if xyFrom[1] == xyTo[1]:
            startX = xyFrom[0] if xyFrom[0] < xyTo[0] else xyTo[0]
            endX = xyFrom[0] if xyFrom[0] > xyTo[0] else xyTo[0]

            # The y changes, while loop until values matches.
            while startX < endX:
                i = ','.join([str(startX), str(xyFrom[1])])
                if i not in grid:
                    grid[i] = 0
                grid[i] += 1
                startX += 1
