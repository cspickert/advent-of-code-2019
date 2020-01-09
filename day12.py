import itertools

def gravity(self_value, other_value):
    if self_value == other_value:
        return 0
    return 1 if self_value < other_value else -1

class Vec(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    @property
    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def acceleration(self, other):
        return Vec(
            0 if self.x == other.x else 1 if self.x < other.x else -1,
            0 if self.y == other.y else 1 if self.y < other.y else -1,
            0 if self.z == other.z else 1 if self.z < other.z else -1)

class Moon(object):
    def __init__(self, x, y, z):
        self.pos = Vec(x, y, z)
        self.vel = Vec(0, 0, 0)

    def __repr__(self):
        return f'Moon(pos={self.pos}, vel={self.vel})'

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
        self.vel += self.pos.acceleration(other.pos)

    def apply_velocity(self):
        self.pos += self.vel

    @property
    def potential_energy(self):
        return self.pos.energy

    @property
    def kinetic_energy(self):
        return self.vel.energy

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
