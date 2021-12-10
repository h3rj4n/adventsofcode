import numpy as np

with open('10_data.txt') as f:
    # Loop trough the lines.
    data = []
    for line in f:
        data.append(line)

score = {'(': 1, '[': 2, '{': 3, '<': 4}
lineScores = []

# Search for the corrupt lines
for line in data:
    lineAns = 0
    opens = []
    closes = []
    for char in list(line):
        for openChar, closeChar in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
            if (char == openChar):
                opens.append(char)
            elif char == closeChar:
                if opens[len(opens) - 1] == openChar:
                    # Remove the previous item from the array
                    opens.pop()
                else:
                    closes.append(char)
    # Get the first illegal char.
    if len(closes) == 0:
        opens.reverse()
        for c in opens:
            lineAns = lineAns * 5 + score[c]

        lineScores.append(lineAns)

x = np.array(lineScores)
print('answer: ', int(np.median(x)))

# 2924734236
