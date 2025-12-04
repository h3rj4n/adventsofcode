import time


def convert_input_to_rolls(line_number: int, line: str) -> list:
    rolls = []
    for index, value in enumerate(line):
        if value == '@':
            rolls.append((line_number, index))

    return rolls


def access_paper_roll(rolls: set, position: tuple, remove: bool = False) -> bool:
    # There are 8 positions we need to check for a given roll.
    adjacent_positions = [
        (position[0] - 1, position[1] - 1),
        (position[0] - 1, position[1]),
        (position[0] - 1, position[1] + 1),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    ]
    # Count amount of positions contains a roll.
    count = 0
    for pos in adjacent_positions:
        if pos in rolls:
            count += 1
        if remove is False and count >= 4:
            return False

    if remove is True and count < 4:
        rolls.remove(position)

    return count < 4


def day_one_and_two(rolls: set, part='one') -> int:
    roll_len = 0
    output = 0

    while roll_len != len(rolls):
        roll_len = len(rolls)
        for roll in list(rolls):
            if access_paper_roll(rolls, roll, remove=(part == 'two')):
                output += 1

    return output


def main():
    start_time = time.time()
    rolls = set()
    with open("data.txt", encoding="utf-8") as f:
        for index, line in enumerate(f):
            new_line = convert_input_to_rolls(index, line.rstrip())
            rolls.update(new_line)

    print(
        f"Input processed in {time.time() - start_time:.4f}s")

    start_time = time.time()
    print(
        f"Part 1: {day_one_and_two(rolls)} (took {time.time() - start_time:.4f}s)")
    start_time = time.time()
    print(
        f"Part 2: {day_one_and_two(rolls, 'two')} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
