from computer import Computer

def main(data):
    computer = Computer(data)
    result = computer.run()
    print(result)

if __name__ == '__main__':
    from input import day05
    data = list(map(int, day05.split(',')))
    main(data)
