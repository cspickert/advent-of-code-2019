import enum
import sys

class Ref(object):
    def __init__(self, data, offset, base=0):
        self.data = data
        self.offset = offset
        self.base = base

    @property
    def position(self):
        return self.base + self.offset

    @property
    def value(self):
        return self.data[self.position]

    @value.setter
    def value(self, value):
        self.data[self.position] = value

    def __repr__(self):
        return f'Ref({self.value} @ {self.position} [{self.offset} + {self.base}])'

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
        dest.value = computer.get_input()

@Operation.register
class Output(Operation):
    def __init__(self):
        super().__init__(4, 1)

    def execute(self, computer, arg0):
        computer.output = arg0.value

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
class OffsetRelativeBase(Operation):
    def __init__(self):
        super().__init__(9, 1)

    def execute(self, computer, arg0):
        computer.relative_base += arg0.value

@Operation.register
class Halt(Operation):
    def __init__(self):
        super().__init__(99, 0)

    def execute(self, computer, *args):
        computer.is_halted = True

class ParameterMode(enum.Enum):
    POSITIONAL = 0
    IMMEDIATE = 1
    RELATIVE = 2

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
    def __init__(self, data, index, relative_base=0):
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
            elif parameter_mode == ParameterMode.RELATIVE:
                arg = Ref(data, value, relative_base)
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

class Computer(object):
    def __init__(self, data):
        self.data = data.copy() + [0] * 10000
        self.data_index = 0
        self.inputs = []
        self.output = None
        self.is_halted = False
        self.relative_base = 0

    def input(self, value):
        self.inputs.insert(0, value)

    def get_input(self):
        if self.inputs:
            return self.inputs.pop()
        return int(sys.stdin.readline())

    # Runs until the next output occurs or the program halts.
    def run_partial(self):
        self.output = None
        while not self.is_halted:
            instruction = Instruction(
                self.data, self.data_index, self.relative_base)
            try:
                instruction.execute(self)
                self.data_index += instruction.size
                if self.output is not None:
                    break
            except JumpException as e:
                self.data_index = e.index
        return self.output

    def run(self):
        last_output = self.output
        while not self.is_halted:
            output = self.run_partial()
            if output is not None:
                last_output = output
        if last_output is not None:
            return last_output
        return self.data[0]
