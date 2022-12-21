full_commands = """addx 1
addx 4
addx 1
noop
noop
addx 4
addx 1
addx 4
noop
noop
addx 5
noop
noop
noop
addx -3
addx 9
addx -1
addx 5
addx -28
addx 29
addx 2
addx -28
addx -7
addx 10
noop
noop
noop
noop
noop
addx -2
addx 2
addx 25
addx -18
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 2
addx 3
noop
addx -15
addx 8
addx -28
noop
noop
noop
addx 7
addx -2
noop
addx 5
noop
noop
noop
addx 3
noop
addx 3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 3
addx -31
addx 37
addx -28
addx -9
noop
noop
noop
addx 37
addx -29
addx 4
noop
addx -2
noop
noop
noop
addx 7
noop
noop
noop
addx 5
noop
noop
noop
addx 4
addx 2
addx 4
addx 2
addx 3
addx -2
noop
noop
addx -34
addx 6
noop
noop
noop
addx -4
addx 9
noop
addx 5
noop
noop
addx -2
noop
addx 7
noop
addx 2
addx 15
addx -14
addx 5
addx 2
addx 2
addx -32
addx 33
addx -31
addx -2
noop
noop
addx 1
addx 3
addx 2
noop
addx 2
noop
addx 7
noop
addx 5
addx -6
addx 4
addx 5
addx 2
addx -14
addx 15
addx 2
noop
addx 3
addx 4
noop
addx 1
noop
noop"""

test_commands = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

class Command:
    command_lengths = {
        'noop': 1,
        'addx': 2}
        
    def __init__(self, name, length, *args):
        self.name = name
        self.length = length
        self.args = list(args)
        
    def __str__(self):
        return f'{self.name},{self.length}'
        
def command_from_str(str):
    # We assume here that all args will be ints
    name, *args = str.split(' ')
    return Command(name, Command.command_lengths[name], *map(int, args))

class Processor:
    
    def __init__(self, commands_str):
        self.clock = 1
        self.register = 1
        self.commands = list(map(command_from_str, commands_str.split('\n')))
        # Initialize first command?
        self.command = self.commands.pop(0)
        self.command_start = 1
        
    def __str__(self):
        return f'Cycle #{self.clock}, reg={self.register}, executing {self.command} started at {self.command_start}'
    
    def tick(self):
        self.clock += 1
        if self.clock - self.command_start >= self.command.length:
            self.execute(self.command)
            try:
                self.command = self.commands.pop(0)
            except:
                self.command = None
            self.command_start = self.clock
        
    def execute(self, command):
        if command.name == 'noop':
            pass
        elif command.name == 'addx':
            self.register += command.args[0]
        else:
            print('Unrecognized command')
            
    def sum_signal_strengths(self, start=20, step=40):
        total = 0
        while self.command is not None:
            if (self.clock - start) % step == 0:
                total += self.clock * self.register
            self.tick()
        return total
        
    def generate_crt(self, width=40, height=6):
        screen = ''
        for i in range(width*height):
            if i != 0 and i % width == 0:
                screen += '\n'
            if abs(self.register - (i % width)) <= 1:
                screen += '#'
            else:
                screen += '.'
            self.tick()
        return screen
            
test_processor = Processor(test_commands)
print(test_processor.sum_signal_strengths())

full_processor = Processor(full_commands)
print(full_processor.sum_signal_strengths())

test_screen_processor = Processor(test_commands)
print(test_screen_processor.generate_crt())
print()
full_screen_processor = Processor(full_commands)
print(full_screen_processor.generate_crt())