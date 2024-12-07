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
    rules_str, updates_str = input_str.split('\n\n')
    rules = [[int(num) for num in rule.split('|')] for rule in rules_str.split('\n')]
    updates = [[int(num_str) for num_str in update.split(',')] for update in updates_str.split('\n')]
    corrected_middles = 0
    # Create a dictionary with the 'before' numbers as keys, and sets of all
    # corresponding 'after' numbers as values 
    rule_dict = dict()
    for before, after in rules:
        if before in rule_dict:
            rule_dict[before].add(after)
        else:
            rule_dict[before] = set([after])
    # For each update, create a new list and copy over the items, keeping them
    # sorted as we go.
    for update in updates:
        corrected = []
        for page in update:
            i = 0
            while i < len(corrected) and page in rule_dict.get(corrected[i], set()):
                i += 1
            corrected.insert(i, page)
        # If the corrected list is the same as the original list, don't include
        # it in our sum.
        # We could improve efficiency by abstracting out the check for a sorted
        # list from part 1 and checking if sorted before resorting, but this is
        # asymptotically the same, so meh
        if corrected != update:
            corrected_middles += corrected[len(corrected)//2]
    return corrected_middles
            
    

def main():
    with open('aoc_day_5_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
