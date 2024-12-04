import re


def part1(inp):
    ans = 0
    matches = re.findall(r'mul\((\d+,\d+)\)', inp)
    for pair_string in matches:
        i,j = pair_string.split(',')
        ans += int(i)*int(j)
    return ans

def part2(inp):
    ans = 0
    on = True
    matches = re.findall(r"mul\((\d+,\d+)\)|(do\(\))|(don't\(\))", inp)
    for match in matches:
        num, do, dont = match
        if on and num:
            ans += int(num.split(',')[0]) * int(num.split(',')[1])
        elif on and dont:
            on = False
        elif not on and do:
            on = True
    return ans

with open('3.in') as f:
    inp = f.read()
    print('Part 1: ')
    p1_ans = part1(inp)
    print(p1_ans)
    print('Part 2: ')
    p2_ans = part2(inp)
    print(p2_ans)