"""Advent of Code 2024: Day 3"""
import re

test_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

test_input_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def part_1(input_str):
    total = 0
    matches = re.findall(r'mul\([0-9]*,[0-9]*\)', input_str)
    for match in matches:
        nums = [int(x) for x in re.findall(r'[0-9]+', match)]
        total += nums[0] * nums[1]
    return total
            
def part_2(input_str):
    matches = re.findall(r'mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)', input_str)
    executing = True
    total = 0
    for match in matches:
        if match == 'do()':
            executing = True
        elif match == "don't()":
            executing = False
        elif executing:
            nums = [int(x) for x in re.findall(r'[0-9]+', match)]
            total += nums[0] * nums[1]
    return total

def main():
    with open('aoc_day_3_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input_2))
    print(part_2(full_input))

if __name__ == '__main__':
    main()