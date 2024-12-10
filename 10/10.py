def get_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if int(grid[y][x]) == 0:
                trailheads.append((y,x))
    return trailheads

def find_next(path, grid, trails=[]):
    y,x = path[-1]
    print(grid[y][x])
    current = int(grid[y][x])
    next_height = current + 1
    max_y = len(grid)
    max_x = len(grid[0])
    count = 0

    dirs = [(0,-1), (-1,0), (0,1), (1,0)]

    for dy, dx in dirs:
        new_y = y + dy
        new_x = x + dx
    
        # Within Grid Limits
        if new_y < 0 or new_y >= max_y or new_x < 0 or new_x >= max_x:
            continue

        # If next cell is not valid then continue
        if grid[new_y][new_x] != next_height:
            continue

        if (new_y, new_x) in path:
            continue

        path_copy = path.copy()
        path_copy.append((new_y, new_x))

        # Exit criteria for valid trail
        if current == 8 and grid[new_y][new_x] == 9:
            trails.append(path)
        
        find_next(path_copy, grid, trails)
    return trails

    # # Left
    # if x-1 >= 0:
    #     if current == 8 and int(grid[y][x-1]) == 9:
    #         print('Valid')
    #         return 1
    #     if int(grid[y][x-1]) == next_height:
    #         count += find_next((y, x-1), next_height, grid)
    # # Up
    # if y-1 >= 0:
    #     if current == 8 and int(grid[y-1][x]) == 9:
    #         print('Valid')
    #         return 1
    #     if int(grid[y-1][x]) == next_height:
    #         count += find_next((y-1, x), next_height, grid)
    # # Right
    # if x+1< max_x:
    #     if current == 8 and int(grid[y][x+1]) == 9:
    #         print('Valid')
    #         return 1
    #     if int(grid[y][x+1]) == next_height:
    #         count += find_next((y, x+1), next_height, grid)
    # # Down
    # if y+1 < max_y:
    #     if current == 8 and int(grid[y+1][x]) == 9:
    #         print('Valid')
    #         return 1
    #     if int(grid[y+1][x]) == next_height:
    #         count += find_next((y+1, x), next_height, grid)
    # # print(count)
    # return count

def get_score(trailhead, grid):
    trails = find_next([trailhead], 0, grid)
    print(trails)

def part1(grid):
    trailheads = get_trailheads(grid)
    print(trailheads)
    for trailhead in trailheads:
        print(trailhead)
        get_score(trailhead, grid)

with open('10.test') as f:
    grid = [list(line) for line in f.read().split('\n')]
    print(grid)
    part1(grid)