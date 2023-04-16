from Menu import Menu
import view
import model
import messages as txt

menu = Menu(txt.menu_source, txt.menu_links, txt.file_info)

def main_loop():
    while True:
        """ Menu states and actions """
        state = model.get_menu_state()
        menu.__setstate__(state)
        lang = model.get_lang()
        constraints = model.get_user_input_constraints(lang, state)
        cases = model.get_menu_cases(lang)
        # labels = model.get_menu_labels(lang, txt.main_menu)
        menu.set_last_opened(model.get_last_file_opened())
        menu.set_last_saved(model.get_last_file_saved())
        # info = model.get_info(lang, txt.info_list)
        # view.show_main_menu(labels, info, state, last_opened, last_saved)
        menu.draw()
        user_input = view.get_user_input(constraints).lower()
        print(user_input)

        match cases:
            case { 'lang': val } if val == user_input:
                if user_input == 'r':
                    model.set_lang('ru')
                    menu.set_lang(1)
                if user_input == 'а':
                    model.set_lang('en')
                    menu.set_lang(0)
            case { 'exit': val } if val == user_input:
                case_exit()
            case { 'file': val } if val == user_input:
                model.set_menu_state('file')
                menu.__setstate__('file')
            case { 'book': val } if val == user_input:
                model.set_menu_state('book')
                menu.__setstate__('book')
            case { 'main': val } if val == user_input and (state == 'file' or state == 'book'):
                model.set_menu_state('main')
                menu.__setstate__('main')
            case { 'open': val } if val == user_input and state == 'file':
                case_open()
            case { 'save': val } if val == user_input and state == 'file':
                case_save()
            case { 'new': val } if val == user_input and state == 'book':
                case_new()
            case { 'find': val } if val == user_input and state == 'book':
                case_find()
            case { 'show': val } if val == user_input and state == 'book':
                case_show()
            case { 'edit': val } if val == user_input and state == 'book':
                case_edit()
            case { 'delete': val } if val == user_input and state == 'book':
                case_delete()


def case_exit():
    if model.is_there_changes():
        if view.get_user_confirmation(model.get_lang(), txt.message_save_changes):
            case_save()
    exit()

def case_open():
    lang = model.get_lang()
    files = model.get_files_list_in_dir()
    view.prompt_user_for_read_file(lang, files)
    if not files:
        return
    while True:
        user_file = view.get_user_input()
        if model.is_user_file_in_files(user_file):
            if view.get_user_confirmation(lang, txt.message_confirm_file_reading):
                if model.read_from_file(user_file):
                    view.show_message(lang, txt.message_success_file_opened)
                    model.set_menu_state('book')
                    menu.__setstate__('book')
                    break
                else:
                    view.show_message(lang, txt.message_error_fail_to_open)
                    break
            else:
                break


def case_save():
    lang = model.get_lang()
    files = model.get_files_list_in_dir()
    view.prompt_user_for_save_file(lang, files)
    while True:
        user_file = view.get_user_input()
        if model.is_user_file_in_files(user_file):
            if view.get_user_confirmation(lang, txt.message_confirm_file_overwriting):
                if model.write_to_file(user_file):
                    view.show_message(lang, txt.message_success_file_saved)
                    break
            else:
                continue
        else:
            if view.get_user_confirmation(lang, txt.message_confirm_file_writing):
                if model.write_to_file(user_file):
                    view.show_message(lang, txt.message_success_file_saved)
                    break
            else:
                break


def case_new():
    lang = model.get_lang()
    while True:
        view.show_message(lang, txt.message_new_entry_constructor)
        if model.check_full_name_input(view.get_user_input()):
            view.show_message(lang, txt.message_input_phone)
            model.get_new_entry().append(model.check_phone_num_input(view.get_user_input()))
            view.show_message(lang, txt.message_input_memo)
            model.get_new_entry().append(view.get_user_input())
            if model.check_for_duplicates(model.get_new_entry()):
                view.show_message(lang, txt.message_duplicates_matches_found)
                view.show_duplicates(model.get_dublicates(), model.get_book())
            else:
                view.show_message(lang, txt.message_duplicates_no_matches_found)
            view.show_new_entry(lang, model.get_new_entry())
            if view.get_user_confirmation(lang, txt.message_new_entry_confirm):
                model.save_entry(model.get_new_entry())
                return
            else:
                continue
        else:
            if view.get_user_confirmation(lang, txt.message_error_new_entry_min):
                continue
            else:
                break


def case_find():
    lang = model.get_lang()
    query = view.get_simple_search_query(lang, model.get_default_fields())
    model.search_for_contact(query[0], query[1])
    view.show_search_results(lang, model.get_book(), model.get_search_results())


def case_show():
    lang = model.get_lang()
    if model.is_book_empty():
        view.show_message(lang, txt.message_empty_book)
    else:
        view.show_all_contacts(lang, model.get_book(), model.get_widest_book_string(model.get_book()))
        view.show_message(lang, 'pause')


def case_edit():
    lang = model.get_lang()
    if model.is_book_empty():
        view.show_message(lang, txt.message_empty_book)
        return
    if view.get_user_confirmation(lang, txt.message_input_ask_for_search_method):
        # search by direct number input
        id_enum_dict = view.show_all_contacts(lang, model.get_book(), model.get_widest_book_string(model.get_book()))
        case_edit_menu_actions(lang,
                               view.show_contact_by_number_input(lang,
                                                                 model.get_book(),
                                                                 id_enum_dict,
                                                                 view.get_user_input(list(id_enum_dict))))
    else:
        # or search by field
        while True:
            query = view.get_advanced_search_query(lang)
            # if query was ignored - empty
            if view.check_for_empty_advanced_query(lang, query):
                # get another query
                if view.get_user_confirmation(lang, txt.message_input_confirm_to_try_advanced_search):
                    continue  # yes
                else:
                    break  # no
            # query checked for duplicates
            if model.check_for_duplicates(query):
                view.show_message(lang, txt.message_duplicates_matches_found)
                id_dupl_dict = view.show_duplicates(model.get_dublicates(), model.get_book())
                # enter contact number to edit
                case_edit_menu_actions(lang,
                                       view.show_contact_by_number_input(lang,
                                                                         model.get_book(),
                                                                         id_dupl_dict,
                                                                         view.get_user_input(list(id_dupl_dict))))
                break
            else:
                view.show_message(lang, txt.message_duplicates_no_matches_found)


def case_edit_menu_actions(lang: int, in_id: int):
    contact_initial_state = model.get_contact_by_id(in_id).copy()
    contact_edited = view.show_contact_edit(lang, contact_initial_state)
    if contact_initial_state == contact_edited:
        view.show_message(lang, txt.message_edit_no_changes)
        return
    else:
        # parse phone
        if contact_initial_state[3] != contact_edited[3]:
            contact_edited[3] = model.check_phone_num_input(contact_edited[3])
        view.show_message(lang, txt.message_edit_changes_made)
        view.show_contact_compare(lang, contact_initial_state, contact_edited)
        if view.get_user_confirmation(lang, txt.message_edit_save_changes):
            model.save_entry(contact_edited, in_id)


def case_delete():
    lang = model.get_lang()
    id_to_delete = -1
    if model.is_book_empty():
        view.show_message(lang, txt.message_empty_book)
        return
    if view.get_user_confirmation(lang, txt.message_input_ask_for_search_method):
        # search by direct number input
        id_enum_dict = view.show_all_contacts(lang, model.get_book(), model.get_widest_book_string(model.get_book()))
        id_to_delete = view.show_contact_by_number_input(lang, model.get_book(), id_enum_dict,
                                                         view.get_user_input(list(id_enum_dict)))
    else:
        # or search by field
        while True:
            query = view.get_advanced_search_query(lang)
            # if query was ignored - empty
            if view.check_for_empty_advanced_query(lang, query):
                # get another query
                if view.get_user_confirmation(lang, txt.message_input_confirm_to_try_advanced_search):
                    continue  # yes
                else:
                    break  # no
            # query checked for duplicates
            if model.check_for_duplicates(query):
                view.show_message(lang, txt.message_duplicates_matches_found)
                id_dupl_dict = view.show_duplicates(model.get_dublicates(), model.get_book())
                # enter contact number to delete
                id_to_delete = view.show_contact_by_number_input(lang, model.get_book(), id_dupl_dict,
                                                                 view.get_user_input(list(id_dupl_dict)))
                break
            else:
                view.show_message(lang, txt.message_duplicates_no_matches_found)
    if id_to_delete > 0:
        # view.show_contact_by_id(model.get_book(), id_to_delete)
        if view.get_user_confirmation(lang, txt.message_remove_entry):
            model.delete_entry(id_to_delete)
            view.show_message(lang, txt.message_remove_entry_success)

