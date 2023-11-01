from datetime import datetime
from note import Note
import json


class Notebook:
    notes = []
    max_id = 0

    def __init__(self):
        self.read_notes()

    def add_note(self, header, body):
        new_id = self.max_id + 1
        new_note = Note(note_id=new_id,
                        header=header,
                        body=body)
        self.notes.append(new_note)
        self.write_notes()

    def edit_note(self, id_number: int, header, body):
        for note in self.notes:
            if note.note_id == id_number:
                note.header = header
                note.body = body
                note.change_time = datetime.now()
                self.write_notes()
                return
        raise KeyError(f"Запись с индексом {id_number} не найдена")

    def delete_note(self, id_number: int):
        for (index, note) in enumerate(self.notes):
            if note.note_id == id_number:
                self.notes.pop(index)
                self.write_notes()
                return
        raise KeyError(f"Запись с индексом {id_number} не найдена")

    def read_notes(self):
        try:
            with open('notes.json', mode='r+') as file:
                data = json.load(file)
                self.notes = [Note(note_id=record['note_id'],
                                   header=record['header'],
                                   body=record['body'],
                                   create_time=datetime.strptime(record['create_time'], "%d.%m.%Y %H:%M:%S"),
                                   change_time=datetime.strptime(record['change_time'], "%d.%m.%Y %H:%M:%S")
                                   ) for record in data]
            self.max_id = max([note.note_id for note in self.notes])
        except FileNotFoundError:
            with open('notes.json', mode='w'):
                pass

    def write_notes(self):
        with open('notes.json', mode='w') as file:
            data_to_write = [note.as_dict() for note in self.notes]
            if data_to_write is not None:
                json.dump(data_to_write, file)
        self.read_notes()

    def filter_by_date(self, start: datetime, end=datetime.now()) -> str:
        filtered_notes = [note for note in self.notes if start <= note.change_time <= end]
        return '\n====================================\n'.join([str(note) for note in filtered_notes])

    def __str__(self):
        return '\n====================================\n'.join([str(note) for note in self.notes])