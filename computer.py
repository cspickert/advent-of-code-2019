class Ref(object):
    def __init__(self, data, position):
        self.data = data
        self.position = position

    @property
    def value(self):
        return self.data[self.position]

    @value.setter
    def value(self, value):
        self.data[self.position] = value

class HaltException(Exception):
    pass

class Operation(object):
    operations = {}

    @classmethod
    def register(cls, subcls):
        operation = subcls()
        cls.operations[operation.opcode] = operation

    @classmethod
    def from_opcode(cls, opcode):
        return cls.operations[opcode]

    def __init__(self, opcode, num_args):
        self.opcode = opcode
        self.num_args = num_args

    def execute(self, *args):
        pass

@Operation.register
class Add(Operation):
    def __init__(self):
        super().__init__(1, 3)

    def execute(self, arg0, arg1, dest):
        dest.value = arg0.value + arg1.value

@Operation.register
class Multiply(Operation):
    def __init__(self):
        super().__init__(2, 3)

    def execute(self, arg0, arg1, dest):
        dest.value = arg0.value * arg1.value

@Operation.register
class Halt(Operation):
    def __init__(self):
        super().__init__(99, 0)

    def execute(self, *args):
        raise HaltException()

class Computer(object):
    def run(self, data, noun=12, verb=2):
        data = data.copy()
        data[1] = noun
        data[2] = verb
        index = 0
        while index < len(data):
            operation = Operation.from_opcode(data[index])
            index += 1
            args = map(
                lambda position: Ref(data, position),
                data[index:index + operation.num_args])
            try:
                operation.execute(*args)
            except HaltException:
                break
            index += operation.num_args
        return data[0]
