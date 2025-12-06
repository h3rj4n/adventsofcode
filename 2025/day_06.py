import time


def process_str_data(data: list[str]) -> list[list]:
    """Process string data into a list of lists.
    """

    subsets = []
    start = -1
    end = max(len(line) for line in data)
    for index in range(end):
        char = data[-1][index] if index < len(data[-1]) else ' '

        if char != ' ':
            if start != -1:
                subsets.append((start, index - 1))
            start = index

        if index == end - 1:
            subsets.append((start, index + 1))

    output = []
    for line in data:
        new_data = []
        for start, stop in subsets:
            new_data.append(line[start:stop])

        output.append(new_data)

    return output


def calculate_math(operator: str, number_list: list[int]) -> int:
    """Calculate a math expression based on the operator and number list.
    """

    if operator == '+':
        return sum(number_list)
    elif operator == '*':
        product = 1
        for number in number_list:
            product *= number
        return product


def solve_cephalopod_math_to_normal(math_expression: list[list]) -> int:
    """Solve cephalopod math expression to normal math expression.
    """

    # Use zip and unpacking
    columns = [list(col) for col in zip(*math_expression)]

    output = 0

    for col in columns:
        # The last item contains the operature, pop it.
        operator = col.pop()
        output += calculate_math(operator, list(map(int, col)))

    return output


def actually_solve_cephalopod_math(math_expression: list[list[str]]) -> str:
    columns = [list(col) for col in zip(*math_expression)]

    output = 0

    for col in columns:
        operator = col.pop().strip()
        math_list = []
        # Get the max char length in dhe list.
        max_length = len(col[0])

        for _i in range(max_length):
            i = max_length - _i - 1
            the_number = ''
            for item in col:
                # Get the last character of the item.
                the_number += item[i:i+1]

            if len(the_number.strip()) > 0:
                math_list.append(int(the_number))

        output += calculate_math(operator, math_list)

    return output


def main():
    data = []
    str_data = []
    with open("data/06.txt", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip().split())
            str_data.append(line.strip())

    new_data = process_str_data(str_data)

    start_time = time.time()
    print(
        f"Part 1: {solve_cephalopod_math_to_normal(data)} (took {time.time() - start_time:.4f}s)")
    start_time = time.time()
    print(
        f"Part 2: {actually_solve_cephalopod_math(new_data)} (took {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    main()
