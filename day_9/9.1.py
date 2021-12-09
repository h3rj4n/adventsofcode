# Let's bruteforce the solution. Build a multidimensional array.
with open('9_data.txt') as f:
    # Loop trough the lines.
    data = []
    for line in f:
        data.append(list(map(lambda x: int(x), list(line.strip()))))

ans = 0

for index, row in enumerate(data):
    for col, number in enumerate(row):
        # Search for the item up, down, left and right. If lower,
        # do nothing, else count it.
        id = 0

        # Check up
        if index - 1 >= 0 and data[index - 1][col] > number:
            # print('number: ', number, ',    up: ', data[index - 1][col])
            id += 1

        # Check left
        if col - 1 >= 0 and row[col - 1] > number:
            # print('number: ', number, ',  left: ', data[index - 1][col])
            id += 1

        # Check right
        if col + 1 < len(row) and row[col + 1] > number:
            # print('number: ', number, ', right: ',  row[col + 1])
            id += 1

        # Check down
        if index + 1 < len(data) and data[index + 1][col] > number:
            # print('number: ', number, ',  down: ', data[index + 1][col])
            id += 1

        match = 4
        if index - 1 < 0:
            match -= 1
        if index + 1 >= len(data):
            match -= 1
        if col - 1 < 0:
            match -= 1
        if col + 1 >= len(row):
            match -= 1

        # print('number: ', number, ', id: ', id, ', match: ', match)

        if id == match:
            ans += 1 + number

    # break
print('anser: ', ans)

# 494 (too low)
