# Open the file
with open("1_data.txt") as f:
    answer = 0

    for lines in f:
        data = [(c) for i, c in enumerate(lines) if c.isdigit()]
        answer += int(data[0] + data[-1])

print(answer)

# Part 2.
with open("data.txt") as f:
    answer = 0

    textual = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for lines in f:
        data = [(i, c) for i, c in enumerate(lines) if c.isdigit()]

        for spelled, number in textual.items():
            indices = [index for index in range(len(lines)) if lines.startswith(spelled, index)]
            if len(indices) > 0:
                for i in indices:
                    data.append((i, number))

        if len(data) > 1:
            data.sort(key=lambda x: x[0])

        answer += int(str(data[0][1]) + str(data[-1][1]))

print(answer)