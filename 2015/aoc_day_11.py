"""Advent of Code 2015, Day 11"""

def increment_password(password):
    """Increment the password by 1, rolling over if necessary
    
    password should be a string made up only of [a-z]. We increment
    starting from the right like a number, increasing the character by
    1 (e.g. a -> b).  If the right-most character is a 'z', it becomes
    'a' and we continue incrementing the second character from the 
    right. A string of all 'z' will "overflow" and return all 'a's"""
    if password == '':
        return ''
    last_char_ord = ord(password[-1])
    if last_char_ord < 122:
        return password[:-1] + chr(last_char_ord + 1)
    else:
        return increment_password(password[:-1]) + 'a'
        
def is_valid_password(password):
    """Returns boolean indicating if the password is valid
    
    A valid password meets the following 3 conditions:
    1. Has a 3-character straight of increasing characters
       (e.g. 'abc' would work, but 'abd' would not)
    2. Does not contain the letters 'i', 'o', or 'l'
    3. Contains 2 non-overlapping pairs of letters.
       (e.g. 'aabcc' would work, but 'aaa' would not)"""
    has_straight = False
    forbidden_chars = ['i', 'o', 'l']
    first_pair_index = second_pair_index = None
    for i, char in enumerate(password):
        if char in forbidden_chars:
            return False
        if i >= 2 and (ord(char) == ord(password[i-1]) + 1 == ord(password[i-2]) + 2):
            has_straight = True
        if i >= 1 and char == password[i-1]:
            if first_pair_index is None:
                first_pair_index = i-1
            elif first_pair_index <= i - 3:
                second_pair_index = i-1
    return has_straight and first_pair_index is not None and second_pair_index is not None

def find_next_valid_password(password):
    """Returns the next valid password, found by incrementing password"""
    while not is_valid_password(password):
        password = increment_password(password)
    return password
    
def main():
    with open('aoc_day_11_input.txt') as input_file:
        full_input = input_file.read()
    second_password = find_next_valid_password(full_input)
    print('Next valid pass:', second_password)
    third_password = find_next_valid_password(increment_password(second_password))
    print('Next after that:', third_password)
    
if __name__ == '__main__':
    main()