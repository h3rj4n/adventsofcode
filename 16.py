from functools import lru_cache

directions = {
    ( 1,  0): "R", # Right
    (-1,  0): "L", # Left
    ( 0,  1): "U", # Up
     (0, -1): "D"  # Down
}
rdirections = {
    "R": ( 1,  0),
    "L": (-1,  0),
    "U": ( 0,  1),
    "D": ( 0, -1)
}


data = {}
x_max = 0
y_max = 0
pos = []
with open("16_data.txt") as f:
    for y, line in enumerate(f.read().split("\n")):
        if len(line) > 0:
            y_max += 1
        if x_max == 0:
            x_max = len(line) - 1
        for x, char in enumerate(line):
            if char in ["|", "-", "/", "\\"]:
                data[(x, y)] = char
            if (0, 0) == (x, y):
                if char in ["|", "\\"]:
                    pos.append(((0, 0), (0, -1)))
                else:
                    pos.append(((0, 0), (1, 0)))
        print(line)

y_max -= 1

@lru_cache(maxsize=512)
def get_bounces(line, direction):
    cur_dir = directions[direction]
    bounces = []
    if cur_dir in ["L", "R"]: # x-axis
        bounces = [x for x in data if x[1] == line[1]]
        bounces.append((0, line[1]) if direction[0] == -1 else (x_max, line[1]))
        bounces = list(set(bounces))
        bounces.sort(key=lambda x: x[0], reverse=direction[0] == -1)

    if cur_dir in ["U", "D"]: # y-axis
        bounces = [x for x in data if x[0] == line[0]]
        bounces.append((line[0], 0) if direction[1] == 1 else (line[0], y_max))
        bounces = list(set(bounces))
        bounces.sort(key=lambda x: x[1], reverse=directions[direction] == "U")
    return bounces

def get_next_bounce(beam, bounces):
    cur_dir = directions[beam[1]]
    for posible in bounces:
        if posible == beam[0]:
            continue

        try:
            if cur_dir in ["R", "L"]:
                if data[posible] == '-':
                    # Skip this one.
                    continue
            if cur_dir in ["U", "D"]:
                if data[posible] == '|':
                    # Skip this one.
                    continue
        except KeyError:
            pass

        if cur_dir == "R" and beam[0][0] < posible[0]:
            return posible
        
        if cur_dir == "L" and beam[0][0] > posible[0]:
            return posible
        
        if cur_dir == "U" and beam[0][1] > posible[1]:
            return posible
        
        if cur_dir == "D" and beam[0][1] < posible[1]:
            return posible

    if cur_dir == "U":
        return (beam[0][0], 0)
    if cur_dir == "D":
        return (beam[0][0], y_max)
    if cur_dir == "R":
        return (x_max, beam[0][1])
    if cur_dir == "L":
        return (0, beam[0][1])

energized = []
count = 0
count_new_pos_in_energized = 0

while count < 100 and count_new_pos_in_energized < 4:
    count += 1
    start_pos = list(set(pos.copy()))
    pos = []
    new_pos_in_energized = 0

    # print("\nstart pos", start_pos)
    for beam_index, beam in enumerate(start_pos):
        # print('start:', beam[0], 'direc:', directions[beam[1]])
        cur_dir = directions[beam[1]]

        req = (None, beam[0][1]) if beam[1][1] == 0 else (beam[0][0], None)
        bounces_in_line = get_bounces(req, beam[1])
        bounce = get_next_bounce(beam, bounces_in_line)

        if bounce not in energized:
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

        if bounce not in data:
            # print('  end:', beam[0], 'direc:', directions[beam[1]], "=>", bounce, new_pos_in_energized)
            continue

        try:
            if data[bounce] == '|' and cur_dir in ["L", "R"]:
                # Split the beam, we're going up and down now.
                pos.append((bounce, (0, 1)))
                pos.append((bounce, (0, -1)))
                # break

            if data[bounce] == '-' and cur_dir in ["U", "D"]:
                # Split the beam, we're going up and down now.
                pos.append((bounce, (1, 0)))
                pos.append((bounce, (-1, 0)))
                # break

            if data[bounce] == "/":
                map = {
                    "R": "U",
                    "L": "D",
                    "D": "L",
                    "U": "R",
                }
                pos.append((bounce, rdirections[map[cur_dir]]))

            if data[bounce] == "\\":
                map = {
                    "R": "D",
                    "D": "R",
                    "L": "U",
                    "U": "L"
                }
                pos.append((bounce, rdirections[map[cur_dir]]))

        except ValueError:
            pass

        # print('  end:', beam[0], 'direc:', directions[beam[1]], "=>", bounce, new_pos_in_energized)

    if new_pos_in_energized == 0:
        count_new_pos_in_energized += 1

    # Search for
    if count > 1000:
        print("error?")
        break

# print("  ", end="")
# for x in range(0, x_max + 1):
#     print(x, end="")
# print()
# for y in range(0, y_max + 1):
#     print(y, "", end="")
#     for x in range(0, x_max + 1):
#         if (x, y) in energized:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
#print(count)
print("Answer 1:", len(set(energized)))

# Answer: 8034
# Anser 2: 8225