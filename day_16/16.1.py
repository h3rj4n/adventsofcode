from textwrap import wrap

with open('16_demo.txt') as f:
    data = []
    for line in f:
        line = line.strip()
        h_size = len(line) * 4
        data.append((bin(int(line, 16))[2:]).zfill(h_size))

ans = 0


def processBit(b, cont=True, type=None, size=None):
    global ans
    print('input: ', b)
    version = int(b[:3], 2)
    # not 4 = operator | 4 = literal value
    typeId = int(b[3:6], 2)

    ans += version

    print('packet version: ', version)
    print('packet type id: ', typeId)

    # For now, skip litteral data.
    if typeId == 4:
        d = b[6:]
        numbers = wrap(d, 5)
        for n in numbers:
            print(n)
            print('number: ', int(n[1:], 2))

            if n[0] == 0:
                break
        return

    # either 1 (length 11), or 0 (lenght 15)
    lengthTypeId = int(b[6:7], 2)
    length = 15 if lengthTypeId == 0 else 11

    print('lenght type id: ', lengthTypeId)

    # Read the next part based
    subPacks = int(b[7:7+length], 2)
    print('subPacks: ', subPacks)

    # Do not continue when not asked.
    if cont is False:
        return

    if lengthTypeId == 0:
        # subPacks describe the length of the subpacks.
        # Grep the next part
        actualData = b[7+length:7+length+subPacks]

        # Loop trough the data, grep the next 11 bits? until
        # last group is found.
        items = wrap(actualData, 11)
        for i, d in enumerate(items):
            lastBit = False

            if int(d[:1]) == 0 and len(items) > i + 1:
                # Found the last group.
                lastBit = True
                d += items[i+1]

            # processBit(d, cont=True)

            if lastBit:
                break
    else:
        # Remove all the process stuff.
        s = b[18:]
        # subPacks describe the amount of subpacks.
        for _ in range(subPacks):
            # processBit(s, cont=True)
            pass


# Loop trough the lines and parse the lines.
for b in data:
    processBit(b)

print(ans)

# 8A004A801A8002F478 represents an operator packet (version 4) which
# contains an operator packet (version 1) which contains an operator packet
# (version 5) which contains a literal value (version 6); this packet has
# a version sum of 16.
