# Get the data
f = open("1.1_data.txt")

slidingWindow = []

amountOfLines = 2000

# Loop trough the file, count each one that is bigger than previous reading.
for index, measurement in enumerate(f):
    if (len(slidingWindow) == index and amountOfLines-index > 2):
        # print("index: ", index)
        slidingWindow.insert(index, int(measurement))
        
    try:
        for i in [2, 1]:
            if (index-i >= 0 and len(slidingWindow) >= index-i):
                # print("current index: ", index, "add to index: ", index-i)
                slidingWindow[index-i] += int(measurement)
    except IndexError:
        pass

# The answer to our problem
answer = 0

# Keep track of previous measurement.
previous = None

for data in slidingWindow:
    if previous != None and previous < data:
        answer += 1

    previous = data

print(answer)
# 1728
