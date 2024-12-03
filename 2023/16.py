from functools import lru_cache


data = {}
x_max = 0
y_max = 0
pos = [
    # cur pos => direction
    #[(0, 0), (1, 0)]
]
with open("16_data.txt") as f:
    for y, line in enumerate(f.read().split("\n")):
        y_max += 1
        if x_max == 0:
            x_max = len(line)
        for x, char in enumerate(line):
            if char in ["|", "-", "/", "\\"]:
                data[(x, y)] = char
            if (0, 0) == (x, y):
                if char in ["|", "-", "/", "\\"]:
                    if char == "|" or char == "\\":
                        pos.append(((x, y), (0, -1)))
                else:
                    pos.append(((0, 0), (1, 0)))
        # print(line)

@lru_cache(maxsize=512)
def get_bounces(line, direction):
    bounces = []
    if line[0] is None: # x-axis
        bounces = [x for x in data if x[1] == line[1]]
        bounces.append((0, line[1]) if direction[0] == -1 else (x_max, line[1]))
        bounces = list(set(bounces))
        bounces.sort(key=lambda x: x[0], reverse=direction[0] == -1)

    if line[1] is None: # y-axis
        bounces = [x for x in data if x[0] == line[0]]
        bounces.append((line[0], 0) if direction[1] == 1 else (line[0], y_max))
        bounces = list(set(bounces))
        bounces.sort(key=lambda x: x[1], reverse=direction[1] == -1)
    return bounces

def get_next_bounce(beam, bounces):
    print("b", beam)
    print("b", bounces)

    for posible in bounces:
        if posible == beam[0]:
            continue

        try:
            if beam[1][1] == 0:
                if data[posible] == '-':
                        # Skip this one.
                        continue
                if beam[1][0] == 0:
                    if data[posible] == '|':
                        # Skip this one.
                        continue
        except KeyError:
            continue

        print("check", beam[0], posible)

        if beam[1][1] == 0:
            if beam[1][0] == 1 and beam[0][0] < posible[0]:
                return posible
            elif beam[1][0] == -1 and beam[0][0] > posible[0]:
                return posible

        if beam[1][0] == 0:
            if beam[1][1] == 1 and beam[0][1] < posible[1]:
                return posible
            elif beam[1][1] == -1 and beam[0][1] > posible[1]:
                return posible
            elif beam[1][1] == -1 and beam[0][1] == 0:
                # Out of bounds
                return None

    return None

# @lru_cache(maxsize=512)
def filter_pos(pos, beam):
    # Return all the positions that require actions.
    if beam[1][1] == 0:
        # Do something on the x-axis.
        return pos[0] > beam[0][0] if beam[1][0] == 1 else pos[0] < beam[0][0]
    if beam[1][0] == 0:
        #print('filter y', pos, pos[1] > beam[0][1], pos[1] < beam[0][1])
        # Do something on the y-axis.
        return pos[1] < beam[0][1] if beam[1][1] == 1 else pos[1] > beam[0][1]

energized = []
count = 0
count_new_pos_in_energized = 0

while count < 100 and count_new_pos_in_energized < 4:
    count += 1
    start_pos = list(set(pos.copy()))
    pos = []
    new_pos_in_energized = 0

    print("\nstart pos", start_pos)
    for beam_index, beam in enumerate(start_pos):
        print('start:', beam[0], 'direc:', beam[1])

        req = (None, beam[0][1]) if beam[1][1] == 0 else (beam[0][0], None)
        bounces_in_line = get_bounces(req, beam[1])
        bounce = get_next_bounce(beam, bounces_in_line)
        # bounces = list(filter(lambda x: filter_pos(x, beam), bounces_in_line))

        if bounce is None:
            print('  end:', beam[0], 'direc:', beam[1], "=>", bounce)
            continue

        next_step = None

        # for bounce in bounces:
        # If moving on x-axis, the |, / and \ are blocking.
        try:
            if beam[1][1] == 0:
                if data[bounce] == '-':
                    # Skip this one.
                    continue
            if beam[1][0] == 0:
                if data[bounce] == '|':
                    # Skip this one.
                    continue
        except KeyError:
            pass

        # Add all the x, y pos to the energized list.
        # @todo Support for y-axis.
        if bounce not in energized and bounce[0] < x_max and bounce[1] < y_max:
            new_pos_in_energized += 1
            energized.append(bounce)
        if beam[1][1] == 0:
            p = sorted([beam[0][0], bounce[0]])
            for x in range(p[0], p[1]):
                ener = (x, beam[0][1])
                if ener not in energized:
                    new_pos_in_energized += 1
                    energized.append(ener)
        else:
            p = sorted([beam[0][1], bounce[1]])
            for x in range(p[0], p[1]):
                ener = (beam[0][0], x)
                if ener not in energized:
                    new_pos_in_energized += 1
                    energized.append(ener)

        try:
            if data[bounce] == '|':
                # Split the beam, we're going up and down now.
                pos.append((bounce, (0, 1)))
                pos.append((bounce, (0, -1)))
                next_step = bounce
                # break

            if data[bounce] == '-':
                # Split the beam, we're going up and down now.
                pos.append((bounce, (1, 0)))
                pos.append((bounce, (-1, 0)))
                next_step = bounce
                # break

            if data[bounce] == "/":
                if beam[1][1] == 0: # x-axis
                    if beam[1][0] == 1:
                        # Going right, now going up.
                        pos.append((bounce, (0, -1)))
                    else:
                        # Going left, now going down.
                        pos.append((bounce, (0, 1)))
                if beam[1][0] == 0: # y-axis
                    if beam[1][1] == 1:
                        # Going up, now going right.
                        pos.append((bounce, (-1, 0)))
                    else:
                        # Going down, now going left.
                        pos.append((bounce, (1, 0)))
                next_step = bounce
                # break

            if data[bounce] == "\\":
                if beam[1][1] == 0: # x-axis
                    if beam[1][0] == -1:
                        # Going left, now going up.
                        pos.append((bounce, (0, -1)))
                    else:
                        # Going right, now going down.
                        pos.append((bounce, (0, 1)))
                if beam[1][0] == 0: # y-axis
                    if beam[1][1] == -1:
                        # Going down, now going right.
                        pos.append((bounce, (1, 0)))
                    else:
                        # Going up, now going left.
                        pos.append((bounce, (-1, 0)))
                next_step = bounce
                # break

        except ValueError:
            pass
        except KeyError:
            pass

        print('  end:', beam[0], 'direc:', beam[1], "=>", next_step)


            # If moving on y-axis, the -, / and \ are blocking.
            #print(data[bounce])
            # break
            # print("b", bounces)
            # print(count, "\n")
        # break
    # print('while?', count, count_new_pos_in_energized)

    if new_pos_in_energized == 0:
        count_new_pos_in_energized += 1

    # Search for
    if count > 1000:
        print("error?")
        break

# print("  ", end="")
# for x in range(0, x_max):
#     print(x, end="")
# print()
for y in range(0, y_max):
    # print(y, "", end="")
    for x in range(0, x_max):
        if (x, y) in energized:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(count)
print(len(energized))

# 8020 to low
# Answer: 8034
# Anser 2: 8225

# ######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..