"""Advent of Code: Day 3"""

def deliver_presents(directions, num_deliverers):
    """Get the set of homes visited based on 'directions'
    
    directions is a string of characters in [^, v, <, >]
    Returns a dictionary with keys of the locations visited
    and values of the number of times the location was visited"""
    visited = {(0,0): 1}
    locations = [[0,0] for _ in range(num_deliverers)]
    cur_deliverer = 0
    for direction in directions:
        if direction == '>':
            locations[cur_deliverer][0] += 1
        elif direction == 'v':
            locations[cur_deliverer][1] += 1
        elif direction == '<':
            locations[cur_deliverer][0] -= 1
        elif direction == '^':
            locations[cur_deliverer][1] -= 1
        loc_tuple = tuple(locations[cur_deliverer])
        if loc_tuple in visited:
            visited[loc_tuple] += 1
        else:
            visited[loc_tuple] = 1
        cur_deliverer = (cur_deliverer + 1) % num_deliverers
    return visited

def part_1(directions):
    """Return the number of houses visited"""
    visited = deliver_presents(directions, 1)
    return len(visited)

def part_2(directions):
    """Return the number of houses visited, using 2 alternating deliverers"""
    visited = deliver_presents(directions, 2)
    return len(visited)

def main():
    """Run parts 1 and 2 and print results"""
    with open('aoc_day_3_input.txt', encoding='utf-8') as input_file:
        full_input = input_file.read()
    print('Houses visited with 1 santa:', part_1(full_input))
    print('Houses visited with 2 alternating santas:', part_2(full_input))


if __name__ == '__main__':
    main()
