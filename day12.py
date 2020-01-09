import itertools
import numpy as np

class Moon(object):
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z])
        self.vel = np.zeros(3, dtype=int)

    @classmethod
    def from_string(cls, string):
        key_pairs = string.strip('<>').split(', ')
        for key_pair in key_pairs:
            key, value = key_pair.split('=')
            if key == 'x': x = int(value)
            if key == 'y': y = int(value)
            if key == 'z': z = int(value)
        return Moon(x, y, z)

    def apply_gravity(self, other):
        self.vel += np.where(
            self.pos == other.pos, 0, np.where(
                self.pos < other.pos, 1, -1))

    def apply_velocity(self):
        self.pos += self.vel

    @property
    def potential_energy(self):
        return np.abs(self.pos).sum()

    @property
    def kinetic_energy(self):
        return np.abs(self.vel).sum()

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

def step(data):
    # Gravity
    for moon1, moon2 in itertools.combinations(data, 2):
        moon1.apply_gravity(moon2)
        moon2.apply_gravity(moon1)
    for moon in data:
        moon.apply_velocity()

def part1(data):
    for _ in range(1000):
        step(data)
    total_energy = 0
    for moon in data:
        total_energy += moon.total_energy
    print(total_energy)

if __name__ == '__main__':
    from input import day12
    data = [Moon.from_string(line) for line in day12.splitlines()]
    part1(data)
