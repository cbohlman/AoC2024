from collections import deque, defaultdict

class Plot:
    def __init__(self, plant, locations):
        self.plant = plant
        self.locations = locations

    def get_area(self):
        return len(self.locations)
    
    def get_perimeter(self):
        perim = 0
        for loc in self.locations:
            y, x = loc
            p = 4
            dirs = [(0,-1), (-1,0), (0,1), (1,0)]
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if (new_y, new_x) in self.locations:
                    p -= 1
            perim += p
        return perim

    def get_sides(self):
        corners = 0
        for loc in self.locations:
            y, x = loc
            # External Corners
            # NE
            if (y-1, x) not in self.locations and (y, x+1) not in self.locations:
                corners += 1
            # SE
            if (y+1, x) not in self.locations and (y, x+1) not in self.locations:
                corners += 1
            # SW
            if (y+1, x) not in self.locations and (y, x-1) not in self.locations:
                corners += 1
            # NW
            if (y-1, x) not in self.locations and (y, x-1) not in self.locations:
                corners += 1
            # Internal Corners
            #NE
            if (y-1, x) in self.locations and (y, x+1) in self.locations and (y-1, x+1) not in self.locations:
                corners += 1
            # SE
            if (y+1, x) in self.locations and (y, x+1) in self.locations and (y+1, x+1) not in self.locations:
                corners += 1
            # SW
            if (y+1, x) in self.locations and (y, x-1) in self.locations and (y+1, x-1) not in self.locations:
                corners += 1
            # NW
            if (y-1, x) in self.locations and (y, x-1) in self.locations and (y-1, x-1) not in self.locations:
                corners += 1
        return corners
    
def find_plot(start, grid):
    max_y = len(grid)
    max_x = len(grid[0])
    plant = grid[start[0]][start[1]]
    plot = []

    Q = deque()
    Q.append(start)
    visited = set()
    visited.add(start)
    plot.append(start)

    while Q:
        curr = Q.popleft()
        y,x = curr
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]
        for dy, dx in dirs:
            new_y, new_x = y + dy, x + dx
            if new_y < 0 or new_y >= max_y or new_x < 0 or new_x >= max_x:
                continue
            if (new_y, new_x) not in visited:
                if grid[new_y][new_x] == plant:
                    visited.add((new_y, new_x))
                    plot.append((new_y, new_x))
                    Q.append((new_y, new_x))
    return plot

def find_plots(grid):
    seen = set()
    plots = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y,x) in seen:
                continue
            seen.add(grid[y][x])
            plot = find_plot((y,x), grid)
            plots.append(Plot(grid[y][x], plot))
            seen.update(plot)
    return plots


def part1(grid):
    count = 0
    plots = find_plots(grid)
    for plot in plots:
        count += (plot.get_area() * plot.get_perimeter())
    return count

def part2(grid):
    plots = find_plots(grid)
    count = 0
    for plot in plots:
        count += plot.get_area() * plot.get_sides()
    return count
with open('12.in') as f:
    grid = [list(line) for line in f.read().split('\n')]
    print('Part 1: ')
    print(part1(grid))
    print('Part 2: ')
    print(part2(grid))