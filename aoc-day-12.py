test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

class Heightmap:
    START_CHAR = 'S'
    END_CHAR = 'E'
    
    @staticmethod
    def _char_height(char):
        if char == START_CHAR:
            return 1
        elif char == END_CHAR:
            return 26
        else:
            return ord(char) - 96
    
    def __init__(self, map_str):
        lines = map_str.split('\n')
        grid = [[] for _ in lines]
        for row,line in enumerate(lines):
            for col,char in enumerate(line):
                grid[row].append(self._char_height(char))
                if char == START_CHAR:
                    self.start = (row, col)
                elif char == END_CHAR:
                    self.end = (row,col)
                    
    @staticmethod
    def _jumpable(height_1, height_2):
        return abs(height_1 - height_2) <= 1
                    
    def get_neighbors(self, row, col):
        neighbors = []
        if row - 1 > 0 and self._jumpable(self.grid[row-1][col], self.grid[row][col]):
            neighbors.append((row-1,col))
        if row + 1 < len(self.grid) and self._jumpable(self.grid[row+1][col], self.grid[row][col]):
            neightbors.append((row+1,col))
        if col - 1 > 0 and self._jumpable(self.grid[row][col-1], self.grid[row][col]):
            neighbors.append((row,col-1))
        if col + 1 < len(self.grid[row]) and self._jumpable(self.grid[row][col+1], self.grid[row][col]):
            neighbors.append((row,col+1))
        return neighbors
    def bfs(self):
        current = self.start
        explored = set()
        queue = []
        while current != self.end:
            neighbors = self.get_neighbors(*current)