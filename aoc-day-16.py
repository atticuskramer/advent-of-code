def valve_from_str(str):
    name = str.split('Valve ')[1][:2]
    flow = int(str.split('rate=')[1].split(';')[0])
    valves = str.split('valves ')[1].split(', ')
    print(f'{name}, {flow}, {valves}')
