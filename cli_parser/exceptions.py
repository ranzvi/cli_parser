class CommandException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.__class__.__name__}, {self.message}'
        else:
            return f'{self.__class__.__name__} has been raised'


class NoSuchCommandError(CommandException):
    pass
