from heapq import heappop, heappush
from collections import defaultdict

data = []
with open("17_data.txt") as f:
    for index, line in enumerate(f.read().split("\n")):
        if line.strip("\n"):
            data.append([])
            for char in line:
                data[index].append(int(char))
            # print(line)

queue = [(0, 0, "R", -1)]
# queue_finder = {}

end = (len(data[0]) - 1, len(data) - 1)

move = {
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
    "U": (0, -1),
}

disable_back = {
    "R": "L",
    "L": "R",
    "D": "U",
    "U": "D"
}

total_heat = defaultdict(lambda: 1000000)
total_heat[queue[0]] = 0

min_value = 10000000

# while len(queue) > 0:
#     _t = heappop(queue)
#     x, y, direction, consecutive = _t

#     if (x, y) == end:
#         if total_heat[_t] < min_value:
#             min_value = total_heat[_t]
#         continue

#     for new_direction in ["R", "L", "U", "D"]:
#         if disable_back[direction] == new_direction:
#             continue
#         new_consecutive = 0 if new_direction != direction else consecutive + 1
#         if new_consecutive >= 3:
#             continue
#         add_x, add_y = move[new_direction]
#         new_x, new_y = x + add_x, y + add_y
#         # Check out of bound.
#         if 0 <= new_x <= end[0] and 0 <= new_y <= end[1]:
#             new_t = (new_x, new_y, new_direction, new_consecutive)
#             new_heat = total_heat[_t] + int(data[new_y][new_x])
#             if new_heat < total_heat[new_t]:
#                 total_heat[new_t] = new_heat
#                 heappush(queue, new_t)

# print("Answer 1:", min_value)

queue = [(0, 0, "R")]
total_heat = defaultdict(lambda: 1000000)
total_heat[queue[0]] = 0

min_value = 10000000

count = 0
while len(queue) > 0:
    count += 1
    _t = heappop(queue)
    x, y, direction = _t

    if (x, y) == end:
        # print('At end!')
        if total_heat[_t] < min_value:
            min_value = total_heat[_t]
        continue

    for new_direction in ["R", "L", "U", "D"]:
        if disable_back[direction] == new_direction or (new_direction == direction and (x, y) != (0, 0)):
            continue
        add_x, add_y = move[new_direction]

        if 0 <= x + add_x <= end[0] and 0 <= y + add_y <= end[1]:
            for i in range(4, 10):
                if add_x and 0 <= x + i <= end[0]:
                    new_x = x + i
                    new_heat = total_heat[_t] + sum(data[y][x:new_x])
                    new_t = (new_x, y, new_direction)
                    if new_heat < total_heat[new_t]:
                        total_heat[new_t] = new_heat
                        heappush(queue, new_t)

                if add_y and 0 <= y + i <= end[0]:
                    new_y = y + i
                    new_heat = total_heat[_t] + sum([data[_y][x] for _y in range(y, new_y)])
                    new_t = (x, new_y, new_direction)
                    if new_heat < total_heat[new_t]:
                        total_heat[new_t] = new_heat
                        heappush(queue, new_t)

                # @todo!
                # pass
    # break




        # print(direction, new_consecutive)
        # if direction != new_direction or new_consecutive == 0:
        #     add_x = add_x * 4
        #     add_y = add_y * 4
        # new_x, new_y = x + add_x, y + add_y
        # # Check out of bound.
        # if 0 <= new_x <= end[0] and 0 <= new_y <= end[1]:
        #     # print(new_direction, (x, y), (new_x, new_y))
        #     new_t = (new_x, new_y, new_direction, new_consecutive)
        #     coords = list(zip((x, y), (new_x, new_y)))
        #     move_x, move_y = list(set(coords[0])), list(set(coords[1]))
        #     move_x.sort()
        #     move_y.sort()
        #     range_x_y = [move_x[0], move_x[1]] if len(move_x) == 2 else [move_y[0], move_y[1]]
        #     new_heat = total_heat[_t]
        #     # print("range", range_x_y)
        #     for i in range(range_x_y[0], range_x_y[1]):
        #         if len(move_x) == 2:
        #             # print((i, new_y), int(data[new_y][i]))
        #             new_heat += int(data[new_y][i])
        #         if len(move_y) == 2:
        #             # print((new_x, i), int(data[i][new_x]))
        #             new_heat += int(data[i][new_x])

        #     # print(coords[0])
        #     # print(new_direction, (x, y), (new_x, new_y), new_heat)
        #     # new_heat = total_heat[_t] + int(data[new_y][new_x])
        #     if new_heat < total_heat[new_t]:
        #         total_heat[new_t] = new_heat
        #         heappush(queue, new_t)

    # if count > 2:
    #     break

print("Answer 2:", min_value)

