import math
import sys

from computer import Computer

def opposite(direction):
    if direction == 1: return 2
    if direction == 2: return 1
    if direction == 3: return 4
    if direction == 4: return 3

def adjacent_position(position, direction):
    row, col = position
    if direction == 1: return (row - 1, col)
    if direction == 2: return (row + 1, col)
    if direction == 3: return (row, col - 1)
    if direction == 4: return (row, col + 1)

def find_min_count(computer, start_position=(0, 0), past_positions=[]):
    min_count = None
    for direction in range(1, 5):
        success, count = try_direction(
            computer, direction, start_position, past_positions)
        if success and (min_count is None or count < min_count):
            min_count = count
    return min_count is not None, min_count or -1

def try_direction(computer, direction, start_position, past_positions):
    if start_position in past_positions:
        return False, -1
    computer.input(direction)
    status = computer.run_partial()
    if status == 0:
        return False, -1
    if status == 2:
        success, count = True, 1
    if status == 1:
        success, next_count = find_min_count(
            computer,
            adjacent_position(start_position, direction),
            past_positions + [start_position])
        count = 1 + next_count
    computer.input(opposite(direction))
    computer.run_partial()
    return success, count

def visit_all(computer):
    grid = {}
    directions = []
    position = (0, 0)
    while True:
        next_direction = None
        for direction in range(1, 5):
            next_position = adjacent_position(position, direction)
            if next_position not in grid:
                next_direction = direction
                break
        if next_direction is None:
            backtracking = True
            if directions:
                next_direction = opposite(directions.pop())
                next_position = adjacent_position(position, next_direction)
            else:
                break
        else:
            backtracking = False
        computer.input(next_direction)
        status = computer.run_partial()
        grid[next_position] = status
        if status != 0:
            if not backtracking:
                directions.append(next_direction)
            position = next_position
    return grid

def show(grid):
    string = ''
    min_row = min(key[0] for key in grid)
    min_col = min(key[1] for key in grid)
    max_row = max(key[0] for key in grid)
    max_col = max(key[1] for key in grid)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) not in grid:
                string += ' '
            else:
                if grid[row, col] == 0: string += '#'
                if grid[row, col] == 1: string += '.'
                if grid[row, col] == 2: string += 'O'
        string += '\n'
    print(string)

def expand_o2(grid):
    positions_to_update = set()
    min_row = min(key[0] for key in grid)
    min_col = min(key[1] for key in grid)
    max_row = max(key[0] for key in grid)
    max_col = max(key[1] for key in grid)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            position = (row, col)
            if position not in grid or grid[position] != 2:
                continue
            for direction in range(1, 5):
                neighbor = adjacent_position(position, direction)
                if neighbor in grid and grid[neighbor] == 1:
                    positions_to_update.add(neighbor)
    for position in positions_to_update:
        grid[position] = 2
    return len(positions_to_update) > 0

def part1(data):
    computer = Computer(data)
    success, count = find_min_count(computer)
    print(count)

def part2(data):
    computer = Computer(data)
    grid = visit_all(computer)
    count = 0
    while expand_o2(grid):
        count += 1
        # show(grid)
        # sys.stdin.readline()
    print(count)

if __name__ == '__main__':
    from input import day15
    data = [int(code) for code in day15.split(',')]
    part1(data)
    part2(data)
