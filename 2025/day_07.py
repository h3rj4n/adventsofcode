import time


def count_beam_splits(grid: str) -> int:
    rows = grid.split(',')

    beams = set()
    splits = 0

    for row in rows:
        if 'S' not in row and '^' not in row:
            continue

        for index, char in enumerate(row):
            if char == 'S':
                beams.add(index)
            elif char == '^' and index in beams:
                beams.discard(index)
                beams.add(index - 1)
                beams.add(index + 1)
                splits += 1

    return splits


def main():
    data = []
    with open("data/07.txt", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip())

    start_time = time.time()
    print(
        f"Part 1: {count_beam_splits(",".join(data))} (took {time.time() - start_time:.4f}s)")
    # start_time = time.time()
    # print(
    #     f"Part 2: {actually_solve_cephalopod_math(new_data)} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
