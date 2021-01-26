from collections import defaultdict, deque

from computer import Computer


class Network:
    def __init__(self, program):
        self.computers = [Computer(program) for _ in range(50)]
        self.computer_queues = [deque() for _ in range(len(self.computers))]

        for i, computer in enumerate(self.computers):
            computer.input(i)

    def run(self):
        def get_input(i):
            queue = self.computer_queues[i]
            while queue:
                x, y = queue.pop()
                yield x
                yield y
            yield -1

        while True:
            idle_count = 0

            for i, computer in enumerate(self.computers):
                computer_input_generator = get_input(i)
                computer.get_next_input = lambda: next(computer_input_generator)

                try:
                    d, x, y = [computer.run_partial() for _ in range(3)]
                except StopIteration:
                    idle_count += 1
                    continue

                if d == 255:
                    done = self.handle_nat(x, y)
                    if done:
                        return
                else:
                    self.computer_queues[d].appendleft((x, y))

            if idle_count == len(self.computers):
                done = self.handle_idle()
                if done:
                    return

    def handle_nat(self, x, y):
        return True

    def handle_idle(self):
        return True


def part1(program):
    class Part1Network(Network):
        def handle_nat(self, x, y):
            print(y)
            return True

    network = Part1Network(program)
    network.run()


def part2(program):
    class Part2Network(Network):
        def __init__(self, program):
            super().__init__(program)
            self.nat_packet = None
            self.nat_y_counts = defaultdict(int)

        def handle_nat(self, x, y):
            self.nat_packet = (x, y)
            return False

        def handle_idle(self):
            x, y = self.nat_packet
            self.nat_y_counts[y] += 1
            if self.nat_y_counts[y] == 2:
                print(y)
                return True
            self.computer_queues[0].appendleft((x, y))
            return False

    network = Part2Network(program)
    network.run()


def main(program):
    part1(program)
    part2(program)


if __name__ == "__main__":
    from input import day23

    program = [int(c) for c in day23.split(",")]
    main(program)
