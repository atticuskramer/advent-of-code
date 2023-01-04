# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# ##

class Rocktris:
    DEFAULT_SHAPES = [
        [[True, True, True, True]],
        
        [[False, True, False],
         [True, True, True],
         [False, True, False]],
         
        [[False, False, True],
         [False, False, True],
         [True, True, True]],
          
        [[True],
         [True],
         [True],
         [True]],
         
        [[True, True],
         [True, True]]
        ]
    
    STARTING_HEIGHT=1000
    
    ROCK = '#'
    EMPTY = '.'
    
    def __init__(self, jets, width=7, num_drops=2023, shapes=None):
        self.jets = jets
        self.width = width
        self.num_drops = num_drops
        if shapes is None:
            shapes = self.DEFAULT_SHAPES
        self.grid = [[False for _ in range(width)] for _ in range(self.STARTING_HEIGHT)]
        self.top = 0
        self.current_shape = None
        self.bottom_left = None
        
    def __str__(self):
        result = ''
        for line in self.grid:
            any_rocks = False
            line_str = ''
            for space in line:
                any_rocks = any_rocks or space
                line_str += self.ROCK if space else self.EMPTY
            result = line_str + '\n' + result
            if not any_rocks:
                break
        return result
    
    # These three functions have very similar structures. Could/should that structures
    # be abstracted out into its own function?
    def remove_shape(self):
        x,y = self.bottom_left
        for dy, row in enumerate(reversed(self.current_shape)):
            for dx, space in row:
                if space:
                    self.grid[y+dy][x+dx] = False
                    
    def try_shape(self, sx, sy):
        x, y = self.bottom_left
        for dy, row in enumerate(reversed(self.current_shape)):
            for dx, space in row:
                if space and self.grid[y+dy][x+dx]:
                    return False
        return True
                    
    def place_shape(self, sx, sy):
        x, y = self.bottom_left
        for dy, row in enumerate(reversed(self.current_shape)):
            for dx, space in row:
                if space:
                    self.grid[y+dy][x+dx] = True
        
    def move_shape(dx, dy):
        x, y = self.bottom_left
        # First check to make sure the coordinates are valid
        newx = x + dx
        newy = y + dy
        if not 0 <= newx < self.width or not 0 <= newy < len(self.grid):
            return False
        self.remove_shape()
        if self.try_shape(newx, newy):
            self.place_shape(newx, newy)
            return True
        else:
            self.place_shape(x, y)
            return False
        
print(Rocktris.DEFAULT_SHAPES)
r = Rocktris('')
print(r)
