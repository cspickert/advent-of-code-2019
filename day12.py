import itertools
import numpy as np

def step(pos, vel):
    tmp = pos.reshape(len(pos), 1)
    vel += np.where(pos == tmp, 0, np.where(pos < tmp, -1, 1)).sum(1)
    pos += vel

def part1(data):
    x = np.array([moon[0] for moon in data])
    y = np.array([moon[1] for moon in data])
    z = np.array([moon[2] for moon in data])
    xv = np.zeros(4, dtype=int)
    yv = np.zeros(4, dtype=int)
    zv = np.zeros(4, dtype=int)
    for _ in range(1000):
        step(x, xv)
        step(y, yv)
        step(z, zv)
    total_energy = 0
    for i in range(len(data)):
        pos = np.array([x[i], y[i], z[i]])
        vel = np.array([xv[i], yv[i], zv[i]])
        pot = np.abs(pos).sum()
        kin = np.abs(vel).sum()
        total_energy += pot * kin
    print(total_energy)

def part2(data):
    pass

if __name__ == '__main__':
    from input import day12
    from parse import parse
    data = []
    for line in day12.splitlines():
        r = parse('<x={x:d}, y={y:d}, z={z:d}>', line)
        if r:
            data.append((r['x'], r['y'], r['z']))
    part1(data)
    # part2(data)
