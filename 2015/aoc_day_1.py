"""Advent of Code: 2015, Day 1"""

PART_1_TEST_PAIRS = [
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3)
]

PART_2_TEST_PAIRS = [
    (')', 1),
    ('(()))', 5),
    ('())((', 3),
    ('())(())))', 3)
]

def climb_floors(instr_str):
    """Return the number of '(' in instr_str - the number of ')'"""
    return instr_str.count('(') - instr_str.count(')')

def get_basement_position(instr_str):
    """Returns the index of the first character that causes the sum to go to -1"""
    floor = 0
    for i, char in enumerate(instr_str):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1
    # If we get through the whole input without entering the basement, return -1
    return -1


def test(func, test_pairs):
    """Tests the inputs/outputs provided in test_pairs. Returns nothing"""
    for test_str, output in test_pairs:
        assert func(test_str) == output

def main():
    """Main method"""
    test(climb_floors, PART_1_TEST_PAIRS)
    test(get_basement_position, PART_2_TEST_PAIRS)
    with open('aoc_day_1_input.txt', encoding='utf-8') as input_file:
        full_input = input_file.read()
    print(f'Ending floor: {climb_floors(full_input)}')
    print(f'First Basement Instruction: {get_basement_position(full_input)}')

if __name__ == '__main__':
    main()
