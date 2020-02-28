from cli_parser.commands import Command, ParentCommand
from cli_parser.parser import CliParser


def test_command_creation(command_fixture, parent_command_fixture):
    assert isinstance(command_fixture, Command)
    assert isinstance(parent_command_fixture, ParentCommand)


def test_cmd_tree(command_fixture, parent_command_fixture):
    parent_command_fixture.add_sub_cmds(command_fixture)
    assert parent_command_fixture.get_sub_cmd('test') == command_fixture


def test_parser_cmds(command_fixture, parent_command_fixture):
    parent_command_fixture.add_sub_cmds(command_fixture)
    parser = CliParser([parent_command_fixture])

    response = parser.process_response('test_parent test 5')
    assert response == '5'
