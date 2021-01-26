from collections import deque

from computer import Computer


def part1(program):
    computers = [Computer(program) for _ in range(50)]
    computer_queues = [deque() for _ in range(50)]

    def get_input(i):
        queue = computer_queues[i]
        while queue:
            x, y = queue.pop()
            yield x
            yield y
        yield -1

    for i, computer in enumerate(computers):
        computer.input(i)

    while True:
        for i, computer in enumerate(computers):
            computer_input_generator = get_input(i)
            computer.get_next_input = lambda: next(computer_input_generator)

            try:
                d, x, y = [computer.run_partial() for _ in range(3)]
            except StopIteration:
                continue

            if d == 255:
                print(y)
                return

            computer_queues[d].appendleft((x, y))


def main(program):
    part1(program)


if __name__ == "__main__":
    from input import day23

    program = [int(c) for c in day23.split(",")]
    main(program)
