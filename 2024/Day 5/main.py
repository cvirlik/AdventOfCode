def read_file(file_name):
    with open(file_name, 'r') as data:
        content = data.read()
        a, b = content.split('\n\n')
        a = a.split('\n')
        rules = [[int(x.split("|")[0]), int (x.split("|")[1])] for x in a]

        b = b.split('\n')
        update = [[int(num) for num in x.split(",")] for x in b]
        return rules, update

def check(rules, num, to_check):
    for number in to_check:
        for rule in rules:
            if rule == [number, num]:
                return False
    return True

def fix(rules, update):    
    for i in range(len(update)):
        for j in range(i, len(update)):
            for rule in rules:
                if rule == [update[j], update[i]]:
                    update[i], update[j] = update[j], update[i]
                    fix(rules, update)
    return update

def first_task(rules, update):
    sum = 0
    for update in update:
        valid = True
        for i in range(len(update)):
            if not check(rules, update[i], update[i+1:]):
                valid = False
                break
        if valid : sum += update[len(update)//2]
    print(sum)

def second_task(rules, update):
    sum = 0
    for update in update:
        for i in range(len(update)):
            if not check(rules, update[i], update[i+1:]):
                new = fix(rules, update)
                sum += new[len(new)//2]
                break
    print(sum)

if __name__ == '__main__':
    rules, update= read_file("Day 5/input.txt")
    first_task(rules, update)
    second_task(rules, update)
    