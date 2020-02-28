from typing import List
from .commands import ParentCommand, Command
from .exceptions import CommandException


class CliParser:
    def __init__(self, commands: List[Command]):
        self.commands = {command.name: command for command in commands}

    def process_response(self, response):
        if response.lower() in ['q', 'quit', 'stop', 'kill', 'exit']:
            raise RuntimeError('Quitting Interpreter')
        elif response.lower() in ['h', '-h', '--help', 'help']:
            return self.get_help()
        else:
            command, args = self._cmd_lookup(response)
            print(f'Executing command {command.name} with arguments: {" ".join(args)}')
            return command(*args)

    def _get_cmd(self, cmd_name):
        try:
            return self.commands[cmd_name]
        except KeyError:
            raise CommandException(f'No such command: {cmd_name}')

    def _cmd_lookup(self, response):
        cmd, args = CliParser._parse_response(response)
        cmd_obj = None

        while len(args) >= 1:
            cmd_obj = self._get_cmd(cmd) if not cmd_obj else cmd_obj

            if isinstance(cmd_obj, ParentCommand):
                sub_cmd = cmd_obj.get_sub_cmd(args[0])
                cmd_obj, args = sub_cmd, args[1:]
            else:
                return cmd_obj, args

        return self._get_cmd(cmd), args

    def get_help(self):
        return '\n'.join([cmd.get_help() for cmd in self.commands.values()])

    @staticmethod
    def _parse_response(response):
        try:
            cmd, *args = response.split(' ')
            return cmd, args
        except ValueError:
            return response.strip(' '), None
