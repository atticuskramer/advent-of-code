"""Advent of Code 2024: Day 5"""

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def part_1(input_str):
    rules_str, updates_str = input_str.split('\n\n')
    rules = [[int(num) for num in rule.split('|')] for rule in rules_str.split('\n')]
    updates = [[int(num_str) for num_str in update.split(',')] for update in updates_str.split('\n')]
    correct_middles = 0
    for update in updates:
        valid = True
        # Record the position of each page in the update
        page_positions = {num:i for i, num in enumerate(update)}
        # Check that each rule is followed
        for before, after in rules:
            # If a rule is broken, mark this update as invalid and stop checking rules
            if (before in page_positions and after in page_positions
               and page_positions[before] > page_positions[after]):
                valid = False
                break
        # If all rules were followed, add the middle element to our total
        if valid:
            correct_middles += update[len(update)//2]
    return correct_middles
            
def part_2(input_str):
    pass

def main():
    with open('aoc_day_5_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
