from collections import defaultdict

with open('12_data.txt') as f:
    # Loop trough the lines and create multidimensional array.
    data = defaultdict(list)
    for line in f:
        d = line.strip().split('-')
        for x, y in [(0, 1), (1, 0)]:
            #value = data[d[x]]
            if d[y] != 'start' and d[x] != 'end':
                data[d[x]].append(d[y])
            #data[d[x]].append(value)

print(data)

# Start with the start point. Add unique lines/steps to this list.
start = [
    ['start']
]
# All the fully build entries end up in the following list.
end = []
# Keep looping trough the array until it's empty.
while len(start) > 0:
#for _ in range(3):
    output = []
    for i, s in enumerate(start):
        # last entry.
        startPoint = s[-1]
        # Get all the next steps.
        for char in data[startPoint]:
            clone = s.copy()
            if (clone[-1] != 'start' and char != 'end' and char.islower() and char in clone):
                # We've reached a dead end.
                #print('readed a dead end, char: ', char)
                pass
            else:
                # Copy the existing when first index is used
                clone.append(char)
                if char == 'end':
                    end.append(clone)
                else:
                    output.append(clone)
    start = output

# print(print('\n'.join(','.join(str(x) for x in row) for row in start)))
# print('--- end')
# print(print('\n'.join(','.join(str(x) for x in row) for row in end)))

print('answer: ', len(end))
