from collections import OrderedDict

answer = 0
boxes = [OrderedDict() for x in range(256)]

with open("15_data.txt") as f:
    for line in f:
        for group in line.strip("\n").split(","):
            ans = 0
            second_ans = 0
            label = ''
            action = ''
            lens = None
            for char in group:
                ans = ((ans + ord(char)) * 17) % 256

                if char.isalpha():
                    label += char
                    second_ans = ((second_ans + ord(char)) * 17) % 256
                elif char == '=' or char == '-':
                    action = 'add' if char == '=' else 'remove'
                elif char.isalnum():
                    lens = char

            if action == 'add':
                boxes[second_ans][label] = lens
            if action == "remove":
                try:
                    del boxes[second_ans][label]
                except KeyError:
                    pass

            answer += ans

print("Answer 1:", answer)

answer = 0
for i, box in enumerate(boxes):
    for pos, item in enumerate(box):
        answer += (i + 1) * (pos + 1) * int(box[item])

print("Answer 2:", answer)
