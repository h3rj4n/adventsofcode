# Import the data
with open("8_data.txt") as f:
    data = []
    for l in f:
        data.append(l.strip().split('|'))


# data = list(map(lambda x: int(x), raw_data))
ans = 0
for item in data:
    # For the current record, search for the known numbers (1,4,7,8).
    known = {}
    output = {}
    numbers = item[0].strip().split(' ')
    for n in numbers:
        n = ''.join(sorted(n))
        if len(n) == 2:
            known[n] = 1
        if len(n) == 4:
            known[n] = 4
        if len(n) == 3:
            known[n] = 7
        if len(n) == 7:
            known[n] = 8

    for n in numbers:
        n = ''.join(sorted(n))

        if n in known:
            continue

        match = 0.0
        for k in known:
            match += 1 if len(set(k) - set(n)) == 0 else (len(k)
                                                          - len(set(k) - set(n))) / len(k)

        match = int(match * 100)

        if match == 263:
            output[n] = 5
        if match == 238:
            output[n] = 2
        if match == 346:
            output[n] = 3
        if match == 385:
            output[n] = 9
        if match == 277:
            output[n] = 6
        if match == 360:
            output[n] = 0

    output.update(known)

    on = []
    for s in item[1].strip().split(' '):
        on.append(str(output[''.join(sorted(s))]))

    ans += int(''.join(on))


print('answer: ', ans)

# 983030
