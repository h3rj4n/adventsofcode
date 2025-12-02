import time


def process_range_part_one(start: int, stop: int) -> int:
    output = 0
    for i in range(start, stop + 1):
        # Split the number into 2 equal halves based on its length
        s = str(i)
        mid = len(s) // 2

        if s[:mid] == s[mid:]:
            output += i

    return output


def part_one(line):
    output = 0
    values = line.rstrip().split(",")
    for item in values:
        start, stop = item.split("-")
        output += process_range_part_one(int(start), int(stop))
    return output


def process_range_part_two(start: int, stop: int) -> int:
    output = 0
    for i in range(start, stop + 1):
        # Split the number into 2 equal halves based on its length
        s = str(i)
        mid = len(s) // 2

        for char_length in range(1, mid + 1):
            parts = [s[j:j+char_length] for j in range(0, len(s), char_length)]
            if len(set(len(part) for part in parts)) == 1 and len(set(parts)) == 1:
                output += i
                break

    return output


def part_two(line):
    output = 0
    values = line.rstrip().split(",")
    for item in values:
        start, stop = item.split("-")
        output += process_range_part_two(int(start), int(stop))

    return output


def main():
    with open("data.txt", encoding="utf-8") as f:
        for line in f:
            start_time = time.time()

            print(
                f"Part 1: {part_one(line)} (took {time.time() - start_time:.4f}s)")

            start_time = time.time()
            print(
                f"Part 2: {part_two(line)} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
