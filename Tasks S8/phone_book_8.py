phone_book_8 = []

def get_phone_book_8():
    global phone_book_8
    return phone_book_8


def set_phone_book_8(new_phone_book_8):
    global phone_book_8
    phone_book_8 = new_phone_book_8

def add_contact(contact: list):
    global phone_book_8
    phone_book_8.append(contact)

def remove_contact(id):
    global phone_book_8
    name = phone_book_8[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book_8.pop(id-1)
        return True
    return False

def edit_contact(id, upd_contact):
    global phone_book_8
    phone_book_8[id-1] = upd_contact

def search_contact(search_str: str):
    global phone_book_8
    result = []
    for contact in phone_book_8:
        if search_str in contact:
            result.append(contact)
        return result
