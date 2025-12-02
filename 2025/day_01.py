import time


def process_dial(start: int, rotation: str, part: str = 'one') -> (int, int):
    move = rotation[0]
    amount = int(rotation[1:])
    count = 0

    if part == "two":
        count += amount // 100
        amount = amount % 100

    new_pos = 0

    if move == "L":
        new_pos = (start - amount)
    elif move == "R":
        new_pos = (start + amount)

    if part == "two" and start != 0 and (new_pos < 0 or new_pos > 100):
        count += 1

    start = new_pos % 100
    count += 1 if start == 0 else 0

    return (start, count)


def day_one(line, part='one') -> int:
    output = 0
    values = line.rstrip().split(",")
    start = 50  # Starting position

    for rotation in values:
        start, count = process_dial(start, rotation, part)
        output += count

    return output


def main():
    with open("data.txt", encoding="utf-8") as f:
        contents = f.read().replace('\n', ',').rstrip(',')

        start_time = time.time()
        print(
            f"Part 1: {day_one(contents)} (took {time.time() - start_time:.4f}s)")
        start_time = time.time()
        print(
            f"Part 2: {day_one(contents, 'two')} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
