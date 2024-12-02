"""Advent of Code 2024: Day 1"""

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

def num_lists_from_input(input_str):
    list_1 = []
    list_2 = []
    for line in input_str.split('\n'):
        num_1, num_2 = [int(digit) for digit in line.split()]
        list_1.append(num_1)
        list_2.append(num_2)
    return list_1, list_2

def part_1(input_str):
    list_1, list_2 = num_lists_from_input(input_str)
    return sum(abs(a - b) for a,b in zip(sorted(list_1), sorted(list_2)))

def part_2(input_str):
    pass

def main():
    with open('aoc_day_1_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
