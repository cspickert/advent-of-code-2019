from computer import Computer

def paint(data, start_color=0):
    computer = Computer(data)
    x, y, direction = 0, 0, 0
    panels = {(x, y): start_color}
    while not computer.is_halted:
        color = panels.get((x, y), 0)
        computer.input(color)
        color = computer.run_partial()
        if color is None:
            assert(computer.is_halted)
            break
        panels[(x, y)] = color
        turn = computer.run_partial()
        if turn is None:
            assert(computer.is_halted)
            break
        direction = (direction + (turn and 1 or -1)) % 4
        if direction == 0: y -= 1
        if direction == 1: x += 1
        if direction == 2: y += 1
        if direction == 3: x -= 1
    return panels

def print_panels(panels):
    min_x = min(panels, key=lambda pos: pos[0])[0]
    max_x = max(panels, key=lambda pos: pos[0])[0]
    min_y = min(panels, key=lambda pos: pos[1])[1]
    max_y = max(panels, key=lambda pos: pos[1])[1]
    num_rows = max_y - min_y + 1
    num_cols = max_x - min_x + 1
    lines = []
    for y in range(min_y, min_y + num_rows):
        line = [' '] * num_cols
        for x in range(min_x, min_x + num_cols):
            key = (x, y)
            if key in panels and panels[key] == 1:
                line[x - min_x] = 'x'
            else:
                line[x - min_x] = ' '
        lines.append(line)
    for line in lines:
        print(''.join(line))

if __name__ == "__main__":
    from input import day11
    data = [int(s) for s in day11.split(',')]
    # Part 1
    panels = paint(data, start_color=0)
    print(len(panels))
    # Part 2
    panels = paint(data, start_color=1)
    print_panels(panels)
