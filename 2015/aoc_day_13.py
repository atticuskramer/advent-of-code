"""Advent of Code: 2015, Day 13"""

def make_happiness_dict(input_str):
    """Returns a dictionary detailing happiness relations
    
    The dictionary is nested, where given strings person_a and person_b,
    dict[person_a][person_b] is an int denoting the change in happiness
    person_a experiences from being seated next to person_b. Note that
    these relationships are NOT expected to be symmetric"""
    happiness_dict = {}
    for line in input_str.split('\n'):
        words = line.split()
        person = words[0]
        # Neighbor is the last word in the list, but then we also need
        # to strip off the period at the end
        neighbor = words[-1][:-1]
        happiness_change = int(words[3])
        if words[2] == 'lose':
            happiness_change *= -1
        if person not in happiness_dict:
            happiness_dict[person] = {}
        happiness_dict[person][neighbor] = happiness_change
    return happiness_dict
    
def calculate_happiness(happiness_dict, table):
    """Returns the happiness of the table, using happiness_dict
    
    Table is a list, but it is considered circular, so when table is
    the same length as happiness_dict (i.e. all the seats are filled),
    the first and last in the table are also considered neighbors.
    
    table will not have empty spots in the list for empty seats. Instead,
    we just assume that any entry in happiness_dict that is not in table
    is not yet seated"""
    total_happiness = 0
    for person_a, person_b in zip(table, table[1:]):
        total_happiness += happiness_dict[person_a].get(person_b, 0)
        total_happiness += happiness_dict[person_b].get(person_a, 0)
    if len(table) == len(happiness_dict):
        person_a = table[0]
        person_b = table[-1]
        total_happiness += happiness_dict[person_a].get(person_b, 0)
        total_happiness += happiness_dict[person_b].get(person_a, 0)
    return total_happiness
    
def optimize_happiness(happiness_dict, table=None):
    """Given a happiness dict, return the max happiness possible
    
    Also returns a list representing the full table that produces
    that max happiness.
    
    This function could be greatly improved, as right now it simply
    checks every possible seating.  There is currently no attempt to
    find the highest value first or perform any pruning of bad
    orderings.  However, this is fine, since we know that the input
    only has 8 (9 in part 2) options, so we only need to check 362880
    options in part 2, which is perfectly manageable"""
    if table is None:
        table = []
    if len(table) == len(happiness_dict):
        return (calculate_happiness(happiness_dict, table), table)
        
    best = -999999
    final_table = None
    for person in happiness_dict:
        # This is pretty inefficient, we should probably get an
        # adjusted dictionary first instead
        if person in table:
            continue
        next_table = table + [person]
        happiness, full_table = optimize_happiness(happiness_dict, next_table)
        if happiness > best:
            best = happiness
            final_table = full_table
    return best, final_table
        
    
def main():
    """Find the answers to  part 1 and 2 of the problem
    
    For part 1, read the input, create a happiness dictionary based on
    it, and optimize happiness using that dictionary. For part 2, just
    add 'Me' to the dictionary and run it again."""
    with open('aoc_day_13_input.txt') as input_file:
        full_input = input_file.read()
    happiness_dict = make_happiness_dict(full_input)
    print(optimize_happiness(happiness_dict))
    happiness_dict['Me'] = {}
    print(optimize_happiness(happiness_dict))
    
if __name__ == '__main__':
    main()