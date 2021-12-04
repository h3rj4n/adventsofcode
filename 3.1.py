# Get the data
f = open("3_data.txt")

splitted = None

for bit in f:
    if splitted == None:
        splitted = [0] * len(bit.rstrip('\n'))

    for index, char in enumerate(bit):
        if char == '\n':
            continue

        if int(char) == 1:
            splitted[index] += 1
        else:
            splitted[index] -= 1

print(splitted)

gamma = ''
epsilon = ''

for value in splitted:
    if value > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('gamma: ', gamma)
print('espilon: ', epsilon)

print('gamma: ', int(gamma, 2))
print('espilon: ', int(epsilon, 2))

print('answer: ', int(gamma, 2) * int(epsilon, 2))
