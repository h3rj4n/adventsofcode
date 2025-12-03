import time


def analyze_bank(battery: int, joltage: int = 2) -> int:
    number = ''
    bank = str(battery)
    while len(number) < joltage:
        highest = 0
        high_index = -1
        pos = ((joltage - 1) - len(number)) * -1

        for index, digit in enumerate(bank[:pos] if pos != 0 else bank):
            if int(digit) > highest:
                highest = int(digit)
                high_index = index
                if highest == 9:
                    break
        bank = bank[high_index+1:]
        number += str(highest)

    return int(number)


def part_one_and_two(line, joltage) -> int:
    batteries = line.rstrip().split(",")
    output = 0

    for battery in batteries:
        output += analyze_bank(int(battery), joltage)

    return output


def main():
    with open("data.txt", encoding="utf-8") as f:
        contents = f.read().replace('\n', ',').rstrip(',')

        start_time = time.time()
        print(
            f"Part 1: {part_one_and_two(contents, 2)} (took {time.time() - start_time:.4f}s)")
        start_time = time.time()
        print(
            f"Part 2: {part_one_and_two(contents, 12)} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
