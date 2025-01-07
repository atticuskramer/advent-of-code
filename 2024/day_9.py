"""Advent of Code 2024: Day 9"""

test_input = """2333133121414131402"""

def part_1(input_str):
    # First, we will build our expanded data list and keep track of the empty spots
    # so that we can later fill them without having to search the list again
    EMPTY = '.'
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
    # First, we will take our input string, and create a list of empty ranges
    # and a list of the ranges for each piece of data
    # The empty ranges are given as (start_idx, length), and the data ranges as
    # (start_idx, length, value)
    is_data = True
    data_val = 0
    data_ranges = []
    empty_ranges = []
    idx = 0
    for num in [int(num_str) for num_str in input_str]:
        if is_data:
            data_ranges.append((idx, num, data_val))
            data_val += 1
        else:
            empty_ranges.append((idx, num))
        idx += num
        is_data = not is_data
    # Next, we move backwards through our data ranges, filling in the empty ranges
    # if possible, front to back
    new_data_ranges = []
    for start_idx, length, value, in data_ranges[::-1]:
        # Start assuming we will leave the data in place, then update if needed
        new_range = (start_idx, length, value)
        for i, (e_start_idx, e_length) in enumerate(empty_ranges):
            # If our data range starts before the empty range, skip
            if start_idx < e_start_idx:
                break
            if length <= e_length:
                new_range = (e_start_idx, length, value)
                # Here we are modifying empty_ranges while looping through it,
                # which would normally be a problem, but is ok here since we
                # break immediately afterwards
                if length == e_length:
                    empty_ranges = empty_ranges[:i] + empty_ranges[i+1:]
                else:
                    empty_ranges[i] = (e_start_idx + length, e_length - length)
                break
        new_data_ranges.append(new_range)
    # Lastly, we go through our new data ranges, and get our checksum
    checksum = 0
    for start_idx, length, value in new_data_ranges:
        for i in range(start_idx, start_idx + length):
            checksum += i * value
    return checksum
            
def main():
    with open('aoc_day_9_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
