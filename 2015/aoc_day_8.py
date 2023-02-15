def raw_chars(string):
    """Return the number of raw characters in the string
    
    e.g. for the string "ab\"c", this would return 7"""
    return len(string)

def memory_chars(string):
    """Return the number of characters for the string in memory
    
    e.g. for the string "ab\"c", the data stored in memory would
    just be ab"c, so this would return 4"""
    return len(eval(string))
    
def encoded_chars(string):
    """Return the number of characters in the encoded string
    
    e.g. the string "ab\"c" would encode to "\"ab\\\"c\"",
    so this function would return 13"""
    characters_needing_encoding = {'\\', '"'}
    length = 2
    for char in string:
        length += 1
        if char in characters_needing_encoding:
            length += 1
    return length

def main():
    """Read the input file and print the answers to parts 1 and 2
    
    Part 1 asks for the total number of raw characters in the strings
    on each line of the input minus the total number of memory characters.
    Part 2 asks for the total number of encoded characters, minus the total
    number of raw characters"""
    with open('aoc_day_8_input.txt') as input_file:
        full_input = input_file.read()
    total_raw_chars = 0
    total_memory_chars = 0
    total_encoded_chars = 0
    for line in full_input.split('\n'):
        total_raw_chars += raw_chars(line)
        total_memory_chars += memory_chars(line)
        total_encoded_chars += encoded_chars(line)
    print(f'Raw: {total_raw_chars}, Memory: {total_memory_chars}, Raw - Memory: {total_raw_chars - total_memory_chars}')
    print(f'After encoding: {total_encoded_chars}, Encoded - raw: {total_encoded_chars - total_raw_chars}')
        
if __name__ == '__main__':
    main()