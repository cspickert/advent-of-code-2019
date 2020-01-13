from collections import defaultdict

def produce(requested_amount, chemical, reactions, materials=defaultdict(int)):
    try:
        chem_output = next(key for key in reactions if key[1] == chemical)
    except StopIteration:
        materials[chemical] += requested_amount
        return requested_amount
    chem_inputs = reactions[chem_output]
    total_ore_used = 0
    for input_amount, input_chemical in chem_inputs:
        while materials[input_chemical] < input_amount:
            total_ore_used += produce(
                input_amount, input_chemical, reactions, materials)
        materials[input_chemical] -= input_amount
    output_amount, output_chemical = chem_output
    materials[output_chemical] += output_amount
    return total_ore_used

def part1(reactions):
    total_ore = produce(1, 'FUEL', reactions)
    print(total_ore)

if __name__ == '__main__':
    import parse
    from input import day14

    reactions = {}
    pattern = parse.compile('{:d} {:w}')

    for line in day14.splitlines():
        inputs_str, output_str = line.split(' => ')
        inputs = []
        for result in pattern.findall(inputs_str):
            inputs.append(tuple(result))
        output = tuple(pattern.search(output_str))
        reactions[output] = inputs
    part1(reactions)

