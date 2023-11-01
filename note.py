from datetime import datetime

"""
Пока не внедрил
"""


class Note:
    def __init__(self, note_id, header, body,
                 create_time=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                 change_time=datetime.now().strftime("%d.%m.%Y %H:%M:%S")):
        self.note_id = note_id
        self.header = header
        self.body = body
        self.create_time = create_time
        self.change_time = change_time

    def __str__(self):
        return (f"ID: {self.note_id}\n"
                f"Заголовок: {self.header}\n"
                f"Тело: {self.body}\n"
                f"Дата создания: {self.create_time}, Дата изменения: {self.change_time}"
                )
