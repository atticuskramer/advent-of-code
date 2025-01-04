"""Advent of Code 2024: Day 9"""

test_input = """2333133121414131402"""

def part_1(input_str):
    # First, we will build our expanded data list and keep track of the empty spots
    # so that we can later fill them without having to search the list again
    EMPTY = ','
    is_data = True
    data_val = 0
    expanded = []
    empty_spots = []
    for num in [int(num_str) for num_str in input_str]:
        if is_data:
            expanded += [data_val] * num
            data_val += 1
        else:
            empty_spots += [i for i in range(len(expanded), len(expanded) + num)]
            expanded += [EMPTY] * num
        is_data = not is_data
    # Next, we move backwards through the expanded data, filling in the empty spots
    # front to back
    i = len(expanded) - 1
    while empty_spots and i > empty_spots[0]:
        if expanded[i] != EMPTY:
            expanded[empty_spots[0]] = expanded[i]
            expanded[i] = EMPTY
            empty_spots = empty_spots[1:]
        i -= 1
    # Lastly, we walk forward through expanded, adding up the checksum values
    checksum = 0
    for i, item in enumerate(expanded):
        if item == EMPTY:
            break
        checksum += i * item
    return checksum

        
            
def part_2(input_str):
    pass
            
def main():
    with open('aoc_day_9_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
