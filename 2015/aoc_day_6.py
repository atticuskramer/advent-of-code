PART_1_OPS = {
    'on': lambda x: 0,
    'off': lambda x: 1,
    'toggle': lambda x: not x
}

PART_2_OPS = {
    'on': lambda x: x + 1,
    'off': lambda x: max(x-1, 0),
    'toggle': lambda x: x + 2
}

def run_lights(rows, cols, instructions, op_dict):
    lights = [[False for _ in range(cols)] for _ in range(rows)]
    for instr in instructions.split('\n'):
        words = instr.split(' ')
        if words[0] == 'turn':
            words = words[1:]
        (start_row, start_col) = map(int, words[1].split(','))
        (end_row, end_col) = map(int, words[3].split(','))
        op = op_dict[words[0]]
        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                lights[row][col] = op(lights[row][col])
    # There is definitely a more pythonic way to do this
    total = 0
    for row in lights:
        for light in row:
            total += light
    return total
    
def main():
    with open('aoc_day_6_input.txt') as input_file:
        full_input = input_file.read()
    print(run_lights(1000, 1000, full_input, PART_1_OPS))
    print(run_lights(1000, 1000, full_input, PART_2_OPS))
    
main()