"""Advent of Code: 2015, Day 2"""

def calculate_wrapping(width, length, height):
    """
    Returns the amount of paper needed for a box of given dimensions
    
    The box takes paper exactly equal to its surface area plus the area
    of its smallest side
    """
    side_a = width * length
    side_b = width * height
    side_c = length * height
    return 2 * (side_a + side_b + side_c) + min(side_a, side_b, side_c)

def calculate_ribbon(width, length, height):
    """
    Returns the amount of ribbon needed for a box of given dimensions
    
    The amount of ribbon needed is the perimeter of the smallest side of
    the box, plus the area of the box
    """
    perim_a = 2 * (width + length)
    perim_b = 2 * (width + height)
    perim_c = 2 * (length + height)
    return min(perim_a, perim_b, perim_c) + width * length * height

def part_1(dimensions_list):
    """Return the sum of the paper needed for all cubes in dimensions_list"""
    total = 0
    for width, length, height in dimensions_list:
        total += calculate_wrapping(width, length, height)
    return total

def part_2(dimensions_list):
    """Return the sum of the ribbon needed for all cubes in dimensions_list"""
    total = 0
    for width, length, height in dimensions_list:
        total += calculate_ribbon(width, length, height)
    return total

def main():
    """Read the input file, then call part_1"""
    with open('aoc_day_2_input.txt', encoding='utf-8') as input_file:
        full_input = input_file.read()
    lines = full_input.split('\n')
    dimensions_list = [tuple(map(int, dims.split('x'))) for dims in lines]
    print('Total wrapping paper needed', part_1(dimensions_list))
    print('Total ribbon needed:', part_2(dimensions_list))

if __name__ == '__main__':
    main()
