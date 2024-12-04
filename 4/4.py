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

def part1(grid):
    count = 0
    max_y = len(grid)
    max_x = len(grid[0])
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            count += check(grid, y, x, max_y, max_x)
    return count
def part2(input_lines):
    ...



with open('4.in') as f:
    grid = [list(x) for x in [line.strip() for line in f]]
    print('Part 1: ')
    print(part1(grid))
    print('Part 2: ')
    part2(grid)