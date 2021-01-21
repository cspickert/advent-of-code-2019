import string
import heapq


def find_doors(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in string.ascii_uppercase:
                if c < len(grid[r]) - 1 and grid[r][c + 1] in string.ascii_uppercase:
                    door_label = "".join((grid[r][c], grid[r][c + 1]))
                    is_outer = c == 0 or c == len(grid[r]) - 2
                    level = -1 if is_outer else 1
                    for x in (c - 1, c + 2):
                        if x in range(len(grid[r])) and grid[r][x] == ".":
                            yield (r, x), (door_label, level)
                elif r < len(grid) - 1 and grid[r + 1][c] in string.ascii_uppercase:
                    door_label = "".join((grid[r][c], grid[r + 1][c]))
                    is_outer = r == 0 or r == len(grid) - 2
                    level = -1 if is_outer else 1
                    for y in (r - 1, r + 2):
                        if y in range(len(grid)) and grid[y][c] == ".":
                            yield (y, c), (door_label, level)


def find_start(doors):
    return next(key for key, (value, _) in doors.items() if value == "AA")


def find_end(doors):
    return next(key for key, (value, _) in doors.items() if value == "ZZ")


def part1(grid):
    doors = dict(find_doors(grid))
    start, end = find_start(doors), find_end(doors)

    queue = [(0, start, set())]
    while queue:
        steps, (r, c), visited = heapq.heappop(queue)

        if (r, c) == end:
            print(steps)
            return

        if (r, c) != start and (r, c) in doors:
            door, _ = doors[r, c]
            next_r, next_c = next(
                key
                for key, (value, _) in doors.items()
                if value == door and key != (r, c)
            )
            if (next_r, next_c) not in visited:
                heapq.heappush(queue, (steps + 1, (next_r, next_c), {*visited, (r, c)}))
                continue

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_r, next_c = r + dr, c + dc
            if grid[next_r][next_c] == "." and (next_r, next_c) not in visited:
                heapq.heappush(queue, (steps + 1, (next_r, next_c), {*visited, (r, c)}))


def main(grid):
    part1(grid)


if __name__ == "__main__":
    from input import day20

    grid = [list(line) for line in day20.splitlines()]
    main(grid)
