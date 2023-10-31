import io
from datetime import datetime
import json


class Notebook:
    notes = []
    max_id = 0

    def __init__(self):
        self.read_notes()

    def add_note(self, header, body):
        new_id = self.max_id + 1
        self.notes.append({
            "id": new_id,
            "header": header,
            "body": body,
            "create_time": datetime.now().strftime("%d.%m%Y %H:%M:%S"),
            "change_time": datetime.now().strftime("%d.%m%Y %H:%M:%S")
        })
        self.write_notes()

    def edit_note(self, id_number: int, header, body):
        for note in self.notes:
            print(type(note['id']))
            if note['id'] == int(id_number):
                note['header'] = header
                note['body'] = body
                note['change_time'] = datetime.now().strftime("%d.%m%Y %H:%M:%S")
                self.write_notes()
                return
        raise KeyError(f"Запись с индексом {id_number} не найдена")

    def delete_note(self, id_number: int):
        for (index, note) in enumerate(self.notes):
            if note['id'] == int(id_number):
                self.notes.pop(index)
                self.write_notes()
                return
        raise KeyError(f"Запись с индексом {id_number} не найдена")

    def read_notes(self):
        try:
            with open('notes.json', mode='r+') as file:
                self.notes = json.load(file)
            self.max_id = max(self.notes, key=lambda x: x['id'])['id']
        except FileNotFoundError:
            with open('notes.json', mode='w'):
                pass

    def write_notes(self):
        with open('notes.json', mode='w') as file:
            json.dump(self.notes, file)
        self.read_notes()

    def __str__(self):
        text = []
        for note in self.notes:
            text.append(f"ID: {note['id']}\n"
                        f"Заголовок: {note['header']}\n"
                        f"Тело: {note['body']}\n"
                        f"Дата создания: {note['create_time']}, Дата изменения: {note['change_time']}"
                        )
        return '\n====================================\n'.join(text)