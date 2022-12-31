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
        
    def find_elephant_flow(self, cur_valve=None, cd=0, ele_cur_valve=None, ele_cd=0, cur_flow=0, time=26, unopened=None):
        if time == 0:
            return (0, ([],[]))
        if cur_valve is None:
            cur_valve = self.start.name
        if ele_cur_valve is None:
            ele_cur_valve = self.start.name
        if unopened is None:
            unopened = [valve for valve in self.valves if self.valves[valve].flow > 0]
        best = 0
        path = []
        ele_path = []
        if cd == 0 and ele_cd == 0 and unopened:
            cur_flow += self.valves[cur_valve].flow + self.valves[ele_cur_valve].flow
            for i, valve in enumerate(unopened):
                #unopened.remove(valve)
                ele_picks = unopened[:i] + unopened[i+1:]
                for j, ele_valve in enumerate(ele_picks):
                    #unopened.remove(ele_valve)
                    next_unopened = ele_picks[:j] + ele_picks[j+1:]
                    # This is one longer than the distance, but we would need to add
                    # one again anyway, to account for the step spent opening the valve
                    time_to_open = len(self.paths[cur_valve][valve])
                    ele_time_to_open = len(self.paths[ele_cur_valve][ele_valve])
                    flow, paths = self.find_elephant_flow(valve, time_to_open-1, ele_valve, ele_time_to_open-1, cur_flow, time-1, next_unopened)
                    flow += cur_flow
                    if flow > best:
                        best = flow
                        path, ele_path = paths
                        path.extend(self.paths[cur_valve][valve])
                        ele_path.extend(self.paths[ele_cur_valve][ele_valve])
                    #unopened.add(ele_valve)
                #unopened.add(valve)
        elif cd == 0 and unopened:
            cur_flow += self.valves[cur_valve].flow
            for i, valve in enumerate(unopened):
                next_unopened = unopened[:i] + unopened[i+1:]
                #unopened.remove(valve)
                time_to_open = len(self.paths[cur_valve][valve])
                flow, paths = self.find_elephant_flow(valve, time_to_open-1, ele_cur_valve, ele_cd-1, cur_flow, time-1, next_unopened)
                flow += cur_flow
                if flow > best:
                    best = flow
                    path, ele_path = paths
                    path.extend(self.paths[cur_valve][valve])
                #unopened.add(valve)
        elif ele_cd == 0 and unopened:
            cur_flow += self.valves[ele_cur_valve].flow
            for i, ele_valve in enumerate(unopened):
                next_unopened = unopened[:i] + unopened[i+1:]
                # unopened.remove(ele_valve)
                ele_time_to_open = len(self.paths[ele_cur_valve][ele_valve])
                flow, paths = self.find_elephant_flow(cur_valve, cd-1, ele_valve, ele_time_to_open-1, cur_flow, time-1, next_unopened)
                flow += cur_flow
                if flow > best:
                    best = flow
                    path, ele_path = paths
                    ele_path.extend(self.paths[ele_cur_valve][ele_valve])
                # unopened.add(ele_valve)
        if best == 0:
            best, paths = self.find_elephant_flow(cur_valve, cd-1, ele_cur_valve, ele_cd-1, cur_flow, time-1, unopened)
            best += cur_flow
            path, ele_path = paths
        # print('At time', time, 'best is', best)
        return (best, (path, ele_path))
    
    # def find_elephant_flow(self, cur_valve=None, cd=0, ele_cur_valve=None, ele_cd=0, cur_flow=0, time=26, unopened=None):
    #     if time == 0:
    #         return (0, ([], []))
    #     if cur_valve is None:
    #         cur_valve = self.start.name
    #     if ele_cur_valve is None:
    #         ele_cur_valve = self.start.name
    #     if unopened is None:
    #         unopened = [name for name,valve in self.valves.items() if valve.flow > 0]
        
    #     best = 0 
    #     next_kwargs_list = []
    #     if cd == 0 and ele_cd == 0:
    #         for valve in unopened:
    #             for ele_valve in unopened:
    #                 if valve != ele_valve:
    #                     new_cd = len(self.paths[cur_valve][valve])
    #                     new_ele_cd = len(self.paths[ele_cur_valve][ele_valve])
    #                     added_flow = self.valves[cur_valve].flow + self.valves[ele_cur_valve].flow
    #                     if new_cd < time or new_ele_cd < time:
    #                         next_kwargs = {
    #                             'cur_valve': valve,
    #                             'ele_cur_valve': ele_valve,
    #                             'cd': new_cd - 1,
    #                             'ele_cd': new_ele_cd - 1,
    #                             'cur_flow': cur_flow + self.valves[cur_valve].flow + self.valves[ele_cur_valve].flow,
    #                             'time': time - 1,
    #                             'unopened': [v for v in unopened if v != valve and v != ele_valve]
    #                         }
    #                         next_kwargs_list.append((added_flow, next_kwargs))
    #     elif cd == 0:
    #         for valve in unopened:
    #             new_cd = len(self.paths[cur_valve][valve])
    #             added_flow = self.valves[cur_valve].flow
    #             if new_cd < time:
    #                 next_kwargs = {
    #                     'cur_valve': valve,
    #                     'ele_cur_valve': ele_cur_valve,
    #                     'cd': new_cd - 1,
    #                     'ele_cd': ele_cd - 1,
    #                     'cur_flow': cur_flow + self.valves[cur_valve].flow,
    #                     'time': time - 1,
    #                     'unopened': [v for v in unopened if v != valve]
    #                 }
    #                 next_kwargs_list.append((added_flow, next_kwargs))
    #     elif ele_cd == 0:
    #         for ele_valve in unopened:
    #             new_ele_cd = len(self.paths[ele_cur_valve][ele_valve])
    #             added_flow = self.valves[ele_cur_valve].flow
    #             if new_ele_cd < time:
    #                 next_kwargs = {
    #                     'cur_valve': cur_valve,
    #                     'ele_cur_valve': ele_valve,
    #                     'cd': cd - 1,
    #                     'ele_cd': new_ele_cd - 1,
    #                     'cur_flow': cur_flow + self.valves[ele_cur_valve].flow,
    #                     'time': time - 1,
    #                     'unopened': [v for v in unopened if v != ele_valve]
    #                 }
    #                 next_kwargs_list.append((added_flow, next_kwargs))
    #     for added_flow, kwargs in next_kwargs_list:
    #         next_flow, paths = self.find_elephant_flow(**kwargs)
    #         next_flow += added_flow
    #         if next_flow > best:
    #             best = next_flow
    
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
print(test_graph.find_elephant_flow(time=26))

full_graph = Graph(full_input)
print(full_graph.find_highest_flow())
#print(full_graph.find_elephant_flow())