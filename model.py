import datetime
import csv


class Note:
    count_id = 1

    def __init__(self, name: str, comment: str, data_time=datetime.datetime.now().replace(microsecond=0), change_data_time=None):
        self.name = name
        self.comment = comment
        self.uid = Note.count_id
        Note.count_id += 1
        self.data_time = data_time
        self.change_data_time = change_data_time

    def __str__(self) -> str:
        if self.change_data_time == None:
            return f'{self.uid}:{self.name}:{self.comment}:{self.data_time}'
        else:
            return f'{self.uid}:{self.name}:{self.comment}:{self.data_time}:{self.change_data_time}'

    def for_search(self):
        return f'{self.name} {self.comment}'.lower()


class Notebook:

    def __init__(self, path: str):
        self.notes: list[Note] = []
        self.path = path

    def open_file(self):
        if len(self.notes) == 0:
            with open(self.path, encoding='UTF-8') as file:
                file_reader = csv.reader(file, delimiter=':')
                for row in file_reader:
                    stt = row[3]
                    print(row)
                    date_time_obj = datetime.datetime.strptime(stt, '%Y-%m-%d %H:%M:%S')
                    if len(row) == 5:
                        _, name, comment, data_time, change_data = \
                            row[0], row[1], row[2], date_time_obj, row[4]
                        self.notes.append(Note(name, comment, data_time, change_data))
                    else:
                        _, name, comment, data_time = row[0], row[1], row[2], date_time_obj
                        self.notes.append(Note(name, comment, data_time))

    def add_note(self, new: Note):
        self.notes.append(new)

    def search(self, word: str) -> list[Note]:
        result = Notebook('поиск')
        for note in self.notes:
            if word.lower() in note.for_search():
                result.notes.append(note)
        return result

    def change(self, index: int, new):
        for note in self.notes:
            if index == note.uid:
                note.name = note.name if new.name == '' else new.name
                note.comment = note.comment if new.comment == '' else new.comment
                note.change_data_time = datetime.datetime.now()

    def deleted(self, index: int):
        note = self.notes.pop(index - 1)
        return note.name

    def save_file(self):
        with open(self.path, mode="w", encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter=':',lineterminator="\r")
            for note in self.notes:
                if note.change_data_time != 0:
                    file_writer.writerow([note.uid, note.name, note.comment, note.data_time, note.change_data_time])
                else:
                    file_writer.writerow([note.uid, note.name, note.comment, note.data_time])
