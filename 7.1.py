import numpy as np

# Import the data
with open("7_data.txt") as f:
    raw_data = f.read().strip().split(',')
    data = list(map(lambda x: int(x), raw_data))

x = np.array(data)
median = np.median(x)

print('the median: ', median)

o = []

for i in x:
    # Calculate the difference with the median.
    o.append(abs(i - median))

ans = 0
for a in o:
    ans += a

print('answer: ', ans)

# 342534
