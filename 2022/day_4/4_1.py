answer = 0

with open("4_data.txt") as f:
    for line in f:
        [aa, ab], [ba, bb] = sorted([[ int(x) for x in i.split('-')] for i in line.strip().split(',')], key=lambda x: x[0])

        if aa == ba and ab <= bb or aa <= ba and ab >= bb:
            answer += 1

print(answer)