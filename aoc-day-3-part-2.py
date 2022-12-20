test_rucksacks = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# Gets the value of an individual character
# a-z get 1-26, 'A-Z' get 27-52
def char_value(char):
    ord_val = ord(char)
    if 97 <= ord_val <= 122:
        return ord_val - 96
    elif 65 <= ord_val <= 90:
        return ord_val - 38
    else:
        #uh-oh
        return -1
    
def check_rucksacks(rucksacks):
    total_value = 0
    for rucksack in rucksacks.split('\n'):
        midpoint = len(rucksack)//2
        char_set = set(rucksack[:midpoint])
        for char in rucksack[midpoint:]:
            if char in char_set:
                total_value += char_value(char)
                break # This assumes only one misplaced item
    return total_value
    
def check_badges(rucksacks, group_size=3):
    group_counter = 0
    total = 0
    elf_intersection = set()
    for line in rucksacks.split('\n'):
        group_counter += 1
        elf_set = set(line[:])
        if len(elf_intersection) == 0:
            elf_intersection.update(elf_set)
        else:
            elf_intersection = elf_intersection.intersection(elf_set)
        if(group_counter == group_size):
            badge = elf_intersection.pop()
            total += char_value(badge)
            group_counter = 0
    return total
    
        
print(check_badges(test_rucksacks))