def path(orbits, start):
    if start not in orbits:
        return []
    return [start] + path(orbits, orbits[start])

def count(orbits, start):
    return len(path(orbits, start))

def main(entries):
    orbits = {}
    for body, satellite in entries:
        orbits[satellite] = body

    # Part 1
    total_count = 0
    for start in orbits:
        total_count += count(orbits, start)
    print(total_count)

    # Part 2
    you_path = path(orbits, 'YOU')[1:]
    san_path = path(orbits, 'SAN')[1:]
    common_body = next(body for body in san_path if body in you_path)
    print(you_path.index(common_body) + san_path.index(common_body))

if __name__ == '__main__':
    from input import day06
    entries = []
    for line in day06.splitlines():
        entries.append(line.rstrip().split(')'))
    main(entries)
