def trace_wire(commands):
    x, y = 0, 0
    for command in commands:
        direction, distance = command[0], int(command[1:])
        for _ in range(distance):
            if direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'L': x -= 1
            elif direction == 'R': x += 1
            else: raise Exception('invalid direction')
            yield (x, y)

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def wire_length(point, *wires):
    return sum(map(lambda l: l.index(point) + 1, wires))

def main(commands_list):
    wire1 = list(trace_wire(commands_list[0]))
    wire2 = list(trace_wire(commands_list[1]))
    intersections = set(wire1) & set(wire2)

    part1 = min(intersections, key=manhattan_distance)
    print(manhattan_distance(part1))

    part2 = min(intersections, key=lambda i: wire_length(i, wire1, wire2))
    print(wire_length(part2, wire1, wire2))

if __name__ == '__main__':
    from input import day03
    commands_list = []
    for line in day03.splitlines():
        commands = line.split(',')
        commands_list.append(commands)
    main(commands_list)
