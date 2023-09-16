from text import *
from model import Note,Notebook


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_notes(book):
    if book.notes:
        max_len = 0
        for note in book.notes:
            if len(note.__str__()) > max_len:
                max_len = len(note.__str__())
        print('\n' + '=' * max_len)
        for note in book.notes:
            print(note)
        print('=' * max_len + '\n')
    else:
        print(book_error)


def input_note(message: str) -> dict[str, str]:
    print(message)
    new = Note(input(new_note[0]), input(new_note[1]), change_data_time=0)
    return new


def input_return(message: str) -> str:
    return input(message)