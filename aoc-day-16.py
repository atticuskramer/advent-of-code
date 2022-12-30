full_input = """Valve OS has flow rate=0; tunnels lead to valves EE, CL
Valve EN has flow rate=0; tunnels lead to valves CL, GV
Valve RR has flow rate=24; tunnels lead to valves FS, YP
Valve VB has flow rate=20; tunnels lead to valves UU, EY, SG, ZB
Valve UU has flow rate=0; tunnels lead to valves OT, VB
Valve WH has flow rate=0; tunnels lead to valves CS, JS
Valve OF has flow rate=25; tunnel leads to valve YM
Valve TY has flow rate=0; tunnels lead to valves AA, GQ
Valve RV has flow rate=0; tunnels lead to valves BT, YX
Valve GK has flow rate=0; tunnels lead to valves GD, AA
Valve EL has flow rate=0; tunnels lead to valves EK, EE
Valve OT has flow rate=9; tunnels lead to valves YR, BJ, OX, UU, HJ
Valve DG has flow rate=11; tunnels lead to valves BN, QE
Valve YR has flow rate=0; tunnels lead to valves OT, YX
Valve GV has flow rate=0; tunnels lead to valves AA, EN
Valve BN has flow rate=0; tunnels lead to valves DG, LU
Valve FS has flow rate=0; tunnels lead to valves TI, RR
Valve DW has flow rate=0; tunnels lead to valves SS, MS
Valve DJ has flow rate=0; tunnels lead to valves KY, GD
Valve BJ has flow rate=0; tunnels lead to valves OT, BT
Valve KY has flow rate=0; tunnels lead to valves EE, DJ
Valve YP has flow rate=0; tunnels lead to valves YM, RR
Valve LU has flow rate=0; tunnels lead to valves BN, CS
Valve OX has flow rate=0; tunnels lead to valves OT, XD
Valve ZB has flow rate=0; tunnels lead to valves VB, PP
Valve CL has flow rate=10; tunnels lead to valves KQ, EN, OS, MQ
Valve XD has flow rate=0; tunnels lead to valves KR, OX
Valve YM has flow rate=0; tunnels lead to valves OF, YP
Valve EY has flow rate=0; tunnels lead to valves MS, VB
Valve KQ has flow rate=0; tunnels lead to valves CS, CL
Valve SS has flow rate=0; tunnels lead to valves AA, DW
Valve SG has flow rate=0; tunnels lead to valves VB, KR
Valve EE has flow rate=22; tunnels lead to valves XR, OS, KY, EL
Valve OI has flow rate=0; tunnels lead to valves RE, MS
Valve QE has flow rate=0; tunnels lead to valves DG, GD
Valve GD has flow rate=3; tunnels lead to valves GK, DJ, MQ, QE, JS
Valve EK has flow rate=23; tunnel leads to valve EL
Valve GQ has flow rate=0; tunnels lead to valves CS, TY
Valve CS has flow rate=7; tunnels lead to valves GQ, WH, KQ, LU
Valve MS has flow rate=4; tunnels lead to valves HJ, EY, DW, OI
Valve XR has flow rate=0; tunnels lead to valves EE, AA
Valve RE has flow rate=6; tunnels lead to valves TI, PP, OI
Valve KR has flow rate=17; tunnels lead to valves XD, SG
Valve BT has flow rate=15; tunnels lead to valves BJ, RV
Valve PP has flow rate=0; tunnels lead to valves RE, ZB
Valve TI has flow rate=0; tunnels lead to valves RE, FS
Valve HJ has flow rate=0; tunnels lead to valves OT, MS
Valve AA has flow rate=0; tunnels lead to valves GK, GV, SS, XR, TY
Valve MQ has flow rate=0; tunnels lead to valves GD, CL
Valve JS has flow rate=0; tunnels lead to valves GD, WH
Valve YX has flow rate=5; tunnels lead to valves YR, RV"""

test_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

class Valve:
    def __init__(self, valve_str):
        self.name = valve_str.split('Valve ')[1][:2]
        self.flow = int(valve_str.split('rate=')[1].split(';')[0])
        if 'valves' in valve_str:
            self.connections = valve_str.split('valves ')[1].split(', ')
        else:
            self.connections = [valve_str.split('valve ')[1]]
        print(self)
            
    def __str__(self):
        return f'Valve {self.name} - flow:{self.flow}, {self.connections}'
        
    __repr__ = __str__

class Graph:
    START_VALVE = 'AA'
    
    def __init__(self, input_str):
        self.valves = {}
        lines = input_str.split('\n')
        for line in lines:
            cur_valve = Valve(line)
            if cur_valve.name == self.START_VALVE:
                self.start = cur_valve
            self.valves[cur_valve.name] = cur_valve
        self.paths = {valve: dict() for valve in self.valves}
        self.fill_paths()
    
    # Try each permutation of paths between
    # nodes with flow > 0, selecting the best performing one.  **if we had no time constraint,
    # This would be prohibitively expensive, since there are 15 valves with flow > 0 and thus
    # 15! possible permutations between them.  However, the vast majority of these paths will
    # not be explored because they would take longer than the time limit**
    # - Reasoning in ** ** was found via adventofcode subreddit
    def find_highest_flow(self, cur_valve=None, time=30, unopened=None):
        if cur_valve is None:
            cur_valve = self.start.name
        if unopened is None:
            unopened = {valve for valve in self.valves if self.valves[valve].flow > 0}
        best = 0
        for valve in unopened:
            # This is one longer than the distance, but we would need to add
            # one again anyway, to account for the step spent opening the valve
            time_to_open = len(self.paths[cur_valve][valve])
            if time_to_open < time:
                unopened.remove(valve)
                flow = self.find_highest_flow(valve, time - time_to_open, unopened)
                flow += (time - time_to_open)*self.valves[valve].flow
                unopened.add(valve)
                best = max(flow, best)
        # If every valve was too far away to open in time, best will still be 0
        return best
    
    # Returns the shortest distance between valves start_name and end_name using bfs, and
    # additionally, updates the 'distances' property for each valve on the path from the start
    # to the end for the distance to the end
    def find_path(self, start_name, end_name):
        if end_name in self.paths[start_name]:
            return self.paths[start_name][end_name]
        current = start_name
        explored = {}
        queue = [current]
        explored[current] = None
        while current != end_name:
            current = queue.pop(0)
            neighbors = [neighbor for neighbor in self.valves[current].connections if neighbor not in explored]
            for neighbor in neighbors:
                explored[neighbor] = current
            queue.extend(neighbors)
        path = [current]
        self.paths[current][end_name] = path[:]
        while explored[current] != None:
            current = explored[current]
            path.append(current)
            self.paths[current][end_name] = path[:]
        return len(path)
        
    def fill_paths(self):
        for start_valve in self.valves:
            for end_valve in self.valves:
                # There is certainly a better way to do this, there's a lot of
                # duplicate work being done here.  Ideally, the bfs algorithm would check
                # at each step to see if the rest of the path is alredy known
                self.find_path(start_valve, end_valve)

test_graph = Graph(test_input)
print(test_graph.find_highest_flow())

full_graph = Graph(full_input)
print(full_graph.find_highest_flow())