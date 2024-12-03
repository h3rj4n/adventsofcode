card_values = {
    'A': 24,
    'K': 23,
    'Q': 22,
    'J': 21,
    'T': 20,
}

data = {}

with open('7_data.txt') as f:
    for line in f:
        record = line.split(" ")

        chars = {}
        d = ""
        for t in record[0]:
            dd = int(t) + 10 if t not in card_values else card_values[t]
            d += str(dd)
            if t not in chars:
                chars[t] = 0
            chars[t] += 1

        c_value = int(d)
        for key, value in chars.items():
            if value == 2:
                c_value += 1 * 10000000000
            if value == 3:
                c_value += 10 * 10000000000
            if value == 4:
                c_value += 100 * 10000000000
            if value == 5:
                c_value += 1000 * 10000000000

        data[record[1]] = int(c_value)

answer = 0
rows = dict(sorted(data.items(), key=lambda item: item[1]))
for index, value in enumerate(rows.keys()):
    answer += int(value) * (index + 1)

print("Answer 1:", answer)


card_values = {
    'A': 24,
    'K': 23,
    'Q': 22,
    'J': 11,
    'T': 20,
}

data = {}

with open('7_data.txt') as f:
    for line in f:
        record = line.split(" ")

        chars = {}
        d = ""
        for t in record[0]:
            dd = int(t) + 10 if t not in card_values else card_values[t]
            d += str(dd)
            if t not in chars:
                chars[t] = 0
            chars[t] += 1

        jack_count = 0
        if "J" in chars and len(chars.keys()) > 1:
            jack_count = chars["J"]
            del chars["J"]

        chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        if jack_count > 0:
            i = list(chars.keys())[0]
            chars[i] += jack_count

        c_value = int(d)
        for key, value in chars.items():
            if value == 2:
                c_value += 1 * 10000000000
            if value == 3:
                c_value += 10 * 10000000000
            if value == 4:
                c_value += 100 * 10000000000
            if value == 5:
                c_value += 1000 * 10000000000

        data[record[1]] = int(c_value)

answer = 0
rows = dict(sorted(data.items(), key=lambda item: item[1]))
for index, value in enumerate(rows.keys()):
    answer += int(value) * (index + 1)

print("Answer 2:", answer)