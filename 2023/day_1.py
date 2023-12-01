"""Advent of Code 2023: Day 1"""

def get_digits(stringy):
    """Returns a list of all digit strings in the given string"""
    digits = [c for c in stringy if c.isdigit()]
    return digits

def get_digits_spelled(stringy):
    """Same as get_digits, but also counts spelled out words for digits (e.g. 'one')"""
    SPELLED_DIGITS = {
        # zero isn't allowed in the spelled digits
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    digits = []
    for idx in range(len(stringy)):
        if stringy[idx].isdigit():
            digits.append(stringy[idx])
        for spelled_digit in SPELLED_DIGITS:
            if stringy[idx:].startswith(spelled_digit):
                digits.append(SPELLED_DIGITS[spelled_digit])
    return digits

def num_from_first_and_last(digit_string_list):
    return int(digit_string_list[0] + digit_string_list[-1])

def part_1(input_str):
    calibration_values = []
    for line in input_str.split('\n'):
        digits = get_digits(line)
        calibration_values.append(num_from_first_and_last(digits))
    return sum(calibration_values)

def part_2(input_str):
    calibration_values = []
    for line in input_str.split('\n'):
        digits = get_digits_spelled(line)
        calibration_values.append(num_from_first_and_last(digits))
    return sum(calibration_values)

def main():
    with open('aoc_day_1_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(full_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
