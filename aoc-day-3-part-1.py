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
        
print(check_rucksacks(test_rucksacks))