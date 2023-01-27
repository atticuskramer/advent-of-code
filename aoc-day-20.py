test_input = """1
2
-3
3
-2
0
4"""

class CircleList(list):
    
    def __getitem__(self, i):
        return super().__getitem__(i % len(self))
        
    def __setitem__(self, i, item):
        super().__setitem__(i % len(self), item)

def pos_neg_range(dif, start):
    if dif >= 0:
        return zip(range(start, start+dif), range(start + 1, start + dif + 1))
    else:
        return zip(range(start,start + dif,-1), range(start-1,start + dif -1,-1))

def mix(listy):
    mixed = CircleList(listy)
    # indices = CircleList(range(len(listy)))
    indices = CircleList([0, 0, 1, 3, 3, 5, 0])
    print(mixed, indices)
    for i in range(len(listy)):
        mixed_i = indices[i]
        num = mixed[mixed_i]
        for cur, next in pos_neg_range(num, mixed_i):
            temp = mixed[cur]
            mixed[cur] = mixed[next]
            mixed[next] = temp
        print(mixed, indices)
        
test_list = list(map(int, test_input.split('\n')))
print(mix(test_list))