"""Advent of Code 2024: Day 7"""
import re

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def can_make_add_mult(goal, parts):
    """Determine if goal can be made with the numbers in parts using +/*"""

    # We will do this recursively, combining the first two members of parts
    # with both addition and multiplication and then checking if we can make
    # goal using the new parts lists

    # If we are down to just one number in the list, it must be goal to be true
    if len(parts) == 1:
        return goal == parts[0]
    # If the first number in parts is larger than the goal, there is definitely
    # no way to get back down to goal
    if parts[0] > goal:
        return False
    # Otherwise, do our operations and check the new lists
    return (can_make_add_mult(goal, [parts[0] * parts[1]] + parts[2:]) 
            or can_make_add_mult(goal, [parts[0] + parts[1]] + parts[2:]))
    

def part_1(input_str):
    """Return sum of numbers that can be created using + and * with the
    given operators
    
    For now, we will just brute force this, since the most operators in the
    full input seems to be 10, requiring a maximum of 1024 checks"""
    lines = input_str.split('\n')
    total = 0
    for line in lines:
        goal_str, nums_str = line.split(':')
        goal = int(goal_str)
        nums = [int(num_str) for num_str in re.findall(r'[0-9]+', nums_str)]
        if can_make_add_mult(goal, nums):
            total += goal
    return total

            
def part_2(input_str):
    pass
            
def main():
    with open('aoc_day_7_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
