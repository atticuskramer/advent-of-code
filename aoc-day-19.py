full_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 12 clay. Each geode robot costs 4 ore and 19 obsidian.
Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 3: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 3 ore and 12 obsidian.
Blueprint 4: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 5: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 13 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 8: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 13 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 12 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 10: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 12: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 13: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 14: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 13 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 16: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 18: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 19: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 12 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 21: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 25: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 26: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 27: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 8 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 30: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 13 obsidian."""

test_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

import re

def get_all_nums_from_str(str):
    return list(map(int, re.findall(r'\d+', str)))
    
class RobotFactory:
    NADA = -1
    ORE = 0
    CLAY = 1
    OBS = 2
    GEO = 3
    
    def __init__(self, blueprint_str):
        nums = get_all_nums_from_str(blueprint_str)
        self.id = nums[0]
        # Is this over-designed? There probably is a simpler method that would work
        # For this
        self.costs = {
            self.ORE: {
                self.ORE: nums[1]
            },
            self.CLAY: {
                self.ORE: nums[2]
            },
            self.OBS: {
                self.ORE: nums[3],
                self.CLAY: nums[4]
            },
            self.GEO: {
                self.ORE: nums[5],
                self.OBS: nums[6]
            }
        }
        self.max_needed = {
            self.ORE: max(nums[2], nums[3], nums[5]),
            self.CLAY: nums[4],
            self.OBS: nums[6],
            self.GEO: 999999
        }
        self.resources = {type: 0 for type in [self.ORE, self.CLAY, self.OBS, self.GEO]}
        self.bots = {self.ORE: 1, self.CLAY: 0, self.OBS: 0, self.GEO: 0}
        self.history = []
        self.prev_states = {}
        self.counter = 0
        
    def __str__(self):
        return (f'Factory: {self.id}\n' +
                f'  Ore bot cost: {self.costs[self.ORE][self.ORE]} ore\n' +
                f'  Clay bot cost: {self.costs[self.CLAY][self.ORE]} ore\n' +
                f'  Obs bot cost: {self.costs[self.OBS][self.ORE]} ore, {self.costs[self.OBS][self.CLAY]} clay\n' +
                f'  Geo bot cost: {self.costs[self.GEO][self.ORE]} ore, {self.costs[self.GEO][self.OBS]} obs\n') # +
                # f'  {self.bots[self.ORE]} ore bots, {self.bots[self.CLAY]} clay bots, {self.bots[self.OBS]} obs bots, {self.bots[self.GEO]} geo bots\n' +
                # f'  {self.resources[self.ORE]} ore, {self.resources[self.CLAY]} clay, {self.resources[self.OBS]} obs, {self.resources[self.GEO]} geo\n')
                   
        
    def can_make_bot(self, type):
        if type == self.NADA:
            return True
        for resource, cost in self.costs[type].items():
            if self.resources[resource] < cost:
                return False
        return True
        
    def make_bot(self, type):
        if type == self.NADA:
            return
        for resource, cost in self.costs[type].items():
            self.resources[resource] -= cost
        self.bots[type] += 1
        
    def destroy_bot(self, type):
        if type == self.NADA:
            return
        for resource, cost in self.costs[type].items():
            self.resources[resource] += cost
        self.bots[type] -= 1
        
    def step(self, type):
        for bot_type, num in self.bots.items():
            self.resources[bot_type] += num
        self.make_bot(type)
        self.history.append(type)
        
    def back_up(self):
        last_bot = self.history.pop(-1)
        self.destroy_bot(last_bot)
        for bot_type, num in self.bots.items():
            self.resources[bot_type] -= num
            
    def get_state(self):
        return (self.bots[self.ORE], self.bots[self.CLAY], self.bots[self.OBS],
            self.bots[self.GEO], self.resources[self.ORE], self.resources[self.CLAY], 
            self.resources[self.OBS], self.resources[self.GEO])
            
    def add_state(self, time):
        self.prev_states[self.get_state()] = time
                
    def seen_state(self, time):
        state = self.get_state()
        if state in self.prev_states and time >= self.prev_states[state]:
            return True
        self.prev_states[state] = time
        return False
        
    def visualize_history(self, history):
        minute = 1
        for type in history:
            self.step(type)
            print('Minute', minute)
            minute += 1
            print(self)
    
    # Given the remaining time, return the maximum number of geodes that could be
    # made ASSUMING that we have the resources to make a geode factory on every
    # Subsequent step
    def upper_geode_bound(self, time):
        return self.resources[self.GEO] + self.bots[self.GEO]*time + sum(range(time))
            
    def find_max_geodes(self, time = 24, best_above = 0, options = None):
        self.counter += 1
        if time == 0:
            return self.resources[self.GEO], self.history[:]
        # If we have seen this state before elsewhere with an equal or greater amount
        # of time remaining, we can just ignore this whole branch. If we have not seen
        # the state before or have only seen it with less time available, this check will
        # update the states to include this state with the current time
        # TODO: refactor this so that the adding of the state isn't hidden
        # if self.seen_state(time):
        #     return 0, []
        # Before we go down the next step, check if it is theoretically possible
        # to improve from here
        if self.upper_geode_bound(time) <= best_above:
            return 0, []
        if options is None:
            options = [self.GEO, self.OBS, self.CLAY, self.ORE, self.NADA]
        best = 0
        best_history = []
        next_options = options[:]
        for type in options:
            if type == self.NADA:
                continue
            if self.bots[type] >= self.max_needed[type]:
                next_options.remove(type)
        buildable = [type for type in next_options if self.can_make_bot(type)]
        for type in buildable:
            self.step(type)
            geodes, history = self.find_max_geodes(time - 1, max(best, best_above), next_options)
            self.back_up()
            if geodes > best:
                best = geodes
                best_history = history
        return best, best_history
        
def part_1(input_str):
    total = 0
    for factory_str in input_str.split('\n'):
        factory = RobotFactory(factory_str)
        geodes, history = factory.find_max_geodes()
        print(factory)
        print(geodes, history)
        print()
        total += factory.id * geodes
    return total
            
# test_factory_1 = RobotFactory(test_input.split('\n')[0])
# print(test_factory_1.find_max_geodes())
# print(test_factory_1.counter)
# test_factory_2 = RobotFactory(test_input.split('\n')[1])
# print(test_factory_2.find_max_geodes())
# print(test_factory_2.counter)

print(part_1(test_input))
print(part_1(full_input))