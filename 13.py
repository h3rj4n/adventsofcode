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
                # print("join", "".join(left[:min_lenght]))
                # print("join", "".join(right[:min_lenght]))
                if "".join(left[:min_lenght]) == "".join(right[:min_lenght]):
                    return mid
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
        print(line.strip("\n"))
        if line.strip("\n") != "":
            x.append(line.strip("\n"))
            if len(y) == 0:
                y = [""] * len(line.strip("\n"))
            try:
                for i, char in enumerate(line.strip("\n")):
                    # try:
                        y[i] += line[i]
            except IndexError:
                print(len(y))
                print(line)
                break

        if line.strip("\n") == "":
            print("Start mirror")
            # We have a full "image". Let's find the right index.
            # print("X", int(len(x) / 2 - 2))
            # for i in range(0, max(len(x), len(y))):
            #     try:
            # Check the X.
            # print('wo', x)
            # print("check x")
            the_x = check_full_map(x)
            if the_x > 0:
                answer += (the_x + 1) * 100
                print("x", the_x)
                continue
            # Check the Y.
            # print("check y")
            the_y = check_full_map(y)
            if the_y > 0:
                answer += (the_y + 1)
                print("y", the_y)
                continue
            #     except IndexError:
            #         pass
                
            # print("X", x, len(x))
            # print("Y", y, len(y))
            # Reset
            x = []
            y = []

print("Answer 1:", answer)