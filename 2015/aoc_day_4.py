"""Advent of Code: 2015 Day 4"""

import hashlib

def mine_coin(code, hex_start):
    """Return the first number that yields a 'hex_start...' hash when appended to 'code'"""
    num = 0
    while True:
        hash_string = code + str(num)
        md5_hash = hashlib.md5(hash_string.encode('utf-8'))
        md5_hex = md5_hash.hexdigest()
        if md5_hex.startswith(hex_start):
            return num
        num += 1

def main():
    """Run parts 1 and 2 and print results"""
    with open('aoc_day_4_input.txt', encoding='utf-8') as input_file:
        full_input = input_file.read()
    print('First number that yields 00000 hash:', mine_coin(full_input, '00000'))
    print('First number that yields 000000 hash:', mine_coin(full_input, '000000'))


if __name__ == '__main__':
    main()
