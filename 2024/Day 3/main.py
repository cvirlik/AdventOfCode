import re
def read_file(file_name):
    with open(file_name, 'r') as data:
        content = data.read()
        return content

def first_task(memory):
    numbers = re.findall(r"mul\((\d+),(\d+)\)", memory)
    mul = sum(map(lambda x: int(x[0]) * int(x[1]), numbers))
    print(mul)


def second_task(memory):
    do_dont = memory.split("do()")
    dos = [x.split("don't()")[0] for x in do_dont]
    dos = "".join(dos)
    numbers = re.findall(r"mul\((\d+),(\d+)\)", dos)
    mul = sum(map(lambda x: int(x[0]) * int(x[1]), numbers))
    print(mul)


if __name__ == '__main__':
    memory= read_file("Day 3/input.txt")
    first_task(memory)
    second_task(memory)
    