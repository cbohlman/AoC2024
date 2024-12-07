def solve1(target, currs, remaining):
    while True:
        out = []
        if len(remaining) == 0:
            for curr in currs:
                if curr == target:
                    return True
            return False
        for curr in currs:
            add = curr + remaining[0]
            mul = curr * remaining[0]
            if add <= target:
                out.append(add)
            if mul <= target:
                out.append(mul)
        remaining = remaining[1:]
        currs = out

def solve2(target, currs, remaining):
    while True:
        out = []
        if len(remaining) == 0:
            for curr in currs:
                if curr == target:
                    return True
            return False
        for curr in currs:
            add = curr + remaining[0]
            mul = curr * remaining[0]
            op = int(str(curr) + str(remaining[0]))
            if add <= target:
                out.append(add)
            if mul <= target:
                out.append(mul)
            if op <= target:
                out.append(op)
        remaining = remaining[1:]
        currs = out



def part1(data):
    count = 0
    progress = 1
    total = len(data)
    for line in data:
        val = int(line.split(':')[0])
        nums = list(map(int, line.split(':')[1].strip().split()))
        # print(f'On {progress} of {total}')
        progress += 1
        valid = solve1(val, [nums[0]], nums[1:])
        if valid:
            count += val
    return count

def part2(data):
    count = 0
    progress = 1
    total = len(data)
    for line in data:
        val = int(line.split(':')[0])
        nums = list(map(int, line.split(':')[1].strip().split()))
        # print(f'On {progress} of {total}')
        progress += 1
        valid = solve2(val, [nums[0]], nums[1:])
        if valid:
            count += val
    return count
            

with open('7.in') as f:
    data = f.read().split('\n')
    print('Part 1: ')
    print(part1(data))
    print('Part 2: ')
    print(part2(data))