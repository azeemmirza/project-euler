import pyfiglet
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
from os import listdir
from os.path import isfile, join
import subprocess

SOLUTIONS_DIR = 'solutions'
console = Console()


# gets the list of solutions file
def get_solutions_list(path, with_ext=False) -> list[str]:
    files_list = listdir(path)

    def extension_remover(filename):
        return filename.rsplit('.', 1)[0]

    if with_ext:
        return list(map(extension_remover, files_list))

    return files_list


def calculate_solved():
    mypath = './solutions'
    files = []

    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            files.append(f)

    return str(len(files))


def exit_program():
    console.print('\n\nProject Euler - \xa9 Azeem Mirza')
    quit()


def run_solution(name: str):
    file_path = join(SOLUTIONS_DIR, name + '.py')
    subprocess.run(['python', file_path])


def main():
    running = True
    title = 'PROJECT EULER'
    files = get_solutions_list(SOLUTIONS_DIR, True)

    table = Table(show_header=False, box=box.ASCII)
    figlet = pyfiglet.figlet_format(title, font='doom', width=500)
    heading = Text(figlet, style='#767676')
    author = Text('Solutions by AZEEM MIRZA', justify='center')

    num_solved = Text('Solved: ' + calculate_solved(), justify='center')

    table.add_row(heading)
    table.add_row(author)
    # table.add_row(num_solved)

    # print main header and info
    console.print(table)

    while running:
        input_str = input('\nEnter Program Name: ')

        if input_str == 'end' or input_str == 'exit':
            running = False
            exit_program()

        elif input_str in files:
            print(input_str)
            run_solution(input_str)

        else:
            print('Invalid input or no solution available')


# run program
main()
