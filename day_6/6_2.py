import numpy

search = 14

with open("6_data.txt") as f:
    line = f.readline().strip()

    values = []

    # Convert the entire string in numbers.
    for i in line:
        values.append(ord(i))

    i = 0
    while i < len(values) - search:
        if len(numpy.unique(values[i:i+search])) == search:
            # Found our answer.
            print(i + search)
            break

        i += 1