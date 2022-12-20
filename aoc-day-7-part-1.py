test_cl = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class Directory:
    def __init__(self, name, children, parent=None, depth=0):
        self.name = name
        self.children = children
        self.children.sort()
        self.parent = parent
        self.depth = 0
        
    def __str__(self):
        tab_size = 2
        result_str = ' '*tab_size*self.depth + '- ' + self.name + ' (dir)\n'
        for child in self.children:
            result_str += str(child)
        return result_str
        
    def add_child(self, child):
        # Could certainly be smarter about inserting this to avoid needing sort
        self.children.append(child)
        self.children.sort(key=lambda c: c.name)
        child.depth = self.depth + 1
        child.parent = self
        
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError('No child named ' + name)
        
    def get_size(self):
        return sum(map(lambda x: x.get_size(), self.children))
        
class File:
    def __init__(self, name, size, parent=None, depth=0):
        self.name = name
        self.size = size
        self.parent = parent
        self.depth = depth
        
    def __str__(self):
        tab_size = 2
        return ' '*tab_size*self.depth + '- ' +self.name + ' (file, size=' + str(self.size) + ')\n'
        
    def get_size(self):
        return self.size
        
def build_fs(cl):
    lines = cl.split('\n')
    if lines[0] != '$ cd /':
        print('bad input')
        return -1
    wd = bd = Directory('/', [])
    for line in lines[1:]:
        parts = line.split(' ')
        if parts[0] == '$' and parts[1] == 'cd':
            if parts[2] == '/':
                wd = bd
            elif parts[2] == '..':
                wd = wd.parent
            else:
                wd = wd.get_child(parts[2])
        elif parts[0] == '$' and parts[1] == 'ls':
            continue
        elif parts[0] == 'dir':
            wd.add_child(Directory(parts[1], [], wd, wd.depth+1))
        else:
            wd.add_child(File(parts[1], int(parts[0]), wd, wd.depth+1))
    return bd
    
# Returns a list of pairs of type (dir, size)
def get_dirs_under_size(dir, max_size=100000):
    dirs = []
    size = 0
    for child in dir.children:
        # This could be more efficient.  We are traversing the tree twice, once
        # to calculate the sizes, and then again to get the dirs under the max_size
        size += child.get_size()
        if isinstance(child, Directory):
            dirs.extend(get_dirs_under_size(child, 100000))
    if size <= 100000:
        dirs.append((dir.name,size))
    return dirs
    
def main(cl_str):
    dir = build_fs(cl_str)
    total = 0
    relevant_dirs = get_dirs_under_size(dir)
    for sd, size in relevant_dirs:
        total += size
    return total
    
                
test_fs = build_fs(test_cl)
print(test_fs)
print(get_dirs_under_size(test_fs))
print('Final answer test:', main(test_cl))