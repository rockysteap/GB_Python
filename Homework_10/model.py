import os
import pathlib
import string

# Current phone_book in memory
book = dict()
book[0] = ['last_name', 'first_name', 'patronymic', 'phone_num', 'memo']
book_initial_state = dict()
book_initial_state[0] = ['last_name', 'first_name', 'patronymic', 'phone_num', 'memo']

# New entry constructor
new_entry = list()

# Search results and history
search_results = dict()
last_search = str()
last_advanced_search = str()

# Fields used in search
search_fields = list()
default_fields = { 'l': 'last_name', 'f': 'first_name', 'p': 'patronymic', 't': 'phone_num', 'm': 'memo',
                   'ф': 'last_name', 'и': 'first_name', 'о': 'patronymic', 'т': 'phone_num', 'д': 'memo' }


# Search duplicates saved
duplicates = set()

# LANGUAGE SETUP
lang = 0  # 0 - 'en', 1 - 'ru'

# Language setter/getter
def set_lang(in_string: str):
    global lang
    if in_string == 'en':
        lang = 0
    elif in_string == 'ru':
        lang = 1
def get_lang():
    return lang


# MENU SETUP
menu_state = 'main'

# Menu state setter/getter
def set_menu_state(in_state: str):
    global menu_state
    menu_state = in_state
def get_menu_state() -> str:
    return menu_state

# Menu items used
menu_items = ['exit', 'file', 'lang', 'book', 'main', 'open', 'save', 'new', 'find', 'show', 'edit', 'delete']

# Menu items available user inputs
choices = [['x', 'f', 'r', 'b', 'm', 'o', 's', 'n', 'i', 's', 'e', 'd'],
           ['в', 'ф', 'а', 'к', 'г', 'о', 'с', 'с', 'н', 'п', 'и', 'у']]

# Menu language choices available for passed language
def get_choices_list(language: int) -> list:
    choices_list = list(choices[0]) if language == 0 else list(choices[1])
    return choices_list

# Menu cases for controller's use based on passed language
def get_menu_cases(language: int) -> dict:
    choices_list = get_choices_list(language)
    cases = dict()
    for i in range(len(menu_items)):
        cases[menu_items[i]] = choices_list[i]
    return cases

# User input constraint sets based on menu state and language
constraints = {
    'main': [{'f', 'b', 'x', 'r'},
             {'ф', 'к', 'в', 'а'}],
    'file': [{'m', 'f', 'b', 'x', 'r', 'o', 's'},
             {'г', 'ф', 'к', 'в', 'а', 'о', 'с'}],
    'book': [{'m', 'f', 'b', 'x', 'r', 'n', 'i', 's', 'e', 'd'},
             {'г', 'ф', 'к', 'в', 'а', 'с', 'н', 'п', 'и', 'у'}],
    'search_fields': [{'l', 'f', 'p', 't', 'm', ''},
                      {'ф', 'и', 'о', 'т', 'д'}]}
def get_user_input_constraints(language: int, state: str) -> list:
    input_constraints = constraints[state][language]
    return input_constraints

# Menu labels for passed language
def get_menu_labels(language: int, main_menu: dict) -> dict:
    """ Menu assembly using passed language: 0 - 'en', 1 - 'ru' """
    menu = { 'titles': [], 'main': [], 'file': [], 'book': [] }
    for k, v in main_menu.items():
        menu[k] = v[language]
    return menu

# History info labels for passed language
def get_info(language: int, info_list: dict) -> list:
    key = list(info_list)[language]
    info = list()
    for i in range(len(info_list[key])):
        info.append(info_list[key][i])
    return info


# WORKING WITH FILES
# File names
file_to_read = ''
file_to_write = ''
last_file_opened = '-'
last_file_saved = '-'

# File last open/save history setter/getter
def set_last_file_opened(in_last_file_opened: str):
    global last_file_opened
    last_file_opened = in_last_file_opened
def get_last_file_opened() -> str:
    return last_file_opened

def set_last_file_saved(in_last_file_saved: str):
    global last_file_saved
    last_file_saved = in_last_file_saved
def get_last_file_saved() -> str:
    return last_file_saved


# File to read
def get_files_list_in_dir() -> list:
    return [item for item in list(pathlib.Path().glob("*.csv"))]

def is_user_file_in_files(file: str) -> bool:
    file.replace('.csv', '')
    file += '.csv'
    return True if os.path.isfile(file) else False

def read_from_file(file: str) -> bool:
    global book_initial_state
    file.replace('.csv', '')
    file += '.csv'
    try:
        clear_book(book)
        with open(file, 'r', encoding='UTF-8') as data:
            for i, line in enumerate(data):
                if line.strip():
                    line = line.rstrip('\n')
                    book[i] = []
                    for item in line.split(','):
                        book[i].append(item)
            set_last_file_opened(file)
            book_initial_state = book.copy()
            return True
    except FileNotFoundError:
        return False

def is_there_changes() -> bool:
    return True if book != book_initial_state else False

def write_to_file(file: str) -> bool:
    file.replace('.csv', '')
    file += '.csv'
    try:
        with open(file, 'w', encoding='UTF-8') as data:
            for value in book.values():
                data.write(','.join(value))
                data.write('\n')
            set_last_file_saved(file)
            clear_book(book_initial_state)
            clear_book(book)
            initialize_book(book_initial_state)
            initialize_book(book)
            return True
    except FileNotFoundError:
        return False


# WORKING WITH BOOK

def clear_book(in_book: dict):
    in_book.clear()

def initialize_book(in_book: dict):
    """ Add titles to book """
    in_book[0] = ['last_name', 'first_name', 'patronymic', 'phone_num', 'memo']

def is_book_empty():
    """ Check if book is empty """
    return True if len(book) < 2 else False

def get_new_entry_id() -> int:
    """ Check for next available id number """
    global book
    new_id = len(list(book))
    while new_id in list(book):
        new_id += 1
    return new_id

def get_book() -> dict:
    return book


def get_widest_book_string(in_dict) -> int:
    i = 0
    u_line_len = 0
    for key, value in in_dict.items():
        k_len = 0
        if key == 0:
            continue
        elif value:
            i += 1
            k_len += len('. ')
            for item in value:
                k_len += len(f'{item} ')
        if u_line_len < k_len:
            u_line_len = k_len
    return u_line_len


# WORKING WITH CONTACTS

#  New entry setter/getter
def set_new_entry(in_entry: list):
    global new_entry
    new_entry = in_entry

def get_new_entry() -> list:
    global new_entry
    return new_entry

def check_phone_num_input(phone_user_input: str) -> str:
    """ Phone number input formatter """
    phone_num = phone_user_input.split()
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


def check_full_name_input(full_name: str) -> bool:
    name_list = ['', '', '']
    parsed_string = full_name.split()
    for i in range(len(parsed_string)):
        if i < 3:
            for char in string.punctuation:
                parsed_string[i] = parsed_string[i].replace(char, '')
            name_list.insert(i, parsed_string[i].capitalize())
            name_list.pop()
    set_new_entry(name_list)
    return True if name_list[0] and name_list[1] else False


# Search results setter/getter
def set_search_result(in_search: dict):
    global search_results
    search_results = in_search

def get_search_results() -> dict:
    global search_results
    return search_results

def search_for_contact(querry: str, fields=()):
    """ Search by given field, save results to global """
    global book, search_results, search_fields
    # Identify fields for search
    search_fields = fields if fields else book[0]
    # Get search indices of titles from our file (book[0])
    search_indices = list()
    for item in search_fields:
        search_indices.append(book[0].index(item))
    # Clear previous search results
    search_results.clear()
    # Add passed search fields to zero key
    search_results[0] = [querry, search_fields]
    # Search
    keys_found = list()
    for key, value in book.items():
        for index in search_indices:  # look only in search fields
            if value:
                if querry.lower() in value[index].lower():
                    if key not in keys_found:  # save each key only once
                        search_results[list(search_results)[-1] + 1] = key
                        keys_found.append(key)


# Dublicates setter/getter
def set_dublicates(in_dublicates: set):
    global duplicates
    duplicates = in_dublicates

def get_dublicates() -> set:
    global duplicates
    return duplicates

def check_for_duplicates(entry: list) -> bool:
    """ Search for duplicates in the book """
    global book, duplicates, search_results
    duplicates_count = { key: [] for key in range(len(book[0])) }
    contact_parsed = { i: value for i, value in enumerate(entry) }
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
    set_dublicates(interlaced_search)
    return True if interlaced_search else False

def save_entry(entry: list, in_id = -1):
    """ Save entry for new or edited contact """
    global book
    # save new
    if in_id == -1:
        new_id = get_new_entry_id()
        book[new_id] = entry
    # rewrite edited
    elif in_id > 0:
        book[in_id] = entry


def delete_entry(in_id):
    global book
    book[in_id] = []


def set_search_fields(fields: list):
    global search_fields
    search_fields = fields

def get_search_fields() -> list:
    global search_fields
    return search_fields


def set_last_search(search_list: list):
    global last_search
    last_search = search_list

def get_last_search() -> list:
    global last_search
    return last_search

def set_last_advanced_search(advanced_search_list: list):
    global last_advanced_search
    last_advanced_search = advanced_search_list

def get_last_advanced_search() -> list:
    global last_advanced_search
    return last_advanced_search

def get_contact_by_id(in_id: int) -> list:
    contact = book[in_id]
    return contact

def get_default_fields() -> dict:
    global default_fields
    return default_fields
