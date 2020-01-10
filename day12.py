import numpy as np

def step(data):
    for pos, vel in data.T:
        tmp = pos.reshape(len(pos), 1)
        vel += np.where(pos == tmp, 0, np.where(pos < tmp, -1, 1)).sum(1)
        pos += vel

def part1(data):
    for _ in range(1000):
        step(data)
    total_energy = 0
    for pos, vel in data:
        pot = np.abs(pos).sum()
        kin = np.abs(vel).sum()
        total_energy += pot * kin
    print(total_energy)

def part2(data):
    pass

def load_data():
    from input import day12
    from parse import parse
    data = []
    for line in day12.splitlines():
        result = parse('<x={:d}, y={:d}, z={:d}>', line)
        if result:
            moon = np.array([list(result), [0] * 3])
            data.append(moon)
    return np.array(data)

if __name__ == '__main__':
    data = load_data()
    part1(data)
    # part2(data)
