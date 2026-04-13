#В пассажирском поезде N вагонов. Выведите все возможные варианты рассадки в поезде К человек, при условии, что все они должны ехать в различных вагонах?
from itertools import permutations
import time

# Алгоритмический подход
def generate_permutations(N, K):
    def backtrack(start, path):
        if len(path) == K:
            permutations.append(path.copy())
            return
        for i in range(0,N,2):
            if i not in path:
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

    permutations = []
    backtrack(0, [])
    return permutations

def generate_seating_a(N, K):
    result = []
    count = 0

    permutations = generate_permutations(N, K)

    # Создание рассадки для каждой перестановки
    for positions in permutations:
        seating = [0] * N
        for i in range(len(positions)):
            pos = positions[i]
            seating[pos] = i + 1
        result.append(seating)
        count += 1  # Увеличиваем счетчик

    return result, count

# Использование функций Python (itertools)
def generate_seating_i(N, K):
    result = []
    count = 0
#    valid_people = [i for i in range(N) if (i + 1) % 2 != 0]  # Только нечетные номера
#    for positions in permutations(valid_people, K):
    for positions in permutations(range(N), K):
        seating = [0] * N
        for idx, pos in enumerate(positions):
            seating[pos] = idx + 1
        result.append(seating)
        count += 1
    return result, count

# Тестирование времени выполнения
N = int(input("Введите количество вагонов: "))
K = int(input("Введите количество человек: "))

start_time = time.time()
seating_algorithmic, count_algorithmic = generate_seating_a(N, K)
algorithmic_time = time.time() - start_time

start_time = time.time()
seating_itertools, count_itertools = generate_seating_i(N, K)
itertools_time = time.time() - start_time

print("Алгоритмический подход:")
for s in seating_algorithmic:
    print(s)
print(f"Количество комбинаций: {count_algorithmic}")
print(f"Время выполнения: {algorithmic_time:.6f} секунд\n")

print("Подход с использованием itertools:")
for s in seating_itertools:
    print(s)
print(f"Количество комбинаций: {count_itertools}")
print(f"Время выполнения: {itertools_time:.6f} секунд")
