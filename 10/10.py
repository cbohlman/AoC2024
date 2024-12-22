def get_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if int(grid[y][x]) == 0:
                trailheads.append((y,x))
    return trailheads

def find_next(point, grid, seen, part):
    y, x = point
    max_y = len(grid)
    max_x = len(grid[0])
    if part == 1:
        if (y,x) in seen:
            return 0
        seen.add((y,x))
    if int(grid[y][x]) == 9:
        return 1
    count = 0
    dirs = [(0,-1), (-1,0), (0,1), (1,0)]
    for dy, dx in dirs:
        new_y, new_x = y + dy, x + dx
        if new_y < 0 or new_y >= max_y or new_x < 0 or new_x >= max_x:
            continue
        if int(grid[new_y][new_x]) == 1 + int(grid[y][x]):
            count += find_next((new_y, new_x), grid, seen, part)
    return count

def get_score(trailhead, grid, part):
    seen = set()
    score = find_next(trailhead, grid, seen, part)
    # print(f'head: {trailhead}, score: {score}')
    return score

def part1(grid):
    trailheads = get_trailheads(grid)
    count = 0
    for trailhead in trailheads:
        count += get_score(trailhead, grid, 1)
    return count

def part2(grid):
    trailheads = get_trailheads(grid)
    count = 0
    for trailhead in trailheads:
        count += get_score(trailhead, grid, 2)
    return count

with open('10.in') as f:
    grid = [list(line) for line in f.read().split('\n')]
    print('Part 1:')
    print(part1(grid))
    print('Part 2:')
    print(part2(grid))