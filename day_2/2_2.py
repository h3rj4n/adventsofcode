score = 0

responses = {
    "A": {
        0: "Z",
        3: "X",
        6: "Y",
    },
    "B": {
        0: "X",
        3: "Y",
        6: "Z",
    },
    "C": {
        0: "Y",
        3: "Z",
        6: "X",
    }
}

ourInputScores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

with open("2_data.txt") as f:
    for lines in f:
        input = lines.strip().split(" ")

        match input[1]:
            case 'X':
                # We need to loose.
                val = responses[input[0]][0]
                score += ourInputScores[val]

            case 'Y':
                # We need a draw.
                val = responses[input[0]][3]
                score += ourInputScores[val] + 3

            case 'Z':
                # We need to win!
                val = responses[input[0]][6]
                score += ourInputScores[val] + 6


print(score)
