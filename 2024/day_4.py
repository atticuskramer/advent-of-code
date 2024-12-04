"""Advent of Code 2024: Day 4"""

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def pad_string_block(stringy, layers, pad_char=' '):
    """Adds 'layers' number of lines of 'pad_char' surrounding 'stringy'
    
    So for example pad_string_block(s, 2, '.') with the following string s 
    would give you:
             ......
             ......
       AB -> ..AB..
       CD    ..CD..
             ......
             ......
    This function assumes that stringy is a perfectly rectangular string block with
    no ending newline"""
    lines = stringy.split('\n')
    width = len(lines[0])
    height = len(lines)
    result_str = ''
    # Add top lines
    result_str += (pad_char * (2 * layers + width) + '\n') * layers
    # Pad front and back of each original line
    for line in lines:
        result_str += pad_char * layers + line + pad_char * layers + '\n'
    # Add bottom lines
    result_str += (pad_char * (2 * layers + width) + '\n') * layers
    # This is awkward, but we just return the string without the last newline
    return result_str[:-1]
    
def is_xmas(lines, row, col, drow, dcol):
    return (lines[row+drow][col+dcol] == 'M' and
            lines[row+2*drow][col+2*dcol] == 'A' and
            lines[row+3*drow][col+3*dcol] == 'S')

def part_1(input_str):
    """Count the number of times XMAS is found in the input_str
    
    XMAS can be spelled in any direction, backwards and forwards, 
    straight and diagonal"""
    padded = pad_string_block(input_str, 3, pad_char='.')
    lines = padded.split()
    xmases = 0
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    # These loops are currently checking more than necessary since they look
    # at the padding as well, but it's ultimately a pretty minor inefficiency
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            # If we see an X, check around it for XMAS
            if char == 'X':
                for drow, dcol in directions:
                    xmases += is_xmas(lines, row, col, drow, dcol)
    return xmases
            
def part_2(input_str):
    pass

def main():
    with open('aoc_day_4_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()