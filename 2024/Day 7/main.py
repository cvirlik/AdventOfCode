import itertools

def read_file(file_name):
    with open(file_name, 'r') as data:
        return [
            (int(result), list(map(int, equation.split(" ")))) 
            for line in data.read().splitlines() 
            for result, equation in [line.split(": ")]
        ]



def first_task(equations):
    total = 0
    combinations_cache = {}
    
    for result, vars in equations:
        num_operators = len(vars) - 1
        
        if num_operators not in combinations_cache:
            elements = ['+', '*']
            combinations_cache[num_operators] = list(itertools.product(elements, repeat=num_operators))
        
        for combination in combinations_cache[num_operators]:
            t = vars[0]
            for op, var in zip(combination, vars[1:]):
                t = eval(f"{t}{op}{var}")
            
            if result == t:
                total += result
                break
    
    print(total)


def second_task(equations):
    combinations_cache = {}
    total = 0
    for result, vars in equations:
        num_operators = len(vars) - 1
        
        if num_operators not in combinations_cache:
            elements = ['+', '||', '*']
            combinations_cache[num_operators] = list(itertools.product(elements, repeat=num_operators))
        
        for combination in combinations_cache[num_operators]:
            t = vars[0]
            for op, var in zip(combination, vars[1:]):
                if op == "||":
                    t = int(str(t) + str(var))
                else:
                    t = eval(f"{t}{op}{var}")   
            
            if result == t:
                total += result
                break
    
    print(total)


if __name__ == '__main__':
    equations = read_file("Day 7/input.txt")
    first_task(equations)
    second_task(equations)
