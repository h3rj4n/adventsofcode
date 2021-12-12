from collections import defaultdict
from collections import Counter

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

# Start with the start point. Add unique lines/steps to this list.
start = [
    ['start']
]
# All the fully build entries end up in the following list.
end = []
# Keep looping trough the array until it's empty.
while len(start) > 0:
#for _ in range(2):
    output = []
    for i, s in enumerate(start):
        # last entry.
        startPoint = s[-1]
        # Get all the next steps.
        for char in data[startPoint]:
            count = 1 if len(data[char]) > 1 else 1
            clone = s.copy()
            smallChars = list(filter(lambda x: x.islower() and x != 'start', clone))
            #print(Counter(smallChars))
            keys = [item for item, count in Counter(smallChars).items() if count == 2]
            #print(keys)
            #keys = (Counter(clone) - Counter(set(clone))).keys()

            if (clone[-1] != 'start' and char != 'end' and char.islower() and (len(keys) > 0 and char in smallChars)):
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

# with open('answer.txt') as f:
#     # Loop trough the lines and create multidimensional array.
#     yow = []
#     for line in f:
#         yow.append(line.strip())
#
#     diff = list(set(yow) - set(list(map(lambda x: ','.join(x), end))))
#     print('--- diff')
#     print(print('\n'.join(diff)))

print('answer: ', len(end))
