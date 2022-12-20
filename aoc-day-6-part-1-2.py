test_signals = ["""mjqjpqmgbljsphdztnvjfqwrcgsmlb""",
'bvwbjplbgvbhsrlpgdmjqwftvncz',
'nppdvjthqldpwncqszvftbrmjlhg',
'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

def detect_packet(signal, packet_length=4):
    chars = []
    for i in range(packet_length, len(signal)+1):
        chars = signal[i-packet_length:i]
        char_set = set(chars)
        if len(char_set) == packet_length:
            return i,str(chars)
    return (-1, 'uh-oh, we never found it')
    
for signal in test_signals:
    print(signal, detect_packet(signal))
    
print(detect_packet(full_signal))