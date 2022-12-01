# Open the file
with open("1_data.txt") as f:
    answer = 0
    elf = 0
    # Loop trough the records until you find a blank line
    for lines in f:
        if (lines.strip() == ""):
            answer = elf if answer < elf else answer
            elf = 0
        else:
            elf += int(lines.strip())

print(answer)
