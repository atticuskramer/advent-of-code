test_elves = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def count_calories(elves_string):
    elves = [0]
    largest = 0
    largest_line = 0
    for line in elves_string.split('\n'):
        if line == '':
            if elves[-1] > largest:
                largest = elves[-1]
                largest_index = len(elves)-1
            elves.append(0)
        else:
            elves[-1] += int(line)
    return (largest_index, largest)