import heapq
import string


OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

DOOR_CHARS = set(string.ascii_uppercase)

KEY_CHARS = set(string.ascii_lowercase)


def find_start(grid):
    return next(
        (r, c)
        for r in range(len(grid))
        for c in range(len(grid[r]))
        if grid[r][c] == "@"
    )


def find_all_keys(grid):
    return set(
        grid[r][c]
        for r in range(len(grid))
        for c in range(len(grid[r]))
        if grid[r][c] in KEY_CHARS
    )


def part1(grid):
    all_keys = find_all_keys(grid)
    queue = [(0, set(), find_start(grid))]
    visited_states = set()

    while queue:
        steps, have_keys, (r, c) = heapq.heappop(queue)
        state = (frozenset(have_keys), (r, c))

        if grid[r][c] == "#":
            continue

        if state in visited_states:
            continue
        visited_states.add(state)

        if grid[r][c] in DOOR_CHARS and grid[r][c].lower() not in have_keys:
            continue

        if grid[r][c] in KEY_CHARS:
            have_keys.add(grid[r][c])

        if have_keys == all_keys:
            print(steps)
            return steps

        for dr, dc in OFFSETS:
            next_r, next_c = r + dr, c + dc
            heapq.heappush(queue, (steps + 1, set(have_keys), (next_r, next_c)))


def main(grid):
    part1(grid)


if __name__ == "__main__":
    from input import day18

    grid = day18.splitlines()
    main(grid)
