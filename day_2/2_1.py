score = 0

with open("2_data.txt") as f:
    for lines in f:
        input = lines.strip().split(" ")

        match input[0]:
            case 'A':
                if input[1] == 'X':
                    # A draw
                    score += 3
                elif input[1] == 'Y':
                    # A win
                    score += 6
                else:
                    # Lost
                    score += 0
            case 'B':
                if input[1] == 'Y':
                    # A draw
                    score += 3
                elif input[1] == 'Z':
                    # A win
                    score += 6
                else:
                    # Lost
                    score += 0

            case 'C':
                if input[1] == 'Z':
                    # A draw
                    score += 3
                elif input[1] == 'X':
                    # A win
                    score += 6
                else:
                    # Lost
                    score += 0

        # Now ad the value of our input.
        if input[1] == 'X':
            score += 1
        elif input[1] == 'Y':
            score += 2
        elif input[1] == 'Z':
            score += 3

print(score)
