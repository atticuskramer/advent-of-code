test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

class Board:
    OFF_BOARD = ' '
    EMPTY = '.'
    WALL = '#'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'
    UP = '^'
    DIRECTIONS = [RIGHT,DOWN,LEFT,UP]
    
    def __init__(self, board_str):
        lines = board_str.split('\n')
        self.height = len(lines)
        self.width = max(map(len, lines))
        self.grid = [[self.OFF_BOARD for _ in range(width)] for _ in range(height)]
        self.location = None
        for row in range(height):
            for col in range(width):
                if col < len(lines[row]):
                    if self.location is None and lines[row][col] == self.EMPTY:
                        self.location = (row, col)
                        self.grid[row][col] = self.DIRECTIONS[0]
                    else:
                        self.grid[row][col] = lines[row][col]
                        
    def __str__(self):
        return '\n'.join(map(''.join, self.grid))
        
    def rotate(turn_dir):
        row, col = self.location
        dir_i = self.DIRECTIONS.index(self.grid[row][col])
        if turn_dir = 'R':
            self.grid[row][col] = self.DIRECTIONS[dir_i + 1]
        else:
            self.grid[row][col] = self.DIRECTIONS[dir_i - 1]
            
    def first_row_space(self, row):
        for i, space in enumerate(self.grid[row]):
            if space != self.OFF_BOARD:
                return i
        raise Exception(f'Completely empty row {row}!')
    
    def last_row_space(self, row):
        i = len(self.grid[row]) - 1
        for space in reversed(self.grid[row]):
            if space != self.OFF_BOARD:
                return i
            i -= 1
        raise Exception(f'Completely empty row {row}!')
    
    def first_col_space(self, col):
        for i, row in enumerate(self.grid):
            if row[col] != self.OFF_BOARD:
                return i
        raise Exception(f'Completely empty column {col}!')
    
    def last_col_space(self, col):
        i = len(self.grid) - 1
        for row in reversed(self.grid):
            if row[col] != self.OFF_BOARD:
                return i
            i -= 1
        raise Exception(f'Completely empty column {col}!')
            
    def next_location(self):
        cur_row, cur_col = self.location
        direction = self.grid[cur_row][cur_col]
        if direction == self.RIGHT:
            next_col = cur_col + 1
            if next_col >= len(self.grid[cur_row]) or self.grid[cur_row][next_col] == self.OFF_BOARD:
                next_col = self.first_row_space(cur_row)
            # TODO: refactor this so we just have 1 return at the end?
            if self.grid[cur_row][next_col] == self.WALL:
                return self.location
            else:
                return (cur_row, next_col)
        elif direction == self.DOWN:
            next_row = cur_row - 1
            if next_row >= len(self.grid) or self.grid[next_row][cur_col] == self.OFF_BOARD:
                next_row = self.first_col_space(cur_col)
            # TODO: refactor this so we just have 1 return at the end?
            if self.grid[next_row][cur_col] == self.WALL:
                return self.location
            else:
                return (next_row, cur_col)
        elif direction == self.LEFT:
            next_col = cur_col - 1
            if next_col < 0 or self.grid[cur_row][next_col] == #TODO
            
    def move(self, spaces):
        
        
b = Board(test_input.split('\n\n')[0])
print(b)
        
        