import os
import os.path
import pathlib
import string

# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Keys: last_name, first_name, patronymic, phone_num, memo

# Телефонный справочник.
# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# Global variables for current dataset in use
book = dict()
last_search = str()
last_advanced_search = list()
search_fields = list()
search_results = dict()
duplicates = set()
new_entry = list()
menu_state = str()

# File names
file_to_read = 'book.csv'
file_to_write = 'new_book.csv'
last_file_opened = 'no file'
last_file_saved = 'no file'


def is_book_empty():
    """ Check if book is empty """
    global book
    if 0 not in book:
        return True
    return False


def add_book_titles():
    """ Add titles to book """
    global book
    book[0] = ['last_name', 'first_name', 'patronymic', 'phone_num', 'memo']


def initialize_book():
    """ Check if book is empty, if empty -> add titles """
    if is_book_empty():
        add_book_titles()


def get_new_entry_id():
    """ Check for next available id number """
    global book
    initialize_book()
    new_id = len(list(book))
    while new_id in list(book):
        new_id += 1
    return new_id


def get_phone_num_from_user():
    """ Phone number input formatter """
    print('Enter phone number using space for separation.\n'
          ':country <<space bar>> operator code <<space bar>> main 7-digit number')
    phone_num = input(':').split()
    for index in range(len(phone_num)):
        for char in string.punctuation:
            phone_num[index] = phone_num[index].replace(char, '')
    phone_string = ''
    if len(phone_num) > 2:
        if phone_num[0] and phone_num[0].isdigit():
            phone_string += f'+{phone_num[0]}'
        if phone_num[1] and phone_num[1].isdigit():
            phone_string += f' ({phone_num[1]})'
        if phone_num[2] and phone_num[2].isdigit() and len(phone_num[2]) > 6:
            phone_string += f' {phone_num[2][:3]}-{phone_num[2][3:5]}-{phone_num[2][5:7]}'
    return phone_string


def get_file_to_read():
    """ Get user input for file name to open """
    global file_to_read
    while True:
        print('List of *.csv files:')
        # check_path = pathlib.Path().glob("*.csv")
        file_list = [item for item in list(pathlib.Path().glob("*.csv"))]
        for item in file_list:
            print(item)
        print('Type in file name to read.')
        file = input(': ')
        file.replace('.csv', '')
        file += '.csv'
        if os.path.isfile(file):
            confirm = input(f'Confirm reading from \'{file}\' (y/n): ')
            if confirm.lower() == 'y':
                file_to_read = file
                break
        elif not os.path.isfile(file):
            print(f'File \'{file}\' doesn\'t exist! Try again.')


def get_file_to_write():
    """ Get user input for file name to write """
    global file_to_write
    while True:
        print('List of *.csv files:')
        # check_path = pathlib.Path().glob("*.csv")
        file_list = [item for item in list(pathlib.Path().glob("*.csv"))]
        for item in file_list:
            print(item)
        print('Type in file name to write.')
        file = input(': ')
        file.replace('.csv', '')
        file += '.csv'
        if os.path.isfile(file):
            print('File already exists!')
            confirm = input(f'Confirm re-writing to \'{file}\' (y/n): ')
            if confirm.lower() == 'y':
                file_to_write = file
                break
        elif not os.path.isfile(file):
            print(f'File \'{file}\' doesn\'t exist.')
            confirm = input(f'Confirm writing to new file \'{file}\' (y/n): ')
            if confirm.lower() == 'y':
                file_to_write = file
                break


def read_from_file(file, override='no'):
    """ Open file and read lines to dictionary
        key 0 -> titles header
        from key 1 -> number is generally used as unique id """
    global book, last_file_opened
    try:
        book.clear()
        with open(file, 'r', encoding='UTF-8') as data:
            for i, line in enumerate(data):
                if line.strip():
                    line = line.rstrip('\n')
                    book[i] = []
                    for item in line.split(','):
                        book[i].append(item)
            last_file_opened = file
    except FileNotFoundError:
        print('File name you\'ve entered does not exist or can\'t be readed. Try again.')


def write_to_file(file):
    """ Write to file """
    global book, last_file_saved
    try:
        with open(file, 'w', encoding='UTF-8') as data:
            for value in book.values():
                data.write(','.join(value))
                data.write('\n')
            last_file_saved = file
    except FileNotFoundError:
        print('File name you\'ve entered does not exist or can\'t be readed. Try again.')


def show_all_contacts():
    """ Print contact list to terminal, check for empty(deleted) entries before printing """
    global book
    initialize_book()
    if len(list(book)) == 1:
        print('Book is empty. Add some contacts.')
    i = 0
    for key, value in book.items():
        if key == 0:
            continue
        elif value:
            i += 1
            print(f'{i}. ', end='')
            for item in value:
                print(item, '', end='')
            print()


def get_new_entry():
    """ Parse new entry user input """
    global new_entry
    while True:
        print('New entry constructor!\n'
              'Type in names using space for separation.\n'
              ':lastname <<space bar>> firstname <<space bar>> patronymic')
        full_name = input(':').split()
        for index in range(len(full_name)):
            for char in string.punctuation:
                full_name[index] = full_name[index].replace(char, '')
            new_entry.append(full_name[index].capitalize())
        phone_string = get_phone_num_from_user()
        new_entry.append(phone_string)
        print('Enter a memo:')
        new_entry.append(input(':'))
        print(*new_entry)
        confirm = input('Are you satisfied with this entry? (y/n): ')
        if confirm.lower() == 'y':
            break
        elif confirm.lower() == 'n':
            new_entry = []


def create_new_contact(contact):
    """ Create new contact """

    # Check if request is not empty, otherwise return
    if len([li for li in contact if li]) == 0 or not contact[0] or not contact[1]:
        return print('Empty request or minimum requirement are not met: last_name + first_name')

    global book
    initialize_book()

    # Parse new contact attributes
    contact_parsed = { i: value for i, value in enumerate(contact) }

    # Call for duplicates
    get_duplicates(contact_parsed)

    # Ask user to confirm
    while True:
        confirm = input('Save new entry (y/n): ')
        if confirm.lower() == 'n':
            break
        elif confirm.lower() == 'y':
            new_id = get_new_entry_id()
            book[new_id] = contact
            break


def get_duplicates(contact_parsed):
    """ Search for duplicates in the book """
    global book, search_results, duplicates

    duplicates_count = { key: [] for key in range(len(book[0])) }
    for key in contact_parsed:
        if contact_parsed[key] and key in range(4):  # check only: last_name, first_name, patronymic, phone_num
            search_for_contact(contact_parsed[key], [book[0][key]])  # call search func with field
            for i in range(1, len(list(search_results))):  # check search results global dict for every call
                duplicates_count[key].append(search_results[i])  # append search results on each call

    # Report duplicates search results
    interlaced_search = set()
    # if last_name + first_name + phone_num in request
    if contact_parsed[0] and contact_parsed[1] and contact_parsed[3]:
        interlaced_search = (set(duplicates_count[0])
                             .intersection(set(duplicates_count[1]))
                             .intersection(set(duplicates_count[3])))
    # if last_name + first_name + patronymic in request
    elif contact_parsed[0] and contact_parsed[1] and contact_parsed[2]:
        interlaced_search = (set(duplicates_count[0])
                             .intersection(set(duplicates_count[1]))
                             .intersection(set(duplicates_count[2])))
    # if last_name + first_name in request
    elif contact_parsed[0] and contact_parsed[1]:
        interlaced_search = (set(duplicates_count[0])
                             .intersection(set(duplicates_count[1])))
    elif contact_parsed[0]:
        interlaced_search = (set(duplicates_count[0]))
    elif contact_parsed[1]:
        interlaced_search = (set(duplicates_count[1]))
    if len(interlaced_search) > 0:
        print('Matches found:')
        for i, item in enumerate(interlaced_search, start=1):
            print(f'{i}. ', end='')
            print(*book[item], sep=' ')
    elif len(interlaced_search) == 0:
        print('No matches found.')
    duplicates = interlaced_search


def search_for_contact(search, fields=()):
    """ Search by given field, save results to global """
    global book, search_fields, search_results
    initialize_book()
    # Identify fields for search
    search_fields = fields if fields else book[0]
    # Get search indices of titles from our file (book[0])
    search_indices = list()
    for item in search_fields:
        search_indices.append(book[0].index(item))
    # Clear previous search results
    search_results.clear()
    # Add passed search fields to zero key
    search_results[0] = [search, search_fields]
    # Search
    for key, value in book.items():
        for index in search_indices:  # look only in search fields
            if search.lower() in value[index].lower():
                if key not in list(search_results):  # save each key only once
                    search_results[list(search_results)[-1] + 1] = key


def print_search_results():
    """ Search results to terminal """
    global search_results, book
    if search_results:
        fields = ', '.join([item for item in search_results[0][1]])
        print(f'On inquiry \'{search_results[0][0]}\' '
              f'in fields {fields} '
              f'found {list(search_results)[-1]} matches:')
        for i, key in enumerate(search_results):
            if key == 0:
                continue
            print(f'{i}. ', end='')
            print(*book[search_results[key]], sep=' ')


def get_search_query():
    """ Assemble simple query """
    global last_search, search_fields
    default_fields = { 'l': 'last_name', 'f': 'first_name', 'p': 'patronymic', 't': 'phone_num', 'm': 'memo' }
    last_search = input('Type in search query: ')
    user_input = input('Fields: (l)ast name, (f)irst name, (p)atronymic, (t)elephone number, (m)emo.\n'
                       'Enter one letter for every field needed or leave blank to search in all: ').strip()
    if len(user_input) == 0:
        search_fields = []
        return search_fields
    for i in ['l', 'f', 'p', 't', 'm']:
        if i in user_input:
            search_fields.append(default_fields[i])


def get_advanced_search_query():
    """ Assemble advanced query """
    global last_advanced_search
    last_advanced_search = []
    default_fields = { 1: 'last_name', 2: 'first_name', 3: 'patronymic', 4: 'phone_num', 5: 'memo' }
    for i in range(1, 5):
        last_advanced_search.append(input(f'Enter query if needed for field \'{default_fields[i]}\': '))


def change_contact(contact):
    """ Edit entry """
    # Check if request is not empty, otherwise return
    if len([li for li in contact if li]) == 0 or not contact[0] or not contact[1]:
        return print('Empty request or minimum requirement are not met: last_name + first_name')

    global book, duplicates
    initialize_book()

    # Parse contact attributes
    contact_parsed = { i: value for i, value in enumerate(contact) }

    # Call for duplicates
    first_run = True
    get_duplicates(contact_parsed)

    if len(duplicates) == 0:
        print('Use another search to change entry.')
    elif len(duplicates) > 0:
        # Ask user to confirm
        while True:
            choice = input(f'Choose (Q)uit or number to edit: ')
            if choice.lower() == 'q':
                break
            elif choice.isdigit():
                choice = int(choice)
            else:
                continue
            confirm = input(f'Edit entry: {" ".join(book[list(duplicates)[choice - 1]])} (y/n): ')
            if confirm.lower() == 'n':
                break
            elif confirm.lower() == 'y':
                while True:
                    if not first_run:
                        get_duplicates(contact_parsed)
                    first_run = False
                    print(f'What are you changing?\n'
                          f'(L)ast name\n'
                          f'(F)irst name\n'
                          f'(P)atronymic\n'
                          f'(T)elephone number\n'
                          f'(M)emo\n'
                          f'(Q)uit menu')
                    menu_choice = input(': ')
                    match menu_choice.lower():
                        case 'l':
                            temp = input('Enter new last name: ')
                            confirm = input(f'Change \'{book[list(duplicates)[choice - 1]][0]}\' '
                                            f'to \'{temp}\' (y/n): ')
                            if confirm.lower() == 'n':
                                continue
                            elif confirm.lower() == 'y':
                                book[list(duplicates)[choice - 1]][0] = temp
                                contact_parsed[0] = temp
                                continue
                        case 'f':
                            temp = input('Enter new first name: ')
                            confirm = input(f'Change \'{book[list(duplicates)[choice - 1]][1]}\' '
                                            f'to \'{temp}\' (y/n): ')
                            if confirm.lower() == 'n':
                                continue
                            elif confirm.lower() == 'y':
                                book[list(duplicates)[choice - 1]][1] = temp
                                contact_parsed[1] = temp
                                continue
                        case 'p':
                            temp = input('Enter new patronymic name: ')
                            confirm = input(f'Change \'{book[list(duplicates)[choice - 1]][2]}\' '
                                            f'to \'{temp}\' (y/n): ')
                            if confirm.lower() == 'n':
                                continue
                            elif confirm.lower() == 'y':
                                book[list(duplicates)[choice - 1]][2] = temp
                                contact_parsed[2] = temp
                                continue
                        case 't':
                            print('Enter new phone number: ')
                            temp = get_phone_num_from_user()
                            confirm = input(f'Change \'{book[list(duplicates)[choice - 1]][3]}\' '
                                            f'to \'{temp}\' (y/n): ')
                            if confirm.lower() == 'n':
                                continue
                            elif confirm.lower() == 'y':
                                book[list(duplicates)[choice - 1]][3] = temp
                                contact_parsed[3] = temp
                                continue
                        case 'm':
                            temp = input('Enter new memo: ')
                            confirm = input(f'Change \'{book[list(duplicates)[choice - 1]][4]}\' '
                                            f'to \'{temp}\' (y/n): ')
                            if confirm.lower() == 'n':
                                continue
                            elif confirm.lower() == 'y':
                                book[list(duplicates)[choice - 1]][4] = temp
                                contact_parsed[4] = temp
                                continue
                        case 'q':
                            break
            get_duplicates(contact_parsed)


def remove_contact(contact):
    """ Remove entry """

    # Check if request is not empty, otherwise return
    if len([li for li in contact if li]) == 0 or not contact[0] or not contact[1]:
        return print('Empty request or minimum requirement are not met: last_name + first_name')

    global book, duplicates
    initialize_book()

    # Parse contact attributes
    contact_parsed = { i: value for i, value in enumerate(contact) }

    # Call for duplicates
    get_duplicates(contact_parsed)

    # Ask user to confirm
    while True:
        choice = int(input(f'Choose number to delete: '))
        if choice != '':
            confirm = input(f'Remove entry: {" ".join(book[list(duplicates)[choice - 1]])} (y/n): ')
            if confirm.lower() == 'n':
                break
            elif confirm.lower() == 'y':
                book[list(duplicates)[choice - 1]] = []
                break


def show_menu(state='1'):
    """ Active menu """
    global last_file_opened, last_file_saved, menu_state
    menu_state = state
    menu = { '(M)ain menu': ['(F)ile', '(B)ook', 'E(x)it', '', ''],
             'File menu': ['(O)pen - read from file', '(S)ave - write to file'],
             'Book menu': ['(N)ew - make new entry',
                           'F(I)nd - search for entry',
                           '(S)how - show book content',
                           '(E)dit - change existing entry',
                           '(D)elete - remove existing entry',
                           ] }
    pointer, p_offset, offset, p_offset2, offset2 = '->', 12, 9, 15, 9
    match state:
        case '1':
            info = f'\nLast opened: {last_file_opened}    Last saved: {last_file_saved}'
            print(info)
            print('-' * len(info))
            print(f'{pointer} {list(menu)[0]}'.rjust(p_offset))
            for i in range(3):
                print(str(menu['(M)ain menu'][i]).rjust(offset))
        case '2':
            info = f'\nLast opened: {last_file_opened}    Last saved: {last_file_saved}'
            print(info)
            print('-' * len(info))
            print(f'{list(menu)[0]}'.rjust(p_offset) + f'{pointer} {list(menu)[1]}'.rjust(p_offset2))
            for i in range(2):
                print(f'{menu["(M)ain menu"][i]}'.rjust(offset) + f'{" " * offset2}{menu["File menu"][i]}')
        case '3':
            info = f'\nLast opened: {last_file_opened}    Last saved: {last_file_saved}'
            print(info)
            print('-' * len(info))
            print(f'{list(menu)[0]}'.rjust(p_offset) + f'{pointer} {list(menu)[2]}'.rjust(p_offset2))
            for i in range(5):
                print(f'{menu["(M)ain menu"][i]}'.rjust(offset) + f'{" " * offset2}{menu["Book menu"][i]}')


def get_action(user_input):
    """ Menu states and actions """
    global file_to_read, file_to_write, new_entry, menu_state, last_search, search_fields
    if menu_state == '1':
        # States for main menu
        # '1' -> Cases: E(X)it, (F)ile, (B)ook
        match user_input.lower():
            case 'x':  # Exit program
                exit()
            case 'f':  # File menu
                show_menu('2')
            case 'b':  # Book menu
                show_menu('3')

    elif menu_state == '2':
        # States for file menu
        # '2' -> Cases: E(X)it, (M)ain, (F)ile, (O)pen, (S)ave, (B)ook
        match user_input.lower():
            case 'x':  # Exit program
                exit()
            case 'm':  # Main menu
                show_menu('1')
            case 'f':  # File menu
                show_menu('2')
            case 'o':  # File menu - Open
                get_file_to_read()
                read_from_file(file_to_read)
                show_menu('2')
            case 's':  # File menu - Save
                get_file_to_write()
                write_to_file(file_to_write)
                show_menu('2')
            case 'b':  # Book menu
                show_menu('3')

    elif menu_state == '3':
        # States for book menu
        # '3' -> Cases: E(X)it, (M)ain, (F)ile, (B)ook, (N)ew, F(I)nd, (S)how, (E)dit, (D)elete
        match user_input.lower():
            case 'x':  # Exit program
                exit()
            case 'm':  # Main menu
                show_menu('1')
            case 'f':  # File menu
                show_menu('2')
            case 'b':  # Book menu
                show_menu('3')
            case 'n':  # Book menu - New
                get_new_entry()
                create_new_contact(new_entry)
                show_menu('3')
            case 'i':  # Book menu - Find
                get_search_query()
                search_for_contact(last_search, search_fields)
                print_search_results()
                show_menu('3')
            case 's':  # Book menu - Show
                show_all_contacts()
                show_menu('3')
            case 'e':  # Book menu - Edit
                get_advanced_search_query()
                change_contact(last_advanced_search)
                show_menu('3')
            case 'd':  # Book menu - Delete
                get_advanced_search_query()
                remove_contact(last_advanced_search)
                show_menu('3')


def main():
    # global book, search_fields, search_results, duplicates, new_entry, file_to_read, file_to_write
    while True:
        get_action(input(' : '))


if __name__ == '__main__':
    show_menu()
    main()
