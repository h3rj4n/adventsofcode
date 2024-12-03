# Get the data
f = open("1.1_data.txt")

# The answer to our problem
answer = 0

# Keep track of previous measurement.
previous = None

# Loop trough the file, count each one that is bigger than previous reading.
for measurement in f:
    measurement = int(measurement)
    print(type(measurement))
    print(measurement)
    if previous != None and previous > measurement:
        answer += 1

    previous = measurement

print(answer)
# 1688
