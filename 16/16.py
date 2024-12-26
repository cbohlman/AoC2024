import heapq
from math import inf

def get_location(grid, letter):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == letter:
                return (i,j)
def get_start(grid):
    return get_location(grid,'S')

def get_end(grid):
    return get_location(grid,'E')

def dijkstra(grid, start, end):
    dirs = [(0,1), (1,0), (0,-1),(-1,0)] # E, S, W, N
    seen = set()
    q = [(0, start, 0)] # (cost, pos, direction)
    while q:
        cost, pos, direction = heapq.heappop(q)
        if (pos, direction) in seen:
            continue
        if pos == end:
            return cost
        seen.add((pos, direction))

        # Check Forwards
        fy, fx = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
        if grid[fy][fx] != '#':
            heapq.heappush(q, (cost+1, (fy,fx), direction))
        # Turn right and turn left
        heapq.heappush(q, (cost+1000, pos, (direction+1)%4)) 
        heapq.heappush(q, (cost+1000, pos, (direction-1)%4))
'''
I ended up basing this off of a reddit comment due to my failures to solve the problem. 
Source: https://old.reddit.com/r/adventofcode/comments/1hfboft/2024_day_16_solutions/m2cgw50/
'''
def new_dijkstra(grid, start, end):
    dirs = [(0,1), (1,0), (0,-1),(-1,0)] # E, S, W, N
    visited = dict()
    highscore = inf
    paths = list()
    q = [(0, start, 0, "")] # (cost, pos, direction)
    while q:
        cost, pos, direction, path = heapq.heappop(q)
        if cost > highscore:
            break
        if (pos, direction) in visited and visited[(pos,direction)] < cost:
            continue
        visited[(pos, direction)] = cost
        if pos == end:
            highscore = cost
            paths.append(path)
        # Check Forwards
        fy, fx = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
        if grid[fy][fx] != '#':
            heapq.heappush(q, (cost+1, (fy,fx), direction, path+"F"))
        # Turn right and turn left
        heapq.heappush(q, (cost+1000, pos, (direction+1)%4, path+"R")) 
        heapq.heappush(q, (cost+1000, pos, (direction-1)%4, path+"L"))
    print(highscore)
    tiles = set()
    tiles.add(start)
    for p in paths:
        t, d = (start, 1)
        for c in p:
            if c=="L": d=(d-1)%4
            elif c=="R": d=(d+1)%4
            elif c=="F":
                t = (t[0] + dirs[d][0], t[1] + dirs[d][1])
                tiles.add(t)
    return len(tiles)

def dijkstra2(grid, start, end, optimal_score):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    rows, cols = len(grid), len(grid[0])
    min_cost = {}
    prev_tiles = {}
    q = [(0, start, 0)]  # (cost, position, direction)

    # Step 1: Forward Dijkstra to find the minimum cost to the end
    while q:
        cost, pos, direction = heapq.heappop(q)

        if (pos, direction) in min_cost and cost > min_cost[(pos, direction)]:
            continue

        min_cost[(pos, direction)] = cost

        # Record the predecessors for backtracking
        if pos not in prev_tiles:
            prev_tiles[pos] = set()
        prev_tiles[pos].add((cost, direction))

        if pos == end:
            continue

        # Move forward
        fy, fx = pos[0] + dirs[direction][0], pos[1] + dirs[direction][1]
        if 0 <= fy < rows and 0 <= fx < cols and grid[fy][fx] != '#':
            next_pos = (fy, fx)
            next_cost = cost + 1
            if (next_pos, direction) not in min_cost or next_cost < min_cost.get((next_pos, direction), float('inf')):
                heapq.heappush(q, (next_cost, next_pos, direction))

        # Turn right
        right_cost = cost + 1000
        right_direction = (direction + 1) % 4
        if (pos, right_direction) not in min_cost or right_cost < min_cost.get((pos, right_direction), float('inf')):
            heapq.heappush(q, (right_cost, pos, right_direction))

        # Turn left
        left_cost = cost + 1000
        left_direction = (direction - 1) % 4
        if (pos, left_direction) not in min_cost or left_cost < min_cost.get((pos, left_direction), float('inf')):
            heapq.heappush(q, (left_cost, pos, left_direction))



    optimal_tiles = set()
    visited = set()
    stack = [end]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        optimal_tiles.add(current)

        # Find predecessors that contributed to the minimum cost
        for cost, direction in prev_tiles.get(current, []):
            if cost > optimal_score:
                continue
            # Check all possible predecessors
            for dir_idx, (dy, dx) in enumerate(dirs):
                prev_pos = (current[0] - dy, current[1] - dx)
                if 0 <= prev_pos[0] < rows and 0 <= prev_pos[1] < cols and grid[prev_pos[0]][prev_pos[1]] != '#':
                    # Validate movement cost
                    if dir_idx == direction:  # Moving forward
                        prev_cost = cost - 1
                    else:  # Turning
                        prev_cost = cost - 1000

                    if min_cost.get((prev_pos, dir_idx), float('inf')) == prev_cost and prev_pos not in visited:
                        stack.append(prev_pos)

    return optimal_tiles


def part1(grid):
    start = get_start(grid)
    end = get_end(grid)
    cost = dijkstra(grid, start, end)
    return cost

def print_paths(grid, paths):
    for i in range(len(grid)):
        l = []
        for j in range(len(grid[0])):
            if (i,j) in paths:
                l.append('O')
            else: 
                l.append(grid[i][j])
        print(''.join(l))

def part2(grid, optimal_score):
    start = get_start(grid)
    end = get_end(grid)
    return new_dijkstra(grid, start, end)
    # tiles = dijkstra2(grid, start, end, optimal_score)
    # print_paths(grid, tiles)
    # print(len(tiles))

with open('16.in') as f:
    grid = [list(line) for line in f.read().split('\n')]
    print('Part 1')
    optimal_score = part1(grid)
    print(optimal_score)
    print('Part 2')
    path_len = part2(grid, optimal_score)
    print(path_len)