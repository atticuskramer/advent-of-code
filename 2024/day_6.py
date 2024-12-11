"""Advent of Code 2024: Day 6"""

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

class Elf_Grid():
    def __init__(self, input_str):
        lines = input_str.split('\n')
        self.height = len(lines)
        self.width = len(lines[0])
        self.empty = set()
        self.visited = set()
        self.obstacles = set()
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '.':
                    self.empty.add((row,col))
                elif char == '#':
                    self.obstacles.add((row,col))
                elif char == '^':
                    # For now, we assume that the guard always will start facing north
                    self.guard = (row,col)
                    self.visited.add((row,col))
                    self.direction = (-1, 0)

    def turn_right(self):
        next_directions = {
            (-1,0): (0,1),
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0)
        }
        self.direction = next_directions[self.direction]

    def next_position(self):
        return (self.guard[0] + self.direction[0], self.guard[1] + self.direction[1])
    
    def is_valid(self, position):
        return 0 <= position[0] < self.height and 0 <= position[1] < self.width
    
    def move_guard(self, wrapping=False):
        potential_next = self.next_position()
        if potential_next in self.obstacles:
            # If the guard would hit an obstacle, turn right
            self.turn_right()
        else:
            # Otherwise, move the guard and mark the next space as visited
            self.empty.discard(potential_next)
            self.visited.add(potential_next)
            self.guard = potential_next

def part_1(input_str):
    eg = Elf_Grid(input_str)
    while(eg.is_valid(eg.next_position())):
        eg.move_guard()
    return len(eg.visited)
            
def part_2(input_str):
    pass
            
    

def main():
    with open('aoc_day_6_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
