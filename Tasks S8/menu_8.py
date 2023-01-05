import view_8
import phone_book_8 as pb
import data_base_8 as db

print(view_8.main_menu())


#Функция match аналогична если (if)... равно  и дальше несколько значений

def main_menu(choice: int):
    match choice:
        case 1:
            phone_book_8 = pb.get_phone_book_8()
            view_8.print_phone_book_8(phone_book_8)
        case 2:
            db.load_data_base()
            view_8.load_success()
        case 3:
            db.save_data_base()
            view_8.save_success()
        case 4:
            contact = view_8.input_new_contact()
            pb.add_contact(contact)
        case 5:
            phone_book_8 = pb.get_phone_book_8()
            view_8.print_phone_book_8(phone_book_8)
            id = view_8.input_edit_contact()
            update_contact = view_8.update_contact_info(phone_book_8[id - 1])
            pb.edit_contact(id, update_contact)
        case 6:
            phone_book_8 = pb.get_phone_book_8()
            view_8.print_phone_book_8(phone_book_8)
            id = view_8.input_remove_contact()
            if pb.remove_contact(id):
                view_8.remove_success()
        case 7:
            search_str = view_8.input_search()
            result_search = pb.search_contact(search_str)
            view_8.print_result_search(result_search)
        case 0:
            return True
#здесь выполняется выход из цикла когда вводят 0, во всех остальных цифрах - это False

def start():
    while True:
        choice = view_8.main_menu()
        if main_menu(choice):
            view_8.log_off()
            break
