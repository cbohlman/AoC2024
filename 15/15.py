def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return (i,j)
            
def print_grid(grid):
    for line in grid:
        print(''.join(line))
            
def get_move(move):
    dy = dx = 0
    if move == '^':
        dy = -1
    elif move == '>':
        dx = 1
    elif move == 'v':
        dy = 1
    elif move == '<':
        dx = -1
    
    return (dy, dx)

def is_valid(pos, direction, grid):
    max_y = len(grid)
    max_x = len(grid[0])
    y,x = pos
    if y < 0 or y >= max_y or x < 0 or x >= max_x:
        return False
    if grid[y][x] == '#':
        return False
    if grid[y][x] == '.':
        return True
    if grid[y][x] == 'O':
        dy, dx = direction
        new_y, new_x = y + dy, x + dx
        valid = is_valid((new_y, new_x), direction, grid)
        if valid:
            grid[new_y][new_x] = 'O'
            return True

        
def get_coords(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O' or grid[i][j] == '[':
                count += (100*i + j)
    return count

            
def process_move(grid, move, pos):
    dy, dx = get_move(move)
    new_y, new_x = pos[0] + dy, pos[1] + dx
    if is_valid((new_y, new_x), (dy, dx), grid):
        grid[new_y][new_x] = '@'
        grid[pos[0]][pos[1]] = '.'
        return (new_y, new_x)
    return pos


def part1(grid, moves):
    grid = [list(line) for line in grid.split('\n')]
    start = find_start(grid)
    pos = start
    for move in moves:
        if move == '\n':
            continue
        pos = process_move(grid, move, pos)
        # print_grid(grid)
        # print('----------')
    return get_coords(grid)

def out_of_bounds(pos, grid):
    max_y = len(grid)
    max_x = len(grid[0])
    y,x = pos
    if y < 0 or y >= max_y or x < 0 or x >= max_x or grid[y][x] == '#':
        return True
    return False

def make_p2_grid(grid):
    g2 = []
    for i in range(len(grid)):
        l = []
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                l.append('@')
                l.append('.')
            if grid[i][j] == 'O':
                l.append('[')
                l.append(']')
            if grid[i][j] == '#':
                l.append('#')
                l.append('#')
            if grid[i][j] == '.':
                l.append('.')
                l.append('.')
        g2.append(l)
    return g2


def valid_bfs(pos, direction, grid, seen):
    if pos in seen:
        return True
    seen.add(pos)

    y,x = pos
    dy,dx = direction
    new_y, new_x = y+dy, x+dx

    if grid[new_y][new_x] == '#':
        return False
    if grid[new_y][new_x] == '.':
        return True
    if grid[new_y][new_x] == '[':
        return valid_bfs((new_y, new_x), direction, grid, seen) and valid_bfs((new_y, new_x + 1), direction, grid, seen)
    if grid[new_y][new_x] == ']':
        return valid_bfs((new_y, new_x), direction, grid, seen) and valid_bfs((new_y, new_x - 1), direction, grid, seen)
  
            
def process_move2(grid, move, pos):
    dy, dx = get_move(move)
    cur_y, cur_x = pos
    new_y, new_x = cur_y + dy, cur_x + dx

    if out_of_bounds((new_y, new_x), grid):
        return pos

    if grid[new_y][new_x] in ['[',']']:
        seen = set()
        if not valid_bfs((cur_y, cur_x), (dy, dx), grid, seen):
            return pos
        
        while len(seen) > 0:
            for y,x in seen.copy():
                y2, x2 = y+dy, x+dx
                if (y2,x2) not in seen:
                    if grid[y2][x2] != '@' and grid[y][x] != '@':
                        grid[y2][x2] = grid[y][x]
                        grid[y][x] = '.'
                    seen.remove((y,x))
        grid[cur_y][cur_x], grid[new_y][new_x] = grid[new_y][new_x], grid[cur_y][cur_x]
        return (new_y, new_x)
    grid[cur_y][cur_x], grid[new_y][new_x] = grid[new_y][new_x], grid[cur_y][cur_x]
    return (new_y, new_x)
    
def part2(grid, moves):
    grid = [list(line) for line in grid.split('\n')]
    g2 = make_p2_grid(grid)
    # print_grid(g2)
    # print('=============')
    start = find_start(g2)
    pos = start
    for move in moves:
        if move == '\n':
            continue
        # print(move)
        pos = process_move2(g2, move, pos)
        # print_grid(g2)
        # print('--------------')
    # return get_coords(grid)
    return get_coords(g2)


with open('15.in') as f:
    grid, moves = f.read().split('\n\n')
    # grid = [list(line) for line in grid.split('\n')]
    # print_grid(grid)
    # print('============')
    print('Part 1')
    print(part1(grid, moves.strip()))
    print('Part 2')
    print(part2(grid, moves.strip()))