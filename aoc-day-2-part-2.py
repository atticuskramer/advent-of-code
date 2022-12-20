test_code = """A Y
B X
C Z"""

rps_dict = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}

rps_dict_two = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}

def round_score(line, decrypter):
    opponent, me = line.split(' ')
    return decrypter[(opponent, me)]
    
def rps_tourney(code, decrypter):
    total = 0
    try:
        for line in code.split('\n'):
            total += round_score(line, decrypter)
    except:
        print('Failed on line', total)
    return total