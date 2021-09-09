import time

table = [
    [" ", " ", " ", " ", "x", " ", "x", " ", " ", " "],
    [" ", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", "x", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    ["x", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", " ", "x", " ", "x", " ", "x", " ", "x", " "],
    [" ", " ", "x", " ", " ", " ", "x", " ", "x", " "]
]

class Node:
    def __init__(self, g_cost, h_cost, parent, x, y):
        self.parent = parent # parent node
        self.g_cost = g_cost # distance from the start
        self.h_cost = h_cost # distance from the goal
        self.f_cost = g_cost + h_cost
        self.x = x
        self.y = y
        table[x][y] = self


    def __lt__(self, other):
        return self.f_cost < other.f_cost

    
    def __gt__(self, other):
        return self.f_cost > other.f_cost


    def __str__(self):
        return f"({self.f_cost})"

    
    def explore(self):
        open.remove(self)
        closed.append(self)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.x + i < 0 or self.x + i > 9 or self.y + j < 0 or self.y + j > 9:
                    continue
                if table[self.x + i][self.y + j] == goal:
                    goal.update(self)
                    current = table[self.x + i][self.y + j]
                    while current.parent != None:
                        table[current.x][current.y] = 'O'
                        current = current.parent
                    table[current.x][current.y] = 'O'
                    

                    for row in table:
                        for node in row:
                            if isinstance(node, Node):
                                print('[   ]', end=' ')
                            elif node == 'x':
                                print('[ x ]', end=' ')
                            elif node == '':
                                print('[   ]', end=' ')
                            else:
                                print(f'[ {node} ]', end=' ')
                        print()
                    print()

                    exit()
                if (i == 0 and j == 0) or table[self.x + i][self.y + j] == "x":
                    continue
                elif not isinstance(table[self.x + i][self.y + j], Node):
                    open.append(Node(self.g_cost + 1, abs(max(abs(self.x + i - goal.x), abs(self.y + j - goal.y))), self, self.x + i, self.y + j))
                else:
                    table[self.x + i][self.y + j].update(self)


    def update(self, other):
        if other < self and self not in closed:
            self.parent = other
            self.g_cost = other.g_cost + 1
            self.f_cost = self.g_cost + self.h_cost


start = Node(0, abs(max(1 - 9, 1 - 9)), None, 1, 1)
goal = Node(999, 999, None, 9, 9)

open = [start]
closed = []

while True:
    current = min(open)
    current.explore()