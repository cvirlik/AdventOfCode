import re


def parse(filepath: str):
    with open(filepath) as file:
        seeds = list(map(int, re.findall(r'\d+', file.readline())))

        steps = []
        for block in file.read().split('\n\n'):
            block = block.split('\n')
            while '' in block:
                block.remove('')
            nums = []
            for item in block[1:]:
                nums.append(list(map(int,item.split(' '))))
            steps.append(nums)
        return seeds, steps
            

def process(step, seeds):
    nr = []
    for seed_start, seed_end in seeds:
        lr = [seed_start, seed_end]
        for offset, start, end in step:
            if end < seed_start or start > seed_end:
                continue
            if seed_start >= start:
                if seed_end <= end:
                    nr.append([seed_start-offset, seed_end-offset])
                    lr = []
                    break
                if seed_end > end:
                    nr.append([seed_start-offset, end-offset])
                    seed_start = end + 1
                    lr = [seed_start, seed_end]
            else:
                nr.append([seed_start, start-1])
                if seed_end <= end:
                    nr.append([start-offset, seed_end-offset])
                    lr = []
                    break
                else: 
                    nr.append([start-offset, end-offset])
                    seed_start = end + 1
                    lr = [seed_start, seed_end]
        if lr != []:
            nr.append(lr)
    return nr



if __name__ == '__main__':
    seeds, steps = parse("2023/Day 5/input.txt")
    seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]  
    seeds = [[x[0], x[0] + x[1] - 1] for x in seeds]
    
    for i in range(len(steps)):
        steps[i].sort(key=lambda x: x[0])
        steps[i] = list(map(lambda x: [x[1]-x[0], x[1], x[1]+x[2]-1], steps[i]))

    i = seeds
    for step in steps:
        i = process(step, i)

    print(min(map(lambda x: x[0], i)))
    


