import pyfiglet
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
from os import listdir
from os.path import isfile, join


def calculate_solved():
    mypath = './solutions'
    files = []

    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            files.append(f)

    return str(len(files))


def print_header():
    table = Table(show_header=False, box=box.ASCII)

    console = Console()

    title = 'Project Euler'

    f = pyfiglet.figlet_format(title, font='doom', width=500)
    heading = Text(f, style='#767676')
    author = Text('Solved by AZEEM MIRZA', justify='center')
    num_solved = Text('Solved: ' + calculate_solved(), justify='center')


    table.add_row(heading)
    table.add_row(author)
    # table.add_row(num_solved)

    console.print(table)


print_header()


