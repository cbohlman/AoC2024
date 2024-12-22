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

def get_antinodes_in_line(p1, x_diff, y_diff, y_max, x_max):
    res = []
    res.append(p1)
    count = 0
    p2 = p1
    while True:
        a1 = Point(p1.y + y_diff, p1.x + x_diff)
        # print(f'p1: {a1}')
        a2 = Point(p2.y - y_diff, p2.x - x_diff)
        # print(f'p2: {a2}')
        # count += 1
        # if count > 1:
        #     break
        if a1.in_range(y_max, x_max):
            res.append(a1)
        if a2.in_range(y_max, x_max):
            res.append(a2)
        if not(a1.in_range(y_max, x_max)) and not(a2.in_range(y_max, x_max)):
            # print('breaking')
            break
        p1 = a1
        p2 = a2
    return res

def get_antinodes2(first, second, y_max, x_max):
    if not first and second:
        return None
    y1, x1 = first
    # print(y1, x1)
    y2, x2 = second
    # print(y2, x2)
    y_diff = y2-y1
    x_diff = x2-x1
    y_diff_abs = abs(y_diff)
    x_diff_abs = abs(x_diff)
    # print(f'y_diff {y_diff}')
    # print(f'x_diff {x_diff}')

    a1 = Point(y1, x1)
    a2 = Point(None, None)
    # print(f'a1 {a1}')
    res = get_antinodes_in_line(a1,x_diff, y_diff, y_max, x_max)
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
    # get_antinodes2((3,4),(5,5), max_y, max_x)
    # return
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
                res = get_antinodes2(locs[i], locs[j], max_y, max_x)
                for point in res:
                    if point.in_range(max_y, max_x):
                        antinodes.append(point.to_tuple())
    
    return len(set(antinodes))
          


with open('8.in') as f:
     grid = [list(x) for x in f.read().split('\n')]
     print('Part 1: ')
     print(part1(grid))
     print('Part 2')
     print(part2(grid))
