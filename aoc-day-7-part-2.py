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

# For part 1, we tried to calculate directory sizes on the fly, but this was annoying
# and inefficient, so for part 2, size will just be a property of directories that is
# updated any time a file is added or removed (not currently possible) from the fs
# (part 1 has also been retrofitted to this solution)

# In retrospect it might have been a good idea to have an overarching FileSystem class,
# rather than having the base class just be a Directory with name '/'

class Directory:
    def __init__(self, name, children, size=0, parent=None, depth=0):
        self.name = name
        self.children = children
        self.children.sort()
        self.size = sum(map(lambda x: x.size, self.children))
        self.parent = parent
        self.depth = depth
        
    def __str__(self):
        tab_size = 2
        result_str = ' '*tab_size*self.depth + '- ' + self.name + ' (dir, size='+str(self.size)+')\n'
        for child in self.children:
            result_str += str(child)
        return result_str
        
    def add_child(self, child):
        # Could certainly be smarter about inserting this to avoid needing sort
        self.children.append(child)
        self.children.sort(key=lambda c: c.name)
        child.depth = self.depth + 1
        child.parent = self
        # Update dir sizes back up the tree
        current = self
        while current != None:
            current.size += child.size
            current = current.parent
        
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError('No child named ' + name)
        
    def get_size(self):
        return self.size
        
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
    for child in dir.children:
        if isinstance(child, Directory):
            dirs.extend(get_dirs_under_size(child, 100000))
    if dir.size <= 100000:
        dirs.append((dir.name,dir.size))
    return dirs

# Given a directory dir, returns the smallest directory in its tree (including itself)
# that, if deleted, would create free space of size needed_space, assuming the directory
# has size total_space
def get_smallest_dir_over(dir, total_space=70000000, needed_space=30000000):
    min_size = needed_space - (total_space - dir.size)
    return get_smallest_helper(dir, min_size)
    
def get_smallest_helper(dir, min_size):
    smallest = None
    for child in filter(lambda x: isinstance(x, Directory), dir.children):
        child_smallest = get_smallest_helper(child, min_size)
        if child_smallest and child_smallest > min_size and (smallest is None or child_smallest < smallest):
            smallest = child_smallest
            print('Passing up:', child.name, ', size:', child_smallest)
    if smallest is None and dir.size > min_size:
        smallest = dir.size
        print('Found new smallest, dir:', dir.name, ', size:', dir.size)
    return smallest
    
def main_part_one(cl_str):
    dir = build_fs(cl_str)
    total = 0
    relevant_dirs = get_dirs_under_size(dir)
    for sd, size in relevant_dirs:
        total += size
    return total
    
def main_part_two(cl_str):
    dir = build_fs(cl_str)
    return get_smallest_dir_over(dir)
    
                
test_fs = build_fs(test_cl)
print(test_fs)
print(get_dirs_under_size(test_fs))
print('Part one answer - test:', main_part_one(test_cl))
print('Part two answer - test:', main_part_two(test_cl))

full_fs = build_fs(full_cl)
print(full_fs)
print(full_fs.get_size())
print('Part one answer - full:', main_part_one(full_cl))
print('Part two answer - full:', main_part_two(full_cl))