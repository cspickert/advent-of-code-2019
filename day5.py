from computer import Computer

def main(data):
    computer = Computer()
    computer.run(data)

if __name__ == '__main__':
    import os.path
    input_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'input', 'day5.txt')
    with open(input_path, 'r') as f:
        data = list(map(int, f.read().split(',')))
        main(data)
