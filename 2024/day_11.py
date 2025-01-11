"""Advent of Code 2024: Day 11"""

test_input = """125 17"""

def blink(nums):
    """Transform the given list of numbers according to the following rules:
    
    For each number in the list, perform the appropriate action
    1. If the number is 0, change it to 1
    2. If the number has an even number of digits, split the number into 2
       numbers, one with the first half of the digits, and one with the
       second half, keeping the location in the list the same, and dropping
       any leading 0's from the second half
    3. Otherwise, multiply the number by 2024"""
    # To start off, we will try doing this naively, though I expect we will
    # need a smarter way to do this in the future
    blinked = []
    for num in nums:
        str_num = str(num)
        if num == 0:
            blinked.append(1)
        elif len(str_num) % 2 == 0:
            first = int(str_num[:len(str_num)//2])
            second = int(str_num[len(str_num)//2:])
            blinked.extend([first, second])
        else:
            blinked.append(num * 2024)
    return blinked


def part_1(input_str):
    """Return the length of the given list of number after blinking 25 times
    
    See the blink function for specifics on what blinking does"""
    nums = [int(x) for x in input_str.split()]
    for _ in range(25):
        nums = blink(nums)
    return len(nums)

            
def part_2(input_str):
    pass
            
def main():
    with open('aoc_day_11_input.txt') as input_file:
        full_input = input_file.read()
    print(part_1(test_input))
    print(part_1(full_input))
    print(part_2(test_input))
    print(part_2(full_input))

if __name__ == '__main__':
    main()
