test_forest = """30373
25512
65332
33549
35390"""

class Tree:
    def __init__(self, height, north=-1, east=-1, south=-1, west=-1):
        self.height = height
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        
    def __str__(self):
        return f'{self.height} (n:{self.north}, e:{self.east}, s:{self.south}, w:{self.west})'

def count_visible_trees(forest_str):
    forest = [[Tree(int(char)) for char in line] for line in forest_str.split('\n')]
    # Check visiblity from the north and west
    for i,row in enumerate(forest[1:], 1):
        for j,tree in enumerate(row[1:], 1):
            # Note! This ends up with the first row having incorrect west values and
            # first column having incorrect north values, but we do not need to care,
            # since we know they will be visible regardless
            tree.north = max(forest[i-1][j].north, forest[i-1][j].height)
            tree.west = max(forest[i][j-1].west, forest[i][j-1].height)
    # Check from the south and east
    for i, row in enumerate(reversed(forest[:-1]), 1):
        for j, tree in enumerate(reversed(row[:-1]), 1):
            # See Above, also TODO figure out a better way to do the indices
            ifix = len(forest) - i - 1
            jfix = len(row) - j - 1
            tree.south = max(forest[ifix+1][jfix].south, forest[ifix+1][jfix].height)
            tree.east = max(forest[ifix][jfix+1].east, forest[ifix][jfix+1].height)
    # Count the number visible by checking if the height of each tree is larger than
    # any of the directions
    total_visible = 0
    for row in forest:
        for tree in row:
            if (tree.height > tree.north or
                tree.height > tree.east or
                tree.height > tree.south or
                tree.height > tree.west):
                total_visible += 1
    return total_visible
            
print(f'Test: {count_visible_trees(test_forest)}')