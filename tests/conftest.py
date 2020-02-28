from pytest import fixture
from cli_parser.utils import command
from cli_parser import ParentCommand


@fixture
def command_fixture():
    @command
    def test(a):
        return a

    return test


@fixture
def parent_command_fixture():
    return ParentCommand('test_parent')
