"""AoC 2015, Day 7"""

class Circuit:
    
    BITMASK = 0xFFFF
    
    def __init__(self, input_str):
        self.rules = {}
        self.values = {}
        lines = input_str.split('\n')
        for line in lines:
            tokens = line.split(' ')
            output = tokens[-1]
            # Figure out what kind of rule we have
            # This should definitely be simplified in some way using a dict
            if len(tokens) == 3:
                self.rules[output] = (self.get_value, tokens[0])
            elif tokens[0] == 'NOT':
                self.rules[output] = (self.bit_not, tokens[1])
            elif tokens[1] == 'LSHIFT':
                self.rules[output] = (self.bit_lshift, tokens[0], int(tokens[2]))
            elif tokens[1] == 'RSHIFT':
                self.rules[output] = (self.bit_rshift, tokens[0], int(tokens[2]))
            elif tokens[1] == 'OR':
                self.rules[output] = (self.bit_or, tokens[0], tokens[2])
            elif tokens[1] == 'AND':
                self.rules[output] = (self.bit_and, tokens[0], tokens[2])
                
    def reset_values(self):
        self.values = {}
                
    def get_value(self, wire):
        if wire.isdecimal():
            return int(wire)
        try:
            return self.values[wire]
        except KeyError:
            func, *args = self.rules[wire]
            value = func(*args)
            self.values[wire] = value
            return value
    
    def bit_not(self, wire):
        wire_value = self.get_value(wire)
        return ~wire_value & self.BITMASK
        
    def bit_lshift(self, wire, amt):
        wire_value = self.get_value(wire)
        return (wire_value << amt) & self.BITMASK
        
    def bit_rshift(self, wire, amt):
        wire_value = self.get_value(wire)
        # TODO: is this bitmask ever necessary?
        return (wire_value >> amt) & self.BITMASK
        
    def bit_or(self, wire1, wire2):
        wire1_value = self.get_value(wire1)
        wire2_value = self.get_value(wire2)
        return wire1_value | wire2_value
        
    def bit_and(self, wire1, wire2):
        wire1_value = self.get_value(wire1)
        wire2_value = self.get_value(wire2)
        return wire1_value & wire2_value

def main():
    with open('aoc_day_7_input.txt') as input_file:
        full_input = input_file.read()
    circuit = Circuit(full_input)
    initial_a_val = circuit.get_value('a')
    circuit.reset_values()
    circuit.values['b'] = initial_a_val
    second_a_val = circuit.get_value('a')
    print('Initial value of wire a:', initial_a_val)
    print('Value of a after setting b to initial value:', second_a_val)
    
if __name__ == '__main__':
    main()