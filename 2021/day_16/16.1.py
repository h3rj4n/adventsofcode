from textwrap import wrap

with open('16_data.txt') as f:
    data = []
    for line in f:
        line = line.strip()
        h_size = len(line) * 4
        data.append((bin(int(line, 16))[2:]).zfill(h_size))

ans = 0


def processBit(b, depth=0):
    global ans

    version = int(b[:3], 2)
    # not 4 = operator | 4 = literal value
    typeId = int(b[3:6], 2)

    ans += version

    # For now, skip litteral data.
    if typeId == 4:
        d = b[6:]
        rm = 0
        numbers = wrap(d, 5)
        for n in numbers:
            rm += 5

            if int(n[0]) == 0:
                break
        return b[6+rm:]

    # either 1 (length 11), or 0 (lenght 15)
    lengthTypeId = int(b[6:7], 2)
    length = 15 if lengthTypeId == 0 else 11

    # Read the next part based
    subPacks = int(b[7:7+length], 2)

    # We've established some values and stats. remove this from the bit string.
    b = b[7+length:]

    # Do not continue when not asked.
    if cont is False:
        return b

    if lengthTypeId == 0:
        # subPacks describe the length of the subpacks.
        # Grep the next part
        actualData = b[:subPacks]

        while len(actualData) > 0:
            actualData = processBit(actualData, cont=True, depth=depth)

        # Remove the part we've just processed.
        b = b[subPacks:]

    else:
        # subPacks describe the amount of subpacks.
        for _ in range(subPacks):
            b = processBit(b, cont=True, depth=depth)

    return b


# Loop trough the lines and parse the lines.
for b in data:
    processBit(b)

print(ans)
