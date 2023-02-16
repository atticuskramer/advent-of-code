import math

class UndirectedGraph:
    
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    @classmethod
    def from_edges_string(cls, edges_string):
        graph = cls()
        for edge_string in edges_string.split('\n'):
            tokens = edge_string.split()
            node_a = tokens[0]
            node_b = tokens[2]
            weight = int(tokens[4])
            graph.add_double_edge(node_a, node_b, weight)
        return graph
        
    def add_node(self, name):
        self.nodes.add(name)
        
    def add_edge(self, node_a, node_b, weight):
        self.nodes.add(node_a)
        self.nodes.add(node_b)
        if node_a in self.edges:
            self.edges[node_a][node_b] = weight
        else:
            self.edges[node_a] = {node_b: weight}
            
    def add_double_edge(self, node_a, node_b, weight):
        self.add_edge(node_a, node_b, weight)
        self.add_edge(node_b, node_a, weight)
        
    def shortest_path_starting_at(self, node):
        visited = set()
        path = [node]
        cur_node = node
        next_edges = self.edges[node]
        while next_edges:
            min_weight = math.inf
            for edge, weight in next_edges.items():
                if weight < min_weight:
                    min_weight = weight
                    next = edge
            path.append(next)
            visited.add(cur_node)
            next_edges = {x: self.edges[next][x] for x in self.edges[next] if x not in visited}
            cur_node = next
        return path
        
    def longest_path_starting_at(self, node):
        visited = set()
        path = [node]
        cur_node = node
        next_edges = self.edges[node]
        while next_edges:
            max_weight = -math.inf
            for edge, weight in next_edges.items():
                if weight > max_weight:
                    max_weight = weight
                    next = edge
            path.append(next)
            visited.add(cur_node)
            next_edges = {x: self.edges[next][x] for x in self.edges[next] if x not in visited}
            cur_node = next
        return path
        
    def shortest_ham_path(self):
        shortest_path = None
        shortest_length = math.inf
        for node in self.nodes:
            path = self.shortest_path_starting_at(node)
            length = 0
            for start_node, end_node in zip(path, path[1:]):
                length += self.edges[start_node][end_node]
            if length < shortest_length:
                shortest_length = length
                shortest_path = path
        return shortest_path, shortest_length
    
    def longest_ham_path(self):
        longest_path = None
        longest_length = -math.inf
        for node in self.nodes:
            path = self.longest_path_starting_at(node)
            length = 0
            for start_node, end_node in zip(path, path[1:]):
                length += self.edges[start_node][end_node]
            if length > longest_length:
                longest_length = length
                longest_path = path
        return longest_path, longest_length
                
def main():
    with open('aoc_day_9_input.txt') as input_file:
        full_input = input_file.read()
    graph = UndirectedGraph.from_edges_string(full_input)
    print(graph.nodes)
    print(graph.edges)
    print(graph.shortest_ham_path())
    print(graph.longest_ham_path())

if __name__ == '__main__':
    main()