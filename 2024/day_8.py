"""Advent of Code 2024: Day 8"""

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

class Antenna_Grid():
    def __init__(self, input_str):
        lines = input_str.split('\n')
        self.height = len(lines)
        self.width = len(lines[0])
        self.antennae = dict()
        self.antinodes = set()
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '.':
                    continue
                else:
                    if char in self.antennae:
                        self.antennae[char].add((row,col))
                    else:
                        self.antennae[char] = set([(row,col)])

    def in_bounds(self, point):
        row,col = point
        return 0 <= row < self.width and 0 <= col < self.height

    def add_antinodes(self):
        for antenna_type, locations in self.antennae.items():
            # This structure is going to do double work (checking each pair of
            # Antennas A,B and B,A), but this should not change end result or
            # asymptotic time complexity
            for (row1, col1) in locations:
                for (row2, col2) in locations:
                    # Same antenna, no antinode
                    if (row1,col1) == (row2, col2):
                        continue
                    # Otherwise, find the antinodes and add them if in bounds
                    drow = row1 - row2
                    dcol = col1 - col2
                    antinode1 = (row1+drow, col1+dcol)
                    antinode2 = (row2-drow, col2-dcol)
                    if self.in_bounds(antinode1): 
                        self.antinodes.add(antinode1)
                    if self.in_bounds(antinode2):
                        self.antinodes.add(antinode2)
                    


def part_1(input_str):
    ag = Antenna_Grid(input_str)
    ag.add_antinodes()
    return len(ag.antinodes)
            
def part_2(input_str):
    pass
            
def main():
    with open('aoc_day_8_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
