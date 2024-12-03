import numpy as np

# Import the data
with open("7_data.txt") as f:
    raw_data = f.read().strip().split(',')
    data = list(map(lambda x: int(x), raw_data))

x = np.array(data)
average = round(np.average(x))

print('the average: ', average, ' raw: ', np.average(x))

ans = 1 << 60
# Semi bruteforce this.
for _ in range(average - 5, average + 5):
    o = []

    for i in x:
        # Calculate the difference with the median.
        o.append(sum(range(0, int(abs(i - _) + 1))))

    tempAns = 0
    for a in o:
        tempAns += a

    if ans > tempAns:
        ans = tempAns

print('answer: ', ans)

# 94004217 (too high)
# 94004208
