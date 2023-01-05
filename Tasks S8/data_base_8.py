import phone_book_8 as pb
import view_8

path = 'phone_book_8.txt'

#Функция чтения справочника из файла

def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book_8 = file.readlines()
    pb.set_phone_book_8(str_to_list(phone_book_8))

#Функция показывает справочника по строчно
def str_to_list(phone_book_8: list):
    new_phone_book_8 = []
    for contact in phone_book_8:
        new_phone_book_8.append(contact.strip().split(';'))
    return new_phone_book_8

# Эта функция strip позволяет избавиться от \n после каждого контакта из списка строк и split поделить строку по знаку ';'

# Функция пересохранения справочника

def save_data_base():
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(list_to_str())
# Функция добавления в файл новой записи

def list_to_str():
    phone_book_8 = pb.get_phone_book_8()
    new_phone_book_8 = []
    for contact in phone_book_8:
        new_phone_book_8.append(';'.join(contact) + '\n')
    new_phone_book_8[-1] = new_phone_book_8[-1][:-1]    # 'здесь убираем последний \n'
    return ''.join(new_phone_book_8)
