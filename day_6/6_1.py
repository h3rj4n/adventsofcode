import numpy

with open("6_data.txt") as f:
    line = f.readline().strip()

    values = []

    # Convert the entire string in numbers.
    for i in line:
        values.append(ord(i))

    i = 0
    while i < len(values) - 4:
        if len(numpy.unique(values[i:i+4])) == 4:
            # Found our answer.
            print(i + 4)
            break

        i += 1