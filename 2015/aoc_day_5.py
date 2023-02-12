"""Advent of Code: 2015 Day 5"""

def is_string_nice(s):
    """Returns True if the string is 'nice', False otherwise
    
    A nice string is one that contains at least three vowels,
    contains a double letter, and does NOT contain any of the
    following 2-character sequences: ab, cd, pq, xy"""
    vowel_count = 0
    has_double = False
    NAUGHTY_PAIRS = ['ab', 'cd', 'pq', 'xy']
    VOWELS = ['a','e','i','o','u']
    for i, char in enumerate(s):
        if char in VOWELS:
            vowel_count += 1
        if i > 0 and s[i-1] == char:
            has_double = True
        if i > 0 and s[i-1:i+1] in NAUGHTY_PAIRS:
            return False
    return has_double and vowel_count >= 3
    
def is_string_nicer(s):
    """Returns True if the string is 'nice' by the below rules
    
    1. It contains a two character sequence that appears twice in
       the string WITHOUT overlapping (e.g. axybcxy, but not aaa)
    2. It contains a three letter sequence where letters 1 and 3
       are the same (e.g. ada or aaa)"""
    has_repeat = False
    has_sandwich = False
    two_char_sequences = {}
    for i, char in enumerate(s):
        if i >= 2 and s[i-2] == s[i]:
            has_sandwich = True
        if i >= 1:
            two_chars = s[i-1:i+1]
            try:
                previous = two_char_sequences[two_chars]
                if i - previous >= 3:
                    has_repeat = True
            except KeyError:
                two_char_sequences[two_chars] = i-1
        if has_sandwich and has_repeat:
            break
    return has_sandwich and has_repeat
        
    
def part_1(string_list):
    """Return the number of strings in string_list that are nice"""
    total = 0
    for s in string_list:
        if is_string_nice(s):
            total += 1
    return total
    
def part_2(string_list):
    """Return the number of strings in string_list that are nicER"""
    total = 0
    for s in string_list:
        if is_string_nicer(s):
            total += 1
    return total
    
def main():
    with open('aoc_day_5_input.txt') as f:
        full_input = f.read()
    string_list = full_input.split('\n')
    print('Total nice strings:', part_1(string_list))
    print('Total nicER strings:', part_2(string_list))

if __name__ == '__main__':
    main()
    