# Папка в папке 📂🌶️🌶️
#
# Напишите функцию is_subfolder(), которая принимает три аргумента в следующем порядке:
#
#     folder_dict – словарь, содержащий структуру папок и файлов операционной системы, где ключами являются строки с именами папок, а значениями – списки строк с именами вложенных в них папок
#     subfolder – строка с именем папки
#     folder – строка с именем папки
#
# Функция is_subfolder() должна возвращать True, если папка subfolder вложена в папку folder, или False в противном случае. Под вложенностью понимается не только непосредственная вложенность в папку folder, но и вложенность в любую папку внутри нее, на любой глубине. То есть если subfolder лежит в folder, или в папке внутри folder, или еще глубже, то это тоже считается вложенностью.
#
# Примечание. Вызывать функцию is_subfolder() не нужно, требуется только реализовать ее.
#
# Входные данные
# folder_system = {
#     'My': [
#         'Cartoons', 'Films', 'Series',
#     ],
#     'Cartoons': [
#         'Bolt (2008)', 'Ben 10 (2005)',
#         'Finding Nemo (2003)',
#     ],
#     'Films': [
#         'Joker (2019)', 'Wonka (2023)',
#         'Gone Girl (2014)',
#     ],
#     'Series': [
#         'Stranger Things (2016-2025)',
#         'Fallout (2024-)',
#         'Chernobyl (2019)',
#     ],
# }
# print(is_subfolder(
#     folder_system,
#     'Fallout (2024-)',
#     'My',
# ))
#
# Выходные данные
# True

def is_subfolder(folder_dict, subfolder, folder):
    # Если текущая папка не имеет подпапок — выходим
    if folder not in folder_dict:
        return False

    # Проверяем непосредственные подпапки
    for child in folder_dict[folder]:
        if child == subfolder:
            return True
        # Рекурсивно проверяем вложенность глубже
        if is_subfolder(folder_dict, subfolder, child):
            return True

    return False
