import os.path

input_dir = os.path.dirname(os.path.realpath(__file__))

def file_contents(filename):
    with open(os.path.join(input_dir, filename)) as f:
        return f.read()

day1 = file_contents('day1.txt')
day2 = file_contents('day2.txt')
day3 = file_contents('day3.txt')
day5 = file_contents('day5.txt')
day6 = file_contents('day6.txt')
day7 = file_contents('day7.txt')
day8 = file_contents('day8.txt')
