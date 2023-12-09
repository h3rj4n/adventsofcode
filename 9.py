import numpy

answer = 0
second_answer = 0

with open("9_data.txt") as f:
    for line in f:
        record = [int(n) for n in line.rstrip("\n").split(" ")]
        steps = []
        start = 0
        while len(steps) == 0 or len(set(steps[-1])) > 1:
            c = steps[-1] if len(steps) > 0 else record
            diff = numpy.diff(c)
            steps.append(diff)
            start = diff[0]

        answer += record[-1] + sum(s[-1] for s in reversed(steps))

        for s in reversed(steps[:-1]):
            start = s[0] - start

        second_answer += record[0] - start

print("Answer 1:", answer)
print("Answer 2:", second_answer)