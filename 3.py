import re
from itertools import islice

lines = []

with open("3_data.txt") as f:
    for line in f:
        lines.append(line)

answer = 0

for line_index, line in enumerate(lines):
    m = re.finditer('(\d+)', line)
    for mm in m:
        start_index = 0 if mm.start(0) - 1 < 0 else mm.start(0) - 1
        end_index = len(line) - 1 if mm.end(0) + 1 > len(line) - 1 else mm.end(0) + 1

        for line_search in [line_index - 1, line_index, line_index + 1]:
            if line_search < 0 or line_search >= len(lines):
                continue

            matches = bool(re.search(r"([^.0-9a-zA-Z])", lines[line_search][start_index:end_index]))
            if matches:
                answer += int(mm.group(0))

print("Part 1:", answer)


answer = 0

for line_index, line in enumerate(lines):
    m = re.finditer('(\*)', line)
    for mm in m:
        start_index = 0 if mm.start(0) - 1 < 0 else mm.start(0) - 1
        end_index = len(line) - 1 if mm.end(0) + 1 > len(line) - 1 else mm.end(0) + 1

        count_matches = 0
        adjecent = []
        for line_search in [line_index - 1, line_index, line_index + 1]:
            if line_search < 0 or line_search >= len(lines):
                continue

            star_matches = re.finditer(r"([0-9]+)", lines[line_search][start_index:end_index])

            for mz in star_matches:
                count_matches += 1
                all_numbers = re.finditer('(\d+)', lines[line_search])
                for s_number in all_numbers:
                    if s_number.start(0) <= start_index + mz.start(0) <= s_number.end(0):
                        adjecent.append(int(s_number.group(0)))

        if count_matches == 2:
            answer += adjecent[0] * adjecent[1]


print("Part 2:", answer)


