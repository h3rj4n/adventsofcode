from collections import defaultdict

# Import the data
f = open("6_data.txt")

data = f.readline().rstrip('\n').split(',')
fishes = defaultdict(int)

for i in data:
    fishes[int(i)] += 1

days = 256

for _ in range(days):
    # Create a new dictionary to copy the values.
    clone_fishes = defaultdict(int)

    for n in fishes:
        # Create a new fish.
        if n == 0:
            # Reset the current fish.
            clone_fishes[6] += fishes[n]
            clone_fishes[8] = fishes[n]
        else:
            clone_fishes[n - 1] += fishes[n]

    fishes = clone_fishes

ans = 0
for n in fishes:
    ans += fishes[n]
print('answer: ', ans)

# 1743335992042
