from collections import Counter

left = []
right = []
with open("input_01.txt", encoding="utf-8") as f:
    for line in f:
        values = line.rstrip().split("   ")
        left.append(int(values[0]))
        right.append(int(values[1]))

left = sorted(left)
right = sorted(right)

# @see https://stackoverflow.com/a/5829377
counted = Counter(right)

diff = 0
second = 0
for i, value in enumerate(left):
    diff += abs(left[i] - right[i])
    second += value * counted[value]

print("Part 1:", diff)
print("Part 2:", second)
