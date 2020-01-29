import itertools

PATTERN = [0, 1, 0, -1]

def factor(row, col):
    return PATTERN[((col + 1) // (row + 1)) % 4]

def step(data):
    n = len(data)
    return [
        abs(sum(data[col] * factor(row, col) for col in range(n))) % 10
        for row in range(n)]

def part1(data):
    data = data[:]
    for _ in range(100):
        data = step(data)
    print(''.join(str(i) for i in data[:8]))

def part2(data):
    data = data[:]
    offset = 0
    for i, value in enumerate(reversed(data[:7])):
        offset += 10 ** i * value
    data *= 10000
    data = data[offset:]
    for _ in range(100):
        total = 0
        next_data = data[:]
        for i in range(len(data) - 1, -1, -1):
            total = (total + data[i]) % 10
            next_data[i] = total
        data = next_data
    print(''.join(str(i) for i in data[:8]))

if __name__ == '__main__':
    from input import day16
    data = [int(c) for c in day16]
    # part1(data)
    part2(data)
