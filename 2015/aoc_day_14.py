"""Advent of Code: 2015, Day 14"""

class Reindeer:
    """Simple class to represent a flying reindeer
    
    A reindeer is capable of flying at flight_speed for flight_time.
    It then must rest for rest_time before it can start flying again"""
    def __init__(self, name, flight_speed, flight_time, rest_time):
        self.name = name
        self.flight_speed = flight_speed
        self.flight_time = flight_time
        self.rest_time = rest_time
        
    def distance_after(self, time):
        """Return the reindeers distance travelled after time
        
        This assumes the reindeer starts flying immediately and only
        stops when it has to do so to rest"""
        cycles = time // (self.flight_time + self.rest_time)
        cycle_distance = self.flight_time * self.flight_speed
        remaining = time % (self.flight_time + self.rest_time)
        remaining = min(remaining, self.flight_time)
        return (cycles * cycle_distance) + (remaining * self.flight_speed)
        
def make_reindeer_list(input_str):
    """Return a list of reindeer created from the input string"""
    reindeers = []
    for line in input_str.split('\n'):
        words = line.split()
        name = words[0]
        flight_speed = int(words[3])
        flight_time = int(words[6])
        rest_time = int(words[13])
        reindeers.append(Reindeer(name, flight_speed, flight_time, rest_time))
    return reindeers
        
def find_winning_reindeer(reindeers, time):
    """Return the name and distance of the winning reindeer after time"""
    best = 0
    for reindeer in reindeers:
        distance = reindeer.distance_after(time)
        if distance > best:
            best = distance
            name = reindeer.name
    return name, best

# This function is ugly and unpythonic, but hey, it works
def find_winning_reindeer_scored(reindeers, time):
    """Return the winning reindeer, given the following scoring system
    
    At each second, a reindeer gets 1 point if it has currently
    travelled the farthest distance or is tied for farthest. The
    reindeer with the most points after 'time' wins"""
    scores = {reindeer.name: 0 for reindeer in reindeers}
    for i in range(1,time+1):
        best = 0
        best_list = []
        for reindeer in reindeers:
            distance = reindeer.distance_after(i)
            if distance == best:
                best_list.append(reindeer.name)
            elif distance > best:
                best = distance
                best_list = [reindeer.name]
        for rein_name in best_list:
            scores[rein_name] += 1
    best_score = 0
    rein_name = None
    for reindeer, score in scores.items():
        if score > best_score:
            best_score = score
            rein_name = reindeer
    return rein_name, best_score
        
    
def main():
    with open('aoc_day_14_input.txt') as input_file:
        full_input = input_file.read()
    reindeer_list = make_reindeer_list(full_input)
    print(find_winning_reindeer(reindeer_list, 2503))
    print(find_winning_reindeer_scored(reindeer_list, 2503))
    
if __name__ == '__main__':
    main()
