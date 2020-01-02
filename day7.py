import io
import itertools

from computer import Computer

def main(data):
    best_signal = 0
    phase_settings = [0, 1, 2, 3, 4]
    for configuration in itertools.permutations(phase_settings):
        signal = 0
        for phase_setting in configuration:
            computer = Computer()
            computer.io.stdin = io.StringIO(f'{phase_setting}\n{signal}\n')
            computer.io.stdout = io.StringIO()
            computer.run(data)
            computer.io.stdout.seek(0)
            signal = int(computer.io.stdout.read())
            best_signal = max(best_signal, signal)
    print(best_signal)

if __name__ == '__main__':
    from input import day7
    data = list(map(int, day7.split(',')))
    main(data)
