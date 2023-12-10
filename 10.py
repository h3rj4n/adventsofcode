grid = []
startpos = ()
with open("10.1.txt") as f:
    for index, line in enumerate(f):
        grid.append(line)
        if line.find("S") >= 0:
            startpos = (index, line.find("S"))

pos_change = {
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

next_step = startpos
previous = None
steps = 0

while steps == 0 or next_step != startpos:
    current_char = grid[next_step[0]][next_step[1]]
    for change in pos_change[current_char]:
        x = next_step[0] + change[0]
        y = next_step[1] + change[1]
        try:
            # print("try: ", grid[x][y])
            if previous != (x, y) and grid[x][y] != ".":
                previous = next_step
                next_step = (x, y)
                break
        except IndexError:
            pass

    steps += 1
    if steps > (140 * 140):
        break

print("Answer 1:", int(steps / 2))

