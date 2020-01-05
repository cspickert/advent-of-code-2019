from computer import Computer

def main(data):
    computer = Computer(data)
    print(computer.run())

if __name__ == '__main__':
    from input import day9
    data = list(map(int, day9.split(',')))
    main(data)
