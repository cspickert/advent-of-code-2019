from computer import Computer


def run_script(program, script):
    computer = Computer(program)
    computer.input_str(script)
    while not computer.is_halted:
        output = computer.run_partial()
        if output:
            try:
                print(chr(output), end="")
            except ValueError:
                print(output)


def part1(program):
    # If there are any holes coming up in the next three spaces (A, B,
    # C), AND there is no hole at the fourth space (D), then jump.
    #
    # Pseudocode: J = D AND (NOT A OR NOT B OR NOT C)
    #
    script = """\
NOT A T
NOT B J
OR T J
NOT C T
OR T J
NOT D T
NOT T T
AND T J
WALK
"""
    run_script(program, script)


def part2(program):
    # If there are any holes coming up in the next three spaces (A, B,
    # C), AND there is no hole at the fourth space (D), AND the fifth
    # space or the eighth space is not a hole, then jump.
    #
    # J = D AND (NOT A OR NOT B OR NOT C) AND (E OR H)
    #
    script = """\
NOT A T
NOT B J
OR T J
NOT C T
OR T J
NOT D T
NOT T T
AND T J
NOT E T
NOT T T
OR H T
AND T J
RUN
"""
    run_script(program, script)


def main(program):
    part1(program)
    part2(program)


if __name__ == "__main__":
    from input import day21

    program = [int(c) for c in day21.split(",")]
    main(program)
