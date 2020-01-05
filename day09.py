from computer import Computer

def main(data):
    computer = Computer(data)
    print(computer.run())

if __name__ == '__main__':
    from input import day09
    data = list(map(int, day09.split(',')))
    main(data)
