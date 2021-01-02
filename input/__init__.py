import os.path

input_dir = os.path.dirname(os.path.realpath(__file__))


def __getattr__(attr):
    with open(os.path.join(input_dir, f"{attr}.txt")) as f:
        return f.read()
