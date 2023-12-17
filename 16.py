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
                        pos.append([(x, y), (0, -1)])
                else:
                    pos.append([(0, 0), (1, 0)])
        # print(line)

def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

@lru_cache(maxsize=512)
def get_bounces(line, direction):
    bounces = []
    if line[0] is None: # x-axis
        bounces = [x for x in data if x[1] == line[1]]
        bounces.append((0, line[1]) if direction[0] == -1 else (x_max, line[1]))
        bounces.sort(key=lambda x: x[1], reverse=direction[1] == 1)
        
    if line[1] is None: # y-axis
        bounces = [x for x in data if x[0] == line[0]]
        bounces.append((line[0], 0) if direction[1] == 1 else (line[0], y_max))
        bounces.sort(key=lambda x: x[1], reverse=direction[1] == 1)
    return bounces

# t1 = get_bounces((None, 2), (1, 0))
# print(t1)
# t2 = get_bounces((2, None), (0, 1))
# print(t2)
# quit()

# @lru_cache(maxsize=512)
def filter_pos(pos, beam):
    # Return all the positions that require actions.
    if beam[1][1] == 0:
        if pos[1] != beam[0][1]:
            return False
        # Do something on the x-axis.
        return pos[0] > beam[0][0] if beam[1][0] == 1 else pos[0] < beam[0][0]
    if beam[1][0] == 0:
        if pos[0] != beam[0][0]:
            return False
        #print('filter y', pos, pos[1] > beam[0][1], pos[1] < beam[0][1])
        # Do something on the y-axis.
        return pos[1] < beam[0][1] if beam[1][1] == 1 else pos[1] > beam[0][1]

energized = []
count = 0
def cprint(*args, **kwargs):
    if count == 2:
        # print(*args, **kwargs)
        pass

prev_energized = None

while count < 12:
    count += 1
    start_pos = pos.copy()
    pos = []
    
    for beam_index, beam in enumerate(start_pos):
        print('beam:', beam[0], '\ndirec:', beam[1])
        # if beam[1][1] == 0: # Direction: x axis
        # Get all the pos on the x axis.
        req = (None, beam[0][1]) if beam[1][1] == 0 else (beam[0][0], None)
        bounces_in_line = get_bounces(req, beam[1])
        print("b line", bounces_in_line)
        bounces = list(filter(lambda x: filter_pos(x, beam), bounces_in_line))

        # Sort based on the direction.
        # if beam[1][1] == 0: # x-axis
        #     bounces.append((0, beam[0][1]) if beam[1][0] == -1 else (x_max, beam[0][1]))
        #     cprint("x", bounces)
        #     bounces.sort(key=lambda x: x[0], reverse=beam[1][0] == -1)
        #     cprint("x", bounces)
        # else: # y-axis
        #     bounces.append((beam[0][0], 0) if beam[1][1] == 1 else (beam[0][0], y_max))
        #     cprint("b", bounces)
        #     bounces.sort(key=lambda x: x[1], reverse=beam[1][1] == 1)
        #     cprint("t", bounces)

        for bounce in bounces:
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
                energized.append(bounce)
            if beam[1][1] == 0:
                p = sorted([beam[0][0], bounce[0]])
                for x in range(p[0], p[1]):
                    ener = (x, beam[0][1])
                    if ener not in energized:
                        energized.append(ener)
            else:
                p = sorted([beam[0][1], bounce[1]])
                for x in range(p[0], p[1]):
                    ener = (beam[0][0], x)
                    if ener not in energized:
                        energized.append(ener)
            
            try:
                if data[bounce] == '|':
                    # Split the beam, we're going up and down now.
                    pos.append([bounce, (0, 1)])
                    pos.append([bounce, (0, -1)])
                    break
                
                if data[bounce] == '-':
                    # Split the beam, we're going up and down now.
                    pos.append([bounce, (1, 0)])
                    pos.append([bounce, (-1, 0)])
                    break

                if data[bounce] == "/":
                    if beam[1][1] == 0: # x-axis
                        if beam[1][0] == 1:
                            # Going right, now going up.
                            pos.append([bounce, (0, 1)])
                        else:
                            # Going left, now going down.
                            pos.append([bounce, (0, -1)])
                    if beam[1][0] == 0: # y-axis
                        if beam[1][1] == 1:
                            # Going up, now going right.
                            pos.append([bounce, (1, 0)])
                        else:
                            # Going down, now going left.
                            pos.append([bounce, (-1, 0)])
                    break
                
                if data[bounce] == "\\":
                    print('--------------- yow')
                    if beam[1][1] == 0: # x-axis
                        if beam[1][0] == -1:
                            print("going up!")
                            # Going left, now going up.
                            pos.append([bounce, (0, 1)])
                        else:
                            # Going right, now going down.
                            pos.append([bounce, (0, -1)])
                    if beam[1][0] == 0: # y-axis
                        print('y ass')
                        if beam[1][1] == -1:
                            # Going down, now going right.
                            pos.append([bounce, (1, 0)])
                        else:
                            print('hellow', bounce)
                            # Going up, now going left.
                            pos.append([bounce, (-1, 0)])
                    break

                # y = beam[1][0] * -1 if data[bounce] == '/' else beam[1][0]
                # pos[beam_index] = (y, 0)
            except KeyError or ValueError:
                if beam in pos:
                    del pos[pos.index(beam)]
                cprint("exception", pos, beam_index)
                # del pos[beam_index]
                pass

                
            # If moving on y-axis, the -, / and \ are blocking.
            #print(data[bounce])
            # break
            # print("b", bounces)
            # print(count, "\n")
        # break
    # print('while?', count, pos)

    # Search for 
    if count > 1000:
        print("error?")
        break

for y in range(0, y_max):
    for x in range(0, x_max):
        if (x, y) in energized:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(len(energized))

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