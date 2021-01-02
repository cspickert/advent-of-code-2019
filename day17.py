from computer import Computer


def part1(grid):
    result = sum(
        r * c
        for r in range(1, len(grid) - 1)
        for c in range(1, len(grid[r]) - 1)
        if all(
            x == "#"
            for x in (
                grid[r][c],
                grid[r - 1][c],
                grid[r][c - 1],
                grid[r + 1][c],
                grid[r][c + 1],
            )
        )
    )
    print(result)


def rotated(orientation):
    return {"^": "<", "<": "v", "v": ">", ">": "^"}[orientation]


def find_instructions(grid):
    orientations = {
        "^": (-1, 0),
        "<": (0, -1),
        "v": (1, 0),
        ">": (0, 1),
    }

    # Find the initial orientation and position.
    state = next(
        (grid[r][c], r, c)
        for r in range(len(grid))
        for c in range(len(grid[r]))
        if grid[r][c] in orientations
    )
    prev_state = None

    rotations = 0
    instructions = []

    while rotations < 4:
        orientation, r, c = state
        dr, dc = orientations[orientation]
        next_r, next_c = r + dr, c + dc
        if (
            next_r not in range(len(grid))
            or next_c not in range(len(grid[next_r]))
            or grid[next_r][next_c] != "#"
            or (prev_state and prev_state[1:] == (next_r, next_c))
        ):
            rotations += 1
            state = (rotated(orientation), r, c)
        else:
            if rotations:
                instructions.append({1: "L", 3: "R"}[rotations])
            if not instructions or not isinstance(instructions[-1], int):
                instructions.append(0)
            instructions[-1] += 1
            rotations = 0
            prev_state = state
            state = (orientation, next_r, next_c)

    return instructions


def find_pattern_sequence(patterns, data):
    result = []
    i = 0
    while i < len(data):
        for pattern_idx, pattern in enumerate(patterns):
            if data[i : i + len(pattern)] == pattern:
                i += len(pattern)
                result.append(pattern_idx)
                break
        else:
            return None
    return result


def find_patterns(data, num_patterns=3):
    if num_patterns == 0:
        return ([], []) if not data else None
    for pattern_len in range(10, 1, -2):
        pattern = data[:pattern_len]
        rest = []
        i = 0
        while i < len(data):
            if data[i : i + pattern_len] == pattern:
                i += pattern_len
            else:
                rest.append(data[i])
                i += 1
        next_result = find_patterns(rest, num_patterns - 1)
        if next_result is not None:
            other_patterns = next_result[0]
            all_patterns = [pattern] + other_patterns
            pattern_sequence = find_pattern_sequence(all_patterns, data)
            if pattern_sequence:
                return all_patterns, pattern_sequence


def part2(grid, data):
    instructions = find_instructions(grid)
    patterns, sequence = find_patterns(instructions)

    main_routine = [
        ord(c) for c in ",".join(chr(ord("A") + i) for i in sequence) + "\n"
    ]
    function_a = [ord(c) for c in ",".join(str(x) for x in patterns[0]) + "\n"]
    function_b = [ord(c) for c in ",".join(str(x) for x in patterns[1]) + "\n"]
    function_c = [ord(c) for c in ",".join(str(x) for x in patterns[2]) + "\n"]
    output_opt = [ord(c) for c in "n\n"]

    data[0] = 2
    computer = Computer(data)

    for value in main_routine + function_a + function_b + function_c + output_opt:
        computer.input(value)
    print(computer.run())


def main(grid, data):
    part1(grid)
    part2(grid, data)


if __name__ == "__main__":
    from input import day17

    data = [int(c) for c in day17.split(",")]
    computer = Computer(data)
    grid_str = "".join(chr(i) for i in computer).strip()
    grid = grid_str.splitlines()
    main(grid, data)
