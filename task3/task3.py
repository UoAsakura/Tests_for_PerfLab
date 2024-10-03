"""Task_3"""
# Импорт модулей для работы с типов данных формата json и системой.
import json
import sys


def fill_test_values(test: list, values_dict: dict):
    """
    Функция с возможностью рекурсивного вызова, для изменения списка test.
    """
    # Пробегаемся по списку из словарей.
    for i in test:
        # Заполняем поле id с проверкой наличия значения value.
        if i["id"] in values_dict:
            i["value"] = values_dict[i["id"]]
        # Если словарь имеет ключ values, то мы рекурсивно вызваем эту же функцию.
        if "values" in i:
            fill_test_values(i["values"], values_dict)


def main():
    # Проверка на наличие трех аргументов (пути к файлам)
    if len(sys.argv) != 4:
        print("Usage: python3 task3.py <values.json> <tests.json> <report.json>")
        return
    # Аргументы из командной строки.
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Чтение values.json (результаты тестов).
    with open(values_file, 'r') as f:
        values_data = json.load(f)

    # Преобразуем список объектов values в словарь для быстрого доступа по id.
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Чтение tests.json (структура тестов)
    with open(tests_file, 'r') as f:
        tests = json.load(f)

    # Рекурсивное заполнение значений тестов.
    fill_test_values(tests["tests"], values_dict)

    # Запись результата в report.json.
    with open(report_file, 'w') as f:
        json.dump(tests, f, indent=4)

    print(f"Отчет успешно создан в файле {report_file}")


if __name__ == "__main__":
    main()
