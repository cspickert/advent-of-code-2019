from computer import Computer

def main(data):
    data[1] = 12
    data[2] = 2

    computer = Computer()

    # Part 1
    # print(computer.run(data))
    
    # Part 2
    for noun in range(100):
        for verb in range(100):
            data[1] = noun
            data[2] = verb
            if computer.run(data) == 19690720:
                print(100 * noun + verb)
                break

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split(',')))
    main(data)
