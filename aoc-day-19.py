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
        self.resources = {type: 0 for type in [self.ORE, self.CLAY, self.OBS, self.GEO]}
        self.bots = {self.ORE: 1, self.CLAY: 0, self.OBS: 0, self.GEO: 0}
        self.history = []
        
    def __str__(self):
        return (f'Factory: {self.id}\n' +
                f'  Ore bot cost: {self.costs[self.ORE][self.ORE]} ore\n' +
                f'  Clay bot cost: {self.costs[self.CLAY][self.ORE]} ore\n' +
                f'  Obs bot cost: {self.costs[self.OBS][self.ORE]} ore, {self.costs[self.OBS][self.CLAY]} clay\n' +
                f'  Geo bot cost: {self.costs[self.GEO][self.ORE]} ore, {self.costs[self.GEO][self.OBS]} obs\n' +
                f'  {self.bots[self.ORE]} ore bots, {self.bots[self.CLAY]} clay bots, {self.bots[self.OBS]} obs bots, {self.bots[self.GEO]} geo bots\n' +
                f'  {self.resources[self.ORE]} ore, {self.resources[self.CLAY]} clay, {self.resources[self.OBS]} obs, {self.resources[self.GEO]} geo\n')
                   
        
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
    
    # Given the remaining time, return the maximum number of geodes that could be
    # made ASSUMING that we have the resources to make a geode factory on every
    # Subsequent step
    def upper_geode_bound(self, time):
        return self.resources[self.GEO] + self.bots[self.GEO]*time + sum(range(time))
            
    def find_max_geodes(self, time, best_above = 0):
        if time == 0:
            return self.resources[self.GEO]
        # Before we go down the next step, check if it is theoretically possible
        # to improve from here
        if self.upper_geode_bound(time) <= best_above:
            return 0
        best = 0
        options = [self.GEO, self.OBS, self.CLAY, self.ORE, self.NADA]
        buildable = [type for type in options if self.can_make_bot(type)]
        for type in buildable:
            self.step(type)
            geodes = self.find_max_geodes(time - 1, max(best, best_above))
            self.back_up()
            best = max(geodes, best)
        return best
            
test_factory_1 = RobotFactory(test_input.split('\n')[0])
print(test_factory_1.find_max_geodes(24))