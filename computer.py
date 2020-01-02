import enum
import sys

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

    def __repr__(self):
        return f'Ref({self.value}@{self.position})'

class Immediate(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f'Immediate({self.value})'

class HaltException(Exception):
    pass

class JumpException(Exception):
    def __init__(self, index):
        self.index = index

class Operation(object):
    operations = {}

    @classmethod
    def register(cls, subcls):
        operation = subcls()
        cls.operations[operation.opcode] = operation

    @classmethod
    def from_opcode(cls, opcode):
        return cls.operations[opcode % 100]

    def __init__(self, opcode, num_args):
        self.opcode = opcode
        self.num_args = num_args

    def execute(self, computer, *args):
        pass

@Operation.register
class Add(Operation):
    def __init__(self):
        super().__init__(1, 3)

    def execute(self, computer, arg0, arg1, dest):
        dest.value = arg0.value + arg1.value

@Operation.register
class Multiply(Operation):
    def __init__(self):
        super().__init__(2, 3)

    def execute(self, computer, arg0, arg1, dest):
        dest.value = arg0.value * arg1.value

@Operation.register
class Input(Operation):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, computer, dest):
        dest.value = int(computer.io.stdin.readline())

@Operation.register
class Output(Operation):
    def __init__(self):
        super().__init__(4, 1)

    def execute(self, computer, arg0):
        print(arg0.value, file=computer.io.stdout)

@Operation.register
class JumpIfTrue(Operation):
    def __init__(self):
        super().__init__(5, 2)

    def execute(self, computer, arg0, arg1):
        if arg0.value != 0:
            raise JumpException(arg1.value)

@Operation.register
class JumpIfFalse(Operation):
    def __init__(self):
        super().__init__(6, 2)

    def execute(self, computer, arg0, arg1):
        if arg0.value == 0:
            raise JumpException(arg1.value)

@Operation.register
class TestLessThan(Operation):
    def __init__(self):
        super().__init__(7, 3)

    def execute(self, computer, arg0, arg1, dest):
        dest.value = 1 if arg0.value < arg1.value else 0

@Operation.register
class TestEqualTo(Operation):
    def __init__(self):
        super().__init__(8, 3)

    def execute(self, computer, arg0, arg1, dest):
        dest.value = 1 if arg0.value == arg1.value else 0

@Operation.register
class Halt(Operation):
    def __init__(self):
        super().__init__(99, 0)

    def execute(self, computer, *args):
        raise HaltException()

class ParameterMode(enum.Enum):
    POSITIONAL = 0
    IMMEDIATE = 1

    @classmethod
    def unpack_modes(cls, value):
        modes = []
        value //= 100
        while value > 0:
            mode = ParameterMode(value % 10)
            modes.append(mode)
            value //= 10
        return modes

class Instruction(object):
    def __init__(self, data, index):
        self.operation = Operation.from_opcode(data[index])
        self.parameter_modes = ParameterMode.unpack_modes(data[index])
        self.args = []
        for i in range(self.operation.num_args):
            parameter_mode = self.parameter_mode_at(i)
            value = data[index + 1 + i]
            if parameter_mode == ParameterMode.POSITIONAL:
                arg = Ref(data, value)
            elif parameter_mode == ParameterMode.IMMEDIATE:
                arg = Immediate(value)
            self.args.append(arg)

    def parameter_mode_at(self, i):
        if i < len(self.parameter_modes):
            return self.parameter_modes[i]
        return ParameterMode.POSITIONAL

    def execute(self, computer):
        self.operation.execute(computer, *self.args)

    @property
    def size(self):
        return 1 + len(self.args)

    def __repr__(self):
        return f'{self.operation.__class__.__name__}({self.args})'

class IO(object):
    def __init__(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout

class Computer(object):
    def __init__(self):
        self.io = IO()

    def run(self, data):
        data = data.copy()
        index = 0
        while index < len(data):
            instruction = Instruction(data, index)
            try:
                instruction.execute(self)
            except HaltException:
                break
            except JumpException as e:
                index = e.index
                continue
            index += instruction.size
        return data[0]
