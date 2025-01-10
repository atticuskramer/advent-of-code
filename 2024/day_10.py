"""Advent of Code 2024: Day 10"""

test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def get_increasing_neighbors(grid, row, col):
    val = grid[row][col]
    potentials = [(row+drow, col+dcol) for drow, dcol in [(-1,0), (1,0), (0,-1), (0,1)]]
    neighbors = []
    for prow, pcol in potentials:
        if (0 <= prow < len(grid) 
            and 0 <= pcol < len(grid[0])
            and grid[prow][pcol] == val+1):
            neighbors.append((prow, pcol))
    return neighbors

def find_nines(grid, row, col):
    next = [(row,col)]
    visited = set(next)
    nines = set()
    while next:
        # We are going to search depth first, popping the end of the list
        row, col = next.pop()
        if grid[row][col] == 9:
            nines.add((row,col))
        else:
            potential_next = get_increasing_neighbors(grid, row, col)
            for neighbor in potential_next:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next.append(neighbor)
    return nines

def part_1(input_str):
    """Find the number of endpoints reachable from all trailheads
    
    A trailhead is the point a hiking trail starts at, in this case,
    it must be 0. Enpoints of hiking trails are 9's, and must be reached
    by orthogonal moves to numbers increasing by exactly 1"""
    grid = [[int(num) for num in line] for line in input_str.split('\n')]
    total = 0
    for row, line in enumerate(grid):
        for col, num in enumerate(line):
            # We only want to start searching on 0's
            if num != 0:
                continue
            nines = find_nines(grid, row, col)
            total += len(nines)
    return total

            
def part_2(input_str):
    pass
            
def main():
    with open('aoc_day_10_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
