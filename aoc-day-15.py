full_input = """Sensor at x=3907621, y=2895218: closest beacon is at x=3790542, y=2949630
Sensor at x=1701067, y=3075142: closest beacon is at x=2275951, y=3717327
Sensor at x=3532369, y=884718: closest beacon is at x=2733699, y=2000000
Sensor at x=2362427, y=41763: closest beacon is at x=2999439, y=-958188
Sensor at x=398408, y=3688691: closest beacon is at x=2275951, y=3717327
Sensor at x=1727615, y=1744968: closest beacon is at x=2733699, y=2000000
Sensor at x=2778183, y=3611924: closest beacon is at x=2275951, y=3717327
Sensor at x=2452818, y=2533012: closest beacon is at x=2733699, y=2000000
Sensor at x=88162, y=2057063: closest beacon is at x=-109096, y=390805
Sensor at x=2985370, y=2315046: closest beacon is at x=2733699, y=2000000
Sensor at x=2758780, y=3000106: closest beacon is at x=3279264, y=2775610
Sensor at x=3501114, y=3193710: closest beacon is at x=3790542, y=2949630
Sensor at x=313171, y=1016326: closest beacon is at x=-109096, y=390805
Sensor at x=3997998, y=3576392: closest beacon is at x=3691556, y=3980872
Sensor at x=84142, y=102550: closest beacon is at x=-109096, y=390805
Sensor at x=3768533, y=3985372: closest beacon is at x=3691556, y=3980872
Sensor at x=2999744, y=3998031: closest beacon is at x=3691556, y=3980872
Sensor at x=3380504, y=2720962: closest beacon is at x=3279264, y=2775610
Sensor at x=3357940, y=3730208: closest beacon is at x=3691556, y=3980872
Sensor at x=1242851, y=838744: closest beacon is at x=-109096, y=390805
Sensor at x=3991401, y=2367688: closest beacon is at x=3790542, y=2949630
Sensor at x=3292286, y=2624894: closest beacon is at x=3279264, y=2775610
Sensor at x=2194423, y=3990859: closest beacon is at x=2275951, y=3717327"""

test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def get_nums_from_str(str):
    nums = []
    in_num = False
    num_str = ''
    for char in str:
        if not in_num and (char == '-' or char.isdigit()):
            in_num = True
            num_str += char
        elif in_num and char.isdigit():
            num_str += char
        elif in_num:
            in_num = False
            nums.append(int(num_str))
            num_str = ''
        else:
            continue
    if num_str:
        nums.append(int(num_str))
    return nums

def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
    
def _overlapping(segment_1, segment_2):
    l1, r1 = segment_1
    l2, r2 = segment_2
    return (l1 <= l2 <= r1 or
            l1 <= r2 <= r1 or
            l2 <= l1 <= r2 or
            l2 <= r1 <= r2)
    
def _insert_bz(new_bz, bzs):
    left, right = new_bz
    placed = False
    i = 0
    while not placed:
        if i == len(bzs):
            bzs.append(new_bz)
            break
        bz_l, bz_r = bzs[i]
        if _overlapping(new_bz,bzs[i]):
            left = min(left, bz_l)
            right = max(right, bz_r)
            new_bz = (left, right)
            bzs.pop(i)
        elif right < bz_l:
            bzs.insert(i, (left, right))
            placed = True
        else:
            i += 1

class Searchzone:
    
    def __init__(self, input_str):
        self.sensors = {}
        self.beacons = set()
        for line in input_str.split('\n'):
            sensor_x, sensor_y, beacon_x, beacon_y = get_nums_from_str(line)
            self.sensors[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
            self.beacons.add((beacon_x, beacon_y))
    
    def __str__(self):
        return f'SearchZone with Sensors: {self.sensors}\nAnd Beacons: {self.beacons}'

    # For each sensor, find the left and right side of the area in the given row that
    # that sensor's range covers.  If one side is within a range already in our list 
    # of ranges, and the other is not, extend that range to include the new values.
    # If both sides are in different ranges, connect the two into a single range. and
    # if neither side is within the already covered ranges, add (left, right) as a new
    # covered range. Return this list of covered ranges
    def beacon_blackzones_in_row(self, row):
        blackzones = []
        for sensor, beacon in self.sensors.items():
            md = manhattan_distance(sensor,beacon)
            y_dif = abs(sensor[1] - row)
            x_dif = md - y_dif
            if x_dif > 0:
                left = sensor[0] - x_dif
                right = sensor[0] + x_dif
                _insert_bz((left, right), blackzones)
        return blackzones
        
    def part_one(self, row):
        blackzones = self.beacon_blackzones_in_row(row)
        bz_lengths = map(lambda pair: pair[1] - pair[0] + 1, blackzones)
        return sum(bz_lengths) - len([beacon for beacon in self.beacons if beacon[1] == row])
    
    # Find the beacon blackzones for each row in y_range, then for each consecutive pair
    # in the blackzone, check if it falls within the x_range. If it does, (assuming there
    # can be only one valid beacon location in the given ranges) then the beacon location
    # is in that row directly between the two ranges
    def part_two(self, x_range, y_range):
        x_start, x_end = x_range
        y_start, y_end = y_range
        for row in range(y_start, y_end):
            blackzones = self.beacon_blackzones_in_row(row)
            for (x1,x2),(x3,x4) in zip (blackzones, blackzones[1:]):
                if x1 <= x_start and x4 >= x_end:
                    return (x2+1, row)
        return (-1,-1)


test_zone = Searchzone(test_input)
print(test_zone.beacon_blackzones_in_row(10))
print(test_zone.part_one(10))
print(test_zone.part_two((0,20),(0,20)))
full_zone = Searchzone(full_input)
print(full_zone.beacon_blackzones_in_row(2000000))
print(full_zone.part_one(2000000))
print(full_zone.part_two((0,4000000), (0,4000000)))