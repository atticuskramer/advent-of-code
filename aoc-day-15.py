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
    # that sensor's range covers, and if either of those fall outside the total range
    # covered by sensors already checked, set them to be the new left and/or right
    def beacon_blackzones_in_row(self, row):
        left = right = None
        for sensor, beacon in self.sensors.items():
            md = manhattan_distance(sensor,beacon)
            y_dif = abs(sensor[1] - row)
            x_dif = md - y_dif
            sensor_left = sensor[0] - x_dif
            sensor_right = sensor[0] + x_dif
            if left is None:
                left = sensor_left
            else:
                left = min(left, sensor_left)
            if right is None:
                right = sensor_right
            else:
                right = max(right, sensor_right)
        total = (right - left) + 1 - len([beacon for beacon in self.beacons if beacon[1] == row])
        return total

test_zone = Searchzone(test_input)
print(test_zone.beacon_blackzones_in_row(10))
full_zone = Searchzone(full_input)
print(full_zone.beacon_blackzones_in_row(2000000))
        