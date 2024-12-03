import re
import math

races = []
time = ''
distance = ''
with open('6_data.txt') as f:
    count = 0
    for line in f:
        m = [int(n) for n in re.findall("(\d+)", line)]
        if count == 0:
            for n in m:
                time += str(n)
                races.append([n])
            count += 1
        else:
            for index, n in enumerate(m):
                distance += str(n)
                races[index].append(n)

wins_total = 1
for race in races:
    x = race[0] - 1
    y = 1
    wins = 0
    while x > 1:
        if x * y > race[1]:
            wins += 1
        x -= 1
        y += 1
    wins_total = wins_total * wins

print("Answer 1:", wins_total)

time = int(time)
distance = int(distance)

y = math.floor(distance / time)
x = time - y
while x * y < distance:
    x -= 1
    y += 1

print("Answer 2:", x - y + 1)