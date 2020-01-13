import math

from collections import defaultdict

def produce_fuel(fuel_amount, reactions):
    total_ore = 0
    materials = defaultdict(int)
    stack = [(fuel_amount, 'FUEL')]
    while stack:
        requested_amount, chemical = stack.pop()
        if chemical not in reactions:
            total_ore += requested_amount
        else:
            requested_amount -= materials[chemical]
            output_amount, inputs = reactions[chemical]
            multiplier = math.ceil(requested_amount / output_amount)
            for input_amount, input_chemical in inputs:
                stack.append((input_amount * multiplier, input_chemical))
            materials[chemical] = output_amount * multiplier - requested_amount
    return total_ore

def part1(reactions):
    total_ore = produce_fuel(1, reactions)
    print(total_ore)

def part2(reactions):
    max_ore = 1000000000000
    fuel_amount = 1
    while produce_fuel(fuel_amount, reactions) < max_ore:
        fuel_amount *= 2
    upper, lower = fuel_amount, fuel_amount / 2
    while upper - lower > 0.001:
        fuel_amount = (lower + upper) / 2
        result = produce_fuel(fuel_amount, reactions)
        if result == max_ore: break
        elif result < max_ore: lower = fuel_amount
        elif result > max_ore: upper = fuel_amount
    print(math.floor(fuel_amount))

def load_reactions(string):
    import parse
    reactions = {}
    pattern = parse.compile('{:d} {:w}')
    for line in string.splitlines():
        inputs_str, output_str = line.split(' => ')
        inputs = []
        for result in pattern.findall(inputs_str):
            inputs.append(tuple(result))
        output_amount, chemical = tuple(pattern.search(output_str))
        reactions[chemical] = (output_amount, inputs)
    return reactions

if __name__ == '__main__':
    from input import day14
    reactions = load_reactions(day14)
    # part1(reactions)
    part2(reactions)
