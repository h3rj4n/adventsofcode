from collections import defaultdict
import copy

with open('14_data.txt') as f:
    start = f.readline().strip()
    # Next up an empty line.
    f.readline()

    # Loop trough the lines.
    data = {}
    for line in f:
        fields = line.strip().split(' -> ')
        data[fields[0]] = fields[1]

print('start: ', start)

freq = defaultdict(int)
# Initiall fill the feq dictionary.
previousChar = None
# Loop trough the start string.
for index, char in enumerate(start):
    if previousChar is None:
        previousChar = char
        continue

    freq[previousChar + char] += 1
    previousChar = char

for _ in range(40):
    clone = copy.copy(freq)
    for pair in freq:
        char = data[pair]
        occ = freq[pair]

        # Create new pairs.
        clone[pair] -= occ
        clone[pair[0] + char] += occ
        clone[char + pair[1]] += occ

    freq = clone

polymer = defaultdict(int)
for pair in freq:
    count = freq[pair]
    polymer[pair[0]] += count
    polymer[pair[1]] += count

polymer[start[0]] += 1
polymer[start[-1]] += 1

sort = sorted(polymer.items(), key=lambda item: item[1])

print('answer: ', int(sort[-1][1] / 2 - sort[0][1] / 2))

# 
