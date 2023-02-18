"""Advent of Code 2015, Day 13"""

def get_relation_dict(input_string):
    """Return a dictionary of relations based on the given input
    
    The dictionary is nested such that d[name1][name2] gives the
    change in happiness that name1 experiences from sitting next to
    name2"""
    relation_dict = {}
    for line in input_string.split('\n'):
        words = line.split()
        person = words[0]
        neighbor = words[-1]
        happiness = int(words[3])
        if words[2] == 'lose':
            happiness *= -1
        if person in result_dict:
            relation_dict[person][neighbor] = happiness
        else:
            relation_dict[person] = {neighbor:happiness}
    return relation_dict
    
def table_happiness(table_list, relation_dict):
    """Return the total happiness of the table, using relation_dict"""
    total = 0
    for i, person in enumerate(table_list):
        left_neighbor = table_list[i-1]
        right_neighbor = table_list[(i + 1) % len(table_list)]
        # Person should always be in the dict, but the neighbors may
        # not be seated yet
        total += relation_dict.get(person).get(left_neighbor, 0)
        total += relation_dict.get(person).get(right_neighbor, 0)
    return total
    
def optimize_happiness(relation_dict):
    table_list = [None for _ in relation_dict]
    # TODO