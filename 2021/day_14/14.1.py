import collections
import numpy

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
output = ''

for _ in range(10):
    if len(output) > 0:
        start = output
        output = ''

    previousChar = None
    # Loop trough the start string.
    for index, char in enumerate(start):
        if previousChar is None:
            previousChar = char
            continue
        else:
            output += previousChar

        addedChar = data[previousChar + char]
        output += addedChar

        previousChar = char

    output += previousChar

a = numpy.array(list(output))
c = collections.Counter(a)

print('answer: ', c.most_common(1)[-1][1] - c.most_common()[-1][1])
