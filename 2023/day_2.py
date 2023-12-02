"""Advent of Code 2023: Day 2"""

def game_from_string(game_str):
    """Given a game string, returns a tuple of game id and a list of pulls
    
    game_string is of the form: 
    'Game n: x red, y green, z blue; y_2 green, x_2 red; ...'
    where the game id is n, and a pull is a tuple of the form
    (x,y,z) where x is the number of red cubes in the pull,
    y is green and z is blue.
    
    Note that red, green, and blue need not appear in that
    order in the original string, if a color has zero pulled
    it will not appear in the string at all, and there can
    be any arbitrary number of pulls in a game"""
    label, pulls_str = game_str.split(':')
    id = int(label.split(' ')[1])
    pulls = []
    for pull in pulls_str.split(';'):
        red = green = blue = 0
        for cube_type in pull.split(','):
            _,num_string,color = cube_type.split(' ')
            num = int(num_string)
            if color == 'red':
                red = num
            elif color == 'green':
                green = num
            elif color == 'blue':
                blue = num
        pulls.append((red, green, blue))
    return (id, pulls)
    
def part_1(input_str):
    """Given the list of games, returns the sum games possible given the max allowed pull
    
    The max allowed pull is 12 red, 13 green, and 14 blue.
    So if any pull of a particular game has a greater number
    of cubes of any color, it is rejected"""
    MAX_ALLOWED_RED = 12
    MAX_ALLOWED_GREEN = 13
    MAX_ALLOWED_BLUE = 14
    total = 0
    def is_pull_allowed(pull):
        "Given a pull, just tells us if each value is under the max"
        return (pull[0] <= MAX_ALLOWED_RED and
                pull[1] <= MAX_ALLOWED_GREEN and
                pull[2] <= MAX_ALLOWED_BLUE)
                
    for game_str in input_str.split('\n'):
        id, pulls = game_from_string(game_str)
        if all([is_pull_allowed(pull) for pull in pulls]):
            total += id
    return total
    
def part_2(input_str):
    """Given the list of games, returns the sum of the power of the minimum possible cubes for each game
    
    The minimum possible cubes is the necessary number to
    make each pull in the game possible (i.e. the maximum
    number of each color across all cubes). The power of the
    pull is all the minimum possible cube numbers multiplied
    together"""
    total = 0
    for game_str in input_str.split('\n'):
        min_red = min_green = min_blue = 0
        id, pulls = game_from_string(game_str)
        for red, green, blue in pulls:
            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)
        total += min_red * min_green * min_blue
    return total

def main():
    with open aoc_day_2_input.txt as input_file:
        full_input = input_file.read()
    print(part_1(full_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
