test_elves = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def count_calories(elves_string):
    elves = [0]
    first = 0
    second = 0
    third = 0
    for line in elves_string.split('\n'):
        if line == '':
            if elves[-1] > first:
                third = second
                second = first
                first = elves[-1]
            elif elves[-1] > second:
                third = second
                second = elves[-1]
            elif elves[-1] > third:
                third = elves[-1]
            elves.append(0)
        else:
            elves[-1] += int(line)
    return first + second + third