answer = 0

with open("3_data.txt") as f:
    # Read the first line.
    for line in f:
        input = line.strip()
        x = len(input)
        firstpart, secondpart = input[:x//2], input[x//2:]

        found = False

        for char in firstpart:
            # Search for the char in the second string.
            if secondpart.find(char) >= 0 and found == False:
                found = True
                # Convert the char to int.
                c = ord(char)

                if c > 96:
                    answer += c - 96
                else:
                    answer += c - 38

print(answer)
