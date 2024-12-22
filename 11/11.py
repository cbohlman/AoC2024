from collections import defaultdict
def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone))//2
            f, s = int(str(stone)[:mid]), int(str(stone)[mid:])
            new_stones[f] += count
            new_stones[s] += count
        else:
            new_stones[stone*2024] += count
    return new_stones

def part1(inp):
    num_blinks = 25
    for i in range(num_blinks):
        output = blink(inp)
        inp = output
    return sum(output.values())

def part2(inp):
    num_blinks = 75
    for i in range(num_blinks):
        output = blink(inp)
        inp = output
    return sum(output.values())


with open('11.test') as f:
    inp = [int(x) for x in f.read().split()]
    stones = {}
    for x in inp:
        stones[x] = 1
    print('Part 1:')
    print(part1(stones))
    print('Part 2:')
    print(part2(stones))