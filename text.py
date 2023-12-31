main_menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все заметки
    4. Создать новую заметку
    5. Найти заметку
    6. Изменить заметку
    7. Удалить заметку
    8. Выход
    '''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите от 1 до 8'
book_error = 'Книга заметок пуста или файл не открыт'

open_successful = 'Книга заметок успешно открыта'

input_new_note = 'Введите данные новой заметки'
new_note = ['Введите загаловок заметки: ', 'Введите коммент: ']
search_word = 'Введите искомый элемент: '
input_index = 'Введите индекс изменяемой заметки: '
input_change_note = 'Введите данные изменяемой заметки или Enter? чтоб оставить без изменений: '
input_index_deleted = 'Введите индекс удаляемой заметки: '

def note_saved(name: str):
    return f'Заметка {name} успешно сохранена'

def note_changed(name: str):
    return f'Заметка {name} успешно изменена'

exit_programm = 'Приятно было поработать возвращайся))'

def note_deleted(name: str):
    return f'Заметка {name} успешно удалена'

save_file = 'Файл успешно сохранен'