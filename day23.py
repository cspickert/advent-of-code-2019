from collections import deque

from computer import Computer


def part1(program):
    computers = [Computer(program) for _ in range(50)]
    computer_queues = [deque() for _ in range(50)]
    
    def get_input(i):
        queue = computer_queues[i]
        if not queue:
            yield -1
        else:
            x, y = queue.pop()
            yield x
            yield y

    for i, computer in enumerate(computers):
        computer.input(i)

    while True:
        for i, computer in enumerate(computers):
            computer_input_generator = get_input(i)
            computer.get_next_input = lambda: next(computer_input_generator)

            dest, x, y = [computer.run_partial() for _ in range(3)]
            if dest == 255:
                print(y)
                return
            computer_queues[dest].appendleft((x, y))


def main(program):
    part1(program)


if __name__ == "__main__":
    from input import day23

    program = [int(c) for c in day23.split(",")]
    main(program)
