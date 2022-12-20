test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def print_stacks(stacks, col_width=3, col_space=1):
    result_str = ''
    tallest_stack = max(map(len, stacks))
    for height in range(tallest_stack,0,-1):
        for stack in stacks:
            crate = str(stack[height-1]) if len(stack) >= height else ' '
            result_str += ' ' + crate + '  '
        result_str += '\n'
    for i, stack in enumerate(stacks):
        result_str += ' ' + str(i+1) + '  '
    result_str += '\n'
    print(result_str)
    return result_str

def read_stacks(stacks_str, col_width=3, col_space=1):
    # First, read in the numbers on the bottom to determine how 
    # many stacks we need
    lines = stacks_str.split('\n')
    stacks = [[] for _ in range((len(lines[-1]) +1)//(col_width+col_space))]
    # Then, read in the contents of the stacks
    for line in lines[-2::-1]:
        for i, char  in enumerate(line[col_width//2::col_width+col_space]):
            if char != ' ':
                stacks[i].append(char)
    return stacks

# Takes the string of instructions, each of the form
# 'move x from y to z' on individual lines, and returns a
# list of tuples (x,y,z)
def read_instr_str(instr_str):
    instructions = []
    for line in instr_str.split('\n'):
        words = line.split(' ')
        instructions.append((int(words[1]), int(words[3]), int(words[5])))
    return instructions
    
def run_crane(input_str):
    stacks_str, instruction_str = input_str.split('\n\n')
    stacks = read_stacks(stacks_str)
    print_stacks(stacks)
    instructions = read_instr_str(instruction_str)
    for num_crates,from_stack,to_stack in instructions:
        for _ in range(num_crates):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
    print_stacks(stacks)
    result_str = ''
    for stack in stacks:
        result_str += str(stack[-1]) if len(stack) > 0 else ' '
    return result_str
            
print(run_crane(test_input))