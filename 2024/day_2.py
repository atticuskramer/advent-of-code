"""Advent of Code 2024: Day 1"""

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else: 
        return 0

def is_gradual(nums):
    """Returns True if the list of numbers in/decreases gradually, False otherwise
    
    A list of numbers increases or decreases gradually if all consecutive elements
    are increasing or all are decreasing, and each difference is between 1 and 3."""
    initial_sign = sign(nums[0] - nums[1])
    for i, num in enumerate(nums[:-1]):
        dif = num - nums[i+1]
        if abs(dif) > 3 or sign(dif) != initial_sign or sign(dif) == 0:
            return False
    return True

def part_1(input_str):
    safe_reports = 0
    for line in input_str.split('\n'):
        levels = [int(digit) for digit in line.split()]
        if is_gradual(levels):
            print('safe levels found', levels)
            safe_reports += 1
    return safe_reports
            

def part_2(input_str):
    pass

def main():
    with open('aoc_day_1_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()