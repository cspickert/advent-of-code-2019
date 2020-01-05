def count_digits(layer, digit):
    return len([pixel for pixel in layer if pixel is digit])

def count_zeros(layer):
    return count_digits(layer, 0)

def part1(data, width, height):
    layers = [
        data[i: i + width * height]
        for i in range(0, len(data), width * height)]
    target = min(layers, key=count_zeros)
    print(count_digits(target, 1) * count_digits(target, 2))

class Image(object):
    def __init__(self, data, width, height):
        self.layers = [
            [layer[row * width: row * width + width] for row in range(height)]
            for layer in [
                data[i: i + width * height]
                for i in range(0, len(data), width * height)]]

    def pixel_at(self, row, col, layer=0):
        upper = self.layers[layer][row][col]
        if layer == len(self.layers) - 1:
            return upper
        lower = self.pixel_at(row, col, layer + 1)
        return upper if upper is not 2 else lower

    def __repr__(self):
        layer = self.layers[0]
        result = ''
        for row in range(len(layer)):
            for col in range(len(layer[row])):
                pixel = self.pixel_at(row, col)
                result += 'x' if pixel is 1 else ' '
            result += '\n'
        return result

def part2(data, width, height):
    image = Image(data, width, height)
    print(image)

if __name__ == '__main__':
    from input import day8
    data = list(map(int, day8))
    part2(data, 25, 6)
