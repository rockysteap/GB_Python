import view
import text_fields as txt
from classes import Contact, PhoneBook


def start():
    phonebook = PhoneBook('sample.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                phonebook.open()
                view.print_message(txt.successful_open)
            case 2:
                phonebook.save()
                view.print_message(txt.successful_save)
            case 3:
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
            case 4:
                new_contact = view.new_contact()
                phonebook.add(new_contact)
                view.print_message(txt.contact_saved(new_contact.name))
            case 5:
                word = view.enter_keyword()
                result = phonebook.find(word)
                view.show_contacts(result, txt.not_found(word))
            case 6:
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view.print_message(txt.successful_edited(edited_contact[1].name))
            case 7:
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete(pb[index - 1].name)):
                        view.print_message(txt.delete_contact(phonebook.remove(index)))
            case 8:
                if phonebook.save_on_exit():
                    if view.confirm(txt.no_saved_book):
                        phonebook.save()
                view.print_message(txt.goodbye)
                exit()
    