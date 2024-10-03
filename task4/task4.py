"""Task 4"""
# Импорт модулей для вычисления медианы и работы с системой.
import sys
import statistics


def main():
    # Проверка на наличие аргумента командной строки (пути к файлу)
    if len(sys.argv) != 2:
        print("Usage: python3 task4.py <input_file>")
        return
    # Аргументы из командной строки.
    input_file = sys.argv[1]

    # Чтение чисел из файла
    with open(input_file, 'r') as f:
        nums = [int(line.strip()) for line in f]

    # Проверка на пустой массив
    if not nums:
        print("Input array is empty.")
        return

    # Определение медианы
    median = statistics.median(nums)

    # Подсчет минимального количества ходов
    moves = int(sum(abs(num - median) for num in nums))

    # Вывод результата
    print(moves)


if __name__ == "__main__":
    main()
