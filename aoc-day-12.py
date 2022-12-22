full_input = """abcccccaaaaaacccaaaccaaaaaaaacccaaaaaaccccccccccccccccccccccccccccaaaaaaaaaaaaaacacccccccccccccccccccccccccccccccaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccaaaaa
abcccccaaaaaaaacaaaaccaaaaaaccccaaaaaaccccccccccaaacccccccccccccccaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccaaaaaaaaaccccccaaaccccccccccccccccccccccccccccccccccaaaaaa
abccccaaaaaaaaacaaaaccaaaaaaccccaaaaaaaaccccccccaaaccccccccccccccccaaaaaaaaaaaaaaccccaaaccccccccccccccccccccccccccaaaaaaaaccccacaaaccccccccccccccccaaccccccccccccccccaaaaaa
abcccaaaaaaaaaacaaaccaaaaaaaacccccaaccaaacaaccccaaaaaaaccccccccccccaacaaaaaaaaaccccccaaaaccccccccccccccccccccaaacaaaaaaccccccaaaaaaaacccccccccccccaaaacccccccccccccccaaacaa
abcccaaacaaaccccccccaaaaaaaaaaccccccccaaaaaacaaaaaaaaaaccccccccccccccaaaaaaaaaaccccccaaaaccccccccccccccccaaccaaacaaaaaaacccccaaaaaaaacccccccccccccaaaaccaaaccccccccccccccaa
abcccccccaaaccccccccaaaaaaaaaaccccccaaaaaaaccaaaaaaaaacccccccccccccccaaaacaaaaaaaacccaaaaccccccccccccccccaaaaaaacaaccaaacccccccaaaaacccccccccccccccaaaaaaaaacccccccccccccaa
abcccccccaacccccccccacaaaaaccaccccccaaaaaaacccaaaaaaaccccccaaacccccccaacacaaaaaaaacccccccccccccccccccccccaaaaaaccccccaaaccccccaaaaaccccccccccccjjkkaaaaaaaacccccccccccccccc
abaccccccccccccccccccccaaaacccccccccccaaaaaaccccaaaaaaccccaaaacccccccccccccaaaaaaccccccccccaccaaccccccccccaaaaaaaaccccccccccccaaaaaaccccccccccjjjkkkkkaaaaccccccccaaccccccc
abaccccccccaaaccccccccccaaccccccccccccaacaaacccaaaaaaaccccaaaacccccccccccccaaaaaaccccccccccaaaaacccccccccaaaaaaaaaccccccccccccaccaaacccccccccjjjjkkkkkkkaacccccccccaccccccc
abaacccccccaaaaccccccccccaaaccccccccccaacccccccaaaacaaccccaaaacccccccccccccaaaaaacccccccccccaaaaaccccccccaaaaaaaacccccccaaccccccccccccccccccjjjjoooookkkkkllllllccccaaacccc
abaacccccccaaaaccccccccccaaaaccccccccccccccccccaacaaacaaaccccccccccaaccccccaaacaaccccccccccaaaaaacccccccaaaaaaaccccccccaaaacccccccccccccccccjjjoooooopkkkklllllllccccaacccc
abaccccccccaaacccccccccccaaaacccccccccccccccccccccaaaaaaacccccccccaaaccccccccccccccccccccccaaaaccccccaaaccccaaaccccccccaaaacccccccccccccccccjjooooooopppklppplllllcccaccccc
abacccaaaaaccccccccccccccaaaccccccccccccccccccccccaaaaaaccccccaaaaaaaccccccccccccccccccccccccaaacccccaaacacccaaccccccccaaaaccccccccccccccccjjjooouuuupppppppppplllcccaccccc
abccccaaaaacccccccccccccccccccccccccccccccccccccaaaaaaaaccccccaaaaaaaaaaccaacccccccccccccccccccccccaacaaaaaccccccccccccccccaaacccccaccaccccjjjoouuuuuupppppppppllllccaccccc
abcccaaaaaacccccccccccccaaccccccaaacccccccccccccaaaaaaaaaccccccaaaaaaaaacaaaaccccccccccccccccccccccaaaaaaaaccccccccccccacccaaccccccaaaacccjjjjoouuuuuuupuuuvvpqqlllccaccccc
abcccaaaaaaccccccccccccaaacaacccaaaaacccccccccccaaaaaaaaaaccccccaaaaaaaccaaaacccccccccccccccccccccccaaaaaccccccccccccccaaaaaaacccccaaaaaccijjooouuuxxxuuuuvvvqqqlmccccccccc
abcccaaaaaaccccaacccccccaaaaaccaaaaaccccccccccccaaaaaacaaacccccaaaaaaccccaaaacccccccccccccccccccaaaccaaaaaccccaaaccccccaaaaaaaacccaaaaaaciiiinootuxxxxuuyyyvvqqqmmccccccccc
abcccacaacccccaaacaaccaaaaaacccaaaaaccccccccccccaaaaaacccccccccaaaaaaaccccccccccccaaccacccccccccaaacaaacaaccaaaaaccccccaaaaaaaaaccaaaaaaiiinnnnnttxxxxxyyyyvvqqqmmdddcccccc
abcccaaacaaacccaaaaaccaaaaaaaaccaaaaacccccccccccaaacaaaccccccccaaccaaaccccccccccccaaaaaccccccaaaaaaaaaacccccaaaaaacccccaaaaaaaaaccccaaciiinnnnttttxxxxxyyyyvvqqmmmdddcccccc
abcccaaaaaaacaaaaaacccaacaaaaaccaacccccccccccaaaaaaaaaaaccccccccccccaacccccccccccaaaaacccccccaaaaaaaacccccccaaaaaacccccaaaaaaaaccccccciiinnnnttttxxxxxyyyyvvqqqmmmdddcccccc
SbcccaaaaaaccaaaaaaaaccccaacccccccccccaacccccaaaaaaaaaaccccccccccccccccccccccccccaaaaaaccccccccaaaaaccccccccaaaaacccccaaaaaaaccccccccciiinnntttxxxEzzzzyyvvvqqqmmmdddcccccc
abccaaaaaaaacaacaaaaacccaaccccccccccccaaacccccaaaaaaaaaaaccccccccccccccccccccccccccaaaacccccccaaaaaaccccccccaaaaaccccccacaaaaccccccccciiinnntttxxxxxyyyyyyvvvqqmmmdddcccccc
abcaaaaaaaaaacccaacccccaacccccccccacacaaaccccccaaaaaaaaaacccccccccccccccccccccacccaaccccccccccaaaaaaccccccccccccccccccccaaaaaccccccccciiinnntttxxxxyyyyyyyyvvvqqmmmdddccccc
abcaaaaaaaaaaccaaccaaaaaacccccccccaaaaaaaaaacccaaaaaaaaaacaaccccccccccccaaaaaaaaccccccccccccccaccaaaccccccccccccccccaaacaaacccccccccaaiiinnnttttxxwwyyyyyyyvvvqqmmmdddccccc
abaaccaaacaaaccccccaaaaaaaccccccccaaaaaaaaaacccaaaaaaaacccaaaccccccccccccaaaaaacccccccccccccccccccccccccccccccccccccaaaaaaaaaacccaaaachhhnnnntttsswwyywwwwwvvvrrqkmdddccccc
abaaacaaacccccccccccaaaaaaacccccccccaaaaaacccccaacccaaacccaaaaaaaccccccccaaaaaaccccccccccccccaaccccccccccccccccccccccaaaaaaaaacccaaaaaahhhmmmmmsssswwywwwwwwvrrrrkkdddccccc
abaaaaaaacccccccccccaaaaaaacccccccccaaaaaaccccccaaccccccaaaaaaaaccccccccaaaaaaaaccccccccaaccaaaccccccccccccccccaacccccaaaaaaacccccaaaaahhhhhmmmmssswwwwwrrrrrrrrkkkeeeccccc
abcaaaaaaccccccccccaaaaaacccccccccccaaaaaacccccaaaaccccaaaaaaaaacccccccaaaaaaaaaacccccccaaacaaacccccccccccccacaaaccccaaaaaaccccccaaaaacchhhhhmmmmsswwwwrrrrrrrrrkkkeeeccccc
abaaaaaacccccccccccaaaaaaccccccccccaaaaaaaaccccaaaaccccaaaaaaaaccccccccaaaaaaaaaacaaacccaaaaaaccccccaacccccaaaaaccaccaaaaaaacccccaccaacccchhhhmmmssswwsrrrrrrrkkkkkeeeccccc
abaaaaaaaccccccccaaccccaaccccccccccaaaaaaacccccaaaacccccccaaaaaacccaaccacaaaaaccccaaaccccaaaaaaaaaacaaaccccaaaaaaaaccaaacaaaccccccccccccccchhhhmmssssssrlllkkkkkkkeeecccccc
abaaaaaaaaccccccaaacaacccccccccccccaaaaaaaaccccccccccccccaaaaaaacccaacccccaaaaccccaaaaaaaaaaaaaaaaaaaacccccccaaaaaccccccccaaaacccccccccccccchhgmmmsssssllllkkkkkeeeeeaacccc
abcaaacaaacccccccaaaaaccccccccccccaaaaaaaaaccccccccccccccaaaccaaaaaaaaaacccaaccaaaaaaaaaaaaaaaaacaaaaaaaccccaaaaacccccccaaaaaacccccccccccccccggmmmlssslllllffeeeeeeeaaacccc
abcaaacccccccccaaaaaacccccccaaacaaacaaaaaaacccccccccccccaaaaccccaaaaaaaacccccccaaaaaaaaaaaaaaaccaaaaaaaaccccaacaacccccccaaaaaacccccccccccccccgggmmlllllllfffffeeeeaaaaacccc
abcaaccccccccccaaaaaaaacccccaaaaaaaaaaaaaccccccccccccccccaaaacccccaaaacccccaacccaaaaaaaccccaaaccaaaaaaaacccccccaaccccccccaaaaaaaccccccccccccccggglllllllffffffecacaaacccccc
abcccccccccaaccaacaaaaaccccccaaaaaaaaaaaaccccccaaccaaccaaaaaaccccaaaaaccccaaccccccaaaaaacccaaaccaacaaaccaaaacccccccccccccaaaaaaaccccccccccccccggggllllfffffcccccccaaacccccc
abcccccccaaaaaaccaaacccccccccaaaaaaaaccaaacccccaaaaaaccaaaaacccccaaaaaacccaaaccaaaaaaaaacccccccccccaaaccaaaaacccccccccccaaaaaaaaaccaaccccccccccggggggfffffccccccccccccccccc
abcaaccccaaaaaaccaaccccccccaaaaaaaaaacccaacccccaaaaaccccaaaaaccccacccaaccaaaaccaaaaaccaacccccccccccccccaaaaaacccccccaaacaaaaaaaaaaaaacccccccccccgggggfffaacccccccccccccaccc
abaaaccccaaaaaaccccccccaaacaaaaaaaaaaaaaaaaaaccaaaaaacccaaccacccccccaaaaaaaaaaaaaaaccccccccccccccaaaaccaaaaaacccccccaaaaaaaaaacaaaaaaccccccccccccagggfcaaaccccccccccccaaaaa
abaaaacccaaaaaccccccccaaaacaaacaaacccaaaaaaaacaaaaaaaaccccccccccccccaaaaaaaaaaaaaaacccccccccccccaaaaacccaaaaaccccccccaaaaaacaaaaaaaaccccccccccccccaccccaaacccccccccccccaaaa
abaaaaccccaaaaccccccccaaaacccccaaacccccaaaacccaaaaaaaacccccccccccccccaaaaaaaaaaaaaacccccccccccccaaaaaaccaaaccccccccccaaaaaaaaaaaaaaaaccccccccccccccccccccacccccccccccccaaaa
abaacccccccccccccccccccaaacccccaacccccaaaaaacccccaacccccccccccccccccccccaaaaaaaaacccccccccccccccaaaaaacccccccccccccaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccaaaaaa"""

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

class Heightmap:
    START_CHAR = 'S'
    END_CHAR = 'E'
    
    def __init__(self, map_str):
        lines = map_str.split('\n')
        self.grid = [[] for _ in lines]
        for row,line in enumerate(lines):
            for col,char in enumerate(line):
                self.grid[row].append(self._char_height(char))
                if char == self.START_CHAR:
                    self.start = (row, col)
                elif char == self.END_CHAR:
                    self.end = (row,col)
    
    @classmethod
    def _char_height(cls, char):
        if char == cls.START_CHAR:
            return 1
        elif char == cls.END_CHAR:
            return 26
        else:
            return ord(char) - 96
                    
    @staticmethod
    def _jumpable(from_height, to_height, reversed=False):
        if reversed:
            return to_height - from_height >= -1
        else:
            return from_height - to_height >= -1
                    
    def get_neighbors(self, row, col, reversed=False):
        neighbors = []
        if row - 1 >= 0 and self._jumpable(self.grid[row][col], self.grid[row-1][col], reversed):
            neighbors.append((row-1,col))
        if row + 1 < len(self.grid) and self._jumpable(self.grid[row][col], self.grid[row+1][col], reversed):
            neighbors.append((row+1,col))
        if col - 1 >= 0 and self._jumpable(self.grid[row][col], self.grid[row][col-1], reversed):
            neighbors.append((row,col-1))
        if col + 1 < len(self.grid[row]) and self._jumpable(self.grid[row][col], self.grid[row][col+1], reversed):
            neighbors.append((row,col+1))
        return neighbors
    
    # Performance could be improve by using A* with a manhattan distance heuristic, instead of bfs
    def bfs(self, start_coord=None, end_coords=None, reversed=False):
        if start_coord is None:
            start_coord = self.start
        if end_coords is None:
            end_coords = set([self.end])
        current = start_coord
        # each visited node is a key in the explored dictionary, with a value of the node that it was
        # reached from, so that we can reconstruct the path once finished
        explored = {}
        queue = [current]
        explored[current] = None
        while current not in end_coords and len(queue) > 0:
            current = queue.pop(0)
            neighbors = [neighbor for neighbor in self.get_neighbors(*current, reversed) if neighbor not in explored]
            for neighbor in neighbors:
                explored[neighbor] = current
            queue.extend(neighbors)
        path = [current]
        while explored[current] != None:
            current = explored[current]
            path.append(current)
        return path

    def best_path(self):
        potential_starts = set()
        for row, line in enumerate(self.grid):
            for col, height in enumerate(line):
                if height == 1:
                    potential_starts.add((row,col))
        # There is probably a cleaner way to do this than passing this reversed variable all the way down
        return self.bfs(start_coord = self.end, end_coords = potential_starts, reversed=True)



test_heightmap = Heightmap(test_input)
test_path = test_heightmap.bfs()
test_path_2 = test_heightmap.best_path()
print(f'Part 1 Test: length {len(test_path)}, path: {test_path}')
print(f'Part 2 Test: length {len(test_path_2)}, path: {test_path_2}')

full_heightmap = Heightmap(full_input)
full_path = full_heightmap.bfs()
full_path_2 = full_heightmap.best_path()
print(f'Part 1 Full: length {len(full_path)}, path: {full_path}')
print(f'Part 2 Full: length {len(full_path_2)}, path: {full_path_2}')