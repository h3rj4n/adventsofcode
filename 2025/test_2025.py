import pytest

import day_01
import day_02
import day_03


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


# @pytest.mark.parametrize("joltage,battery,expected", [
#     (12, 987654321111111, 987654321111),
#     (12, 811111111111119, 811111111119),
#     (12, 234234234234278, 434234234278),
#     (12, 818181911112111, 888911112111),
#     (12, 818181911112911, 888911112911),
# ])
# def test_day_03_analyze_override_bank(joltage, battery, expected):
#     assert day_03.analyze_override_bank(battery, joltage) == expected


def test_day_03_part_one():
    line = "987654321111111,811111111111119,234234234234278,818181911112111"
    assert day_03.part_one(line) == 357


def test_day_03_part_two():
    line = "987654321111111,811111111111119,234234234234278,818181911112111"
    assert day_03.part_two(line) == 3121910778619


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
