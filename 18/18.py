import heapq

def print_grid(grid):
    for i in range(len(grid)):
        l = []
        for j in range(len(grid[0])):
            l.append(grid[i][j])
        print(''.join(l))

def dijkstra(grid, start, end):
    max_y = len(grid)
    max_x = len(grid[0])
    dirs = [(0,1), (1,0), (0,-1),(-1,0)] # E, S, W, N
    seen = set()
    q = [(0, start)]
    while q:
        cost, pos = heapq.heappop(q)
        if pos in seen:
            continue
        if pos == end:
            return cost
        seen.add(pos)

        for dy, dx in dirs:
            ny, nx = pos[0] + dy, pos[1] + dx
            if ny < 0 or ny >= max_y or nx < 0 or nx >= max_x or grid[ny][nx] == '#':
                continue
            heapq.heappush(q, (cost+1, (ny,nx)))
    return -1

def part1(max_size, memory, steps):
    grid = []
    for i in range(max_size + 1):
        tmp = []
        for j in range(max_size + 1):
            tmp.append('.')
        grid.append(tmp)
    for i in range(steps):
        x,y = memory[i]
        grid[y][x] = '#'
    start = (0,0)
    end = (max_size, max_size)
    steps = dijkstra(grid, start, end)
    return(steps)

def part2(max_size, memory, steps):
    grid = []
    for i in range(max_size + 1):
        tmp = []
        for j in range(max_size + 1):
            tmp.append('.')
        grid.append(tmp)
    for i in range(steps):
        # print(memory[i])
        x,y = memory[i]
        grid[y][x] = '#'
    start = (0,0)
    end = (max_size, max_size)
    for i in range(steps, len(memory)):
        x,y = memory[i]
        grid[y][x] = '#'
        steps = dijkstra(grid, start, end)
        if steps == -1:
            return memory[i]


file_name = '18.in'
with open(file_name) as f:
    if file_name == '18.test':
        max_size = 6
        steps = 12
    else: 
        max_size = 70
        steps = 1024
    memory = []
    for line in f.read().split('\n'):
        x,y = line.split(',')
        memory.append((int(x), int(y)))
    print('Part 1:')
    print(part1(max_size, memory, steps))
    print('Part 2:')
    print(part2(max_size, memory, steps))