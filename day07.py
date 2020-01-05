import io
import itertools

from computer import Computer

def part1(data):
    best_signal = 0
    phase_settings = [0, 1, 2, 3, 4]
    for configuration in itertools.permutations(phase_settings):
        signal = 0
        for phase_setting in configuration:
            computer = Computer(data)
            computer.input(phase_setting)
            computer.input(signal)
            signal = computer.run()
            best_signal = max(best_signal, signal)
    print(best_signal)

def part2(data):
    best_signal = 0
    phase_settings = range(5, 10)
    for configuration in itertools.permutations(phase_settings):
        computers = []
        for phase_setting in configuration:
            computer = Computer(data)
            computer.input(phase_setting)
            computers.append(computer)
        signal = 0
        computers_iter = itertools.cycle(computers)
        while all(not computer.is_halted for computer in computers):
            computer = next(computers_iter)
            computer.input(signal)
            next_signal = computer.run_partial()
            if next_signal is not None:
                signal = next_signal
        best_signal = max(best_signal, signal)
    print(best_signal)

if __name__ == '__main__':
    from input import day07
    data = list(map(int, day07.split(',')))
    part2(data)
