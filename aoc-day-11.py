full_input = """Monkey 0:
  Starting items: 76, 88, 96, 97, 58, 61, 67
  Operation: new = old * 19
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 93, 71, 79, 83, 69, 70, 94, 98
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 2:
  Starting items: 50, 74, 67, 92, 61, 76
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 76, 92
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 4:
  Starting items: 74, 94, 55, 87, 62
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 59, 62, 53, 62
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 62
  Operation: new = old + 2
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 7:
  Starting items: 85, 54, 53
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0"""

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

class Monkey:
    def __init__(self, id_num, items, op, test, divisor):
        self.id_num = id_num
        self.items = items
        self.op = op
        self.test = test
        # This is duplicated information from test. Could be more efficient
        self.divisor = divisor
        self.items_inspected = 0
        
    def __str__(self):
        return f'Monkey {self.id_num}. Carrying {self.items}'
        
    __repr__ = __str__
        
    def business(self, monkeys, lcm, part_one=False):
        for item in self.items:
            new_value = self.op(item)
            if part_one:
                new_value //= 3
            new_value = new_value % lcm
            to_monkey = self.test(new_value)
            for monkey in monkeys:
                if monkey.id_num == to_monkey:
                    monkey.items.append(new_value)
                    break
            self.items_inspected += 1
        self.items.clear()
        
        
def monkey_from_str(str):
    op_funcs = {'+': lambda x,y: x+y,
                '*': lambda x,y: x*y}
    # This should probably be done with regexes instead
    lines = str.split('\n')
    id_num = int(lines[0].split(' ')[1].split(':')[0])
    items = list(map(int, lines[1].split(':')[1].split(',')))
    _,_,first,func_str,second = lines[2].split(': ')[1].split(' ')
    op_func = op_funcs[func_str]
    op = lambda x: op_func(x if first == 'old' else int(first), x if second == 'old' else int(second))
    # For now, we will assume the test will always be divisibility
    divisor = int(lines[3].split(' ')[-1])
    true_monkey = int(lines[4].split(' ')[-1])
    false_monkey = int(lines[5].split(' ')[-1])
    test = lambda x: true_monkey if x % divisor == 0 else false_monkey
    return Monkey(id_num, items, op, test, divisor)
    
def monkey_toss(input_str, num_rounds, part_one=False):
    monkeys = [monkey_from_str(str) for str in input_str.split('\n\n')]
    # Calculate the leat common multiple (lcm) for all the monkeys test divisors.
    # Then, we can replace the original worry level with (worry level % lcm) without
    # worrying about changing the results of any divisor tests.  THIS SOLUTION WAS
    # FOUND ONLINE.
    # In this specialized case, we can just multiply all the divisors together, since
    # looking at the input, we can tell they are all prime
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.divisor
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey.business(monkeys, lcm, part_one)
    print(monkeys)
    largest = -1
    second_largest = -1
    for monkey in monkeys:
        if monkey.items_inspected > largest:
            second_largest = largest
            largest = monkey.items_inspected
        elif monkey.items_inspected > second_largest:
            second_largest = monkey.items_inspected
    return largest * second_largest
        
        
#print(monkey_toss(test_input, 200, False))

print(monkey_toss(full_input, 10000))
    