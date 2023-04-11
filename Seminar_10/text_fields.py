main_menu = '''Главное меню:
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выйти'''

choice_menu = '\nВыберите пункт меню: '

empty_list_or_not_open_file = 'Телефонная книга пуста или файл не открыт!'

successful_open = 'Файл открыт успешно!'
successful_save = 'Файл сохранен успешно!'


def successful_edited(name: str) -> str:
    return f'Контакт {name} успешно изменен!'


new_name = 'Введите имя контакта: '
new_phone = 'Введите телефон контакта: '
new_comment = 'Введите комментарий к контакту: '


def contact_saved(name: str) -> str:
    return f'Контакт {name} успешно сохранен!'


def not_found(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'


input_keyword = 'Введите искомый элемент: '

input_index = 'Введите номер изменяемого контакта: '

enter_or_empty = 'Введите новые значения или оставьте пустым для сохранения оригинального значения'

input_delete_index = 'Введите индекс контакта, который хотите удалить: '


def delete_contact(name: str) -> str:
    return f'Контакт {name} успешно удален!'


def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить контакт {name}?'


goodbye = 'Удачного дня! Скоро увидимся!'

no_saved_book = 'В вашей телефонной книге есть несохраненные изменения! Сохранить?'