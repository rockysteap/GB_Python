# MAIN MENU variables and languages
# In order to add new language revise model.choices and model.constraints
# 0 -> 'en' 1 -> 'ru'

main_menu = { 'titles': [['(M)ain menu', 'File menu', 'Book menu'],
                         ['(Г)лавное меню', 'Работа с файлами', 'Работа с книгой']],

              'main': [['(F)ile', '(B)ook', 'E(x)it', 'Change to:', '(R)u'],
                       ['(Ф)айл', '(К)нига', '(В)ыход', 'Сменить на:', '(А)нгл']],

              'file': [['(O)pen - read from file', '(S)ave - write to file', '', '', ''],
                       ['(О)ткрыть - считать из файла', '(С)охранить - записать в файл', '', '', '']],

              'book': [['(N)ew - make new entry', 'F(I)nd - search for entry', '(S)how - show book content',
                        '(E)dit - change existing entry', '(D)elete - remove existing entry'],
                       ['(С)оздать - новая запись', '(Н)айти - поиск записи',
                        '(П)оказать - вывести всё', '(И)зменить - откорректировать запись',
                        '(У)далить - стереть запись']] }

info_list = { 'en': ['Last opened:', 'Last saved:'],
              'ru': ['Последнее открытие:', 'Последнее сохранение:'] }

confirmations_prompt = [['y', 'n'],
                        ['д', 'н']]

# MESSAGES
# Confirm
message_confirmation_prompt = [' (y/n)?: ',
                               ' (д/н)?: ']
# Files
message_files_list_in_dir = ['List of *.csv files:',
                             'Список *.csv файлов:']
message_input_file_to_read = ['__________________________\n'
                              'Type in file name to read.',
                              '_______________________________\n'
                              'Для открытия введите имя файла.']
message_confirm_file_reading = ['Confirm reading from file',
                                'Подтверждаете считывание из файла']
message_no_files_to_read = ['No files to read.',
                            'Нет файлов для чтения.']
message_success_file_opened = ['File successfully readed.',
                               'Файл успешно прочитан.']
message_error_fail_to_open = ['Sorry. file doesn\'t exist or can\'t be readed. Please try again.',
                              'Извините. Файл не существует или не может быть прочитан. Попробуйте ещё раз.']
message_input_file_to_save = ['_______________________________\n'
                              'Type in file name to save book.',
                              '_______________________________________\n'
                              'Введите имя файла для сохранения книги.']
message_confirm_file_writing = ['Confirm writing to file',
                                'Подтверждаете запись в файл']
message_confirm_file_overwriting = ['File already exists!\n'
                                    'Confirm re-writing to file',
                                    'Такой файл существует!\n'
                                    'Подтверждаете перезапись файла']
message_success_file_saved = ['File successfully saved.',
                              'Файл успешно записан.']
message_input_phone = ['Enter phone number using space for separation.\n'
                       ':country <<space bar>> operator code <<space bar>> main 7-digit number',
                       'Введите номер телефона разделяя пробелом.\n'
                       ':код страны <<пробел>> код оператора <<пробел>> основной 7-значный номер']
message_input_memo = ['Enter memo.',
                      'Введите дополнительную информацию.']
message_empty_book = ['Book is empty. Add some contacts.',
                      'Книга пуста. Добавьте контакты.']
message_pause = ['Press Enter to continue...',
                 'Нажмите на Enter чтобы продолжить...']
message_new_entry_constructor = ['New entry constructor ->\n'
                                 'Type in names using space for separation.\n'
                                 ':lastname <<space bar>> firstname <<space bar>> patronymic',
                                 'Конструктор новой записи ->\n'
                                 'Введите данные разделяя пробелом.\n'
                                 ':фамилия <<пробел>> имя <<пробел>> отчество']
message_new_entry = ['New entry: ',
                     'Новая запись: ']
message_new_entry_confirm = ['Are you satisfied with this entry',
                             'Вы довольны собранной записью']
message_error_new_entry_min = ['Enter last and first names at least. Continue',
                               'Введите хотя бы фамилию и имя. Продолжить']
message_duplicates_matches_found = ['Matches found:',
                                    'Найдены совпадения:']
message_duplicates_no_matches_found = ['No matches found:',
                                       'Совпадения не найдены.']
message_search_results_on_inquiry = ['On inquiry',
                                     'По запросу']
message_search_results_in_fields = ['in fields:',
                                    'в полях:']
message_search_results_found = ['found',
                                'найдено']
message_search_results_matches = ['matches',
                                  'совпадений']
message_search_query_input = ['Type in search query: ',
                              'Введите запрос: ']
message_search_fields_input = ['Fields: (l)ast name, (f)irst name, (p)atronymic, (t)elephone number, (m)emo.\n'
                               'Enter one letter for every field needed or leave blank to search in all: ',
                               'Поля: (ф)амилия, (и)мя, (о)тчество, (т)елефон, (д)оп.инфо.\n'
                               'Введите по одной букве для необходимого поля или оставьте пустым: ']
message_fields = { 0: ['Last name', 'Фамилия'],
                   1: ['First name', 'Имя'],
                   2: ['Patronymic', 'Отчество'],
                   3: ['Phone number', 'Номер телефона'],
                   4: ['Memo', 'Дополнительная информация'] }
message_advanced_search_query = ['Enter field query if needed for field ',
                                 'В случае необходимости введите запрос для поля ']
message_error_min_values_in_advanced_search = ['Empty request or minimum requirement are not met: '
                                               '\'last name and first name\'.',
                                               'Пустой запрос или отсутствуют минимальные данные: '
                                               '\'фамилия и имя\'.']
message_input_confirm_to_try_advanced_search = ['Try again',
                                                'Желаете повторить']
message_input_ask_for_search_method = ['Choose contact by number or use search fields, '
                                       '\'y\' - use numbers, \'n\' - use fields',
                                       'Выбрать контакт по номеру или использовать поисковые поля, '
                                       '\'д\' - ввести номер, \'н\' - использовать поля']
message_input_num_for_contact = ['Enter contact number:',
                                 'Введите номер контакта:']
message_error_no_contact_by_number = ['No contact by number',
                                      'Нет контакта под номером']
message_edit_no_changes = ['No changes were made.',
                           'Изменений внесено не было.']
message_edit_changes_made = ['Next changes were made:',
                             'Внесены следующие изменения:']
message_edit_save_changes = ['Save changes',
                             'Сохранить изменения']
message_change_field = ['Change field:',
                        'Изменить поле:']
message_remove_entry = ['Remove entry',
                        'Удалить запись']
message_remove_entry_success = ['Entry successfully removed.',
                                'Запись успешно удалена']
message_save_changes = ['Book has changes since last save.\n'
                        'Save changes before exit',
                        'С момента последнего сохранения книга была изменена\n'
                        'Сохранить изменения перед выходом']
