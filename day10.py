from fractions import Fraction

def find_lines(data, from_row, from_col):
    deltas = set()
    for row in range(len(data)):
        for col in range(len(data[row])):
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
    for dr, dc in deltas:
        line = trace_line(data, from_row, from_col, dr, dc)
        if line:
            yield line

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

def main(data):
    best_count = max(
        count_visible(data, row, col)
        for row in range(len(data))
        for col in range(len(data[row])))
    print(best_count)

if __name__ == '__main__':
    from input import day10
    data = day10.splitlines()
    main(data)