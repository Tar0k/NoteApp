import re
from datetime import datetime

from notebook import Notebook


def numeric_input(input_message, variable_name) -> int:
    number = ''
    while not number.isnumeric():
        number = input(input_message)
        if not number.isnumeric():
            print(f"'{variable_name}' должно быть числовым значением")
    return int(number)


def date_range_input() -> list[datetime]:
    while True:
        user_input = input("Введите диапазон дат в формате\ndd.mm.YYYY-dd.mm.YYYY или dd.mm.YYYY\n")
        data_range = re.findall(r"\d{2}.\d{2}.\d{4}", user_input)
        if len(data_range) != 2 and len(data_range) != 1:
            print("Некорректный формат ввода!")
            continue

        for index, date in enumerate(data_range):
            try:
                data_range[index] = datetime.strptime(date, '%d.%m.%Y')
            except ValueError:
                print(f"Некорректный ввод даты '{data_range[index]}'!")
                continue
        return data_range


if __name__ == '__main__':

    notebook = Notebook()

    while True:
        command = input("Введите команду: ")
        match command:
            case 'add':
                note_header = input("Введите заголовок заметки: ")
                note_body = input("Введите тело заметки: ")
                notebook.add_note(note_header, note_body)
            case 'edit':
                note_id = numeric_input("Введите 'id' редактируемой записи: ", 'id')
                note_header = input("Введите новый заголовок заметки: ")
                note_body = input("Введите новое тело заметки: ")
                notebook.edit_note(note_id, note_header, note_body)
            case 'delete':
                print(notebook)
                note_id = numeric_input("Введите 'id' удаляемой записи: ", 'id')
                notebook.delete_note(note_id)
            case 'print':
                print(notebook)
            case 'filter':
                date_range = date_range_input()
                match len(date_range):
                    case 1:
                        filtered_notes = notebook.print_filter_by_date(start=date_range[0])
                    case 2:
                        filtered_notes = notebook.print_filter_by_date(start=date_range[0], end=date_range[1])
                    case _:
                        filtered_notes = ""
                print(filtered_notes)
            case 'exit':
                break
