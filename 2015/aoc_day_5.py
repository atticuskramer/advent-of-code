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

