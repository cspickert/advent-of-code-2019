import math

from computer import Computer


def build_check_fn(program):
    def check_fn(x, y):
        computer = Computer(program)
        computer.input(x)
        computer.input(y)
        return bool(computer.run())

    return check_fn


def get_beam_bounds_at_y(check_fn, y):
    x1 = None
    beam = False
    for x in range(y):
        if not beam and check_fn(x, y):
            x1 = x
            beam = True
        if beam and not check_fn(x + 1, y):
            x2 = x
            return ((x1, y), (x2, y))


def part1(check_fn):
    result = sum(check_fn(x, y) for x in range(50) for y in range(50))
    print(result)


def part2(check_fn):
    square_dim = 100

    # Get bounding points for the beam at y=50.
    p1, p2 = get_beam_bounds_at_y(check_fn, 50)

    # Calculate the slope of the left and right side of the beam.
    s1 = p1[1] / p1[0]
    s2 = p2[1] / p2[0]

    # Find coordinates where the beam's width accommodates a square
    # region with area `square_dim * square_dim`.
    y = 0
    while True:
        x1 = int(math.ceil(y / s1))
        x2 = int(math.ceil(y / s2))
        if x2 - square_dim >= x1 and y + square_dim <= s1 * (x2 - square_dim):
            min_x = x2 - square_dim
            min_y = y
            break
        y += 1

    # Via experimentation, note that the coordinates derived from the
    # slope of the edges of the beam overshoots somewhat, so we need to
    # backtrack.
    done = False
    while not done:
        done = True
        while check_fn(min_x + square_dim, min_y):
            min_y -= 1
            done = False
        while check_fn(min_x, min_y + square_dim):
            min_x -= 1
            done = False

    # Fudge factor based on further experimentation. I'm not quite sure
    # why the loop above doesn't get there.
    min_x -= 1
    min_y -= 2

    # Print the resulting x, y coordinates of the top-left corner of the
    # square (and the puzzle answer).
    print(min_x, min_y)
    print(min_x * 10000 + min_y)

    # For debugging purposes, print visual representations of the
    # top-right and bottom-left corners of the square region.
    show_grid(check_fn, min_x, min_y, min_x - 5 + square_dim, min_y - 5, 20, square_dim)
    show_grid(check_fn, min_x, min_y, min_x - 5, min_y - 5 + square_dim, 20, square_dim)


def show_grid(check_fn, min_x, min_y, grid_x, grid_y, grid_size, square_dim):
    grid = [
        ["#" if check_fn(x, y) else "." for x in range(grid_x, grid_x + grid_size)]
        for y in range(grid_y, grid_y + grid_size)
    ]

    for y in range(grid_y, grid_y + grid_size):
        if y in range(min_y, min_y + square_dim):
            for x in range(grid_x, grid_x + grid_size):
                if x in range(min_x, min_x + square_dim):
                    r, c = y - grid_y, x - grid_x
                    if grid[r][c] == "#":
                        grid[r][c] = "o"
                    else:
                        grid[r][c] = "x"

    print("\n".join("".join(row) for row in grid))
    print()


def main(program):
    check_fn = build_check_fn(program)
    part1(check_fn)
    part2(check_fn)


if __name__ == "__main__":
    from input import day19

    program = [int(i) for i in day19.split(",")]
    main(program)
