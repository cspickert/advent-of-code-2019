def deal_into_new_stack(deck):
    return list(reversed(deck))


def cut_cards(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    deck_iter = iter(deck)
    result = [None] * len(deck)
    for i in range(0, len(deck) * n, n):
        result[i % len(deck)] = next(deck_iter)
    return result


def handle_instruction(deck, instruction):
    if instruction.startswith("deal into new stack"):
        return deal_into_new_stack(deck)
    if instruction.startswith("deal with increment"):
        value = int(instruction.split()[-1])
        return deal_with_increment(deck, value)
    if instruction.startswith("cut"):
        value = int(instruction.split()[-1])
        return cut_cards(deck, value)


def part1(instructions):
    deck = list(range(10007))
    for instruction in instructions:
        deck = handle_instruction(deck, instruction)
    print(deck.index(2019))


def main(instructions):
    part1(instructions)


if __name__ == "__main__":
    from input import day22

    instructions = day22.splitlines()
    main(instructions)
