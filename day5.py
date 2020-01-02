from computer import Computer

def main(data):
    computer = Computer()
    computer.run(data)

if __name__ == '__main__':
    from input import day5
    data = list(map(int, day5.split(',')))
    main(data)
