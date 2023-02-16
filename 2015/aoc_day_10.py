def look_and_say(num_string):
    i = 0
    cur_char = ''
    count = 0
    result = ''
    while i < len(num_string):
        if num_string[i] == cur_char:
            count += 1
        else:
            if count > 0:
                result += str(count) + cur_char
            cur_char = num_string[i]
            count = 1
        i += 1
    if count > 0:
        result += str(count) + cur_char
    return result
    
def repeated_look_and_say(num_string, repetitions):
    for _ in range(repetitions):
        num_string = look_and_say(num_string)
    return num_string
    
print(look_and_say('11234'))
print(repeated_look_and_say('11234', 5))
print(len(repeated_look_and_say('1113122113', 40)))
print(len(repeated_look_and_say('1113122113', 50)))