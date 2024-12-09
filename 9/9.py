from collections import defaultdict

class File:
    def __init__(self, id, start, end):
        self.start = start
        self.end = end
        self.id = id
        self.length = end - start + 1
        self.moved = False
    
    def __str__(self):
        return f'start: {self.start}, end: {self.end}, id: {self.id}'

def parse_disk(disk):
    disk_map = []
    file_id = 0
    for i in range(len(disk)):
        if i == 0:
            tmp = [str(file_id)] * int(disk[i])
            disk_map.extend(tmp)
            file_id += 1
        elif i % 2 ==  0:
            tmp = [str(file_id)] * int(disk[i])
            disk_map.extend(tmp)
            file_id += 1
        elif i % 2 == 1:
            tmp = ['.'] * int(disk[i])
            disk_map.extend(tmp)
    return disk_map

def sort_disk_map1(disk_map):
    start = 0
    end = len(disk_map) - 1
    while True:
        if disk_map[start] == '.':
            while True:
                if disk_map[end] != '.':
                    break
                end -= 1
            if start > end:
                break
            disk_map[start] = disk_map[end]
            disk_map[end] = '.'
        start += 1
    return disk_map


def part1(disk):
    disk_map = parse_disk(disk) # List of Strings
    disk_map = sort_disk_map1(disk_map)
    # print(disk_map)
    # print(disk_map)
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            break
        checksum += i * int(disk_map[i])
    return checksum


def sort_disk_map2(disk_map):
    files = []
    seen = set()
    # Get files
    for i in range(len(disk_map)):
        if disk_map[i] not in seen and disk_map[i] != '.':
            seen.add(disk_map[i])
            file_id = disk_map[i]
            c_start = i
            c_end = i
            for j in range(c_start + 1, len(disk_map)):
                if disk_map[j] != file_id:
                    break
                c_end = j
            files.append(File(file_id, c_start, c_end))

    files.reverse()
    [print(file) for file in files]
    start = 0
    end = 0
    while start < len(disk_map):
        if disk_map[start] != '.':
            start += 1
            end += 1
        else:
            if disk_map[end + 1] != '.':
                space_len = end - start + 1
                print(start, end, space_len)
                for idx, file in enumerate(files):
                    if file.length <= space_len and not file.moved:
                        print(file)
                        for i in range(start, end):
                            disk_map[i] = file.id
                        del files[idx]
                        break
                start = end +1
                end = start
            else:
                end += 1

    print(disk_map)


            
def part1(disk):
    disk_map = parse_disk(disk) # List of Strings
    disk_map = sort_disk_map1(disk_map)
    # print(disk_map)
    # print(disk_map)
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            break
        checksum += i * int(disk_map[i])
    return checksum

def part2(disk):
    disk_map = parse_disk(disk) # List of Strings
    disk_map = sort_disk_map2(disk_map)
    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            break
        checksum += i * int(disk_map[i])
    return checksum
    

with open('9.test') as f:
    disk = f.read()
    print('Part 1:')
    checksum1 = part1(disk)
    print(checksum1)
    print('Part 2:')
    checksum2 = part2(disk)
    print(checksum2)