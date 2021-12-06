# Import the data
f = open("6_data.txt")

fishes = f.readline().rstrip('\n').split(',')
fishes = list(map(lambda x: int(x), fishes))

days = 256

for x in range(0, days):
    newlyBorns = 0
    # Loop trough all the fishes.
    for index, fish in enumerate(fishes):
        if fish == 0:
            # Rest the timer
            fishes[index] = 6
            # Create a new fish.
            newlyBorns += 1
        else:
            # Decrease on of the fish.
            fishes[index] = fish - 1
    for i in range(0, newlyBorns):
        fishes.append(8)

print('asnwer: ', len(fishes))

# 553267 (too high)
# 231817 (too low)
# 333438 (too low)
# 389726
