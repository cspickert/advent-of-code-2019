import sys

def run(data, noun=12, verb=2):
    data = data.copy()
    data[1] = noun
    data[2] = verb
    index = 0
    while index < len(data):
        op, arg1, arg2, dest = data[index:index+4]
        if op == 1:
            data[dest] = data[arg1] + data[arg2]
        elif op == 2:
            data[dest] = data[arg1] * data[arg2]
        elif op == 99:
            break
        else:
            raise Exception(f'Unknown opcode: {op}')
        index += 4
    return data[0]

def main(data):
    # Part 1
    # print(run(data))
    
    # Part 2
    for noun in range(100):
        for verb in range(100):
            try:
                if run(data, noun, verb) == 19690720:
                    print(100 * noun + verb)
                    break
            except:
                continue

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split(',')))
    main(data)
