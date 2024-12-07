import copy
from time import perf_counter

def next_position(pos, direction):
    x = y = None
    if direction == 'N':
        y, x = pos
        y = y - 1
    elif direction == 'E':
        y, x = pos
        x = x + 1
    elif direction == 'S':
        y, x = pos
        y = y + 1
    elif direction == 'W':
        y, x = pos
        x = x - 1
    return (y,x)

def out_of_bounds(pos, max_y, max_x):
    y, x = pos
    if x < 0 or y < 0 or y>= max_y or x >= max_x:
        return True
    return False

def get_next_direction(direction):
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'

def walk(grid, visited, pos, direction, max_y, max_x):
    seen_obs = set()
    while True:  
        # print(pos, direction)
        next_pos = next_position(pos, direction)
        if out_of_bounds(next_pos, max_y, max_x):
            return 'oob'
        y, x = next_pos
        next_dir = direction
        if grid[y][x] == '#':
            s_obj = f'{y}{x}{next_dir}'
            if s_obj in seen_obs:
                return 'loop'
            seen_obs.add(s_obj)
            next_dir = get_next_direction(direction)
            direction = next_dir
        else:
            visited.add(next_pos)
            direction = next_dir
            pos = next_pos

def print_grid(grid):
    for line in grid:
        print(''.join(line))        

def get_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return (y,x)


def part1(grid):
    visited = set()
    start = tuple()
    max_y = len(grid)
    max_x = len(grid[0])
    start = get_start(grid)
    visited.add(start)
    walk(grid, visited, start, 'N', max_y, max_x)
    return visited

def part2(grid, path):
    count = 0
    path.remove(get_start(grid))
    visited = set()
    start = tuple()
    max_y = len(grid)
    max_x = len(grid[0])
    start = get_start(grid)
    for pos in path:
        # print('Added:', pos)
        y, x = pos
        grid_c = copy.deepcopy(grid)
        grid_c[y][x] = '#'
        # print_grid(grid)
        # print('-------------')
        # print_grid(grid_c)
        res = walk(grid_c, visited, start, 'N', max_y, max_x)
        # print(res)
        if res == 'loop':
            count += 1
    return count




def test(t):
    t.append('1')

with open('6.in') as f:
    grid = [list(x) for x in f.read().split('\n')]
    print('Part 1:')
    start = perf_counter()
    path = part1(grid)
    print(len(path))
    end = perf_counter()
    print(f'Part 1 took {end - start} sec')
    print('Part 2:')
    start = perf_counter()
    count = part2(grid, path)
    end = perf_counter()
    print(f'Part 2 took {end - start} sec')
    print(count)