import os
import sys

from computer import Computer

def count_blocks(grid):
    return sum(
        tile_id == 2 and 1 or 0
        for row in grid for tile_id in row)

def show(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            tile_id = grid[r][c]
            if tile_id == 0: tile_ch = ' '
            if tile_id == 1: tile_ch = 'x'
            if tile_id == 2: tile_ch = 'B'
            if tile_id == 3: tile_ch = '-'
            if tile_id == 4: tile_ch = 'O'
            print(tile_ch, end='')
        print()
    print()

def find_tile(grid, tile_id_to_find):
    for row, row_tile_ids in enumerate(grid):
        for col, tile_id in enumerate(row_tile_ids):
            if tile_id == tile_id_to_find:
                return row, col
    return None

def find_next_input(grid):
    ball = find_tile(grid, 4)
    paddle = find_tile(grid, 3)
    if ball is None or paddle is None:
        return 0
    diff = ball[1] - paddle[1]
    if diff == 0:
        return 0
    return diff / abs(diff)

def main(data):
    grid = [[0] * 45 for _ in range(25)]

    data[0] = 2
    computer = Computer(data)
    score = 0

    def provide_input():
        # show(grid)
        # sys.stdin.readline()
        return find_next_input(grid)
    computer.get_next_input = provide_input

    while not computer.is_halted:
        try:
            col, row, tile_id = [computer.run_partial() for _ in range(3)]
            if col == -1:
                score = tile_id
            else:
                grid[row][col] = tile_id
        except Exception as e:
            break
    print('final score:', score)

if __name__ == '__main__':
    from input import day13
    data = [int(code) for code in day13.split(',')]
    main(data)
