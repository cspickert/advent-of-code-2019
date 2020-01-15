import math

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

def main(data):
    computer = Computer(data)
    success, count = find_min_count(computer)
    print(count)

if __name__ == '__main__':
    from input import day15
    data = [int(code) for code in day15.split(',')]
    main(data)
