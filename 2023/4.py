import re

answer = 0

with open("4_data.txt") as f:
    for line in f:
        m = re.search(r": ([0-9 ]+) \| ([0-9 ]+)", line)
        winning = [int(n) for n in m.group(1).split(" ") if n]
        my_numbers = [int(n) for n in m.group(2).split(" ") if n]
        matches = 0
        for my_n in my_numbers:
            if my_n in winning:
                matches = matches * 2 if matches > 0 else matches + 1

        answer += matches

print("Part 1:", answer)


answer = 0
cards = {}

with open("4_data.txt") as f:
    for line in f:
        m = re.search(r"Card[ ]+([0-9]+): ([0-9 ]+) \| ([0-9 ]+)", line)
        card_number = int(m.group(1))

        if card_number not in cards.keys():
            cards[card_number] = 0

        cards[card_number] += 1

        winning = [int(n) for n in m.group(2).split(" ") if n]
        my_numbers = [int(n) for n in m.group(3).split(" ") if n]
        matches = 0
        for my_n in my_numbers:
            if my_n in winning:
                matches += 1

                if card_number + matches not in cards.keys():
                    cards[card_number + matches] = 0

                cards[card_number + matches] += cards[card_number]

        answer += cards[card_number]

print("Part 2:", answer)