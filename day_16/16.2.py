from textwrap import wrap

with open('16_demo.txt') as f:
    data = []
    for line in f:
        line = line.strip()
        h_size = len(line) * 4
        data.append((bin(int(line, 16))[2:]).zfill(h_size))


def processBit(b, depth=0):
    prefix = ''.join(['\t'] * depth)
    depth += 1

    # print(prefix, 'input: ', b)
    version = int(b[:3], 2)
    # not 4 = operator | 4 = literal value
    typeId = int(b[3:6], 2)

    # print(prefix, 'packet version: ', version)
    # print(prefix, 'packet type id: ', typeId)

    # For now, skip litteral data.
    if typeId == 4:
        d = b[6:]
        rm = 0
        numb = wrap(d, 5)
        oNumber = []
        for n in numb:
            rm += 5
            oNumber.append(int(n[1:], 2))
            # print(prefix, 'number: ', int(n[1:], 2))

            if int(n[0]) == 0:
                break
        return b[6+rm:], oNumber

    # either 1 (length 11), or 0 (lenght 15)
    lengthTypeId = int(b[6:7], 2)
    length = 15 if lengthTypeId == 0 else 11

    # print(prefix, 'lenght type id: ', lengthTypeId, ' length: ', length)

    # Read the next part based
    subPacks = int(b[7:7+length], 2)
    # print(prefix, 'subPacks: ', subPacks)

    # We've established some values and stats. remove this from the bit string.
    b = b[7+length:]

    numbers = []

    if lengthTypeId == 0:
        # subPacks describe the length of the subpacks.
        # Grep the next part
        actualData = b[:subPacks]

        while len(actualData) > 0:
            # print(prefix, actualData)
            actualData, n = processBit(actualData, depth=depth)
            numbers += n

        # Remove the part we've just processed.
        b = b[subPacks:]

    else:
        # subPacks describe the amount of subpacks.
        for _ in range(subPacks):
            b, n = processBit(b, depth=depth)
            numbers += n

    numbOut = []
    # Add the numbers
    if typeId == 0:
        # print(prefix, 'sum: ', sum(numbers))
        numbOut.append(sum(numbers))
    if typeId == 1:
        result = 1
        for x in numbers:
            result = result * x
        # print(prefix, 'product: ', result)
        numbOut.append(result)
    if typeId == 2:
        # print(prefix, 'min: ', min(numbers))
        numbOut.append(min(numbers))
    if typeId == 3:
        # print(prefix, 'max: ', max(numbers))
        numbOut.append(max(numbers))
    if typeId == 5:
        v = 1 if numbers[0] > numbers[1] else 0
        # print(prefix, 'greater: ', v)
        numbOut.append(v)
    if typeId == 6:
        v = 1 if numbers[0] < numbers[1] else 0
        # print(prefix, 'less: ', v)
        numbOut.append(v)
    if typeId == 7:
        v = 1 if numbers[0] == numbers[1] else 0
        # print(prefix, 'equal: ', v)
        numbOut.append(v)


    return b, numbOut


# Loop trough the lines and parse the lines.
for b in data:
    _, n = processBit(b)
    print('answer: ', n[0])

# 111253530
