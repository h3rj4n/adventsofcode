import pytest

import day_01
import day_02
import day_03
import day_04
import day_05
import day_06


@pytest.mark.parametrize("part,start,rotation,expected", [
    ('one', 50, "L68", (82, 0)),
    ('one', 82, "L30", (52, 0)),
    ('one', 52, "R48", (0, 1)),
    ('one', 0, "L5", (95, 0)),
    ('one', 95, "R60", (55, 0)),
    ('one', 55, "L55", (0, 1)),
    ('one', 0, "L1", (99, 0)),
    ('one', 99, "L99", (0, 1)),
    ('one', 0, "R14", (14, 0)),
    ('one', 14, "L82", (32, 0)),

    ('two', 50, "L68", (82, 1)),
    ('two', 82, "L30", (52, 0)),
    ('two', 52, "R48", (0, 1)),
    ('two', 0, "L5", (95, 0)),
    ('two', 95, "R60", (55, 1)),
    ('two', 55, "L55", (0, 1)),
    ('two', 0, "L1", (99, 0)),
    ('two', 99, "L99", (0, 1)),
    ('two', 0, "R14", (14, 0)),
    ('two', 14, "L82", (32, 1)),

    ('two', 50, "R1000", (50, 10)),
])
def test_day_01_process_dial_part_one(part, start, rotation, expected):
    assert day_01.process_dial(start, rotation, part) == expected


@pytest.mark.parametrize("part,expected", [
    ('one', 3),
    ('two', 6),
])
def test_day_01_day_one_part_one(part, expected):
    line = "L68,L30,R48,L5,R60,L55,L1,L99,R14,L82"
    assert day_01.day_one(line, part) == expected


@pytest.mark.parametrize("start,stop,expected", [
    (11, 22, 33),
    (95, 115, 99),
    (1188511880, 1188511890, 1188511885),
    (222220, 222224, 222222),
    (1698522, 1698528, 0),
    (446443, 446449, 446446),
    (38593856, 38593862, 38593859),
    (2121212118, 2121212124, 0),
])
def test_day_02_process_range_part_one(start, stop, expected):
    assert day_02.process_range_part_one(start, stop) == expected


def test_day_02_part_one():
    line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # You can add assertions here based on the expected behavior of part_one
    # For example:
    assert day_02.part_one(line) == 1227775554


@pytest.mark.parametrize("start,stop,expected", [
    (11, 22, 33),
    (95, 115, 99+111),
    (998, 1012, 999+1010),
    (1188511880, 1188511890, 1188511885),
    (222220, 222224, 222222),
    (1698522, 1698528, 0),
    (446443, 446449, 446446),
    (38593856, 38593862, 38593859),
    (565653, 565659, 565656),
    (824824821, 824824827, 824824824),
    (2121212118, 2121212124, 2121212121),
])
def test_day_02_process_range_part_two(start, stop, expected):
    assert day_02.process_range_part_two(start, stop) == expected


def test_day_02_part_two():
    line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # You can add assertions here based on the expected behavior of part_one
    # For example:
    assert day_02.part_two(line) == 4174379265


@pytest.mark.parametrize("joltage,battery,expected", [
    (2, 987654321111111, 98),
    (2, 811111111111119, 89),
    (2, 234234234234278, 78),
    (2, 818181911112111, 92),
    (2, 818181911112911, 99),

    (12, 987654321111111, 987654321111),
    (12, 811111111111119, 811111111119),
    (12, 234234234234278, 434234234278),
    (12, 818181911112111, 888911112111),
    (12, 818181911112911, 888911112911),
])
def test_day_03_analyze_bank(joltage, battery, expected):
    assert day_03.analyze_bank(battery, joltage) == expected


def test_day_03_part_on_and_two():
    line = "987654321111111,811111111111119,234234234234278,818181911112111"
    assert day_03.part_one_and_two(line, 2) == 357
    assert day_03.part_one_and_two(line, 12) == 3121910778619


@pytest.mark.parametrize("rolls,position,expected", [
    ({(0, 0), (0, 1), (1, 0)}, (1, 1), True),
    ({(0, 0), (0, 1), (1, 0), (1, 2)}, (1, 1), False),
    ({(1, 2), (2, 3), (3, 2), (3, 3)}, (2, 2), False),
    (set(), (0, 0), True),
])
def test_day_04_access_paper_roll(rolls, position, expected):
    assert day_04.access_paper_roll(rolls, position) == expected


def test_day_04_convert_input_to_rolls():
    line_number = 2
    line = "..@@.@@@@.@"
    expected = [(2, 2), (2, 3), (2, 5), (2, 6), (2, 7), (2, 8), (2, 10)]
    assert day_04.convert_input_to_rolls(line_number, line) == expected


def test_day_04_day_one_and_two():
    rolls = set()
    data = "..@@.@@@@.,@@@.@.@.@@,@@@@@.@.@@,@.@@@@..@.,@@.@@@@.@@,.@@@@@@@.@,.@.@.@.@@@,@.@@@.@@@@,.@@@@@@@@.,@.@.@@@.@."
    for index, line in enumerate(data.split(",")):
        new_line = day_04.convert_input_to_rolls(index, line.rstrip())
        rolls.update(new_line)

    assert day_04.day_one_and_two(rolls) == 13
    assert day_04.day_one_and_two(rolls, 'two') == 43


@pytest.mark.parametrize("range,expected", [
    ('3-5,10-14', ((3, 5), (10, 14))),
    ('16-20,12-18', ((16, 20), (12, 18))),
])
def test_day_05_create_fresh_ingredients(range, expected):
    assert day_05.create_fresh_ingredients(range) == expected


def test_day_05_part_one():
    ingredients = "3-5,10-14,16-20,12-18"
    available_ingredients = "1,5,8,11,17,32"
    assert day_05.part_one(ingredients, available_ingredients) == 3


def test_day_05_filter_fresh_ingredients_ranges():
    fresh_ingredients = "3-5,10-14,16-20,12-18"
    expected = ((3, 5), (10, 20))
    assert day_05.filter_fresh_ingredients_ranges(
        fresh_ingredients) == expected


def test_day_05_part_two():
    ingredients = "3-5,10-14,16-20,12-18"
    assert day_05.part_two(ingredients) == 14


def test_day_06_solve_cephalopod_math_to_normal():
    math_expression = [
        [123, 328,  51, 64],
        [45, 64,  387, 23],
        [6, 98,  215, 314],
        ['*', '+', '*', '+']
    ]
    assert day_06.solve_cephalopod_math_to_normal(
        math_expression) == 4277556


def test_day_06_process_str_data():
    str_data = [
        "123 328  51 64    4",
        " 45 64  387 23    7",
        "  6 98  215 314 424",
        "*   +   *   +   *",
    ]
    expected = [
        ['123', '328', ' 51', '64 ', '  4'],
        [' 45', '64 ', '387', '23 ', '  7'],
        ['  6', '98 ', '215', '314', '424'],
        ['*  ', '+  ', '*  ', '+  ', '*'],
    ]
    assert day_06.process_str_data(str_data) == expected


def test_day_06_actually_solve_cephalopod_math():
    math_expression = [
        ['123', '328', ' 51', '64 '],
        [' 45', '64 ', '387', '23 '],
        ['  6', '98 ', '215', '314'],
        ['*  ', '+  ', '*  ', '+  ']
    ]
    assert day_06.actually_solve_cephalopod_math(
        math_expression) == 3263827
