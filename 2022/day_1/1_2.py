import numpy as np

elfs = []

# Open the file
with open("1_data.txt") as f:
    elf = 0
    # Loop trough the records until you find a blank line
    for lines in f:
        if (lines.strip() == ""):
            elfs.append(elf)
            elf = 0
        else:
            elf += int(lines.strip())

sorted = np.flip(np.sort(elfs))
print(sorted[0] + sorted[1] + sorted[2])
