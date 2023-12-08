import re
import math

data = {}
instructions = ''
start_pos = []

with open("8_data.txt") as f:
    instructions = f.readline().rstrip()
    for ln in f:
        step = ln.rstrip()
        if step:
            m = re.search(r"(\w{3}) = .(\w{3}), (\w{3}).", step)
            data[m.group(1)] = {
                "L": m.group(2),
                "R": m.group(3)
            }
            if m.group(1)[2] == 'A':
                start_pos.append(m.group(1))

current_pos = 'AAA'
step = 0
while current_pos != 'ZZZ':
    index = (step % len(instructions))
    step += 1
    direction = instructions[index]
    current_pos = data[current_pos][direction]

print("Answer 1:", step)

step = 0
found = []
while len(start_pos) > 0:
    index = (step % len(instructions))
    step += 1
    direction = instructions[index]

    new_start = []
    for pos in start_pos:
        if data[pos][direction][2] == 'Z':
            found.append(step)
        else:
            new_start.append(data[pos][direction])

    start_pos = new_start

print("Answer 2:", math.lcm(*found))
