from computer import Computer

def main(data):
    data[1] = 12
    data[2] = 2

    # Part 1
    # computer = Computer(data)
    # print(computer.run())
    
    # Part 2
    for noun in range(100):
        for verb in range(100):
            data[1] = noun
            data[2] = verb
            computer = Computer(data)
            if computer.run() == 19690720:
                print(100 * noun + verb)
                break

if __name__ == '__main__':
    from input import day2
    data = list(map(int, day2.split(',')))
    main(data)
