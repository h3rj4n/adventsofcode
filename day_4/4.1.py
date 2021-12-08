import re

f = open("4_data.txt")
# f = open("4_example_data.txt")

# Read the first line, the bingo numbers
numbers = f.readline()

# The next line is an empty line.
f.readline()

bingoCards = []

class bingoCard:
    def __init__(self):
        # Keep track of all the rows on the bingo card
        self.lines = []
        self.cols = []
        # Keep track if this one has a winner
        self.winner = False
        # Stash the last numer
        self.number = None

    """ Add a row the the bingo card """
    def addRow(self, row):
        # Remove empty items.
        # items = list(filter(lambda x: x != '', row.split(' ')))
        # Convert all values to ints
        items = list(map(lambda x: int(x), row.split(' ')))
        self.lines.append(items)

        # Create column lines
        for index, n in enumerate(items):
            if len(self.cols) <= index:
                self.cols.append([])

            self.cols[index].append(n)

    def amountOfRows(self):
        return len(self.lines)

    def printRows(self):
        return self.lines

    """ Check if number exists in any row """
    def checkNumber(self, number):
        self.number = int(number)
        for index, line in enumerate(self.lines):
            self.lines[index] = set(self.lines[index]).difference([self.number])

            # Mark as winner when array length is 0.
            if len(self.lines[index]) == 0:
                self.winner = True
                break

        for index, line in enumerate(self.cols):
            self.cols[index] = set(self.cols[index]).difference([self.number])

            # Mark as winner when array length is 0.
            if len(self.cols[index]) == 0:
                self.winner = True
                break

        return self

    """ Check if we have a winner """
    def hasWinner(self):
        return self.winner

    """ Get the results """
    def calculateResult(self):
        # Calculate the results.
        calculated = 0
        # 1. Sum all the unmarked numbers.
        for line in self.lines:
            for n in line:
                calculated += n

        # 2. Times the last number that resulted in bingo.
        return calculated * self.number


# Every 6 lines (last is an empty line) is a new bingo card.
for index, line in enumerate(f):
    bIndex = index // 6

    if len(bingoCards) < bIndex + 1:
        bingoCards.append(bingoCard())

    line = line.rstrip('\n')
    # Remove double spaces from the string.
    line = re.sub(' +', ' ', line).lstrip()

    if len(line) > 0:
        # print(bIndex, ' line data ', line)
        bingoCards[bIndex].addRow(line)

    # Debug code!
    # if (index > 16):
    #     break

# for c in bingoCards:
#     print(c.amountOfRows())

winnerBingo = None

for n in numbers.split(','):
    winner = False
    for card in bingoCards:
        winner = card.checkNumber(n).hasWinner()

        # Stop when we have a winner.
        if winner:
            print('We have a winner! Last number: ', n)
            winnerBingo = card
            break

    # Stop when we have a winner.
    if winner:
        break

print('answer: ', winnerBingo.calculateResult())

# Wrong: 5870087 (too high)
# Wrong: 88803 (too high)
# Wrong: 58764 (too high)
