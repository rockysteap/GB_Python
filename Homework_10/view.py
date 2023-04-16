import string

import messages as txt


# def show_main_menu(in_menu: dict, in_info: list, in_state: str, in_last_opened: str, in_last_saved: str):
#     """ Active menu """
#     pointer, second_col_pos = '->', 18
#     if in_menu['titles'][0] == '(Г)лавное меню':
#         second_col_pos = 20
#     match in_state:
#         case 'main':
#             menu_rows = len(in_menu[in_state])
#             info = f'\n{in_info[0]} {in_last_opened}    {in_info[1]} {in_last_saved}'
#             print(info)
#             print('-' * len(info))
#             print(f'{pointer:>3} {in_menu["titles"][0]:<12}')
#             for i in range(menu_rows):
#                 print(f'{" " * 4}{in_menu[in_state][i]:<12}')
#             print('-' * len(info))
#         case 'file':
#             menu_rows = len(in_menu[in_state])
#             info = f'\n{in_info[0]} {in_last_opened}    {in_info[1]} {in_last_saved}'
#             u_line_len = len(info)
#             for i in range(menu_rows):
#                 item_gap = second_col_pos - len(in_menu["main"][i])
#                 if u_line_len < len(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}'):
#                     u_line_len = len(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}')
#             print(info)
#             print('-' * u_line_len)
#             print(f'{in_menu["titles"][0]:<12}  {pointer:>3} {in_menu["titles"][1]}')
#             for i in range(menu_rows):
#                 item_gap = second_col_pos - len(in_menu["main"][i])
#                 print(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}')
#             print('-' * u_line_len)
#         case 'book':
#             menu_rows = len(in_menu[in_state])
#             info = f'\n{in_info[0]} {in_last_opened}    {in_info[1]} {in_last_saved}'
#             u_line_len = len(info)
#             for i in range(menu_rows):
#                 item_gap = second_col_pos - len(in_menu["main"][i])
#                 if u_line_len < len(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}'):
#                     u_line_len = len(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}')
#             print(info)
#             print('-' * u_line_len)
#             print(f'{in_menu["titles"][0]:<12}  {pointer:>3} {in_menu["titles"][2]}')
#             for i in range(menu_rows):
#                 item_gap = second_col_pos - len(in_menu["main"][i])
#                 print(f'{in_menu["main"][i]}{" " * item_gap}{in_menu[in_state][i]}')
#             print('-' * u_line_len)


def show_message(language: int, message: str):
    if message == 'pause':
        input(txt.message_pause[language])
    else:
        print(message[language])


def get_user_input(*args) -> str:
    prompt = ': '
    constraints = set()
    const_w_upper = set()
    user_input = str()
    for arg in args:
        constraints = arg if arg else set()
    if constraints:
        for item in constraints:
            const_w_upper.add(item.lower())
            const_w_upper.add(item.upper())
        while user_input not in const_w_upper:
            user_input = input(prompt)
        return user_input
    else:
        return input(prompt)


def get_user_confirmation(language: int, message: str) -> bool:
    user_input = str()
    while user_input not in txt.confirmations_prompt[language]:
        user_input = input(message[language] + txt.message_confirmation_prompt[language])
    return True if user_input == txt.confirmations_prompt[language][0] else False


def prompt_user_for_read_file(language: int, files: list):
    print(txt.message_files_list_in_dir[language])
    if files:
        for file in files:
            print(file)
        print(txt.message_input_file_to_read[language])
    else:
        print(txt.message_no_files_to_read[language])


def prompt_user_for_save_file(language: int, files: list):
    print(txt.message_files_list_in_dir[language])
    if files:
        for file in files:
            print(file)
        print(txt.message_input_file_to_save[language])


def show_all_contacts(language: int, in_book: dict, u_line_len: int) -> dict:
    """ Print contact list to terminal """
    contacts_enum_id_dict = dict()
    i = 0
    print('-' * u_line_len)
    for key, value in in_book.items():
        if key == 0:
            continue
        elif value:
            i += 1
            print(f'{i}. ', end='')
            contacts_enum_id_dict[str(i)] = key
            for item in value:
                print(item, '', end='')
            print()
    print('-' * u_line_len)
    return contacts_enum_id_dict


def show_duplicates(duplicates: set, in_book: dict) -> dict:
    """ Print and save duplicates"""
    duplicates_enum_id_dict = dict()
    for i, item in enumerate(duplicates, start=1):
        duplicates_enum_id_dict[str(i)] = list(in_book)[item]
        print(f'{i}. ', end='')
        print(*in_book[item], sep=' ')
    return duplicates_enum_id_dict


def show_search_results(language: int, in_book: dict, search_results: dict):
    """ Print search results """
    if search_results:
        possible_fields = ['last_name', 'first_name', 'patronymic', 'phone_num', 'memo']
        search_fields = []
        for item in search_results[0][1]:
            if item in possible_fields:
                index = possible_fields.index(item)
                search_fields.append(f'{txt.message_fields[index][language]}')
        fields = ', '.join([item for item in search_fields])
        print(f'{txt.message_search_results_on_inquiry[language]} \'{search_results[0][0]}\' '
              f'{txt.message_search_results_in_fields[language]} \'{fields}\' '
              f'{txt.message_search_results_found[language]} {list(search_results)[-1]} '
              f'{txt.message_search_results_matches[language]}:')
        for i, key in enumerate(search_results):
            if key == 0:
                continue
            print(f'{i}. ', end='')
            print(*in_book[search_results[key]], sep=' ')
    input(txt.message_pause[language])


def show_new_entry(language: int, entry: list):
    print(txt.message_new_entry[language], *entry)


def get_simple_search_query(language: int, default_fields: dict) -> list:
    """ Enquire simple query """
    search_fields = []
    query = input(txt.message_search_query_input[language])
    fields = input(txt.message_search_fields_input[language])
    if len(fields) == 0:
        return [query, fields]
    fields_list = ['l', 'f', 'p', 't', 'm'] if language == 0 else ['ф', 'и', 'о', 'т', 'д']
    for i in fields_list:
        if i in fields:
            search_fields.append(default_fields[i])
    return [query, fields]


def get_advanced_search_query(language: int) -> list:
    """ Enquire advanced query """
    last_advanced_search = []
    for i in range(5):
        last_advanced_search.append(input(f'{txt.message_advanced_search_query[language]}'
                                          f'\'{txt.message_fields[i][language]}\': '))
    return last_advanced_search


def check_for_empty_advanced_query(language: int, advanced_entry: list) -> bool:
    # Check if request is not empty, otherwise return
    if len([li for li in advanced_entry if li]) == 0 or not advanced_entry[0] or not advanced_entry[1]:
        print(txt.message_error_min_values_in_advanced_search[language])
        return True
    return False


def show_contact_by_number_input(language: int, in_book: dict, in_contact_id: dict, in_id: str) -> int:
    if in_id in list(in_contact_id):
        print(in_id + '. ', end='')
        for item in in_book[in_contact_id[in_id]]:
            print(item, '', end='')
        print()
        return in_contact_id[in_id]
    else:
        print(txt.message_error_no_contact_by_number[language] + f' {in_id}.')
        return -1


# def show_contact_by_id(in_book: dict, in_book_id: int):
#     if in_book_id in list(in_book):
#         for item in in_book[in_book_id]:
#             print(item, '', end='')
#     print()


def show_contact_edit(language: int, contact_entry: list) -> list:
    contact_edited = ['', '', '', '', '']
    while contact_edited[0] == '' or contact_edited[1] == '':
        for i in range(5):
            user_input = input(f'{txt.message_change_field[language]} \'{txt.message_fields[i][language]}\' ->: ')
            if user_input == '':
                contact_edited[i] = contact_entry[i]
            else:
                if i in [0, 1, 2]:
                    for char in string.punctuation:
                        contact_edited[i] = user_input.replace(char, '').replace(' ', '').capitalize()
                else:
                    contact_edited[i] = user_input
        if contact_edited[0] == '' or contact_edited[1] == '':
            if get_user_confirmation(language, txt.message_error_new_entry_min):
                continue
            else:
                return contact_entry
    return contact_edited


def show_contact_compare(language: int, in_contact1: list, in_contact2: list):
    for i in range(5):
        if in_contact1[i] != in_contact2[i]:
            print(f'\'{txt.message_fields[i][language]}\': ' + in_contact1[i] + ' -> ' + in_contact2[i])
