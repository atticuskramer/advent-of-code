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
        self.visited = dict()
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
                    self.direction = (-1, 0)
                    self.visited[(row,col)] = [self.direction]

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

    def would_loop(self, new_obstacle):
        # First we will save the current state
        saved_guard = self.guard
        saved_visited = {key: val.copy() for (key,val) in self.visited.items()}
        saved_empty = self.empty.copy()
        saved_direction = self.direction
        looping = False
        # Then we will add the obstacle and check to see if we loop
        self.obstacles.add(new_obstacle)
        while(self.is_valid(self.next_position())):
            # If we have visited the next position already WITH OUR CURRENT
            # DIRECTION, then we must be looping
            if self.direction in self.visited.get(self.next_position(), []):
                looping = True
                break
            self.move_guard()
        # Then we will reset the state to what it was before
        self.obstacles.remove(new_obstacle)
        self.guard = saved_guard
        self.empty = saved_empty
        self.visited = saved_visited
        self.direction = saved_direction
        return looping
    
    def move_guard(self):
        potential_next = self.next_position()
        if potential_next in self.obstacles:
            # If the guard would hit an obstacle, turn right
            self.turn_right()
            self.visited[self.guard].append(self.direction)
        else:
            # Otherwise, move the guard and mark the next space as visited
            self.empty.discard(potential_next)
            if potential_next in self.visited:
                self.visited[potential_next].append(self.direction)
            else:
                self.visited[potential_next] = [self.direction]
            self.guard = potential_next

def part_1(input_str):
    eg = Elf_Grid(input_str)
    while(eg.is_valid(eg.next_position())):
        eg.move_guard()
    return len(eg.visited)
            
def part_2(input_str):
    # At each step on the guard's journey, check to see if adding an obstacle
    # right in front of him would cause him to loop
    #
    # I'm pretty sure there are way more efficient ways to do this, but this
    # works, and I am way behind on this year's AoC, so this will do for now
    eg = Elf_Grid(input_str)
    looping_obstacles = set()
    next = eg.next_position()
    checked_obstacles = set()
    while(eg.is_valid(next)):
        # We only need to check for adding an obstacle if:
        # 1. The space is not already an obstacle, and
        # 2. We have not already checked that location for an obstacle
        #    (this prevents miscounting in cases where the path crosses itself)
        if next not in eg.obstacles and next not in checked_obstacles and eg.would_loop(next):
            looping_obstacles.add(next)
        checked_obstacles.add(next)
        eg.move_guard()
        next = eg.next_position()
    return len(looping_obstacles)
            
def main():
    with open('aoc_day_6_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
