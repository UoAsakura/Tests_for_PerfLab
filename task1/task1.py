"""Task 1"""


def calc_path(len_arr: int, step: int):
    """
    Функция для подсчёта кругового массива без его создания.
    :param len_arr: Длина массива.
    :param step: Длина шага.
    :return: Список из элементов пути.
    """
    # Начало массива.
    start = 1
    # Актуальная точка, на которой мы.
    current_position = start
    # Результирующий путь.
    path = []
    # Запускаем цикл.
    while True:
        # Добавляем актуальную точку в путь.
        path.append(current_position)
        # Вычисляем новую точку.
        current_position = (current_position + step - 1) % (len_arr)
        # Условие уточняющее актуальную точку.
        if current_position == 0:
            current_position = len_arr
        # Завершаем, если пришли в начало.
        if current_position == start:
            break
    return path


# Принимаем агрументы из командной строки.
n, m = [int(i) for i in input().split()]
# Печатаем результат.
print(*calc_path(n, m), sep="")


"""Task 1 version 2"""
# from array import array
#
#
# def calc_path_ver_2(len_arr: int, step: int):
#     """
#     Функция для подсчёта кругового массива с его созданием.
#     :param len_arr: Длина массива.
#     :param step: Длина шага.
#     :return: Список из элементов пути.
#     """
#     # Создание массива.
#     calc_array = array("i", list(range(1, len_arr + 1)))
#     # Результирующий путь.
#     path = []
#     # Начинаем с первого элемента.
#     current_position = 0
#     # Пока не вернемся в исходную точку.
#     while True:
#         # Добавляем начальный элемент интервала в путь.
#         path.append(calc_array[current_position])
#         # Двигаемся вперед на step элементов по кругу.
#         current_position = (current_position + step - 1) % len_arr
#         # Если вернулись на исходную позицию, то прерываем цикл.
#         if current_position == 0:
#             break
#     return path
#
#
# # Принимаем агрументы из командной строки.
# n, m = [int(i) for i in input().split()]
# # Печатаем результат.
# print(*calc_path_ver_2(n, m), sep="")





