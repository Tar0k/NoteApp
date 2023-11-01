from datetime import datetime


class Note:
    def __init__(self, note_id, header, body,
                 create_time=None,
                 change_time=None):
        self.note_id = note_id
        self.header = header
        self.body = body
        self.create_time = datetime.now() if create_time is None else create_time
        self.change_time = datetime.now() if change_time is None else change_time

    def as_dict(self):
        temp_dict = self.__dict__
        temp_dict['create_time'] = self.create_time.strftime("%d.%m.%Y %H:%M:%S")
        temp_dict['change_time'] = self.change_time.strftime("%d.%m.%Y %H:%M:%S")
        return temp_dict

    def __str__(self):
        return (f"ID: {self.note_id}\n"
                f"Заголовок: {self.header}\n"
                f"Тело: {self.body}\n"
                f"Дата создания: {self.create_time.strftime("%d.%m.%Y")},"
                f" Дата изменения: {self.change_time.strftime("%d.%m.%Y")}"
                )
