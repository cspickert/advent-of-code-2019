from fractions import Fraction
from math import atan2, pi

def find_lines(data, from_row, from_col):
    deltas = set()
    for row, col in enumerate_coordinates(data):
        if row == from_row:
            dr, dc = 0, 1 if col > from_col else -1
        elif col == from_col:
            dr, dc = 1 if row > from_row else -1, 0
        else:
            fraction = Fraction(abs(row - from_row), abs(col - from_col))
            dr, dc = fraction.numerator, fraction.denominator
            if row < from_row:
                dr = -dr
            if col < from_col:
                dc = -dc
        deltas.add((dr, dc))
    for dr, dc in sorted(deltas, key=lambda coords: angle(*coords)):
        line = trace_line(data, from_row, from_col, dr, dc)
        if line:
            yield line

def angle(dr, dc):
    return (atan2(dr, dc) * 180 / pi + 90) % 360

def trace_line(data, from_row, from_col, dr, dc):
    row, col = from_row + dr, from_col + dc
    if row not in range(len(data)) or col not in range(len(data[row])):
        return []
    return [(row, col)] + trace_line(data, row, col, dr, dc)

def count_visible(data, from_row, from_col):
    if data[from_row][from_col] != '#':
        return -1
    count = 0
    for line in find_lines(data, from_row, from_col):
        for row, col in line:
            if data[row][col] == '#':
                count += 1
                break
    return count

def enumerate_coordinates(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            yield (row, col)

def find_best_position(data):
    return max(
        enumerate_coordinates(data),
        key=lambda coords: count_visible(data, *coords))

def part1(data):
    row, col = find_best_position(data)
    print(count_visible(data, row, col))

def part2(data):
    from_row, from_col = find_best_position(data)
    count = 0
    last_coords = None
    while count < 200:
        for line in find_lines(data, from_row, from_col):
            for row, col in line:
                if data[row][col] == '#':
                    count += 1
                    last_coords = (row, col)
                    data[row][col] = '.'
                    break
            if count == 200:
                break
    row, col = last_coords
    print(col * 100 + row)

if __name__ == '__main__':
    from input import day10
    data = [list(line) for line in day10.splitlines()]
    # part1(data)
    part2(data)
