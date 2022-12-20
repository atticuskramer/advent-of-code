test_code = """A Y
B X
C Z"""

rps_dict = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}

def round_score(line):
    opponent, me = line.split(' ')
    return rps_dict[(opponent, me)]
    
def rps_tourney(code):
    total = 0
    try:
        for line in code.split('\n'):
            total += round_score(line)
    except:
        print('Failed on line', total)
    return total