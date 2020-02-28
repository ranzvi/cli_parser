from .commands import Command


def command(func):
    return Command(func.__name__, func, func.__doc__)
