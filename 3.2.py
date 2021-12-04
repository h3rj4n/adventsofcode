# Get the data
f = open("3_data.txt")
content = f.read().split('\n')

def mostCommonBit(position, array):
    splitted = None

    for bit in array:
        if splitted == None:
            splitted = [0] * len(bit.rstrip('\n'))

        for index, char in enumerate(bit):
            if char == '\n':
                continue

            if int(char) == 1:
                splitted[index] += 1
            else:
                splitted[index] -= 1

    return 1 if splitted[position] >= 0 else 0

manipulatedPos = content
manipulatedLes = content

for i in range(len(content[0].rstrip('\n'))):
    # print('array length before filter: ', len(manipulatedPos
    
    # Only filter if we have more than one number left.
    if len(manipulatedPos) > 1:
        # Get the most common bit for the i-position
        common = mostCommonBit(i, manipulatedPos)
        manipulatedPos = list(filter(lambda record: len(record) > 1 and int(record[i]) == common, manipulatedPos))
        
    if len(manipulatedLes) > 1:
        negative = mostCommonBit(i, manipulatedLes)
        manipulatedLes = list(filter(lambda record: len(record) > 1 and int(record[i]) != negative, manipulatedLes))
    
    print('POS length after filter: ', len(manipulatedPos))
    print('LES length after filter: ', len(manipulatedLes))
    # print(manipulated)

print('oxygen rating: ', int(manipulatedPos[0], 2))
print('co2 scub rating: ', int(manipulatedLes[0], 2))

print('answer: ', int(manipulatedPos[0], 2) * int(manipulatedLes[0], 2))
