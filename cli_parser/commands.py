from typing import Callable, Optional
from .exceptions import NoSuchCommandError
from inspect import signature


class Command:
    def __init__(self, name: str, action: Optional[Callable], help_description: str = ''):
        self.name = name
        self.action = action
        self._help = help_description

    def __call__(self, *args):
        args = [arg for arg in args if arg != '']
        cmd_param_num = len(signature(self.action).parameters)
        args = [' '.join(args)] if len(args) > cmd_param_num else args

        return self.action(*args)

    def get_help(self):
        return self._help if self._help else self.action.__doc__


class ParentCommand(Command):
    f"""
    Parent Command to create a hierarchy, e.g:
    `get` is a parent command of:
        - get names
        - get website
    
    """

    def __init__(self, name: str):
        super().__init__(name, None, '')

        self.children = {}

    def __call__(self, *args):
        return self.action(*args) if self.action else self.get_help()

    def get_help(self):
        cmds_help = '\n'.join([f'\t -- {cmd.get_help()}' for cmd in self.children.values()])
        help_ = f'-- {self.name}' + cmds_help
        return help_

    def add_sub_cmds(self, *sub_commands: Command):
        self.children.update({sc.name: sc for sc in sub_commands})

    def get_sub_cmd(self, sub_cmd):
        try:
            return self.children[sub_cmd]
        except KeyError:
            raise NoSuchCommandError(f'No such command: {sub_cmd}')
