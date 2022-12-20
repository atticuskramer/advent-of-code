test_pairs = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def str_to_tuples(pairs_str):
    tuple_pairs = []
    for line in pairs_str.split('\n'):
        ranges = line.split(',')
        a,b = map(int, ranges[0].split('-'))
        c,d = map(int, ranges[1].split('-'))
        tuple_pairs.append(((a,b),(c,d)))
    return tuple_pairs
    
def num_surrounding_pairs(tuple_pairs_str):
    total = 0
    tuple_pairs = str_to_tuples(tuple_pairs_str)
    for pair in tuple_pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            print(pair[0], 'surrounds', pair[1])
            total += 1
        elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            print(pair[1], 'surrounds', pair[0])
            total += 1
    return total
    
print(num_surrounding_pairs(full_pairs))