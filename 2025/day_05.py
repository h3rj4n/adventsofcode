import time


def create_fresh_ingredients(ingredients: str) -> tuple:
    fresh = ()
    items = ingredients.split(',')
    for item in items:
        start, stop = map(int, item.split('-'))
        fresh += ((start, stop),)

    return fresh


def part_one(ingredients: str, available_ingredients: str) -> int:
    fresh_ingredients = create_fresh_ingredients(ingredients)

    count = 0

    available_ingredients = available_ingredients.split(',')
    for item in available_ingredients:
        for start, stop in fresh_ingredients:
            if int(item) >= start and int(item) <= stop:
                count += 1
                break

    return count


def filter_fresh_ingredients_ranges(fresh_ingredients: str) -> tuple:
    fresh_len = 0
    fresh = ()
    items = fresh_ingredients.split(',')
    # Build the data.
    for item in items:
        start, stop = map(int, item.split('-'))
        fresh += ((start, stop),)

    # Filter overlapping ranges.
    while fresh_len != len(fresh):
        fresh_len = len(fresh)
        new_fresh = []
        skip_indices = set()
        for index_a, (start_a, stop_a) in enumerate(fresh):
            if index_a in skip_indices:
                continue
            for index_b, (start_b, stop_b) in enumerate(fresh):
                if index_a == index_b or index_b in skip_indices:
                    continue
                # Check for overlap.
                if start_a <= stop_b and stop_a >= start_b:
                    # Merge ranges.
                    new_start = min(start_a, start_b)
                    new_stop = max(stop_a, stop_b)
                    new_fresh.append((new_start, new_stop))
                    skip_indices.add(index_a)
                    skip_indices.add(index_b)
                    break
            else:
                if index_a not in skip_indices:
                    new_fresh.append((start_a, stop_a))
        fresh = tuple(new_fresh)

    return fresh


def part_two(ingredients: str) -> int:
    fresh_ingredients = filter_fresh_ingredients_ranges(ingredients)
    count = 0
    for start, stop in fresh_ingredients:
        count += (stop - start + 1)
    return count


def main():
    ingredients = []
    available_ingredients = []
    with open("data.txt", encoding="utf-8") as f:
        new_line_found = False
        for line in f:
            if line.strip() == "":
                new_line_found = True
                continue
            if not new_line_found:
                ingredients.append(line.strip())
            else:
                available_ingredients.append(line.strip())

    ingredients = ",".join(ingredients)
    available_ingredients = ",".join(available_ingredients)

    start_time = time.time()
    print(
        f"Part 1: {part_one(ingredients, available_ingredients)} (took {time.time() - start_time:.4f}s)")
    start_time = time.time()
    print(
        f"Part 2: {part_two(ingredients)} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
