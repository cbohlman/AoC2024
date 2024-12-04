from collections import Counter


def part1(input_lines):
    count = 0

    left = []
    right = []
    for line in input_lines:
        left.append(int(line.split('   ')[0]))
        right.append(int(line.split('   ')[1]))

    left.sort()
    right.sort()
    for i in range(len(left)):
        diff = abs(left[i]-right[i])
        count += diff
    print(count)

def part2(input_lines):
    count = 0
    left = []
    right = []
    for line in input_lines:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))
    r_count = Counter(right)
    for i in range(len(left)):
        l = left[i]
        mult = r_count.get(l, 0)
        count += l*mult
    print(count)

with open('1.in') as f:
    input_lines = [line.strip() for line in f]
    print('Part 1: ')
    part1(input_lines)
    print('Part 2: ')
    part2(input_lines)