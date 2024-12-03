import re

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

answer = 0

with open("2_data.txt") as f:
    for line in f:
        g = re.search(r"Game ([0-9]+):", line)
        game = int(g.group(1))

        t = re.findall(r"(\d{2,}) (red|green|blue)", line)
        if t:
            for find in t:
                if int(find[0]) > max_cubes[find[1]]:
                    game = 0
                    break

        answer += game

print("Part 1:", answer)

answer = 0

with open("2_data.txt") as f:
    for line in f:
        red = list(map(int, re.findall(r"(\d*) red", line)))
        green = list(map(int, re.findall(r"(\d*) green", line)))
        blue = list(map(int, re.findall(r"(\d*) blue", line)))

        red.sort(reverse=True)
        green.sort(reverse=True)
        blue.sort(reverse=True)

        answer += (red[0] * green[0] * blue[0])

print("Part 2:", answer)
