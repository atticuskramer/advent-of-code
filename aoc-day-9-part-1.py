class Rope:
    def __init__(self, head=(0,0), tail=(0,0), trail=set()):
        self.head_x = head[0]
        self.head_y = head[1]
        self.tail_x = tail[0]
        self.tail_y = tail[1]
        self.trail = trail

    def __str__(self):
        return f'head:{(head_x, head_y)}, tail:{(tail_x, tail_y)}'

    def move_head(self, dir):
        if dir == 'U':
            self.head_y += 1
        elif dir == 'R':
            self.head_x += 1
        elif dir == 'D':
            self.head_y -= 1
        elif dir == 'L':
            self.head_x -= 1
        else:
            raise ValueError('Bad Direction Given')
        self.update_tail()

    def update_tail(self):
        self.trail.add(tail_x, tail_y)
        x_dif = self.head_x - self.tail_x
        y_dif = self.head_y - self.tail_y
        if abs(x_dif) > 1 or abs(y_dif) > 1:
            tail_x += x_dif
            tail_y += y_dif
