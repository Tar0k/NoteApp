from notebook import Notebook


def numeric_input(input_message, variable_name):
    number = ''
    while not number.isnumeric():
        number = input(input_message)
        if not number.isnumeric():
            print(f"'{variable_name}' должно быть числовым значением")
    return number


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
            case 'exit':
                break




