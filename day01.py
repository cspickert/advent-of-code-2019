import math

def fuel(mass):
    result = math.floor(mass / 3.0) - 2

    # Part 1
    # return result

    # Part 2
    if result < 0:
        return 0
    return result + fuel(result)

def main():
    from input import day01
    fuel_total = 0
    for line in day01.splitlines():
        mass = int(line)
        fuel_total += fuel(mass)
    print(fuel_total)

if __name__ == '__main__':
    main()
