from collections import defaultdict
import re

class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f'Y: {self.y}, X: {self.x}'
    
    def to_tuple(self):
        return (self.y, self.x)

    def in_range(self, max_y, max_x):
        if self.x < 0 or self.y < 0 or self.y>= max_y or self.x >= max_x:
            return False
        return True

def get_antinodes1(first, second):
    if not first and second:
        return None
    y1, x1 = first
    y2, x2 = second
    y_diff = abs(y2-y1)
    x_diff = abs(x2-x1)
    # print(f'y_diff {y_diff}')
    # print(f'x_diff {x_diff}')
    # Antinode 1
    # X direction
    a1 = Point(None, None)
    a2 = Point(None, None)
    if x2 > x1:
        a1.x = x1 - x_diff
        a2.x = x2 + x_diff
    elif x2 < x1:
        a1.x = x1 + x_diff
        a2.x = x2 - x_diff
    else:
        a1.x = x1
        a2.x = x2
    
    if y2 > y1: 
        a1.y = y1 - y_diff
        a2.y = y2 + y_diff
    elif y2 < y1:
        a1.y = y1 + y_diff
        a2.y = y2 - y_diff
    else:
        a1.y = y1
        a2.y = y2

    res = []
    res.append(a1)
    res.append(a2)
    return res

def get_antiondes_in_line(p1, y_max, x_max):
    

def get_antinodes2(first, second, y_max, x_max):
    if not first and second:
        return None
    y1, x1 = first
    y2, x2 = second
    y_diff = abs(y2-y1)
    x_diff = abs(x2-x1)
    print(y_diff)
    print(x_diff)
    x_dir = y_dir  = None

    a1 = Point(None, None)
    a2 = Point(None, None)
    if x2 > x1:
        
        a1.x = x1 - x_diff
        a2.x = x2 + x_diff
    elif x2 < x1:
        a1.x = x1 + x_diff
        a2.x = x2 - x_diff
    else:
        a1.x = x1
        a2.x = x2
    
    if y2 > y1: 
        a1.y = y1 - y_diff
        a2.y = y2 + y_diff
    elif y2 < y1:
        a1.y = y1 + y_diff
        a2.y = y2 - y_diff
    else:
        a1.y = y1
        a2.y = y2

    res = []
    res.append(a1)
    res.append(a2)
    return res

def part1(grid):
    antinodes = []
    ants = defaultdict(set)
    max_y = len(grid)
    max_x = len(grid[0])
    for y in range(max_y):
        for x in range(max_x):
            val = grid[y][x]
            if re.search("[a-zA-Z\d]", val):
                ants[val].add((y,x))
    
    # Iterate through antennae markers

    for key, locs in ants.items():
        locs = list(locs)
        # Iterate through all locations
        for i in range(len(locs)):
            # print(f'first: {locs[i]}')
            for j in range(i + 1, len(locs)):
                res = get_antinodes1(locs[i], locs[j])
                for point in res:
                    if point.in_range(max_y, max_x):
                        antinodes.append(point.to_tuple())
    
    return len(set(antinodes))

def part2(grid):
    antinodes = []
    ants = defaultdict(set)
    max_y = len(grid)
    max_x = len(grid[0])
    get_antinodes2((5,5),(4,3), max_y, max_x)
    return
    for y in range(max_y):
        for x in range(max_x):
            val = grid[y][x]
            if re.search("[a-zA-Z\d]", val):
                ants[val].add((y,x))
    
    # Iterate through antennae markers

    for key, locs in ants.items():
        locs = list(locs)
        # Iterate through all locations
        for i in range(len(locs)):
            # print(f'first: {locs[i]}')
            for j in range(i + 1, len(locs)):
                res = get_antinodes1(locs[i], locs[j])
                for point in res:
                    if point.in_range(max_y, max_x):
                        antinodes.append(point.to_tuple())
    
    return len(set(antinodes))
          


with open('8.test') as f:
     grid = [list(x) for x in f.read().split('\n')]
     print('Part 1: ')
     print(part1(grid))
     print('Part 2')
     print(part2(grid))
