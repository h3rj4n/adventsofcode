def check_report(values, assignment=1) -> bool:
    diff = [j-i for i, j in zip(values[:-1], values[1:])]
    if all(-3 <= v < 0 for v in diff) or all(3 >= v > 0 for v in diff):
        return True

    if assignment == 1:
        return False

    # Due to first if, this filter out the unsafe values.
    if all(v < 0 for v in diff) or all(v > 0 for v in diff):
        return False

    # It is allowed to have 1 zero in the list.
    if sum(x == 0 for x in diff) == 1:
        return True

    if sum(x < 0 for x in diff) == len(diff) - 1 or sum(x > 0 for x in diff) == len(diff) - 1:
        index = [i for i, x in enumerate(diff) if x > 0] if sum(x < 0 for x in diff) == len(diff) - 1 else [i for i, x in enumerate(diff) if x < 0]
        index = index[0]
        out = False
        for i in list([index, index + 1]):
            new = diff.copy()
            if len(new) < i:
                del new[i]
                if check_report(new, assignment=2):
                    out = True
                    break
        return out

    return False


count = 0
extra = 0
with open("input.txt", encoding="utf-8") as f:
    for line in f:
        values = list(map(int, line.rstrip().split(" ")))

        if check_report(values):
            count += 1
        elif check_report(values, 2):
            extra += 1

print("Part 1:", count)
print("Part 2:", count + extra)

# 730 to high
