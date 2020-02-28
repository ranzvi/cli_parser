# CLI Parser
## Simple Chained Command Parser

This tool will allow you to create a simple command hierarchy to execute from the command line.

### Example
```python
from cli_parser import command, CliParser, ParentCommand, CommandException

get = ParentCommand('get')

@command
def product(x, y):
    return x * y

@command
def sum(x, y):
    return x + y
    
get.add_sub_cmds(product, sum)

parser = CliParser([get])

while True:
    in_ = input("Enter command:\n==> ")
    
    try:
        response = parser.process_response(in_)
        print(response)
    except CommandException:
       pass
```  

Execute your script from the command line:

```
Enter command:
==> get product 5 10
50

Enter command:
==> get sum 10 20
30

Enter command:
==> q

'Quitting Interpreter'

```

pypi: https://pypi.org/project/cli-parser/