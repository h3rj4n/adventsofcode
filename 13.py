x = []
y = []

def check_full_map(x):
    mid = int(len(x) / 2)
    c = 1
    while mid >= 0 and mid <= len(x):
        try:
            if x[mid] == x[mid+1]:
                left = list(reversed(x[:mid+1]))
                right = x[mid+1:]
                min_lenght = min(len(left), len(right))
                if "".join(left[:min_lenght]) == "".join(right[:min_lenght]):
                    return mid + 1
        except IndexError:
            pass
        mid += c
        if c % 2 == 0:
            c = (c * -1) + 1
        else:
            c = (c + 1) * -1

    return 0

answer = 0

with open("13_data.txt") as f:
    for index, line in enumerate(f):
        if line.strip("\n") != "":
            x.append(line.strip("\n"))
            if len(y) == 0:
                y = [""] * len(line.strip("\n"))
            try:
                for i, char in enumerate(line.strip("\n")):
                    y[i] += line[i]
            except IndexError:
                break

        if line.strip("\n") == "":
            found = False
            the_x = check_full_map(x)
            if the_x > 0 and found is False:
                answer += the_x * 100
                found = True

            the_y = check_full_map(y)
            if the_y > 0 and found is False:
                answer += the_y
                found = True

            # Reset
            x = []
            y = []

print("Answer 1:", answer)