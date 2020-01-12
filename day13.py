import os
import sys

from computer import Computer

class Game(object):
    def __init__(self, data):
        self.grid = [[0] * 45 for _ in range(25)]
        self.ball_velocity = (-1, 1)
        self.is_over = False

        # Initialize the grid
        computer = Computer(data)
        while not computer.is_halted:
            col = computer.run_partial()
            row = computer.run_partial()
            tile_id = computer.run_partial()
            if col is None or row is None or tile_id is None:
                break
            self.grid[row][col] = tile_id

    def step(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 4:
                    try:
                        self.move_ball(row, col)
                    except:
                        self.is_over = True
                    return

    def move_ball(self, row, col):
        ball_vel_row, ball_vel_col = self.ball_velocity
        next_row = row + ball_vel_row
        next_col = col + ball_vel_col
        can_move = True
        if self.grid[next_row][col] != 0:
            self.break_block(next_row, col)
            ball_vel_row *= -1
            can_move = False
        if self.grid[row][next_col] != 0:
            self.break_block(row, next_col)
            ball_vel_col *= -1
            can_move = False
        if can_move and self.grid[next_row][next_col] == 0:
            self.grid[next_row][next_col] = 4
            self.grid[row][col] = 0
        self.ball_velocity = (ball_vel_row, ball_vel_col)

    def break_block(self, row, col):
        if self.grid[row][col] == 2:
            self.grid[row][col] = 0

    def count_blocks(self):
        return sum(
            tile_id == 2 and 1 or 0
            for row in self.grid for tile_id in row)

    def show(self):
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                tile_id = self.grid[r][c]
                if tile_id == 0: tile_ch = ' '
                if tile_id == 1: tile_ch = 'x'
                if tile_id == 2: tile_ch = 'B'
                if tile_id == 3: tile_ch = '-'
                if tile_id == 4: tile_ch = 'O'
                print(tile_ch, end='')
            print()
        print()

def main(data):
    game = Game(data)
    while not game.is_over:
        os.system('clear')
        game.show()
        sys.stdin.readline()
        game.step()
    print('block count:', game.count_blocks())

if __name__ == '__main__':
    from input import day13
    data = [int(code) for code in day13.split(',')]
    main(data)
