from collections import defaultdict

def check_update(rules_dict, update):
    valid = True
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            # print(update[i],update[j])
            if update[j] in rules_dict[update[i]]:
                # print(update[i],update[j])
                valid = False
    return valid


def sort_updates(rules, updates):
    valid_updates = []
    invalid_updates = []
    rules_dict = defaultdict(set)
    for rule in rules:
        i,j = rule.split('|')
        rules_dict[j].add(i)
    # print(rules_dict)
    for update in updates:
        valid = check_update(rules_dict, update)
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates

def part1(valid_updates):
    count = 0
    for update in valid_updates:
        count += int(update[len(update)//2])
    return count
                
def fix_update(rules_dict, update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            # print(update[i],update[j])
            if update[j] in rules_dict[update[i]]:
                # print(update[i],update[j])
                update[i], update[j] = update[j], update[i]
                return fix_update(rules_dict, update)
    return update

def part2(rules, invalid_updates):
    rules_dict = defaultdict(set)
    for rule in rules:
        i,j = rule.split('|')
        rules_dict[j].add(i)
    # print(rules_dict)
    fixed = []
    for update in invalid_updates:
        fixed.append(fix_update(rules_dict, update))
    count = 0
    for update in fixed:
        count += int(update[len(update)//2])
    return count

with open('5.test') as f:
    rules, updates = map(lambda x: x.split('\n'), f.read().split('\n\n'))
    updates = list(map(lambda x: x.split(','), updates))
    valid_updates, invalid_updates = sort_updates(rules, updates)
    print('Part 1:')
    print(part1(valid_updates))
    print('Part 2:')
    print(part2(rules, invalid_updates))
