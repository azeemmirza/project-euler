import pyfiglet
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
from os import listdir
from os.path import isfile, join
import subprocess

console = Console()

SOLUTIONS_PATH = 'solutions'


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


def print_header():
    table = Table(show_header=False, box=box.ASCII)

    title = 'PROJECT EULER'

    f = pyfiglet.figlet_format(title, font='doom', width=500)
    heading = Text(f, style='#767676')
    author = Text('Solutions by AZEEM MIRZA', justify='center')
    num_solved = Text('Solved: ' + calculate_solved(), justify='center')


    table.add_row(heading)
    table.add_row(author)
    # table.add_row(num_solved)

    console.print(table)


def exit_program():
    console.print('\n\nProject Euler - \xa9 Azeem Mirza')


def run_solution(name: str):
    file_path = join(SOLUTIONS_PATH, name + '.py')
    subprocess.run(["python3", file_path])



def input_loop():
    running = True
    files = get_solutions_list(SOLUTIONS_PATH, True)

    print(files)

    while running == True:
        input_str = input('\nEnter Program Name: ')

        if input_str == 'end' or input_str == 'exit':
            running = False
            exit_program()

        elif input_str in files:
            print(input_str)
            run_solution(input_str)
            
        else:
            print('Invalid input or no solution available')



print_header()
input_loop()


