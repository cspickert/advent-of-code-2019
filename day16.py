import itertools

def pattern(repeat):
    def generate():
        while True:
            for item in [0, 1, 0, -1]:
                for _ in range(repeat):
                    yield item
    sequence = generate()
    next(sequence)
    return sequence

def step(data):
    result = []
    for position, _ in enumerate(data):
        sequence = pattern(position + 1)
        new_value = sum(value * next(sequence) for value in data)
        result.append(abs(new_value) % 10)
    return result

def part1(data):
    for _ in range(100):
        data = step(data)
    print(''.join(str(i) for i in data[:8]))

if __name__ == '__main__':
    from input import day16
    data = [int(c) for c in day16]
    part1(data)
