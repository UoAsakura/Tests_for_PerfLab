"""Task 2"""
# Импортируем модуль для работы с системой.
import sys


def read_circle_data(file_path: str):
    """Чтение данных окружности (координаты центра и радиус) из файла."""
    with open(file_path, 'r') as file:
        x0 = float(file.readline().strip())  # Координата X центра окружности.
        y0 = float(file.readline().strip())  # Координата Y центра окружности.
        radius = float(file.readline().strip())  # Радиус окружности.
    return x0, y0, radius


def read_points(file_path):
    """Чтение списка точек из файла."""
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = [float(i) for i in line.split()]  # Чтение двух координат точки.
            points.append((x, y))
    return points


def point_position(x0, y0, radius, x, y):
    """Определение положения точки относительно окружности."""
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    radius_squared = radius ** 2
    if distance_squared == radius_squared:
        return 0  # Точка на окружности.
    elif distance_squared < radius_squared:
        return 1  # Точка внутри окружности.
    else:
        return 2  # Точка снаружи окружности.


def main():
    # Получаем пути к файлам из аргументов командной строки.
    if len(sys.argv) != 3:
        print("Usage: python3 task2.py <circle_file.txt> <points_file.txt>")
        return
    # Аргументы из командной строки.
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    # Считываем данные окружности.
    x0, y0, r = read_circle_data(circle_file)
    # Считываем координаты точек.
    points = read_points(points_file)
    # Для каждой точки определяем ее положение относительно окружности.
    for x, y in points:
        position = point_position(x0, y0, r, x, y)
        print(position)


if __name__ == "__main__":
    main()
