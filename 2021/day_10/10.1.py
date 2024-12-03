with open('10_data.txt') as f:
    # Loop trough the lines.
    data = []
    for line in f:
        data.append(line)

output = []

# Search for the corrupt lines
for line in data:
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
    if len(closes) > 0:
        output.append(closes[0])

ans = 0
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
for char in output:
    ans += score[char]
print('anser: ', ans)

# 343863
