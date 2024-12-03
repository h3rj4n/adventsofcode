# Import the data
with open("8_data.txt") as f:
    data = []
    for l in f:
        data.append(l.strip().split('|')[1])

    # data = list(map(lambda x: int(x), raw_data))
ans = 0
for item in data:
    for n in item.split(' '):
        if (len(n) in [2, 3, 4, 7]):
            ans += 1

print('answer: ', ans)
