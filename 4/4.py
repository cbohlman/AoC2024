from collections import defaultdict

def check(grid, y, x, max_y, max_x):
    # print(y,x,max_y,max_x)
    count = 0
    min_y = 0
    min_x = 0
    if grid[y][x] != 'X':
        return count
    # North
    if y - 3 >= min_y and grid[y-1][x] == 'M':
        if grid[y-2][x] == 'A':
            if grid[y-3][x] == 'S':
                count += 1
    # East
    if x + 3 < max_x and grid[y][x+1] == 'M':
        if grid[y][x+2] == 'A':
            if grid[y][x+3] == 'S':
                count += 1
    # South
    if y + 3 < max_y and grid[y+1][x] == 'M':
        if grid[y+2][x] == 'A':
            if grid[y+3][x] == 'S':
                count += 1
    # West
    if x - 3 >= min_x and grid[y][x-1] == 'M':
        if grid[y][x-2] == 'A':
            if grid[y][x-3] == 'S':
                count += 1
    # Northeast
    if y - 3 >= min_y and x + 3 < max_x and grid[y-1][x+1] == 'M':
        if grid[y-2][x+2] == 'A':
            if grid[y-3][x+3] == 'S':
                count += 1
    # Southeast
    if y + 3 < max_y and x + 3 < max_x and grid[y+1][x+1] == 'M':
        if grid[y+2][x+2] == 'A':
            if grid[y+3][x+3] == 'S':
                count += 1
    # Southwest
    if y + 3 < max_y and x - 3 >= min_x and grid[y+1][x-1] == 'M':
        if grid[y+2][x-2] == 'A':
            if grid[y+3][x-3] == 'S':
                count += 1
    # Northwest
    if y - 3 >= min_y and x - 3 >= min_x and grid[y-1][x-1] == 'M':
            if grid[y-2][x-2] == 'A':
                if grid[y-3][x-3] == 'S':
                    count += 1
    return count


def check2(grid_dict, y, x):
    valid = ['SAM', 'MAS']
    l1 = grid_dict[(y-1,x-1)] + grid_dict[(y,x)] + grid_dict[(y+1,x+1)] # top left to bottom right 
    l2 = grid_dict[(y-1,x+1)] + grid_dict[(y,x)] + grid_dict[(y+1,x-1)] # top right to bottom left
    # l3 = grid_dict[(y+1,x-1)] + grid_dict[(y,x)] + grid_dict[(y-1,x+1)] # bottom left to top right
    # l4 = grid_dict[(y+1,x+1)] + grid_dict[(y,x)] + grid_dict[(y-1,x-1)] # bottom right to top left
    if l1 in valid and l2 in valid:
        return 1
    return 0

def part1(grid):
    count = 0
    max_y = len(grid)
    max_x = len(grid[0])
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            count += check(grid, y, x, max_y, max_x)
    return count

def part2(grid_dict, max_y, max_x): # Use default dict instead 
    count = 0
    for y in range(0, max_y):
        for x in range(0, max_x):
            if (grid_dict[(y,x)] == 'A'):
                count += check2(grid_dict, y, x)

    return count



with open('4.in') as f:
    d1 = defaultdict(str)
    grid = [list(x) for x in [line.strip() for line in f]]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            d1[(y,x)] = grid[y][x]
    max_y = len(grid)
    max_x = len(grid[0])
    print(d1)
    print('Part 1: ')
    print(part1(grid))
    print('Part 2: ')
    print(part2(d1, max_y, max_x))