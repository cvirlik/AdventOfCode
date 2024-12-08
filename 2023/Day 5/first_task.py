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
    result = []
    for seed in seeds:
        found = False
        for nums in step:
            if seed >= nums[1] and seed < nums[2]+nums[1]:
                result.append(seed - (nums[1]-nums[0]))
                found = True
                break
        if not found:
            result.append(seed)
    return result



if __name__ == '__main__':
    seeds, steps = parse("2023/Day 5/input.txt")
    input = seeds
    for step in steps:
        input = process(step, input)

    print(min(input))
    


