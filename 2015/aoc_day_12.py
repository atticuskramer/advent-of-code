import json

def sum_nums(json_value, ignore_red=False):
    """Returns the sum of all numbers in a json_value
    
    If ignore_red is True, any Object with a property that has the
    value 'red' will not be added to the sum
    json_value can be any of the following:
        1. String
        2. Number
        3. Object (dict)
        4. Array (list)
        5. true
        6. false
        7. null"""
    if isinstance(json_value, int):
        return json_value
    elif isinstance(json_value, list):
        return sum(sum_nums(value, ignore_red=ignore_red) for value in json_value)
    elif isinstance(json_value, dict):
        if ignore_red and 'red' in json_value.values():
            return 0
        else:
            return sum(sum_nums(value, ignore_red=ignore_red) for value in json_value.values())
    else:
        return 0
    

def main():
    with open('aoc_day_12_input.txt') as input_file:
        full_input = input_file.read()
    json_object = json.loads(full_input)
    print(sum_nums(json_object))
    print(sum_nums(json_object, ignore_red=True))
    
if __name__ == '__main__':
    main()