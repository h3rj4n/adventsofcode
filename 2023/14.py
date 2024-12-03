from functools import lru_cache

grid = []
rocks = []
blocks = []

with open("14_data.txt") as f:
    for row_index, line in enumerate(f):
        line = line.strip("\n")
        if len(grid) == 0:
            grid = [""] * len(line)
        for index, char in enumerate(line):
            grid[index] += char
            if char == "O":
                rocks.append((index, row_index))
            if char == "#":
                blocks.append((index, row_index))

answer = 0

for row in grid:
    row_value = 0
    start = len(grid)

    for index, char in enumerate(row):
        if char == "O":
            row_value += start
            start -= 1
        if char == "#":
            start = len(grid) - (index + 1)

    answer += row_value

print("Answer 1:", answer)

@lru_cache(maxsize=512)
def get_blocking_blocks(x=None, y=None) -> list:
    # Get all the blocks.
    if x is not None:
        return [b for b in blocks if b[0] == x]
    if y is not None:
        return [b for b in blocks if b[1] == y]

def get_rocks_in_direction(x=None, y=None) -> list:
    if x is not None:
        return [r for r in rocks if r[0] == x]
    if y is not None:
        return [r for r in rocks if r[1] == y]

# @lru_cache(maxsize=512)
def get_new_pos(direction, new_pos, old_pos):
    x = new_pos[0] if direction == 'north' or direction == 'south' else None
    y = new_pos[1] if direction == 'east' or direction == 'west' else None
    rocks_direction = get_rocks_in_direction(x, y)
    output = new_pos
    while output in rocks_direction and output != old_pos:
        if direction == 'north':
            output = (output[0], output[1] + 1)
        elif direction == 'west':
            output = (output[0] + 1, output[1])
        elif direction == 'south':
            output = (output[0], output[1] - 1)
        elif direction == 'east':
            output = (output[0] - 1, output[1])
    return output


# print((1000000000 - 115) % 42)

# quit()

# print(rocks)
cycle = 0
# answer_list = []
cycle_list = {}
cycle_answer_list = []
lowest_answer = 1000000000
while cycle < 1000:
    # print(int(cycle / 1000000000 * 100), cycle)
    cycle += 1

    # Move all blocks north.
    # Loop through all the blocks and move them.
    for i, rock in enumerate(rocks):
        # Get all the blocks.
        blocking = get_blocking_blocks(x=rock[0])

        # Can't move further north.
        if rock[1] == 0:
            # print(rock, rock)
            continue

        new_pos = (rock[0], 0)
        for b in blocking:
            if b < rock:
                # Move until block + 1.
                new_pos = (b[0], b[1] + 1)

        # while new_pos in rocks and new_pos != rock:
        #     new_pos = (new_pos[0], new_pos[1] + 1)

        rocks[i] = get_new_pos('north', new_pos, rock)

    # Loop through all the blocks and move them.
    for i, rock in enumerate(rocks):
        # Get all the blocks.
        blocking = get_blocking_blocks(y=rock[1])

        # Can't move further west.
        # if rock[1] == 0:
        #     print(rock, rock)
        #     continue

        new_pos = (0, rock[1])
        for b in blocking:
            if b < rock:
                # Move until block + 1.
                new_pos = (b[0] + 1, b[1])

        # while new_pos in rocks and new_pos != rock:
        #     new_pos = (new_pos[0] + 1, new_pos[1])

        rocks[i] = get_new_pos('west', new_pos, rock)

    # break

    for i, rock in enumerate(rocks):
        # Get all the blocks.
        blocking = get_blocking_blocks(x=rock[0])

        # Can't move further north.
        # if rock[1] == 0:
        #     # print(rock, rock)
        #     continue

        new_pos = (rock[0], len(grid) - 1)
        for b in blocking:
            if b > rock:
                # Move until block.
                new_pos = (b[0], b[1] - 1)
                break

        # while new_pos in rocks and new_pos != rock:
        #     new_pos = (new_pos[0], new_pos[1] - 1)

        rocks[i] = get_new_pos('south', new_pos, rock)

    for i, rock in enumerate(rocks):
        # Get all the blocks.
        blocking = get_blocking_blocks(y=rock[1])

        # Can't move further west.
        # if rock[1] == 0:
        #     print(rock, rock)
        #     continue

        new_pos = (len(grid[0]) - 1, rock[1])
        for b in blocking:
            if b > rock:
                # Move until block + 1.
                new_pos = (b[0] - 1, b[1])
                break

        while new_pos in rocks and new_pos != rock:
            new_pos = (new_pos[0] - 1, new_pos[1])

        rocks[i] = get_new_pos('east', new_pos, rock)


    answer = 0
    for rock in rocks:
        answer += len(grid[0]) - rock[1]

    prev_cycles = [k for k, v in enumerate(cycle_answer_list) if v == answer]
    print("prev cycles:", prev_cycles)
    if len(prev_cycles) > 2:
        print(prev_cycles[1], prev_cycles[0])
        diff = (prev_cycles[1]) - prev_cycles[0]
        diff_i = (1000000000 - prev_cycles[0]) % diff
        print("diff_i", diff, diff_i, prev_cycles[1] + diff_i)
        print("Answer 2:", cycle_answer_list[prev_cycles[1] + diff_i])
        break
        # pass

    cycle_answer_list.append(answer)

    if answer < lowest_answer:
        lowest_answer = answer

    # cycle_answer_list.append(answer)

    # if answer not in answer_list:
    #     answer_list.append(answer)
    #     cycle_list[answer] = cycle

        # print("cycle repeat", cycle, answer, cycle_list[answer])
        # diff = (1000000000 - cycle_list[answer]) % (cycle - cycle_list[answer])
        # diff_index = cycle - (cycle - cycle_list[answer]) - diff
        # print(cycle, (cycle - cycle_list[answer]), diff)
        # print("Answer 2:", cycle_answer_list[diff_index], diff_index, diff)
    # if answer < lowest:
    #     lowest = answer
    #     lowest_cycle = cycle
    # elif answer == lowest:
    #     print("cycle repeat", cycle, answer)

    print("cycle", cycle, answer)


        # print(rock)


    # m = re.finditer(r"([.O]*)(#[\.O]+)", row)
    # for mi in m:
    #     print(mi.span(), mi.group())
    # print(list(m))

# print(len(cycle_answer_list) - 50, cycle_answer_list[-51])
# print((len(cycle_answer_list) - 51 - cycle_list[answer]))
# answer = (1000000000 - len(cycle_answer_list) - 50) % (len(cycle_answer_list) - 51 - cycle_list[answer])

# print(grid)
# answer = 0
# for rock in rocks:
#     answer += len(grid[0]) - rock[1]

# print("Answer 2:", cycle_answer_list[-51 + answer])

# Let's print out the image.
# for index, g in enumerate(grid):
#     line = ""
#     the_rocks = [r for r in rocks if r[1] == index]
#     the_blocks = [b for b in blocks if b[1] == index]

#     for i in range(0, len(grid)):
#         if (i, index) in the_rocks:
#             line += "O"
#         elif (i, index) in the_blocks:
#             line += "#"
#         else:
#             line += "."

#     print(line)
