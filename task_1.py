# Напишите следующие функции: ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import math
import random


def find_square_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(-1000, 1000) for _ in range(3)]
            writer.writerow(row)

def square_roots_decorator(func):
    def wrapper(filename):
        results = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(float, row)
                result = func(a, b, c)
                results.append({
                    "a": a,
                    "b": b,
                    "c": c,
                    "roots": result
                })
        return results
    return wrapper

def save_to_json_decorator(func):
    def wrapper(filename):
        results = func(filename)
        data = {
            "results": results
        }
        with open('result.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
        return results
    return wrapper


# Нахождение корней квадратного уравнения
# roots = find_square_roots(1, -3, 2)
# print(roots)

# Генерация csv файла
generate_csv_file('data.csv', 100)

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
@square_roots_decorator
def process_csv_data(a, b, c):
    return find_square_roots(a, b, c)

results = process_csv_data('data.csv')
for result in results:
    print(f"Roots for {result['a']}, {result['b']}, {result['c']}: {result['roots']}")

# Декоратор, сохраняющий все переданные из csv файла параметры и результаты работы функции нахождения корней квадратного уравнения в json файл
@save_to_json_decorator
def calculate_square(filename):
    return process_csv_data(filename)

calculate_square('data.csv')

