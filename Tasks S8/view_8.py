def main_menu():
    print('\nВыберите пункт меню:')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choise_main_menu()

def choise_main_menu():
    while True:
        try:
            choise = int(input('Выберите пункт из меню: '))
            if choise in range(0, 8):
                print()
                return choise
            else:
                print('Такого пункта нет повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')

def print_phone_book_8(phone_book_8: list):
    if len(phone_book_8) > 0:
        for id, contact in enumerate(phone_book_8, 1):
           print(id, *contact)  # * - позволяет убрать квадратные скобки
    else:
        print('Телефонная книга пуста или не загружена')
def log_off():
    print('До свидания, до новых встреч!')

def load_success():
    print('Телефонная книга загружена!')

def save_success():
    print('Телефонная книга сохранена!')

def remove_success():
    print('Контакт удален!')

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий: ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Введите ID контакта, который желаете удалить: '))
    return id

def remove_success():
    print('Контакт удален.')

def input_edit_contact():
    id = int(input('Введите номер контакта, который хотите изменить: '))
    return id

def update_contact_info(upd_cont: list):
    global new_name
    confirm = input(f'Вы хотите изменить имя контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
       new_name = input(f'Введите новое имя контакта {upd_cont[0]}: ')
       confirm = ''
    else:
        new_phone = upd_cont[0]
    confirm = input(f'Вы хотите изменить телефон контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
        new_phone = input(f'Введите новый телефон контакта {upd_cont[0]}: ')
        confirm = ''
    else:
        new_phone = upd_cont[1]
    confirm = input(f'Хотите изменить комментарий контакта {upd_cont[0]}? (y/n)')
    if confirm.lower() == 'y':
        new_comm = input(f'Введите новый комментарий контакта {upd_cont[0]}: ')
        confirm = ''
    else:
        new_comm = upd_cont[2]
    return [new_name, new_phone, new_comm]

def input_search():
    search_str = input('Введите строку для поиска: ')
    return search_str

def print_result_search(result_search: list):
    if len(result_search) > 0:
        print('Результат поиска: \n')
        for id, contact in enumerate(result_search, 1):
            print(id, *contact)
    else:
        print('Искомая строка не найдена')
