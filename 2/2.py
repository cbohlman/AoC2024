def is_safe_p1(level):
    diff = []
    for i in range(len(level)-1):
        diff.append(level[i] - level[i+1])
    if (0 in diff):
        return False
    if (diff[0] < 0):
        for i in diff: 
            if i < -3 or i > 0:
                return False
        return True
    if (diff[0] > 0):
        for i in diff:
            if i > 3 or i < 0:
                return False
        return True
        

def part1(input_lines):
    safe_count = 0
    for line in input_lines:
        levels = list(map(int, line.split()))
        safe = is_safe_p1(levels)
        if (safe):
            safe_count += 1
    print(safe_count)

def part2(input_lines):
    safe_count = 0
    for line in input_lines:
        levels = list(map(int, line.split()))
        safe = is_safe_p1(levels)
        if (safe):
            safe_count += 1
            continue
        for i in range(len(levels)):
            levels_copy = levels.copy()
            del levels_copy[i]
            if is_safe_p1(levels_copy):
                safe_count += 1
                break
    print(safe_count)


with open('2.in') as f:
    input_lines = [line.strip() for line in f]
    print('Part 1: ')
    part1(input_lines)
    print('Part 2: ')
    part2(input_lines)