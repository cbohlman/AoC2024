def solve(target, currs, remaining):
    # print(target)
    while True:
        # print(f'Currs: {currs}')
        # print(f'Remaining: {remaining}')
        out = []
        if len(remaining) == 0:
            for curr in currs:
                if curr == target:
                    return True
            return False
        # print(currs)
        for curr in currs:
            # print(f'Current: {curr}')
            add = curr + remaining[0]
            # print(f'Add: {add}')
            # add = 3
            mul = curr * remaining[0]
            # print(f'mul: {mul}')
            # mul = 2
            if add <= target:
                out.append(add)
            if mul <= target:
                out.append(mul)
            # print(f'iterout: {out}')
        # print(out)
        remaining = remaining[1:]
        currs = out
        #remaining = [3]


def part1(data):
    count = 0
    progress = 1
    total = len(data)
    for line in data:
        val = int(line.split(':')[0])
        nums = list(map(int, line.split(':')[1].strip().split()))
        print(f'On {progress} of {total}')
        progress += 1
        # print('--------')
        # print(val, nums)
        valid = solve(val, [nums[0]], nums[1:])
        print(valid)
        if valid:
            count += val
    return count
            

with open('7.in') as f:
    data = f.read().split('\n')
    print(part1(data))